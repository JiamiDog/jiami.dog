---
title: "OpenAI 推出超神 ChatGPT 注册攻略"
slug: "openai-launches-chaoshen-chatgpt-registration-strategy"
source_id: "4427"
canonical_url: "https://jiami.dog/4427.html"
date_local: "2022-12-06T17:37:55"
date_published: "2022-12-06T09:37:55Z"
date_modified_local: "2023-02-26T19:59:48"
date_modified: "2023-02-26T11:59:48Z"
draft: false
featured_image_url: "https://jiami.dog/wp-content/uploads/2022/12/1670319068-20221206172440.png"
featured_image_alt: "支付宝支付界面，显示美元金额和卢布支付选项。"
categories:
  - "资源攻略"
tags:
  - "ChatGPT"
  - "openai"
---

# OpenAI 推出超神 ChatGPT 注册攻略

> 本文同步自 [jiami.dog 官方原文](https://jiami.dog/4427.html)，以官网版本为准。

前几天，OpenAI 推出超神 [ChatGPT](https://jiami.dog/tag/chatgpt "ChatGPT")，非常火爆。但是呢，因为不可抗力原因，大部分人无法体验到。这里我分享一下注册的攻略。

### 准备

- 首先能能访问 Google（前置条件，不能明确说，懂得都懂）
- 你得有一个国外手机号，GV 号肯定不行。
  - 如果你没有国外手机号，推荐[sms-activate.org](https://jiami.dog/sms-activate)

### 注册短信平台并充值

- 先行注册[sms-activate.org](https://jiami.dog/sms-activate)
- 注册好之后进行对应的充值

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/12/1670319068-20221206172440.png?resize=1332%2C1204&ssl=1)

接码费用一次为 10.5 卢布，大约1.2 人民币。因为充值默认为美元，可以选择充值 1 美元进去，

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/12/1670319188-20221206172548.png?resize=1270%2C1223&ssl=1)

### 注册OpenAI账号

- 打开[beta.openai.com/signup](https://beta.openai.com/signup) 页面进行相应的注册。
  - 这里同样需要你能访问Google且 ip 不是香港，最好是美国、新加坡等等，不然会提示不能在当前国家服务。
- 注册成功进入下面填写手机号的页面

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/12/1670319218-20221206172612.png?resize=1091%2C1016&ssl=1)

### 准备接码

这里需要注意下的就是，目前好像就只有巴西和印度支持了，之前我选的印尼，是可以收到码的。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/12/1670319245-20221206172656.png?resize=838%2C2192&ssl=1)

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/12/1670319276-20221206172850.png?resize=1786%2C936&ssl=1)

- 然后再刚刚填写手机号码的页面填入申请的手机号

### 开始使用ChatGPT

注册完后，我们去ChatGPT网站去登陆。[chat.openai.com/auth/login](https://chat.openai.com/auth/login)

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/12/1670319430-20221206173604.png?resize=1654%2C1278&ssl=1)

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/12/1670319444-20221206173641.png?resize=2334%2C1241&ssl=1)

当然，有一些人会在这里遇到一个问题，会出现提示说不能在当前国家服务：

Not available OpenAI’s services are not available in your country.

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/12/1670320508-20221206175423.png?resize=1289%2C507&ssl=1)

出现这种问题，就是因为你的代理没有全局，或者位置不对。香港的代理是100%无法通过的。

但是又有个非常神奇的问题，只要你出现了这个提示，那么你接下来怎么切换代理，都是没用的。现在教你一招解决。

### 解决地区问题

首先，你要把你的代理切换到不是香港的地区，我这里选韩国。

然后，先复制下面这段代码

```
window.localStorage.removeItem(Object.keys(window.localStorage).find(i=>i.startsWith('@@auth0spajs')))
```

接着在地址栏里输入

```
javascript:
```

注意，这里一定要输入，因为你复制的话是粘贴不了的。

然后再粘贴我们第一段复制的内容

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/12/1670319786-20221206174224.png?resize=1705%2C210&ssl=1)

最后结果是这样

然后按下回车键，接着刷新页面，如果你的代理没问题，就可以正常看到注册页面了。

---

## 继续阅读与讨论

- 分类：[资源攻略](../../../categories/ziyuan-gonglue.md)
- 主题：[ChatGPT](../../../tags/chatgpt.md), [openai](../../../tags/openai.md)
- [在官网参与本文评论](https://jiami.dog/4427.html#jiami-giscus-comments)
- [浏览 GitHub 文章评论区](https://github.com/JiamiDog/jiami.dog/discussions/categories/article-comments)
- [返回全部文章](../../../INDEX.md)
