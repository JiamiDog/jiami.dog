---
title: "一键CDN脚本，支持设置与SSL证书一键导入导出"
slug: "one-click-cdn-script-supports-one-click-import-and-export"
source_id: "3110"
canonical_url: "https://jiami.dog/3110.html"
date_local: "2021-12-26T00:33:50"
date_published: "2021-12-25T16:33:50Z"
date_modified_local: "2026-07-30T14:38:18"
date_modified: "2026-07-30T06:38:18Z"
draft: false
featured_image_url: "https://jiami.dog/wp-content/uploads/2021/12/1640449829-20211226002822-1.png"
featured_image_alt: "Ubuntu系统下运行的Traffic Server CDN安装脚本界面"
categories:
  - "资源攻略"
tags:
  - "cdn"
  - "ssl"
---

# 一键CDN脚本，支持设置与SSL证书一键导入导出

> 本文同步自 [jiami.dog 官方原文](https://jiami.dog/3110.html)，以官网版本为准。

> 支持Ubuntu 20, Debian 10/11, CentOS 7/8等系统。

## 一键CDN脚本功能简介：

- 自动将您的VPS（512 MB内存即可）部署为CDN节点
- 自动引导配置网站、设置重写规则、配置SSL证书
- 可以一键Let’s Encrypt证书并开启OCSP装订
- 配置缓存规则
- 添加删除网站、修改IP、等等
- 查看日志与统计
- 高级缓存控制
- 备份CDN设置与SSL证书，实现多节点快速导入到处设定
- 支持中英文
- 等等…

## 系统环境要求

目前支持Ubuntu 20.04 LTS, Debian 10, Debian 11, CentOS 7/8操作系统。

CDN服务器正常运行时仅需要系统有500MB的内存。但是，程序第一次编译安装的时候需要1500MB左右的内存。若您的VPS内存不够，可以加一些Swap.

需要注意的是，该脚本需要安装在新装的操作系统中。该程序和其他面板（比如宝塔，cPanel, Directadmin）等不兼容。毕竟，装CDN程序的节点上也不应该搭建其他程序的。

## 安装

### 原版（英文界面）

```
wget https://raw.githubusercontent.com/Har-Kuun/OneClickCDN/master/OneClickCDN.sh && sudo bash OneClickCDN.sh
```

### 中文版

```
wget https://raw.githubusercontent.com/Har-Kuun/OneClickCDN/master/translation/translated_scripts/OneClickCDN_zh-CN.sh && sudo bash OneClickCDN_zh-CN.sh
```

第一次运行时，程序会提示自动编译安装Traffic Server.  安装完毕后，程序会引导新建CDN网站，[自动签发SSL, 等等](https://jiami.dog/4632.html)。您需要将您网站的域名设置A记录解析到这台VPS的IP地址上。

您也可以随时重新运行该脚本，用来管理您的服务器上部署的CDN网站，查看网站统计，等等。

## 使用

### 1，使用脚本部署CDN节点

### 2，将域名解析到CDN节点

### 3，在CDN节点上添加源站信息

### 4，开始使用！

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/12/1640449829-20211226002822-1.png?resize=650%2C558&ssl=1)

## 实现的功能

首先，最基本的功能就是CDN.  安装后，程序就会将您的VPS变成一个高性能CDN节点，用来加速和缓存您的网站。

同时，脚本支持一键设置SSL, 您可以提供您自己的SSL证书，或者也可以一键签发免费的Let’s Encrypt证书，并且开启OCSP装订。

脚本还支持随时增添新的CDN网站。您只需要根据脚本引导，输入网址和源站IP地址，即可分分钟添加CDN网址。您可以使用脚本管理CDN网站，查看网站数据，清除缓存，等等。

2021年12月12日新增：目前已支持配置与SSL证书导入导出，可以快速在多个CDN节点中实现同步配置网站。

**已开源：<https://github.com/Har-Kuun/OneClickCDN/>**
