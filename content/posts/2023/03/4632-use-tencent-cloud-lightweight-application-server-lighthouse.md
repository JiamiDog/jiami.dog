---
title: "使用腾讯云轻量应用服务器 Lighthouse 搭建 WordPress 博客"
slug: "use-tencent-cloud-lightweight-application-server-lighthouse"
source_id: "4632"
canonical_url: "https://jiami.dog/4632.html"
date_local: "2023-03-05T19:02:24"
date_published: "2023-03-05T11:02:24Z"
date_modified_local: "2023-03-05T19:02:24"
date_modified: "2023-03-05T11:02:24Z"
draft: false
featured_image_url: "https://jiami.dog/wp-content/uploads/2023/03/fa00db0e45127284adb47f59abd695b7.webp"
featured_image_alt: "腾讯云轻量应用服务器购买页面，显示新加坡地域的WordPress 5.3.2镜像和不同套餐选项。"
categories:
  - "资源攻略"
tags:
  - "ssl"
  - "wordpress"
  - "wordpress建站"
  - "网站服务器"
  - "软件"
  - "轻博客"
---

# 使用腾讯云轻量应用服务器 Lighthouse 搭建 WordPress 博客

> 本文同步自 [jiami.dog 官方原文](https://jiami.dog/4632.html)，以官网版本为准。

WordPress 是全球最流行的开源的博客和内容管理网站的建站平台，具备使用简单、功能强大、灵活可扩展的特点，提供丰富的主题插件。腾讯云轻量应用服务器 Lighthouse 提供 WordPress 应用镜像，您可以使用它快速搭建博客、企业官网、电商、论坛等各类网站。

**服务器准备**

服务器的选择上，当然是本文的主角：[腾讯云轻量应用服务器（Lighthouse）](https://cloud.tencent.com/act/cps/redirect?redirect=30206&cps_key=e4ed434a2bb235879f62bad3c36dd505)。这是目前最快的建站方式，我们开始上路吧～

### 创建及验证

Lighthosue已经默认支持WordPress、Discuz!Q、LAMP、Node.js、ASP.NET以及宝塔面板等多种应用镜像。对于WordPress应用场景，目前Lighthouse将打包搭建站点相关[软件](https://jiami.dog/tag/software "软件")组件：WordPress 5.3.2、Nginx 1.16.1、PHP 7.3.15、以及MariaDB 10.3.22，完全是业界的标配。而且，用户无需关注如此多的软件的安装、配置及部署等繁杂工作，真正为用户实现“实例创建即服务发布”的极致体验。注意，WordPress 应用镜像底层基于 CentOS 7.6 64位操作系统。

Lighthouse上创建WordPress为什么方便而直接？这得益于Lighthouse特有的应用镜像特性支持，应用镜像可以理解为对某种特定使用场景的软件层面的整体解决方案。针对WordPress场景，依托Lighthouse的应用镜像，我们可以无需关注底层相关软件库配置维护等一切细节，而更多地专注在博客撰写内容产出上。

下图是Lighthouse的创建页面，[传送门->](https://cloud.tencent.com/act/cps/redirect?redirect=30206&cps_key=e4ed434a2bb235879f62bad3c36dd505)，我们本教程中选用新加坡地域的WordPress镜像1核1G套餐。确实看得出，整个购买过程相当简洁，仅需要选择应用镜像和实例套餐就行，体验流畅。

![轻量应用服务器 Lighthouse](https://i0.wp.com/jiami.dog/wp-content/uploads/2023/03/fa00db0e45127284adb47f59abd695b7.webp?ssl=1)购买完成后，我们便可以在Lighthouse服务器页面中查看刚刚创建的WordPress服务器了：

![Lighthouse服务器页面](https://i0.wp.com/jiami.dog/wp-content/uploads/2023/03/761f1ee6e94662c59d1a4a5db231b756.webp?ssl=1)稍等片刻，服务器实例的状态会从“创建中”变为“运行中”，同时展示公网IP以及解锁了“更多”的“管理”功能。

![Lighthouse服务器](https://i0.wp.com/jiami.dog/wp-content/uploads/2023/03/a82a07bb63f82214e98f6df1560d4aec.webp?ssl=1)

点击“管理”即可进入实例管理界面。在“应用管理”下方点击“首页地址”（或者更简单地，直接在浏览器输入服务器公网IP），我们将看到WordPress的站点主页的Hello world!示例博客。服务器创建顺利完成，It works！

![Hello world!](https://i0.wp.com/jiami.dog/wp-content/uploads/2023/03/64d9ce0465570fccc58d7ea2abd7e68c.webp?ssl=1) Hello world!

第一步至此顺利完成！

### 登录服务器

通过Lighthouse的WebShell可以一键免密码登录到服务器。WebShell登录展示如下图。

![WebShell](https://i0.wp.com/jiami.dog/wp-content/uploads/2023/03/999151233c2826e3b4f90fd651ff49e9.webp?ssl=1)

### 登录WordPress控制面板

在Lighthouse的实例控制台页面，其下的“应用管理”标签栏中，详细展示如何登录WordPress控制面板的方法。

通过“管理员登录地址”的链接，通常是服务器IP + `wp-login.php`的形式，打开新的登录页面。

登录页面时需要输入用户名（admin）以及密码，它们存在服务器的lighthouse主目录的credentials.txt文件里。通过`cat`命令查看即可。

![登录WordPress控制面板](https://i0.wp.com/jiami.dog/wp-content/uploads/2023/03/59e553ae9f6e63337558cb058e08e4a3.webp?ssl=1)**发布文章**

下面我们来发布第一篇文章～

首先通过上节所述的方法登录WordPress的后台管理界面（WordPress Dashboard），如下图所示。这个管理界面经过社区多年的完善优化，目前已经非常人性化了：通过它，我们可以清楚地对网站的作者、文章、页面、评论、外观等几乎全部的资源对象进行一站式地查看管理。另外，控制面板内可以设置调整语言为中文。

添加文章可以通过左侧Posts管理子界面里Add New按钮直接完成创建；也可以更简单地，如下图直接通过链接“write your first blog post”进入文章编辑界面。

![wp-admin](https://i0.wp.com/jiami.dog/wp-content/uploads/2023/03/de527d68cd38a71ae89f8c9eafacfd83.webp?ssl=1)

在文章编辑界面，我们可以所看即所得地编辑博客内容。主编辑区域可以完成添加标题、段落、引用、插入图片/视频等等内容编辑工作；而右侧边栏里是用来完成对文章元数据/属性的设置，如所属的分类、标签等。注意Permalink这个属性指的是该文章的永久URL链接，可以理解为它是外部访问此文章时用的“指定ID”，搜索引擎也是通过Permalink来检索文章的。

![我的第一篇博客](https://i0.wp.com/jiami.dog/wp-content/uploads/2023/03/84b13b9f004407857a369b03929a31c0.webp?ssl=1)WordPress生成的页面是终端自适应的，可以通过浏览器的调试功能（Developer tools -> Toggle device toolbar）来调整验证其在手机屏幕上的展示效果。

![手机屏幕上的展示效果](https://i0.wp.com/jiami.dog/wp-content/uploads/2023/03/c196ced3e16c2c2198de29f1665516dd.webp?ssl=1)接下来，我们开始为新博客加一点色彩～

## **风格美化**

“颜值即正义”，形式的意义有时甚至胜过内容。对于如何提升我们的博客颜值，这里介绍两个方法，也是WordPress默认就完善支持的便捷功能。

### 网站自定义

进入控制面板后，点击几乎是最大按钮**Customize Your Site**，即可进入网站的自定义界面。

这里可以更改的网站属性非常多，从网站的标识（标题/副标题）、到文章的背景色/背景图，从主题选项（显示/隐藏搜索框、归档页面设置）到菜单栏及插件设置，甚至还可以添加自定义样式表。而且所有的变更都时可以立即预览的，通过发布“Publish”按钮部署生效。

![网站自定义](https://i0.wp.com/jiami.dog/wp-content/uploads/2023/03/b85c9959713903ba85b56c228893c0f2.webp?ssl=1)

如图，更新网站文章页面的背景色为黄色：

![背景色为黄色](https://i0.wp.com/jiami.dog/wp-content/uploads/2023/03/a45d68e2ed7189a1e8d906c4e46a4c0e.webp?ssl=1)主题更改

WordPress的默认主题（Theme）虽然优雅简洁时尚，但如果仍不能满足你的全部审美需求，那么你需要的是就是通过“Change your theme completetly”的功能来更换网站的整个主题风格。

WordPress默认应该有4、5个预装主题，还可以从官方的主题库下载，目前应该有近4千个主题模板，可谓风格多样，种类齐全，挑一款适合你品味的吧。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2023/03/9ca33a02454684d58a3e998dfe3ebc92.webp?ssl=1)

下图为WordPress.org的主题库，点击“Install & Preview”按钮即可安装（下载需要一些时间）并与即时预览了。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2023/03/d7cedc9c467ba5339dad66e734b21e20.webp?ssl=1)

## **域名解析**

通过IP访问博客显然不能满足需求，我们需要的是一个有意义且辨识度高的主页URL，个性化的域名对于博客类Web站点来说必选项。

如果你还没有域名，去这里申请注册；如果有了域名可以去这里添加解析。

其实，在Lighthouse的实例管理页面，也有对应的传送门。不得不说，这里的产品设计还真是贴心。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2023/03/2a9e7e3cba34e84d1f6873dd48ed5a24.webp?ssl=1)

点击DNS解析，在CNS（腾讯云解析服务）界面，选择快速“添加网站解析”，会将www和@的A记录绑定到我们的服务器IP即可。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2023/03/af61e79a87dcaccc839294f8a65afa33.webp?ssl=1)

后续我们的博客就能通过域名访问了。

## **SSL证书**

网站在部署SSL证书后，可以提供基于HTTPS的服务，整个站点的访问将会被加密，利于确认身份也显著提升了安全性。目前SSL访问对于Web站点服务来说已经时标配，相信你的博客提供的一定是专业的内容资讯类Web服务，我们强烈推荐部署SSL证书。如果已有证书，可以参考官网的安装SSL证书文档，步骤也很清晰。

对于证书申请，首先可以考虑采买各个证书/云服务商代理的SSL证书，肯定没有任何问题，而且通常更通用，安全性也更好。不过对于个人博客这类中小网站，用Let’sEncrypt的免费证书通常已经足够需求，申请过程目前也已经相当方便。我们本文以后者为例。

注意在申请证书时，不能占用80端口，所以需要暂时停止Nginx的服务。

```
# 安装Let'sEncrypt的certbot工具
sudo yum install certbot

# 停止Nginx服务
sudo killall nginx

# 申请证书
# sudo certbot certonly --standalone -n -m your-email@example.com --agree-tos -d YourAwesome.Domain
```

证书申请的执行过程，大致需要几十秒：

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2023/03/e88278997eab2ac8f3ca486944e6891f.webp?ssl=1)

证书的申请过程如上图所示，可以看到，certbot通过ACME协议为我们申请了对应域名的证书。它通过http-01 challenge，即DNS验证来实现身份确认。

对应证书文件在*`/etc/letsencrypt/live/YourAwesome.Domain/fullchain.pem`*；密钥文件在*`/etc/letsencrypt/live/YourAwesome.Domain/privkey.pem`*。

然后更新Nginx配置，*`/usr/local/lighthouse/softwares/nginx/conf/include/wordpress.conf`*。注意我们通常将80端口重定向至443的HTTPS端口，配置可以参考如下（别忘了替换成你自己的域名）：

```
server {
listen 443 ssl default_server;
server_name YourAwesome.Domain;
server_tokens off;

keepalive_timeout 5;

ssl_certificate "/etc/letsencrypt/live/YourAwesome.Domain/fullchain.pem";
ssl_certificate_key "/etc/letsencrypt/live/YourAwesome.Domain/privkey.pem";
ssl_session_cache shared:SSL:1m;
ssl_session_timeout 10m;
ssl_protocols TLSv1.2;
ssl_ciphers ECDHE-RSA-AES256-GCM-SHA384:!aNULL:!MD5:!RC4:!DHE;
ssl_prefer_server_ciphers on;

root /usr/local/lighthouse/softwares/wordpress;
index index.php index.html;

access_log logs/wordpress.log combinediox;
error_log logs/wordpress.error.log;

location ~* \.php$ {
fastcgi_pass 127.0.0.1:9000;

include fastcgi.conf;

client_max_body_size 20m;
fastcgi_connect_timeout 30s;
fastcgi_send_timeout 30s;
fastcgi_read_timeout 30s;
fastcgi_intercept_errors on;
}
}

server {
listen 80;
server_name YourAwesome.Domain;
if ($host = YourAwesome.Domain) {
return 301 https://$host$request_uri;
}
}
```

然后重启Nginx，即可。

```
sudo /usr/local/lighthouse/softwares/nginx/sbin/nginx
```

通过浏览器重新访问我们的站点，可以发现访问时地址栏“加锁”的标记。至此我们完成了验证SSL证书和Nginx配置生效，大功告成！

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2023/03/2d01b027aa7120bc7673e187419f4577.webp?ssl=1)

## **总结展望**

相信看到这里，你一定可以通过Lighthouse服务器配置自己的WordPress博客了。
