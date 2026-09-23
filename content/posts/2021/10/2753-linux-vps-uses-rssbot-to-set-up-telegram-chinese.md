---
title: "Linux VPS使用RSSbot搭建Telegram中文订阅机器人教程"
slug: "linux-vps-uses-rssbot-to-set-up-telegram-chinese"
source_id: "2753"
canonical_url: "https://jiami.dog/2753.html"
date_local: "2021-10-08T18:21:35"
date_published: "2021-10-08T10:21:35Z"
date_modified_local: "2021-10-08T18:21:36"
date_modified: "2021-10-08T10:21:36Z"
draft: false
featured_image_url: "https://jiami.dog/wp-content/uploads/2021/10/2758397562.jpg"
featured_image_alt: "Telegram订阅机器人界面"
categories:
  - "资源攻略"
tags:
  - "rss"
  - "Telegram"
  - "vps"
---

# Linux VPS使用RSSbot搭建Telegram中文订阅机器人教程

> 本文同步自 [jiami.dog 官方原文](https://jiami.dog/2753.html)，以官网版本为准。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/10/2758397562.jpg?resize=1200%2C560&ssl=1)

## 前言

弄了两天，试用了几款`RSS`订阅的手机`APP`都不太满意，最后还是自己搭建一个`Telegram`机器人订阅比较合适，因为日常需要使用`Telegram`不用多一个`APP`非常方便，喜欢的文章也可以收藏，基本的功能也足够了；

欢迎使用搭建的`TG`订阅频道：[中文博客RSS订阅频道](https://t.me/chinarss)
如果需要网页版的`RSS`订阅看这里：[传送门](https://cnwebmasters.com/35.html)

## 搭建

先在`Telegram`申请一个机器人
打开`Telegram`搜索`@BotFather`发送指令`/newbot`申请一个`Bot`
注：申请过程需要输入你要创建机器人的名字和用户名，如果已经被使用会提醒你重新输入
在`HTTP API`下面的一行是机器人的`TOKEN`注意要记录下来，以后会使用到
![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/10/2574734905.png?resize=512%2C636&ssl=1)
然后发送指令`/mybots`找到自己的bot点击，然后选择`Edit Bot`
再选择`Edit Commands`然后在输入框里粘贴以下指令：
注：全部复制一起粘贴

```
rss       - 显示当前订阅的 RSS 列表，加 raw 参数显示链接
sub       - 订阅一个 RSS: /sub http://example.com/feed.xml
unsub     - 退订一个 RSS: /unsub http://example.com/feed.xml
unsubthis - 使用此命令回复想要退订的 RSS 消息即可退订, 不支持 Channel
export    - 导出为 OPML
```

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/10/1326623784.png?resize=513%2C635&ssl=1)

## VPS搭建RSSbot

`Telegram`上的操作完毕，现在在`VPS`上搭建`rssbot`
Github项目：<https://github.com/iovxw/rssbot>
在`VPS`上依次执行以下命令
运行命令中的`TELEGRAM-BOT-TOKEN`需要替换成刚才申请的机器人的`TOKEN`

```
## 下载主程序
wget https://github.com/iovxw/rssbot/releases/download/v2.0.0-alpha.9/rssbot-zh-amd64-linux
## 测试运行
./rssbot-zh-amd64-linux TELEGRAM-BOT-TOKEN
```

说明：

- 其中的`rssbot-zh-amd64-linux`文件是程序主文件
- 目录下生成的`rssbot.json`文件是数据库文件（平时可以备份，重新安装后替换掉就可以恢复订阅）

输入完成后在`Telegram`测试下机器人是否已经对接上了`VPS`
如果测试后没有问题，就用nohup命令让机器人在后台运行；
命令中的`TELEGRAM-BOT-TOKEN`替换成刚才申请的`TOKEN`

```
nohup ./rssbot-zh-amd64-linux TELEGRAM-BOT-TOKEN &
```

OK，搭建完成；后台会每隔五分钟刷新一次`RSS`订阅
