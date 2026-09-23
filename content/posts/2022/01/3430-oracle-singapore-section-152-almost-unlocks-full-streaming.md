---
title: "甲骨文新加坡 152段几乎解锁全流媒体，附无限换IP的方法"
slug: "oracle-singapore-section-152-almost-unlocks-full-streaming"
source_id: "3430"
canonical_url: "https://jiami.dog/3430.html"
date_local: "2022-01-12T19:10:02"
date_published: "2022-01-12T11:10:02Z"
date_modified_local: "2022-01-12T19:19:21"
date_modified: "2022-01-12T11:19:21Z"
draft: false
featured_image_url: "https://jiami.dog/wp-content/uploads/2022/01/1641985600-photo_2022-01-12_18-56-14.jpg"
featured_image_alt: "Oracle Cloud服务器的IPv4解锁测试结果，显示多个流媒体服务在新加坡区域的解锁状态。"
categories:
  - "资源攻略"
tags:
  - "甲骨文"
  - "解锁"
---

# 甲骨文新加坡 152段几乎解锁全流媒体，附无限换IP的方法

> 本文同步自 [jiami.dog 官方原文](https://jiami.dog/3430.html)，以官网版本为准。

![Oracle Cloud服务器的IPv4解锁测试结果，显示多个流媒体服务在新加坡区域的解锁状态。](https://jiami.dog/wp-content/uploads/2022/01/1641985600-photo_2022-01-12_18-56-14.jpg)

昨天听说[甲骨文](https://jiami.dog/tag/oracle "甲骨文")新出的152，138 IP 段可以[解锁](https://jiami.dog/tag/unlock "解锁")全流媒体，于是试了试，果然如此：

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/1641986218-photo_2022-01-12_18-56-14.jpg?resize=577%2C413&ssl=1)

甲骨文的IP是可以无限换的，这里把方法发给大家，同时[检测流媒体解锁，用这个一键脚本](https://cnwebmasters.com/157.html)即可。

甲骨文 / Oracle是可以无限换IP的，但有朋友是通过删除实例，然后再创建实例来实现换IP的，显然，这是小题大做了，现教大家如何在不动实例的情况下快速更换甲骨文 / oracle的IP

![《甲骨文 / oracle 换IP的方法》](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/031c7c0ea1cc8d588020d0625bbb7a73.png?ssl=1)

进入实例，来到：附加的 VNIC

![《甲骨文 / oracle 换IP的方法》](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/f6a0a1d053f4e9fa5c5418d63bc3a7b9.png?ssl=1)

查看详细信息

![《甲骨文 / oracle 换IP的方法》](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/8f2a4925a994540cf043f6f0114f6694.png?ssl=1)

进入：IP 地址

![《甲骨文 / oracle 换IP的方法》](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/778ec67629edd056a13d7f717f446fa5.png?ssl=1)

编辑

![《甲骨文 / oracle 换IP的方法》](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/7f2634a5329a94e188af4f8f341fd953.png?ssl=1)

选择：没有公共 IP并更新

![《甲骨文 / oracle 换IP的方法》](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/621f237b54089d33d0ca89a3bfe30dbd.png?ssl=1)

没有公共 IP了

![《甲骨文 / oracle 换IP的方法》](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/7650af172c655686e7a48409d539d6d6.png?ssl=1)

编辑

![《甲骨文 / oracle 换IP的方法》](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/280d9dcef01c64140bf3bb2f4a820a35.png?ssl=1)

选择：临时公共 IP并更新

![《甲骨文 / oracle 换IP的方法》](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/6e770777a2eac49036742e1329c1be5a.png?ssl=1)

更换IP成功

![《甲骨文 / oracle 换IP的方法》](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/b4ef71401aa0f13b16581aa27d3237f8.png?ssl=1)

---

## 继续阅读与讨论

- 分类：[资源攻略](../../../categories/ziyuan-gonglue.md)
- 主题：[甲骨文](../../../tags/甲骨文.md), [解锁](../../../tags/解锁.md)
- [在官网参与本文评论](https://jiami.dog/3430.html#jiami-giscus-comments)
- [浏览 GitHub 文章评论区](https://github.com/JiamiDog/jiami.dog/discussions/categories/article-comments)
- [返回全部文章](../../../INDEX.md)
