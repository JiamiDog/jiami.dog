---
title: "Telegram 创建一个私聊 bot"
slug: "telegraph-creates-a-private-chat-bot"
source_id: "3886"
canonical_url: "https://jiami.dog/3886.html"
date_local: "2022-02-27T16:40:15"
date_published: "2022-02-27T08:40:15Z"
date_modified_local: "2026-07-30T14:38:17"
date_modified: "2026-07-30T06:38:17Z"
draft: false
featured_image_url: "https://jiami.dog/wp-content/uploads/2022/02/98417e1f4e84821cb20aa7ef380b7d57.webp"
featured_image_alt: "Telegram 中 @BotFather 机器人对话界面，用户发送 /newbot 指令创建新机器人。"
categories:
  - "资源攻略"
tags:
  - "Telegram"
  - "机器人"
---

# Telegram 创建一个私聊 bot

> 本文同步自 [jiami.dog 官方原文](https://jiami.dog/3886.html)，以官网版本为准。

## 写在前面

本文章是针对那些 [Telegram](https://jiami.dog/tag/telegram "Telegram") 是 +86 用户和在意自己隐私问题所记录的一篇教程。

看完本章教程之后，用户就可以和你所创建的[机器人](https://jiami.dog/tag/robot "机器人")聊天，由机器人转发该用户的私聊消息，通过回复机器人所转发的消息即可回复用户，同时还可以减少窗口的数量且也保障了自己一定的隐私问题。

对于 +86 用户来说，基本可以满足，不过貌似可以通过 @SpamBot 申诉解除限制，但万一如果你的[朋友也是 +86 的话](https://jiami.dog/4745.html)，他就不能和你联系了，你也告诉不了他可以通过 @SpamBot 解除。

## 创建机器人

点击 @BotFather ，通过机器人之父创建一个机器人。

向它发送 /newbot 指令

然后就会问你准备要给机器人起一个什么名字（随意，可以中文）

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/98417e1f4e84821cb20aa7ef380b7d57.webp?ssl=1)

接着给机器人取一个 username，不可重复，须以 \_bot 结尾

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/40201aff72085da2c10f926a367f5820.webp?ssl=1)

机器人如此如此就创建成功了，最后生成的那个机器人 Token，不可乱泄露。

## 创建私聊机器人

点击 @LivegramBot 向它发送 /addbot 指令，然后发送刚刚创建机器人 Token。（貌似好像有个服务条款啥的你需要先同意一下，然后再发送。）

出现 Success 则私聊机器人创建成功！

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/f3044850ae9d27a132be830f7e836fd5.webp?ssl=1)

### 机器人 Token 在哪？

给 BotFather 发送 /mybots 然后就会列出你所有的机器人，点击刚刚创建的机器人，就会有个 API Token，再点击 API Token 就出现该机器人的 Token。

其实到这就已经基本创建完毕了，但是那些描述啊，头像啊，关于啥的，都是 null，就比较简陋，因此我们可以通过 BotFather 修改机器人信息。

## 修改机器人信息

给 BotFather 发送 /mybots 指令，选择私聊机器人

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/6220aa8284804358e4f83c7df5948d67.webp?ssl=1)

选择 Edit Bot

Edit Name：修改机器人名称Edit Description：修改机器人描述，它能做什么？Edit About：介绍一下机器人Edit Botpic：给机器人上传一张美美的头像，须压缩图，不能是文件。Edit Commands：编辑 \ 添加指令

以修改描述为例，其它的自己举一反三。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/e40e3435967d9802cf1cbd946ba99471.webp?ssl=1)

修改完成之后，稍等片刻，回到自己的机器人界面，即可看到刚刚那段描述！

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/6afe65ffadab8d3911eb301b1b6386af.webp?ssl=1)

## 测试与使用

切换另一个号，私聊机器人

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/2c64662261a1cc2f8dcbe12e19bdb620.webp?ssl=1)

然后机器人就会转发该用户的私聊信息

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/f1e76f88e2e327c897f444dea79da12a.webp?ssl=1)

如何回复？

你可以右键选择回复进行回复，也可以在消息右侧双击鼠标左键进行回复。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/e84afaab83ecb301b3d97ce4174d2773.gif?ssl=1)

这样即完成了私聊机器人的创建。

---

## 继续阅读与讨论

- 分类：[资源攻略](../../../categories/ziyuan-gonglue.md)
- 主题：[Telegram](../../../tags/telegram.md), [机器人](../../../tags/机器人.md)
- [在官网参与本文评论](https://jiami.dog/3886.html#jiami-giscus-comments)
- [浏览 GitHub 文章评论区](https://github.com/JiamiDog/jiami.dog/discussions/categories/article-comments)
- [返回全部文章](../../../INDEX.md)
