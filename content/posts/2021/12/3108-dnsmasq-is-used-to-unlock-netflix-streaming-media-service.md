---
title: "最新使用Dnsmasq来解锁Netflix（奈飞）流媒体服务"
slug: "dnsmasq-is-used-to-unlock-netflix-streaming-media-service"
source_id: "3108"
canonical_url: "https://jiami.dog/3108.html"
date_local: "2021-12-25T23:32:58"
date_published: "2021-12-25T15:32:58Z"
date_modified_local: "2021-12-25T23:33:51"
date_modified: "2021-12-25T15:33:51Z"
draft: false
featured_image_url: "https://jiami.dog/wp-content/uploads/2021/12/1640446307-20211225232923.png"
featured_image_alt: "Netflix标志和多部影视作品海报拼贴"
categories:
  - "资源攻略"
tags:
  - "dns"
  - "netflix"
  - "解锁"
---

# 最新使用Dnsmasq来解锁Netflix（奈飞）流媒体服务

> 本文同步自 [jiami.dog 官方原文](https://jiami.dog/3108.html)，以官网版本为准。

![Netflix标志和多部影视作品海报拼贴](https://jiami.dog/wp-content/uploads/2021/12/1640446307-20211225232923.png)

> 现在奈飞封IP封的厉害，导致好多VPS看不了，买到能看的IP吧，速度又欠佳，所以才有了这篇文章。简单说说原理：在一台能看Netflix的IP配置Netflix[解锁](https://jiami.dog/tag/unlock "解锁")脚本，然后其他不能看Netflix的机器使用这个能看的机器的DNS，达到能看的目的。

脚本支持系统：CentOS 6+, Debian8+, Ubuntu16+CentOS6/7 测试成功
Debian8+, Ubuntu16+ 测试成功

### 安装方法

```
wget --no-check-certificate -O dnsmasq_sniproxy.sh https://raw.githubusercontent.com/myxuchangbin/dnsmasq_sniproxy_install/master/dnsmasq_sniproxy.sh && bash dnsmasq_sniproxy.sh -f
```

### 卸载方法

```
wget --no-check-certificate -O dnsmasq_sniproxy.sh https://github.com/myxuchangbin/dnsmasq_sniproxy_install/raw/master/dnsmasq_sniproxy.sh && bash dnsmasq_sniproxy.sh -u
```

### 使用方法

- 先在能看的机器上执行安装代码，然后将其他小鸡的的DNS地址修改为这个主机的IP即可，如果不能用，只保留一个DNS试一下。
- 为防止滥用，建议不要随意公布IP地址；或者使用防火墙来限制外部IP访问。
- 本脚本只用作解锁流媒体使用，不能用来FQ。

### 作者Github地址

<https://github.com/myxuchangbin/dnsmasq_sniproxy_install>

---

## 继续阅读与讨论

- 分类：[资源攻略](../../../categories/ziyuan-gonglue.md)
- 主题：[dns](../../../tags/dns.md), [netflix](../../../tags/netflix.md), [解锁](../../../tags/解锁.md)
- [在官网参与本文评论](https://jiami.dog/3108.html#jiami-giscus-comments)
- [浏览 GitHub 文章评论区](https://github.com/JiamiDog/jiami.dog/discussions/categories/article-comments)
- [返回全部文章](../../../INDEX.md)
