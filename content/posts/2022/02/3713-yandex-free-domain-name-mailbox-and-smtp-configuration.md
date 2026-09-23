---
title: "Yandex 免费域名邮箱和配置 SMTP"
slug: "yandex-free-domain-name-mailbox-and-smtp-configuration"
source_id: "3713"
canonical_url: "https://jiami.dog/3713.html"
date_local: "2022-02-22T19:53:26"
date_published: "2022-02-22T11:53:26Z"
date_modified_local: "2022-02-27T00:18:55"
date_modified: "2022-02-26T16:18:55Z"
draft: false
featured_image_url: "https://jiami.dog/wp-content/uploads/2022/02/1645533881-20220222195540.png"
featured_image_alt: "Yandex邮箱的域名管理界面，显示主域Ednovas.org已配置。"
categories:
  - "资源攻略"
tags:
  - "yandex"
---

# Yandex 免费域名邮箱和配置 SMTP

> 本文同步自 [jiami.dog 官方原文](https://jiami.dog/3713.html)，以官网版本为准。

[yandex](https://jiami.dog/tag/yandex "yandex") mail 提供免费的域名邮箱服务。这项服务叫做 Yandex Connect，免费提供 1000 个子邮箱，每个子邮箱 10G 容量。查阅过官方文档，并没有找到明确解释，但是外网网友据说每个邮箱有每天 3000 封邮件的发件限制，相比 QQ、Gmail 这些只有每日 500 封的已经很厉害了。而且注册极其容易。此外还有 SPF/DIKM 配置能十分有效的防止邮件进入垃圾箱的概率。

## 注册主账号

就类似 Office E5 一样，需要一个主要的管理员账户，就是直接去 yandex 官网注册个即可

<https://passport.yandex.com/registration>

可以使用手机号或者安全问题两种方式注册，实测国内 +86 手机号可以验证。GV 貌似也可行。

## 绑定域名

<https://connect.yandex.com/pdd/>

上述链接是原来的界面，但是现在 yandex connect 改版了，免费的 yandex connect 入口被藏起来了，需要去

<https://connect.yandex.com/portal/admin/domains 页面，然后就会提示你的账户还不是> yandex connect 计划，这样就可以选择直接加入免费的 yandex connect 计划（右上角账户那个地方确认加入 yandex connect）。

<https://admin.yandex.ru/ 页面可以再次回到管理页面（类似> Microsoft Admin 一样）

## 验证域名

你可以直接更改 ns 记录到 yandex 的（不推荐）

或者

使用 dns 验证，按照他的要求配置域名的 MX 记录、SPF 与 DKIM 的 TXT 记录

直到显示如下图所示的 Domain Configured 即全部完成了

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/1645533881-20220222195540.png?resize=1653%2C965&ssl=1)

## 添加用户

Users 内添加用户即可，Language 记得选择 English，除非你看的懂俄文。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/1645533882-20220222195556.png?resize=1596%2C1241&ssl=1)

这样就可以设置为管理员用户了，下次就可以直接用这个账户登录 admin 页面了。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/1645533883-20220222195613.png?resize=2560%2C1289&ssl=1)

## 配置 SMTP

转到 Email 中，选择设置，然后 Email clients，把 `From the imap.yandex.com server via IMAP` 和 `App passwords and OAuth tokens` 打开并保存。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/1645533884-20220222195635.png?resize=2560%2C1289&ssl=1)

右上角选择账户管理

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/1645533884-20220222195650.png?resize=665%2C553&ssl=1)

往下拉，选择 `Passwords and authorization`

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/1645533885-20220222195704.png?resize=2560%2C1289&ssl=1)

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/1645534071-20220222195717.png?resize=658%2C388&ssl=1)

创建 APP 密钥，一定要保存下来。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/1645533886-20220222195733.png?resize=729%2C616&ssl=1)

配置 SMTP 的话，就是

SMTP 服务器地址：smtp.yandex.com

SMTP 端口：465

SMTP 加密方式：SSL

SMTP 账户：你的 yandex 邮箱（确保 mail 的设置中开启了 IMAP）

SMTP 密码：你刚刚设置的 APP Passwords

---

## 继续阅读与讨论

- 分类：[资源攻略](../../../categories/ziyuan-gonglue.md)
- 主题：[yandex](../../../tags/yandex.md)
- [在官网参与本文评论](https://jiami.dog/3713.html#jiami-giscus-comments)
- [浏览 GitHub 文章评论区](https://github.com/JiamiDog/jiami.dog/discussions/categories/article-comments)
- [返回全部文章](../../../INDEX.md)
