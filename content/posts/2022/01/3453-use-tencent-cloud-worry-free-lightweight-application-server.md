---
title: "使用腾讯云无忧轻量应用服务器搭建YOURLS: Your Own URL Shortener"
slug: "use-tencent-cloud-worry-free-lightweight-application-server"
source_id: "3453"
canonical_url: "https://jiami.dog/3453.html"
date_local: "2022-01-12T23:55:42"
date_published: "2022-01-12T15:55:42Z"
date_modified_local: "2022-01-13T00:04:06"
date_modified: "2022-01-12T16:04:06Z"
draft: false
featured_image_url: "https://jiami.dog/wp-content/uploads/2022/01/1679091c5a880faf6fb5e6087eb1b2dc.png"
featured_image_alt: "YOURLS网址缩短服务后台管理界面，显示URL列表、统计信息和搜索筛选功能。"
categories:
  - "资源攻略"
tags:
  - "YOURLS"
  - "宝塔"
---

# 使用腾讯云无忧轻量应用服务器搭建YOURLS: Your Own URL Shortener

> 本文同步自 [jiami.dog 官方原文](https://jiami.dog/3453.html)，以官网版本为准。

## 腾讯云轻量应用服务器首单限时秒杀

国内云服务器已经内卷到疯狂的地步了，**[腾讯云上海地区轻量应用服务器4核16G内存12Mbps BGP带宽一年￥370/三年￥1109](https://curl.qcloud.com/xy0VnRpi)**。

### 活动对象

腾讯云官网已注册并已完成实名认证的国内站用户，并且未购买过轻量应用服务器v3。

### 活动套餐

| 配置 | 流量 | 价格 | 购买链接 |
| --- | --- | --- | --- |
| 轻量  4vCPU/16G/120G SSD/1\*IPv4 | 200GB@12Mbps | [￥370/年](https://curl.qcloud.com/xy0VnRpi)  ￥1109/年 | [**点击购买**](https://curl.qcloud.com/xy0VnRpi) |
| 轻量  1vCPU/2G/50G SSD/1\*IPv4 | 500GB@5Mbps | [￥38/年](https://curl.qcloud.com/xy0VnRpi) | [**点击购买**](https://curl.qcloud.com/xy0VnRpi) |
| 轻量  2vCPU/4G/80G SSD/1\*IPv4 | 1200GB@8Mbps | [￥70/年](https://curl.qcloud.com/xy0VnRpi)  ￥222/三年 | [**点击购买**](https://curl.qcloud.com/xy0VnRpi) |

## 配置服务器

## 搭建过程

### 1.安装[宝塔](https://jiami.dog/tag/pagoda "宝塔")

默认安装的是CentOS，这里重置为应用镜像宝塔Linux面板 7.6.0 腾讯云专享版，安装成功后应用管理可以找到面板相关信息，注意将面板端口添加到防火墙。

> 宝塔Linux面板（BT-Panel）是一款简单好用的服务器运维面板，支持一键LAMP/LNMP/集群/监控/网站/FTP/数据库/JAVA等100多项服务器管理功能，能够极大提升运维管理效率。宝塔面板腾讯云专享版由腾讯云与堡塔公司联合开发，与普通版相比，专享版默认集成腾讯云COSFS、CDN和DNS解析插件，让用户更便捷的使用宝塔面板对腾讯云产品进行管理和操作。该镜像基于CentOS 7.8 64位操作系统。（注：创建实例完成后请在防火墙设置中打开面板端口。）

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/c81e728d9d4c2f636f067f89cc14862c.png?resize=600%2C249&ssl=1)

### 2.宝塔添加站点

没有备案，这里直接用IP演示。
![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/eccbc87e4b5ce2fe28308fd9f2a7baf3.png?resize=600%2C625&ssl=1)

### 3.安装[YOURLS](https://jiami.dog/tag/yourls "YOURLS")

#### 建议安装环境：

Nginx 1.20
PHP 7.2.0+
MySQL 5+

#### YourLS官方下载地址

<https://github.com/YOURLS/YOURLS/releases>

通过宝塔上传至网站根目录并解压。
![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/a87ff679a2f3e71d9181a67b7542122c.png?resize=600%2C284&ssl=1)

#### 配置伪静态规则

```
try_files $uri $uri/ @rewrite;
location @rewrite {
rewrite ^/([\w-]+\+?)/?$ /yourls-loader.php?id=$1 last;
}
```

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/b37c8dd8b83fce9b7239550976117d7b.png?resize=600%2C556&ssl=1)

将默认配置文件 user/config-sample.php 重命名为 user/config.php 并配置以下内容

<https://github.com/BotMom/EUserv_extend/raw/main/code.txt>

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/8f14e45fceea167a5a36dedd4bea2543.png?resize=600%2C384&ssl=1)
![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/beb44b5808bc259515b0ada3cd8d5c0f.png?resize=600%2C278&ssl=1)

访问http://yourdomain/admin/点击Install YOURLS即可
![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/0c24bb846d86e3df3d1262880dfb1c70.png?resize=600%2C273&ssl=1)

#### 后台管理地址

<http://yourdomain/admin/>
![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/1679091c5a880faf6fb5e6087eb1b2dc.png?resize=600%2C341&ssl=1)

---

## 继续阅读与讨论

- 分类：[资源攻略](../../../categories/ziyuan-gonglue.md)
- 主题：[YOURLS](../../../tags/yourls.md), [宝塔](../../../tags/宝塔.md)
- [在官网参与本文评论](https://jiami.dog/3453.html#jiami-giscus-comments)
- [浏览 GitHub 文章评论区](https://github.com/JiamiDog/jiami.dog/discussions/categories/article-comments)
- [返回全部文章](../../../INDEX.md)
