---
title: "GDIndex基于CloudFlare搭建无服务器谷歌网盘目录网站实现直链下载"
slug: "gdindex-builds-a-serverless-google-online-disk-directory"
source_id: "2728"
canonical_url: "https://jiami.dog/2728.html"
date_local: "2021-10-06T15:49:23"
date_published: "2021-10-06T07:49:23Z"
date_modified_local: "2021-10-06T15:51:47"
date_modified: "2021-10-06T07:51:47Z"
draft: false
featured_image_url: "https://jiami.dog/wp-content/uploads/2021/10/4069086383.jpg"
featured_image_alt: "一位金发女士手持文件，旁边是Google Drive的标志，下方文字说明“GDIndex 无服务器搭建 Google Drive 目录程序”。"
categories:
  - "资源攻略"
tags:
  - "cloudflare"
  - "谷歌"
---

# GDIndex基于CloudFlare搭建无服务器谷歌网盘目录网站实现直链下载

> 本文同步自 [jiami.dog 官方原文](https://jiami.dog/2728.html)，以官网版本为准。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/10/4069086383.jpg?ssl=1)

## 介绍

`GDIndex`是一个可以在`CloudFlare Workers`上架设`Google Drive`的目录程序，并提供许多功能

- 前端使用 Vue 完成
- 查看图片不用另开新窗口
- 视频播放器支持字幕(目前只支持 srt)
- 支持在线阅读 PDF, EPUB
- 不支持目录加密(.password)
- 支持 Http Basic Auth
- 无需修改程序，即可接入多个云端硬盘
- 支持用户名密码访问
- 支持在线文件上传
- 支持直链
- **国内用户可直接下载，无需科学上网**

`GitHub`项目地址：<https://github.com/sunpma/goIndex>
项目预览：[https://gdindex-demo.maple3142.workers.dev](https://gdindex-demo.maple3142.workers.dev/)

## 搭建

### 第一步

首先前往`https://gdindex-code-builder.glitch.me`获取`GDIndex`代码
![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/10/3181388191.png?resize=695%2C936&ssl=1)
`默认根ID`说明：`默认根ID`即是打开网站默认显示的网盘目录
`Google Drive`团队盘的ID`https://drive.google.com/drive/folders/****`其中的`****`即为团队盘ID
整个团队盘和每个文件夹都有一个固定ID

### 第二部

前往`CloudFlare Workers`新建一个`Worker`
![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/10/4247502607.png?resize=1106%2C566&ssl=1)
然后用`GDIndex`生成的代码替换掉`CloudFlare Workers`默认代码，最后点击`保存并部署`即可；
![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/10/2812926139.png?resize=809%2C980&ssl=1)

## 搭建完毕

---

## 继续阅读与讨论

- 分类：[资源攻略](../../../categories/ziyuan-gonglue.md)
- 主题：[cloudflare](../../../tags/cloudflare.md), [谷歌](../../../tags/谷歌.md)
- [在官网参与本文评论](https://jiami.dog/2728.html#jiami-giscus-comments)
- [浏览 GitHub 文章评论区](https://github.com/JiamiDog/jiami.dog/discussions/categories/article-comments)
- [返回全部文章](../../../INDEX.md)
