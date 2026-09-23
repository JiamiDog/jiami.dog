---
title: "优化谷歌广告 Google Adsense，提高网站加载速度"
slug: "optimize-google-ads-and-google-adsense-to-improve-the"
source_id: "4209"
canonical_url: "https://jiami.dog/4209.html"
date_local: "2022-04-03T14:35:58"
date_published: "2022-04-03T06:35:58Z"
date_modified_local: "2026-07-30T14:38:17"
date_modified: "2026-07-30T06:38:17Z"
draft: false
featured_image_url: "https://jiami.dog/wp-content/uploads/2022/04/ed9704ced7f22178ec7dfcf24fb959af.png"
featured_image_alt: "谷歌广告加载时间过长，影响网站速度"
categories:
  - "赚钱有方"
tags:
  - "AdSense"
---

# 优化谷歌广告 Google Adsense，提高网站加载速度

> 本文同步自 [jiami.dog 官方原文](https://jiami.dog/4209.html)，以官网版本为准。

Google Adsense 在国内是拖慢网页加载速度最牛逼的 JavaScript 文件了，[谷歌广告 JavaScript 文件虽然现在获取解析都是上海和北京的服务器](https://jiami.dog/4447.html)，但速度还是不行，网页加载谷歌广告加载速度真是难以忍受了，查阅了很多解决方法，以下方法获取是目前最有效的了。

## **问题分析**

从下图可以看到网站本身为 1.1kb 的网页，谷歌广告加载需要将近 10s 加载完毕，加载大小将近 1.5MB，这还是一个广告位，可想而知自动广告对网站加载拖慢程度有多厉害！！！

![优化谷歌广告 Google Adsense 加载顺序，提高页面整体加载速度](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/04/ed9704ced7f22178ec7dfcf24fb959af.png?ssl=1)

夸张的是这是通过海外代理访问的，如果放在大陆打开，甚至加载更慢，虽然谷歌拥有异步加载，可仍然会严重拖慢速度，并且当用户没有打算看广告时，广告仍然会加载。

简单统计了一下，我打开网页用了 1s，剩下 9s 我的浏览器上方一直在加载，这种情况非常的讽刺，因为谷歌在 PageSpeedLight 中口口声声说需要降低 js 的渲染速度和外部链接加载。

实际上呢，刚刚的广告，谷歌向服务器发送了 57 次请求，其中 26 次 js 加载，总渲染达到 3.87 秒，接着是图片，总共将近 9 个，总大小 1.4MB，到了这种地步，已经让我无法忍耐了，可以想象打开博客时，最开始跳出来的不是博文的内容，而是毫不相关的广告，这种情况，访客能正常浏览完网页才怪。

## **解决方法**

首先我们来看个谷歌广告实例，比如广告单元是以下这个样子，可以看到 adsbygoogle.js 为核心 js 文件，那么我们就可以通过懒加载来解决，让网站完成在加载谷歌广告内容。

JavaScript

```
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8243002799525237" crossorigin="anonymous"></script>
<!-- 文章页顶部非自适应 -->
<ins class="adsbygoogle"
style="display:inline-block;width:690px;height:90px"
data-ad-client="ca-pub-8243002799525237"
data-ad-slot="7565157539"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
```

以下就是通过 window.addEventListener 来实现谷歌广告懒加载，可直接复制使用，放在网站 head 或 footer 最后，修改实例如下：

JavaScript

```
<script type="text/javascript">
function downloadJSAtOnload() {
var element = document.createElement("script");
element.src = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js";
document.body.appendChild(element);
}
if (window.addEventListener)
window.addEventListener("load", downloadJSAtOnload, false);
else if (window.attachEvent)
window.attachEvent("onload", downloadJSAtOnload);
else window.onload = downloadJSAtOnload;
</script>
```

接着就是将剩下的 ins 和 script 放在指定广告位置上即可，这里不要复制我的，是你自己的，如下：

Markup

```
<ins class="adsbygoogle"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
```

## **注意事项**

网页打开后的加载顺序都是按页面从上到下的顺序加载完成的，所以要想然后谷歌广告不影响页面打开速度，建议将谷歌广告 JS 代码放置网站 JS 代码后，这样就可以等页面加载完再加载广告。

在[国内挂载谷歌广告不建议使用自动部署](https://jiami.dog/4653.html)，手动固定广告位置最合理，不影响加载，也不影响网站整体美观度，如果你在做谷歌搜索引擎优化，手机站不推荐放置谷歌广告，别问我为什么，问了就是影响加载，对优化有影响。

---

## 继续阅读与讨论

- 分类：[赚钱有方](../../../categories/zhuanqian-youfang.md)
- 主题：[AdSense](../../../tags/adsense.md)
- [在官网参与本文评论](https://jiami.dog/4209.html#jiami-giscus-comments)
- [浏览 GitHub 文章评论区](https://github.com/JiamiDog/jiami.dog/discussions/categories/article-comments)
- [返回全部文章](../../../INDEX.md)
