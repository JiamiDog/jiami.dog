---
title: "yourls 结合宝塔搭建私人短链接服务"
slug: "yourls-combined-with-pagoda-to-build-private-short-link"
source_id: "2757"
canonical_url: "https://jiami.dog/2757.html"
date_local: "2021-10-11T14:54:58"
date_published: "2021-10-11T06:54:58Z"
date_modified_local: "2022-01-13T00:23:13"
date_modified: "2022-01-12T16:23:13Z"
draft: false
featured_image_url: "https://jiami.dog/wp-content/uploads/2022/01/0c24bb846d86e3df3d1262880dfb1c70.png"
featured_image_alt: "YOURLS安装页面，显示“Install YOURLS”按钮。"
categories:
  - "资源攻略"
tags:
  - "YOURLS"
  - "宝塔"
  - "短链接"
---

# yourls 结合宝塔搭建私人短链接服务

> 本文同步自 [jiami.dog 官方原文](https://jiami.dog/2757.html)，以官网版本为准。

![YOURLS安装页面，显示“Install YOURLS”按钮。](https://jiami.dog/wp-content/uploads/2022/01/0c24bb846d86e3df3d1262880dfb1c70.png)

突然对短网址转换程序感了兴趣，搜索了下找到一个开源的短网址程序 [YOURLS](https://jiami.dog/tag/yourls "YOURLS") ，于是利用[宝塔](https://jiami.dog/tag/pagoda "宝塔")面板搭建了一个，期间走了一些小弯路记录下搭建过程

## 程序说明

YOURLS stands for Your Own URL Shortener. It is a small set of PHP scripts that will allow you to run your own URL shortening service (a la TinyURL or Bitly).Running your own URL shortener is fun, geeky and useful: you own your data and don’t depend on third-party services. It’s also a great way to add branding to your short URLs, instead of using the same public URL shortener everyone uses.

## 程序特点

- 免费和开源软件
- 私人（仅限您的链接）或公共（每个人都可以创建[短链接](https://jiami.dog/tag/short-link "短链接")，适用于内部网）
- 出色的插件架构和数十个插件，可轻松实现新功能
- 方便的书签可轻松缩短和共享链接
- 很棒的统计数据：历史点击报告、引荐来源跟踪、访问者地理位置
- 开发人员 API 将您的应用程序集成到其他应用程序中
- 友好的安装人员，
- 用于创建您自己的公共界面等的示例文件！

## 准备工作

装好宝塔面板的 VPS 一台，域名一个（越短越好），首先把域名解析到 VPS 上面。

## 开始搭建

### 添加站点

进入宝塔面板后台点击添加站点

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/8d12df7dc948516bbf994eff341085d7.png?ssl=1)

填写必要的信息，域名，数据库名称和密码

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/5bf0508fd502415f54baa4046cd9e8cb.png?ssl=1)

### 下载源码

然后去 YOURLS GETHUB 项目下载最新源码  **[下载 YOURLS](https://github.com/YOURLS/YOURLS/releases)**

### 修改配置文件

下载到本地然后解压打开，找到 `user` 目录打开在 user 目录下有个 `config-sample.php` 文件，复制一份改名为 `config.php`

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/dc1f96794126aa81655329b43326f76e.png?ssl=1)

### 配置数据库

打开 `config.php` 修改里面的数据库参数 `YOURLS_DB_USER` 是代表数据库用户，`YOURLS_DB_PASS` 代表数据库密码，`YOURLS_DB_NAME` 代表数据库名称，就拿三个数据的值都是 `yourl` 演示如下:

|  | /\*\* MySQL database username \*/ |
| --- | --- |
|  | define( ‘YOURLS\_DB\_USER’, ‘yourl’ ); |
|  |  |
|  | /\*\* MySQL database password \*/ |
|  | define( ‘YOURLS\_DB\_PASS’, ‘yourl’ ); |
|  |  |
|  | /\*\* The name of the database for YOURLS |
|  | \*\* Use lower case letters [a-z], digits [0-9] and underscores [\_] only \*/ |
|  | define( ‘YOURLS\_DB\_NAME’, ‘yourl’ ); |
|  |  |
|  | /\*\* MySQL hostname. |
|  | \*\* If using a non standard port, specify it like ‘hostname:port’, e.g. ‘localhost:9999’ or ‘127.0.0.1:666’ \*/ |
|  | define( ‘YOURLS\_DB\_HOST’, ‘localhost’ ); |
|  |  |
|  | /\*\* MySQL tables prefix |
|  | \*\* YOURLS will create tables using this prefix (eg `yourls\_url`, `yourls\_options`, …😉 |
|  | \*\* Use lower case letters [a-z], digits [0-9] and underscores [\_] only \*/ |
|  | define( ‘YOURLS\_DB\_PREFIX’, ‘yourls\_’ ); |
|  |  |

### 配置站点地址

找到 `define( 'YOURLS_SITE', 'http://your-own-domain-here.com' );` 修改为 `define( 'YOURLS_SITE', '你的域名' );`

注意：最后不要加 `/` 符号。

### 配置语言文件

[下载中文语言包](https://github.com/ZvonimirSun/YOURLS-zh_CN/releases) [本地中文包](https://jiamidog.lanzoup.com/i8mbBypbvof)，放到 `/user/languages` 下，在 `config.php` 里找到 `define( 'YOURLS_LANG', '' );` 更改为 `define( 'YOURLS_LANG', 'zh-CN' );`

### 设置长链接对应一个或多个短地址

在 `config.php` 里找到 `define( 'YOURLS_UNIQUE_URLS', true );` 默认是 `true` 一个长链接只能生成一个短地址。

### 设置是否公开

在 `config.php` 里找到 `define( 'YOURLS_PRIVATE', true );` 如果是 `true` 是不公开，只能登陆后生成短地址；设置为 `false` 为公开使用，无需登陆便可以生成短地址，看你的想法了。

### 设置 cookie 密匙

在 `config.php` 里找到 `define( 'YOURLS_COOKIEKEY', 'modify this text with something random' );` 修改为 `'modify this text with something random'`一个数组作为你的 cookie 密匙，可以在 `https://api.yourls.org/services/cookiekey/1.0` 里直接生成：

|  | define( ‘YOURLS\_COOKIEKEY’, ‘y7YaHNM~VQP}%C[dPjV6HhEwEnLSh]\_KT~7|WKYx’ ); |
| --- | --- |

### 设置管理员账户

比如设置管理员账号为 `admin` 密码是 `123456` 在 `config.php` 里找到

|  | $yourls\_user\_passwords = [ |
| --- | --- |
|  | ‘username’ => ‘password’, |
|  | // ‘username2’ => ‘password2’, |
|  | // You can have one or more ‘login’=>’password’ lines |
|  | ]; |

这段代码，修改如下

|  | $yourls\_user\_passwords = array( |
| --- | --- |
|  | ‘admin’ => ‘123456’, |
|  | // ‘username2’ => ‘password2’, |
|  | // You can have one or more ‘login’=>’password’ lines |
|  | ); |

### 上传源码

然后打开宝塔面板进入后台，点击 网站 找到要架设的网站 点击网站目录上的链接如图

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/bffce4d229ab4b5926d94032435b1451.png?ssl=1)

然后点击 上传

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/29ddef23cc81b9e420a0021c1b46eea7.png?ssl=1)

选择 上传目录 找到你下载的源码根目录，点击上传，系统会提示你是否上传此目录下所有文件，然后点击 上传 按钮，最后点击最下方的 上传 按钮，等待几分钟后等所有文件上传完毕。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/a0787b137294ea5d4f0de692d9fc1ddf.png?ssl=1)

### 配置伪静态

打开宝塔面板，点击网站 找到 设置 再找到里面的 伪静态 ，添入如下代码：

|  | location / { |
| --- | --- |
|  | try\_files $uri $uri/ /yourls-loader.php$is\_args$args; |
|  | } |

点击 保存 。

### 安装 YOURLS

在浏览器里打开 `http://你的域名/admin` 会跳转到安装页面，点击 `INSTALL YOURLS` 按钮开始安装。接着打开 `http://你的域名/admin` 输入账号 `admin` 密码 `123456` 开始使用。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/286b7e9cfa9311b83bd11c3d085d4674.png?ssl=1)

---

## 继续阅读与讨论

- 分类：[资源攻略](../../../categories/ziyuan-gonglue.md)
- 主题：[YOURLS](../../../tags/yourls.md), [宝塔](../../../tags/宝塔.md), [短链接](../../../tags/短链接.md)
- [在官网参与本文评论](https://jiami.dog/2757.html#jiami-giscus-comments)
- [浏览 GitHub 文章评论区](https://github.com/JiamiDog/jiami.dog/discussions/categories/article-comments)
- [返回全部文章](../../../INDEX.md)
