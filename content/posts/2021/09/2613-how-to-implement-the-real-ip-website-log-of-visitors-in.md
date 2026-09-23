---
title: "如何在CloudFlare下Nginx实现访客真实IP网站日志？"
slug: "how-to-implement-the-real-ip-website-log-of-visitors-in"
source_id: "2613"
canonical_url: "https://jiami.dog/2613.html"
date_local: "2021-09-17T19:29:05"
date_published: "2021-09-17T11:29:05Z"
date_modified_local: "2021-09-19T20:18:19"
date_modified: "2021-09-19T12:18:19Z"
draft: false
featured_image_url: "https://jiami.dog/wp-content/uploads/2021/08/1629448984-480X300.png"
featured_image_alt: "加密狗文章默认略缩图"
categories:
  - "资源攻略"
tags:
  - "cloudflare"
  - "nginx"
---

# 如何在CloudFlare下Nginx实现访客真实IP网站日志？

> 本文同步自 [jiami.dog 官方原文](https://jiami.dog/2613.html)，以官网版本为准。

![加密狗文章默认略缩图](https://jiami.dog/wp-content/uploads/2021/08/1629448984-480X300.png)

做英文内容站套上Cloudflare CDN既可以加快访问速度又可以避免被攻击。可是如果需要通过网站日志分析蜘蛛来访，是否被采集、被攻击等情况，但日志上全部都是CDN（[cloudflare](https://jiami.dog/tag/cloudflare "cloudflare")）节点的 IP。那么在用CDN加速的同时，如何获取访客真实IP并记录到日志上呢？

查看CloudFlare官方文档[《Restoring original visitor IPs: Logging visitor IP addresses》](https://support.cloudflare.com/hc/en-us/articles/200170786-How-do-I-restore-original-visitor-IP-with-Nginx)，在这种情况下可以通过[nginx](https://jiami.dog/tag/nginx "nginx")的realip模块来获取用户的IP，这里以cloudflare和lnmp一键包为例。

## 1、为nginx添加with-http\_realip\_module模块

修改lnmp.conf文件，并且升级nginx即可。

```
cd /root/lnmp1.7
vi lnmp.conf
```

在lnmp.conf添加–with-http\_realip\_module，如下。

```
Nginx_Modules_Options='--with-http_realip_module'
```

升级nginx

```
./upgrade.sh nginx
```

在 <http://nginx.org/en/download.html> 查看版本，然后输入合适的版本。
等待升级完成即可。

## 2、设置nginx配置

修改网站的配置文件

`/usr/local/nginx/conf/nginx.conf`

在server后面的http{}中添加如下内容

```
set_real_ip_from 103.21.244.0/22;
set_real_ip_from 103.22.200.0/22;
set_real_ip_from 103.31.4.0/22;
set_real_ip_from 104.16.0.0/12;
set_real_ip_from 108.162.192.0/18;
set_real_ip_from 131.0.72.0/22;
set_real_ip_from 141.101.64.0/18;
set_real_ip_from 162.158.0.0/15;
set_real_ip_from 172.64.0.0/13;
set_real_ip_from 173.245.48.0/20;
set_real_ip_from 188.114.96.0/20;
set_real_ip_from 190.93.240.0/20;
set_real_ip_from 197.234.240.0/22;
set_real_ip_from 198.41.128.0/17;
set_real_ip_from 2400:cb00::/32;
set_real_ip_from 2606:4700::/32;
set_real_ip_from 2803:f800::/32;
set_real_ip_from 2405:b500::/32;
set_real_ip_from 2405:8100::/32;
set_real_ip_from 2c0f:f248::/32;
set_real_ip_from 2a06:98c0::/29;
real_ip_header CF-Connecting-IP;
real_ip_recursive on;
```

重载nginx配置生效：

```
/usr/local/nginx/sbin/nginx -s reload
```

以下是nginx.conf例子文件

```
user  www www;

worker_processes auto;
worker_cpu_affinity auto;

error_log  /home/wwwlogs/nginx_error.log  crit;

pid        /usr/local/nginx/logs/nginx.pid;

#Specifies the value for maximum file descriptors that can be opened by this process.
worker_rlimit_nofile 51200;

events
    {
        use epoll;
        worker_connections 51200;
        multi_accept off;
        accept_mutex off;
    }

http
    {
        include       mime.types;
        default_type  application/octet-stream;

        server_names_hash_bucket_size 128;
        client_header_buffer_size 32k;
        large_client_header_buffers 4 32k;
        client_max_body_size 50m;

        sendfile on;
        sendfile_max_chunk 512k;
        tcp_nopush on;

        keepalive_timeout 60;

        tcp_nodelay on;

        fastcgi_connect_timeout 300;
        fastcgi_send_timeout 300;
        fastcgi_read_timeout 300;
        fastcgi_buffer_size 64k;
        fastcgi_buffers 4 64k;
        fastcgi_busy_buffers_size 128k;
        fastcgi_temp_file_write_size 256k;

        gzip on;
        gzip_min_length  1k;
        gzip_buffers     4 16k;
        gzip_http_version 1.1;
        gzip_comp_level 2;
        gzip_types     text/plain application/javascript application/x-javascript text/javascript text/css application/xml application/xml+rss;
        gzip_vary on;
        gzip_proxied   expired no-cache no-store private auth;
        gzip_disable   "MSIE [1-6]\.";

        #limit_conn_zone $binary_remote_addr zone=perip:10m;
        ##If enable limit_conn_zone,add "limit_conn perip 10;" to server section.

        server_tokens off;
        access_log off;

		set_real_ip_from 103.21.244.0/22;
        set_real_ip_from 103.22.200.0/22;
        set_real_ip_from 103.31.4.0/22;
        set_real_ip_from 104.16.0.0/12;
        set_real_ip_from 108.162.192.0/18;
        set_real_ip_from 131.0.72.0/22;
        set_real_ip_from 141.101.64.0/18;
        set_real_ip_from 162.158.0.0/15;
        set_real_ip_from 172.64.0.0/13;
        set_real_ip_from 173.245.48.0/20;
        set_real_ip_from 188.114.96.0/20;
        set_real_ip_from 190.93.240.0/20;
        set_real_ip_from 197.234.240.0/22;
        set_real_ip_from 198.41.128.0/17;
        set_real_ip_from 2400:cb00::/32;
        set_real_ip_from 2606:4700::/32;
        set_real_ip_from 2803:f800::/32;
        set_real_ip_from 2405:b500::/32;
        set_real_ip_from 2405:8100::/32;
        set_real_ip_from 2c0f:f248::/32;
        set_real_ip_from 2a06:98c0::/29;
        real_ip_header CF-Connecting-IP;
        real_ip_recursive on;

server
    {
        listen 80 default_server reuseport;
        #listen [::]:80 default_server ipv6only=on;
        server_name _;
        index index.html index.htm index.php;
        root  /home/wwwroot/default;

        #error_page   404   /404.html;

        # Deny access to PHP files in specific directory
        #location ~ /(wp-content|uploads|wp-includes|images)/.*\.php$ { deny all; }

        location /lua
        {
            default_type text/html;
            content_by_lua 'ngx.say("hello world")';
        }

        include enable-php.conf;

        location /nginx_status
        {
            stub_status on;
            access_log   off;
        }

        location ~ .*\.(gif|jpg|jpeg|png|bmp|swf)$
        {
            expires      30d;
        }

        location ~ .*\.(js|css)?$
        {
            expires      12h;
        }

        location ~ /.well-known {
            allow all;
        }

        location ~ /\.
        {
            deny all;
        }

        access_log  /home/wwwlogs/access.log;
    }
include vhost/*.conf;
}
```
