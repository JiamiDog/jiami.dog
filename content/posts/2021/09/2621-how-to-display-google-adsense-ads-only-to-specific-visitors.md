---
title: "如何只向特定访客展示Google AdSense广告"
slug: "how-to-display-google-adsense-ads-only-to-specific-visitors"
source_id: "2621"
canonical_url: "https://jiami.dog/2621.html"
date_local: "2021-09-17T20:08:11"
date_published: "2021-09-17T12:08:11Z"
date_modified_local: "2021-09-17T20:09:19"
date_modified: "2021-09-17T12:09:19Z"
draft: false
featured_image_url: "https://jiami.dog/wp-content/uploads/2021/09/bad-hit.jpg"
featured_image_alt: "Google AdSense广告点击数据面板，显示IP、点击数、CTR等指标。"
categories:
  - "资源攻略"
tags:
  - "AdSense"
---

# 如何只向特定访客展示Google AdSense广告

> 本文同步自 [jiami.dog 官方原文](https://jiami.dog/2621.html)，以官网版本为准。

最近我的一个网站GG广告无效点击率非常高，导致几次被Google [AdSense](https://jiami.dog/tag/adsense "AdSense")限制广告数量，每次限制要一个月才恢复，广告收入损失十分惨重。那么如何降低Google AdSens广告无效点击率？

![我被恶意点击Google AdSense广告](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/09/bad-hit.jpg?ssl=1)

如上图有个IP点击我广告9次，其实才展示2次，明显恶意点击。而且谷歌统计里显示广告点击了177次。实际google adsense后台才显示60次点击, 有117次无效点击。

这么多无效点击，Google AdSens 账户被限流是必定的，所以不得不降低广告点击率，过滤恶意点击。我想主要有以下2个方向：

1. 优化网站排版布局 —— 让访客意识到广告位是广告，让真正有兴趣的访客去点击广告，尽量不要让访客误点广告
2. 主观规避访客乱点击广告 —— 防止恶意点击Google AdSense广告的小人，只向目标用户展示广告

优化广告展示布局，因各自网站不同，在此不便展开来聊。本文，我们来聊聊如何如何只向特定访客展示Google adSense广告

## 只向搜索引擎的访客显示广告

通过搜索引擎转过来的访客，更容易点击网站上的广告。以下代码将只把Google AdSense广告显示给那些从搜索引擎过来的访客。

平常的访客则看不到这些广告，他可以很好的配合针对性点击付费Pay-Per-Click (PPC)
如果你是用wordpress, 可以把下面这段代码放在functions.php中

```
$ref = $_SERVER['HTTP_REFERER'];
$SE = array('/search?', 'images.google.', 'web.info.com', 'search.', 'del.icio.us/search', 'soso.com', '/search/', '.yahoo.');
foreach ($SE as $source) {
if (strpos($ref,$source)!==false) {
setcookie("sevisitor", 1, time()+3600, "/", ".bawodu.com");
$sevisitor=true;
}
}
function wordpress_from_searchengine(){
global $sevisitor;
if ($sevisitor==true || $_COOKIE["sevisitor"]==1) {
return true;
}
return false;
}
```

注意把里面的网址换成你的网址

然后再把下面这段代码放在你想显示广告的页面中

```
<!--?php if (function_exists('wordpress_from_searchengine')) { if (wordpress_from_searchengine()) { ?
INSERT YOUR CODE HERE
?php } } ?
```

访问之后会在你的浏览器存储一个cookie，时间是一个小时。再他们浏览你的网站的时候会持续看到广告，但是如果访客喜欢你的网站订阅或者书签了，以后再访问的时候就自动看不到你的网页广告了

## 广告被点击一次后即停止再展示

对谷歌Adsense广告点击事件进行统计，如果用户点击过广告，在后续访问过程中将不再展示广告。

原理：当你Adsense广告代码被点击的时候，广告代码里面的adsbygoogle这个class的点击事件，会触发我们添加的js脚本，脚本会把我设置的事件4传回到后台，后台设置个cookie。然后再判断是否cookie存在，从而决定是否展示广告

```
/</script /src="https://code.jquery.com/jquery-3.3.1.min.js"><//script>
/</script type="text/javascript">
    var isOverGoogleAd = false;
    var ad = /adsbygoogle/;
    $(document).ready(function()
    {
        $('ins').on('mouseover', function () {
            if(ad.test($(this).attr('class'))){
                isOverGoogleAd = true;
            }
        });
        $('ins').on('mouseout', function () {
            if(ad.test($(this).attr('class'))){
                isOverGoogleAd = false;
            }
        });
    });
    $(window).blur(function(e){
        if(isOverGoogleAd){
            $.ajax({
                type: "POST",
                url: "https://你后台域名/"+"/p/events",
                data: {"et":4},
                xhrFields: {withCredentials: true},
                crossDomain: true,
            });
        }
    });
/<//script>
```

data: {“et”:4},这个数字是4，我是使用事件4作为在后台接收事件，这个不做限定，可根据需要修改。后台代码这里暂不提供，自己根据原理编写。

---

## 继续阅读与讨论

- 分类：[资源攻略](../../../categories/ziyuan-gonglue.md)
- 主题：[AdSense](../../../tags/adsense.md)
- [在官网参与本文评论](https://jiami.dog/2621.html#jiami-giscus-comments)
- [浏览 GitHub 文章评论区](https://github.com/JiamiDog/jiami.dog/discussions/categories/article-comments)
- [返回全部文章](../../../INDEX.md)
