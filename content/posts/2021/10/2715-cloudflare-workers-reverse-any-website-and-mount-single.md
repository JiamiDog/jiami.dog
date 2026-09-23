---
title: "CloudFlare Workers 反代任意网站和挂载单页代码"
slug: "cloudflare-workers-reverse-any-website-and-mount-single"
source_id: "2715"
canonical_url: "https://jiami.dog/2715.html"
date_local: "2021-10-05T17:37:53"
date_published: "2021-10-05T09:37:53Z"
date_modified_local: "2021-10-05T17:37:54"
date_modified: "2021-10-05T09:37:54Z"
draft: false
featured_image_url: "https://jiami.dog/wp-content/uploads/2021/10/951862000.png"
featured_image_alt: "Cloudflare Workers 的代码编辑界面，显示 JavaScript 代码和一个云图标。"
categories:
  - "资源攻略"
tags:
  - "cloudflare"
---

# CloudFlare Workers 反代任意网站和挂载单页代码

> 本文同步自 [jiami.dog 官方原文](https://jiami.dog/2715.html)，以官网版本为准。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/10/951862000.png?ssl=1)

## 介绍

CloudFlare Workers是一个支持jsproxy的无服务器函数服务，提供全球CDN支持，免费用户有每天10万请求额度；
CloudFlare官网：https://dash.[cloudflare](https://jiami.dog/tag/cloudflare "cloudflare").com

## Workers 单页挂载代码

```
addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request))
})

// HTML代码
let html = `
<!DOCTYPE html>
<html>
  <head><title>Test</title></head>
  <body><div>Hello world!</div></body>
</html>
`;

/**
 * Respond to the request
 * @param {Request} request
 */
async function handleRequest(request) {
  return new Response(html, {
    headers: {
      'Content-Type': 'text/html; charset=UTF-8'
    },
    status: 200
  })
}
```

## Workers 反代任意网站

替换掉其中的`sunpma.com`为你需要反代的网址即可；

```
// Website you intended to retrieve for users.
const upstream = 'sunpma.com'

// Custom pathname for the upstream website.
const upstream_path = '/'

// Website you intended to retrieve for users using mobile devices.
const upstream_mobile = 'sunpma.com'

// Countries and regions where you wish to suspend your service.
const blocked_region = ['KP', 'SY', 'PK', 'CU']

// IP addresses which you wish to block from using your service.
const blocked_ip_address = ['0.0.0.0', '127.0.0.1']

// Whether to use HTTPS protocol for upstream address.
const https = true

// Whether to disable cache.
const disable_cache = false

// Replace texts.
const replace_dict = {
    '$upstream': '$custom_domain',
    '//sunpma.com': ''
}

addEventListener('fetch', event => {
    event.respondWith(fetchAndApply(event.request));
})

async function fetchAndApply(request) {
    const region = request.headers.get('cf-ipcountry').toUpperCase();
    const ip_address = request.headers.get('cf-connecting-ip');
    const user_agent = request.headers.get('user-agent');

    let response = null;
    let url = new URL(request.url);
    let url_hostname = url.hostname;

    if (https == true) {
        url.protocol = 'https:';
    } else {
        url.protocol = 'http:';
    }

    if (await device_status(user_agent)) {
        var upstream_domain = upstream;
    } else {
        var upstream_domain = upstream_mobile;
    }

    url.host = upstream_domain;
    if (url.pathname == '/') {
        url.pathname = upstream_path;
    } else {
        url.pathname = upstream_path + url.pathname;
    }

    if (blocked_region.includes(region)) {
        response = new Response('Access denied: WorkersProxy is not available in your region yet.', {
            status: 403
        });
    } else if (blocked_ip_address.includes(ip_address)) {
        response = new Response('Access denied: Your IP address is blocked by WorkersProxy.', {
            status: 403
        });
    } else {
        let method = request.method;
        let request_headers = request.headers;
        let new_request_headers = new Headers(request_headers);

        new_request_headers.set('Host', upstream_domain);
        new_request_headers.set('Referer', url.protocol + '//' + url_hostname);

        let original_response = await fetch(url.href, {
            method: method,
            headers: new_request_headers
        })

        connection_upgrade = new_request_headers.get("Upgrade");
        if (connection_upgrade && connection_upgrade.toLowerCase() == "websocket") {
            return original_response;
        }

        let original_response_clone = original_response.clone();
        let original_text = null;
        let response_headers = original_response.headers;
        let new_response_headers = new Headers(response_headers);
        let status = original_response.status;

        if (disable_cache) {
            new_response_headers.set('Cache-Control', 'no-store');
        }

        new_response_headers.set('access-control-allow-origin', '*');
        new_response_headers.set('access-control-allow-credentials', true);
        new_response_headers.delete('content-security-policy');
        new_response_headers.delete('content-security-policy-report-only');
        new_response_headers.delete('clear-site-data');

        if (new_response_headers.get("x-pjax-url")) {
            new_response_headers.set("x-pjax-url", response_headers.get("x-pjax-url").replace("//" + upstream_domain, "//" + url_hostname));
        }

        const content_type = new_response_headers.get('content-type');
        if (content_type != null && content_type.includes('text/html') && content_type.includes('UTF-8')) {
            original_text = await replace_response_text(original_response_clone, upstream_domain, url_hostname);
        } else {
            original_text = original_response_clone.body
        }

        response = new Response(original_text, {
            status,
            headers: new_response_headers
        })
    }
    return response;
}

async function replace_response_text(response, upstream_domain, host_name) {
    let text = await response.text()

    var i, j;
    for (i in replace_dict) {
        j = replace_dict[i]
        if (i == '$upstream') {
            i = upstream_domain
        } else if (i == '$custom_domain') {
            i = host_name
        }

        if (j == '$upstream') {
            j = upstream_domain
        } else if (j == '$custom_domain') {
            j = host_name
        }

        let re = new RegExp(i, 'g')
        text = text.replace(re, j);
    }
    return text;
}


async function device_status(user_agent_info) {
    var agents = ["Android", "iPhone", "SymbianOS", "Windows Phone", "iPad", "iPod"];
    var flag = true;
    for (var v = 0; v < agents.length; v++) {
        if (user_agent_info.indexOf(agents[v]) > 0) {
            flag = false;
            break;
        }
    }
    return flag;
}
```
