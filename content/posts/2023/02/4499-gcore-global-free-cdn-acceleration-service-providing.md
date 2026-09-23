---
title: "Gcore全球免费CDN加速服务，提供每月1000GB流量"
slug: "gcore-global-free-cdn-acceleration-service-providing"
source_id: "4499"
canonical_url: "https://jiami.dog/4499.html"
date_local: "2023-02-01T14:45:31"
date_published: "2023-02-01T06:45:31Z"
date_modified_local: "2026-07-30T14:38:16"
date_modified: "2026-07-30T06:38:16Z"
draft: false
featured_image_url: "https://jiami.dog/wp-content/uploads/2023/02/d21de9952a984bf12873cdf32e9e0386.jpg"
featured_image_alt: "Gcore账户注册页面，包含邮箱、国家、密码输入框，以及“使用Promo Code”选项。"
categories:
  - "资源攻略"
tags:
  - "cdn"
  - "ssl"
---

# Gcore全球免费CDN加速服务，提供每月1000GB流量

> 本文同步自 [jiami.dog 官方原文](https://jiami.dog/4499.html)，以官网版本为准。

## 前言

Gcore 是公共云和边缘计算、内容交付、托管和安全解决方案的国际领导者。我们管理一个全球基础设施，旨在为企业级企业提供一流的边缘和基于云的服务。Gcore 总部位于卢森堡，在德国、立陶宛、波兰、格鲁吉亚和塞浦路斯设有办事处。

## Gcore 提供免费CDN套餐

每个月1000GB流量

每月10亿次请求

官方有140+节点加速（免费计划每月那么多）

支持SSL支持WebSocket提供DDoS防护，基础WAF

不用绑定信用卡

## 开始教程

第一步：帐号注册注册地址：https://auth.gcore.com/login/signup填写邮箱，密码，邮箱接收激活优化（收不到查看垃圾箱） ![](https://i0.wp.com/jiami.dog/wp-content/uploads/2023/02/d21de9952a984bf12873cdf32e9e0386.jpg?ssl=1)  第二步：选择免费计划（无需填信用卡） ![](https://i0.wp.com/jiami.dog/wp-content/uploads/2023/02/8d4596d046eee65a6c26fa159c1ad4d6.jpg?ssl=1)   ![](https://i0.wp.com/jiami.dog/wp-content/uploads/2023/02/5b26cf1612e1e0e134220f670d9e287e.jpg?ssl=1)  第三步：[配置CDN账号配置成功后](https://jiami.dog/4632.html)，可见CDN服务已经激活（Active）官方提供2种配置方式：① 加速和保护整个站点使用 CDN 和 DNS 服务对整个站点进行无代码加速和网络层保护。免费计划会自动激活 DNS 服务。（需要修改DNS，不推荐）② 仅加速和保护静态资产使用 CDN 服务对您网站的静态资产进行加速和网络层保护。需要更改代码。（CNAME解析，推荐）1、选择第二项，开始配置CDN； ![](https://i0.wp.com/jiami.dog/wp-content/uploads/2023/02/1675233739-20230201144144.png?resize=1024%2C437&ssl=1)  2、填写基础信息：Origin（源站IP），Custom Demain （您加速的域名），SSL 加速； ![](https://i0.wp.com/jiami.dog/wp-content/uploads/2023/02/1675233806-20230201144302.png?resize=1024%2C431&ssl=1)  3、配置域名解析：自定义域名需要CNAME解析到指定的域名上； ![](https://i0.wp.com/jiami.dog/wp-content/uploads/2023/02/1a26f1247c86096662707300f7761b5a.jpg?ssl=1)  4、配置域名解析：如图为 阿里云 添加解析； ![](https://i0.wp.com/jiami.dog/wp-content/uploads/2023/02/2ec4f73e3f6dcc32b3d7574fd071bc13.jpg?ssl=1)  5、官方提供了一些集成插件，我们暂时不需要； ![](https://i0.wp.com/jiami.dog/wp-content/uploads/2023/02/d724089351f937f1810691dc1b17c327.jpg?ssl=1)  6、优化访问设置：因为我们主要是静态资源CDN加速，GZip可以开启，WebSocket也可以开启（看您需要），WAF防御也开启； ![](https://i0.wp.com/jiami.dog/wp-content/uploads/2023/02/b67ce09349040b523bab4ba65b027250.jpg?ssl=1)  7、提交以后CDN就创建成功了！ ![](https://i0.wp.com/jiami.dog/wp-content/uploads/2023/02/6d7d9628bc22ac5516cfdf30e875d33f.jpg?ssl=1)  8、域名CNAME解析生效需要等10分钟左右，如果开启SSL需要等待的更久一些（博主SSL生效大概等了20分钟左右）；9、请注意，如果站点开启了SSL，请在CDN中开启TLS Version，开启Forward Header，Origin pull protocol选择HTTPS。其实Gcore比Cloudflare大陆访问快，但是不好配置，所以用的人少，也好，不会被滥用，Gcore是全球网络，境外的Gcore是Anycast的，Cloudflare的Antcast在美国东海岸，CF免费版没有香港和中国大陆节点，而Gcore有香港节点，Gcore 官宣免费版有140+节点。
