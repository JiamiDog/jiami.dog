---
title: "利用jsdelivr CDN+GitHub将WordPress JS,CSS文件CDN存储"
slug: "use-jsdelivr-cdn-github-to-store-wordpress-js-and-css"
source_id: "2618"
canonical_url: "https://jiami.dog/2618.html"
date_local: "2021-09-17T20:01:45"
date_published: "2021-09-17T12:01:45Z"
date_modified_local: "2026-07-30T14:38:14"
date_modified: "2026-07-30T06:38:14Z"
draft: false
featured_image_url: "https://jiami.dog/wp-content/uploads/2021/09/1631880169-wpsupercache.jpg"
featured_image_alt: "WordPress插件CDN支持设置界面，包含站点地址、Off-site URL、目录排除和CNAME记录等配置项。"
categories:
  - "资源攻略"
tags:
  - "wordpress"
---

# 利用jsdelivr CDN+GitHub将WordPress JS,CSS文件CDN存储

> 本文同步自 [jiami.dog 官方原文](https://jiami.dog/2618.html)，以官网版本为准。

CDN有几种模式，一种全站CDN，没备案可以选择CF，但是CF国内访问太慢了。还有一种是部分加速，[国内目前能够称之为优秀的免备案CDN只有jsdelivr](https://jiami.dog/4108.html)。

**1.创建加速用仓库**

首先在GitHub上创建一个仓库

**2.WordPress安装WP Super Cache插件后，在cdn一栏，填入cdn地址，仿照我的格式来，最后别加/**

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/09/1631880169-wpsupercache.jpg?resize=843%2C582&ssl=1)

<https://cdn.jsdelivr.net/gh/你的GitHubID/cdn仓库名@commit>

例如：https://cdn.jsdelivr.net/gh/xxx/bw@a661c57c53b7cef49345b2d95a7410f143e7aa26

**3.仓库目录**

不是什么都要放到cdn上的，所以不能简单把wp-content和wp-includes文件夹直接填进去，我们需要针对性的，看我们的网页加载了那些内容，之后再分门别类的添加具体的文件夹目录。uploads一定要排除，否则存储在你服务器上的图片会不显示

这是我添加的文件夹,英文逗号作分隔符

**4.如何将本地文件上传到github托管？**

Github开源代码库以及版本控制系统，可以托管各种git库，可以将个人Blog或小型项目托管到github。

Windows 系统下：
4.1 注册GitHub
4.2下载安装git:<https://cdn.npm.taobao.org/dist/git-for-windows/> 。
4.3 在本地准备好你的项目。 在桌面创建一个同github ID同名文件夹，鼠标右键，点击 Git Bash。
4.4 克隆刚才建的repository到桌面仓库文件夹中 。用git clone <https://github.com/xxx/bw.git命令>
4.5 然后把自己的项目文件粘贴桌面仓库文件夹中
4.6 进入本地仓库目录，输入输入git add .
4.7 输入git commit -m “add” 提交到本地的版本控制库里，引号里面是你对本次提交的说明信息。
4.8 最后输入git push -u origin master 将你本地的仓库提交到你的github，最后会让输入你的github的账号和密码，输入回车之后再去看github项目，就看到你本地项目出现在github上了！

如果是ubuntu等系统下， 安装命令apt-get install git 然后直接进入到上面4.4步。

**5.更新CDN内容**

由于插件经常会更新，所以每次更新完插件后，都应该把该插件下载下来，提交到GitHub仓库中，并且由于jsdelivr的缓存是有延迟的，所以需要我们手动加速commit，来选择最新版本。

**6.清除缓存**

如果你之前就有在使用WP Super Cache，请务必清楚缓存，否则不会加载，并且会出错，配置好CDN后再生成缓存。
