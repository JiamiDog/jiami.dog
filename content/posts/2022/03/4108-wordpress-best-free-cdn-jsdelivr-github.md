---
title: "WordPress最佳免费CDN：jsDelivr + Github"
slug: "wordpress-best-free-cdn-jsdelivr-github"
source_id: "4108"
canonical_url: "https://jiami.dog/4108.html"
date_local: "2022-03-05T18:07:21"
date_published: "2022-03-05T10:07:21Z"
date_modified_local: "2022-03-05T18:11:25"
date_modified: "2022-03-05T10:11:25Z"
draft: false
featured_image_url: "https://jiami.dog/wp-content/uploads/2022/03/1488e325e1a72e73bb8c06b52e667ecc.png"
featured_image_alt: "文章配图展示了 jsDelivr 和 GitHub 结合使用的 WordPress 免费 CDN 加速方案示意图。"
categories:
  - "资源攻略"
tags:
  - "cdn"
  - "Github"
  - "jsDelivr"
  - "wordpress"
---

# WordPress最佳免费CDN：jsDelivr + Github

> 本文同步自 [jiami.dog 官方原文](https://jiami.dog/4108.html)，以官网版本为准。

大家好，我是雷锋哥。博客搭建在垃圾主机上，延迟非常高，没有备案的原因，没办法用国内的CDN，试过「cloudflare」的免费CDN，效果也不是很理想，后来发现了[jsDelivr](https://jiami.dog/tag/jsdeliver "jsDelivr") + [Github](https://jiami.dog/tag/github "Github")才是免费的最佳CDN。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/03/1488e325e1a72e73bb8c06b52e667ecc.png?ssl=1)

## jsDelivr介绍

jsDelivr是一个提供数千种Javascript、CSS等超过1650多种 Libraries 加速的免费CDN服务，支持给Github、WordPress、NPM免费提供CDN加速。而且国内也有 CDN 节点，速度非常快。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/03/df34930f6a8e8da7f2bc399d239e6230.png?ssl=1)

**jsDelivr官方：**<https://www.jsdelivr.com/>

## Github介绍

Github目前最好用的免费开源项目托管站点，众多开源项目都托管在Github，目前Github已被微软收购了。

**Github官方：**<https://github.com/>

## 利用 jsDelivr + Github 给 WordPress 免费加速

1.注册 Github  账号

2.新建Github仓库，Repository name：输入仓库名称，然后点击「Create repository」开始创建。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/03/ba5c06b076ae8f84a368b04b1ead9cbd.png?ssl=1)

3.点击「Upload files」上传你要CDN的文件，如CSS、JS、图片等……

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/03/a762a11426ba22654c1f2481b4f69d7c.png?ssl=1)

4.发布仓库，点击「release」发布，输入自定义发布版本号。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/03/32ef646056584c5ab6f55781f11ce99a.png?ssl=1)

5.使用 jsDelivr 来引用资源

https://[cdn](https://jiami.dog/tag/cdn "cdn").jsdelivr.net/gh/你的用户名/你的仓库名@发布的版本号/文件路径

例如：https://cdn.jsdelivr.net/gh/woshileifeng1/[wordpress](https://jiami.dog/tag/wordpress "wordpress")cdn@1.0/aplayer.min.js

如果不需要版本号区分，也可以直接：

<https://cdn.jsdelivr.net/gh/woshileifeng1/wordpresscdn/aplayer.min.js>

6.接下来把CDN好的CSS和JS等文件地址，都替换到你主题里面去。

7.可以在你主题的头部文件加入 <link rel=’dns-prefetch’ href=’//cdn.jsdelivr.net’ /> 预读DNS，加快解析

## GitHub+jsDelivr+PicGo搭建免费图床

1.新建立一个github仓库，专门存放上传的图片。

2.生成Access token

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/03/3700ad77553d348a86b04683417bbbf1.png?ssl=1)

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/03/974ea2219907097ba5860427d97414aa.png?ssl=1)

3.下载PicGo软件：https://github.com/Molunerfinn/picgo/releases

4.填入刚才在Github创建的信息，指定存储文件夹的路径，PicGo上传文件的时候，将自动在github仓库中创建此文件夹。

自定义域名：https://cdn.jsdelivr.net/gh/用户名/图床仓库名

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/03/a12e9106bf2c8c22705b2ba4dfa1844c.png?ssl=1)

5.可以开始上传图片啦，在上传图片之后自动会将图片链接复制到你的剪贴板里。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/03/853d48109fcfbd4fe0ebf8f12320909e.png?ssl=1)

## 总结

虽然这种免费CDN折腾起来有点麻烦，不过毕竟免费，还可以作为图床用能节省你的主机流量，加上jsDelivr 和 Github 都是大厂还是比较放心的。喜欢瞎折腾的，可以把整站都丢到 Github 上面，然后通过插件「WP Super Cache」里面的CDN功能来处理静态资源，这里就不给大家演示了，有兴趣自己折腾。

---

## 继续阅读与讨论

- 分类：[资源攻略](../../../categories/ziyuan-gonglue.md)
- 主题：[cdn](../../../tags/cdn.md), [Github](../../../tags/github.md), [jsDelivr](../../../tags/jsdelivr.md), [wordpress](../../../tags/wordpress.md)
- [在官网参与本文评论](https://jiami.dog/4108.html#jiami-giscus-comments)
- [浏览 GitHub 文章评论区](https://github.com/JiamiDog/jiami.dog/discussions/categories/article-comments)
- [返回全部文章](../../../INDEX.md)
