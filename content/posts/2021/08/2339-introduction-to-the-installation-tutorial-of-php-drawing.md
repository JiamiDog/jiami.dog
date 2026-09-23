---
title: "PHP图床程序Chevereto安装教程介绍"
slug: "introduction-to-the-installation-tutorial-of-php-drawing"
source_id: "2339"
canonical_url: "https://jiami.dog/2339.html"
date_local: "2021-08-17T20:34:32"
date_published: "2021-08-17T12:34:32Z"
date_modified_local: "2021-08-17T20:35:42"
date_modified: "2021-08-17T12:35:42Z"
draft: false
featured_image_url: "https://jiami.dog/wp-content/uploads/2021/08/1629203673-6b6b294f399b8d15b7d5533ddf97eb1b-1.png"
featured_image_alt: "Chevereto图床程序的演示页面，背景为雪山湖泊，页面中央有“开始上传”按钮。"
categories:
  - "资源攻略"
tags:
  - "nginx"
  - "php"
---

# PHP图床程序Chevereto安装教程介绍

> 本文同步自 [jiami.dog 官方原文](https://jiami.dog/2339.html)，以官网版本为准。

![Chevereto图床程序的演示页面，背景为雪山湖泊，页面中央有“开始上传”按钮。](https://jiami.dog/wp-content/uploads/2021/08/1629203673-6b6b294f399b8d15b7d5533ddf97eb1b-1.png)

这是一款PHP的图床程序，有免费版和付费版。免费付费区别其实不大，仅仅是技术支持和版本更新的区别。

下面给大家介绍下这款程序以及安装的步骤。

官网：https://chevereto.com/

demo：https://demo.chevereto.com/

首页预览图如下

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/08/1629203673-6b6b294f399b8d15b7d5533ddf97eb1b.png?resize=1366%2C637&ssl=1)

安装要求：

Apache或Nginx Web服务器（推荐服务器）
PHP 5.6（推荐7.3）和标准库。
MySQL 8 / MariaDB 10

本人安装环境：[nginx](https://jiami.dog/tag/nginx "nginx")+PHP7.2+mysql5.6，使用的宝塔面板。

官方说是还需要安装PHP的一个扩展程序GD图像处理库，这个是涉及到图片的自动加水印等功能使用，本人没有安装这个支持库。

官方给出的安装文件是一个PHP文件，install.[php](https://jiami.dog/tag/php "php")

我们现需要在网站nginx配置文件中加入以下配置。

```
# Chevereto nginx generated rules for http://img.cheshirex.com/
## Disable access to sensitive files
location ~* /(app|content|lib)/.*\.(po|php|lock|sql)$ {
deny all;
}
## CORS headers
location ~* /.*\.(ttf|ttc|otf|eot|woff|woff2|font.css|css|js) {
add_header Access-Control-Allow-Origin "*";
}
## Upload path for image content only and set 404 replacement
location ^~ /images/ {
location ~* (jpe?g|png|gif) {
log_not_found off;
error_page 404 /content/images/system/default/404.gif;
}
return 403;
}
## Pretty URLs
location / {
index index.php;
try_files $uri $uri/ /index.php?$query_string;
}
# END Chevereto nginx rules
```

加入的位置如下图

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/08/1629203674-561dd2fa8735713c505c61609ab7ce1b.png?resize=630%2C415&ssl=1)

在最后一个}前面粘贴进入即可。

将install.php安装文件上传到网站根目录，然后访问就进入了安装过程

第一步是让你输入序列号，可以不输入安装免费版。

下面就是填入数据库等信息然后市创建管理员账户

然后是输入系统邮件地址等等，按照说明一步步安装下来即可。

安装到最后会自动设置，然后下载程序包，程序包下载可能会出现什么http错误之类的，如果出现错误就刷新网页从头开始重新安装。

安装后默认的全局后台位置是你的域名/dashboard/bulk

没一个账户也都可以进行一些自动已设置，根据自己喜好设置即可。
