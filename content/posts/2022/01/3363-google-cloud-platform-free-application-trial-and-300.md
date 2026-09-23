---
title: "Google Cloud Platform免费申请试用以及$300美金无限重置方法"
slug: "google-cloud-platform-free-application-trial-and-300"
source_id: "3363"
canonical_url: "https://jiami.dog/3363.html"
date_local: "2022-01-05T22:43:29"
date_published: "2022-01-05T14:43:29Z"
date_modified_local: "2022-01-05T22:44:37"
date_modified: "2022-01-05T14:44:37Z"
draft: false
featured_image_url: "https://jiami.dog/wp-content/uploads/2022/01/20190823002-e1566568543429.png"
featured_image_alt: "Google Cloud Platform免费试用页面，蓝色背景，白色文字，包含“免费试用”按钮。"
categories:
  - "资源攻略"
tags:
  - "谷歌"
---

# Google Cloud Platform免费申请试用以及$300美金无限重置方法

> 本文同步自 [jiami.dog 官方原文](https://jiami.dog/3363.html)，以官网版本为准。

## Google Cloud Platform免费申请试用

### 1. Google Cloud Platform (GCP) 简介

Google Cloud Platform (以下简称GCP)是Google提供的云平台, 可以用来搭建加速服务, 网站和存储数据等等, 本文将介绍如何申请GCP一年的免费试用、Linux服务器环境搭建等. 网上关于如何搭建GCP的教程很多, 不过都不是太详尽。如果你是没基础的新手, 希望这篇教程能帮到你。

### 2. Google Cloud Platform 优势

大家用得比较多的可能是Linode, 搬瓦工, Vultr等VPS, 收费$5-$20美金左右。最近Linode的IP段也封得比较多, 基本上开十多台机器都难找到能PING通的IP。另外还有各种VP/恩基本都挂了。

GCP的优势在于:

免费Google云服务平台对新用户赠送300美元, 可以免费使用1年。并且到期后如果不打算续费, 也不会额外收取费用 (像亚马逊AWS就直接扣你费用了)。如果还想继续用, 直接新注册个账号, 免费(现在需要新卡了)。最低配置的机型$5/月, 出口大陆流量1T以内0.23$/1G, 算下来每个月可用80多G的流量, 足够用了, 当然你还可以顺便搭个网站之类的。

速度快

Google GCP有美国, 亚洲, 欧洲等机房, 而亚洲机房就在厦门正对面的台湾省彰化县, TTL只有40ms左右，快到飞起, 而Linode、Vultr等通常是200多；除了TW, 现在有HK机房了

### 3. 需要准备的东西

Gmail账号

双币信用卡 (淘宝购买的虚拟卡无法使用, 不要浪费钱)PUTTY: SSH客户端 (也可用Google自带的在线SSH, 以后比较方便).puttygen: SSH密钥生成工具. 官网下载地址: puttygen 32位 , puttygen 64位

### 4. 申请Google Cloud Platform

#### 4.1 注册

申请地址:  <https://cloud.google.com/free/>

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/20190823002-e1566568543429.png?ssl=1)

点击免费试用, 登入Gmail账号。选其他国家吧。账号类型选个人, 接下来输入账单地址以及信用卡信息。

可能遇到的问题:

提示 “交易遭拒: 付款方式无效”: 一般是信用卡相关信息不正确。账单地址的国家等信息记得与之前选的区域对应。

提交后, Google会从信用卡扣除1美元用于验证, 验证完成后会退还到账户。点击开始免费试用。

#### 4.2 激活结算账号

注册成功后可能并不能马上使用 (国内注册的基本都需要激活, 当然也不排除你人品好的情况), Gmail邮箱会受到一封标题为紧急通知：您的结算帐号 XXXXX 已经被暂停使用的邮件, 你需要点击邮件中的链接, 上传身份证和信用卡照片完成验证 (信用卡照片可以遮住或PS掉敏感信息, 只保留最后四位, 留意看页面提示), 一般提交后10分钟左右就能收到通过的邮件, 验证完成后就可以正常使用了.

这一步很多人会忽略, 结果就是创建实例的时候会不停提示你Enable Billing Account, 但是指引界面又没有明确说明要怎么激活, 即使是进到账号管理界面也无法自己开启. 所以别忘了去喵一眼你的邮箱。

#### 4.3 修改防火墙规则

网上有的文章是先创建实例，再改规则我们先修改好防火墙规则, 后面会更省事一点。

直接访问 <https://console.cloud.google.com/networking/firewalls/list>

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/20190823003-e1566569489422.png?ssl=1)

点击创建防火墙规则, 按下图设置: ![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/20190823004-e1566569551736.png?ssl=1)

名称: 随意, 但是要小写字母开头目标: 网络中的所有实例IP地址范围: 注意是0.0.0.0/0, 别写错了有遇到过有人写成0.0.0.0, 结果后来怎么试都不成功的协议和端口: 全部允许

这里直接全部允许了, 但如果你的VPS上还有网站等其他服务, 可能会有一定风险哦。选好之后点创建实例即可。

[谷歌](https://jiami.dog/tag/google "谷歌")云很好用，而且有免费的300美元可以撸，所以可玩性很高。但是谷歌云有一点不好用，就是默认不是root登陆，同时也不给root密码。现在我简单的讲一下使用root账户的方法和开启密码登陆的方法

## 谷歌云GCP使用root账户登陆并开启密码登陆

### 一：以root账户登陆

在gcp的VM管理界面，点击红框里的SSH

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/201903290002-e1553871563546.jpg?ssl=1)

系统会弹出一个VNC的管理界面。在这个界面里输入sudo su 然后点击回车，就会切换到root账户

### 二：开启密码登陆

闲说一句，在gcp的vnc里面，也是可以ctrl+v粘贴的，如果不开启ssh，反而更安全。

修改ssh配置文件，命令:

```
vi /etc/ssh/sshd_config
```

修改下面两个参数把no改为yes

```
PermitRootLogin no
PasswordAuthentication no
```

重启ssh服务使修改生效

debain命令：

```
/etc/init.d/ssh restart
```

centos命令：

```
service sshd restart
```

给root账户添加密码

```
passwd root
```

输入命令后会让你设置密码，输入两次要设置的密码,此时，就完成了设置，即可通过root账号和你设置的密码登录服务器。

## 最新申请GCP谷歌云免费试用300美金重置方法

谷歌云首次使用的话可以获得300美金免费一年是的使用体验，但是如果提前使用玩300美金或者一年的时间到期后，依旧可以重置后再次获得300美金一年的优惠体验。

### 一、登录谷歌云，https://cloud.google.com，点击转至控制台

![谷歌云 | 重新获取谷歌云300美金免费一年的方法 – Vedio Talk - VLOG、科技、生活、乐分享](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/g1-2.png?resize=2386%2C1698&ssl=1)

### 二、点击进入结算 ，然后添加一个结算账号管理员

![谷歌云 | 重新获取谷歌云300美金免费一年的方法 – Vedio Talk - VLOG、科技、生活、乐分享](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/g2.png?ssl=1) ![谷歌云 | 重新获取谷歌云300美金免费一年的方法 – Vedio Talk - VLOG、科技、生活、乐分享](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/g3.png?ssl=1)

### 三、删除之前的结算账号管理员，只保留新的管理员，然后关闭页面，清空缓存，等待5分钟

![谷歌云 | 重新获取谷歌云300美金免费一年的方法 – Vedio Talk - VLOG、科技、生活、乐分享](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/g4.png?ssl=1) ![谷歌云 | 重新获取谷歌云300美金免费一年的方法 – Vedio Talk - VLOG、科技、生活、乐分享](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/g5.png?ssl=1)

### 四、再次登录谷歌云，https://cloud.google.com，就会看到免费试用GCP ，然后点击

![谷歌云 | 重新获取谷歌云300美金免费一年的方法 – Vedio Talk - VLOG、科技、生活、乐分享](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/g7.png?ssl=1)

### 五、根据提示操作，然后点开始免费试用（注：2018年12月2o日谷歌取消了中国地区，选择香港、台湾、美国都可以）

![谷歌云 | 重新获取谷歌云300美金免费一年的方法 – Vedio Talk - VLOG、科技、生活、乐分享](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/g8.png?ssl=1)

![谷歌云 | 重新获取谷歌云300美金免费一年的方法 – Vedio Talk - VLOG、科技、生活、乐分享](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/g9.png?ssl=1)

### 六、再次点击结算，我的结算账号，就可以看到全新的300美金了

![谷歌云 | 重新获取谷歌云300美金免费一年的方法 – Vedio Talk - VLOG、科技、生活、乐分享](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/g11.png?ssl=1)

![谷歌云 | 重新获取谷歌云300美金免费一年的方法 – Vedio Talk - VLOG、科技、生活、乐分享](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/g12.png?ssl=1)

![谷歌云 | 重新获取谷歌云300美金免费一年的方法 – Vedio Talk - VLOG、科技、生活、乐分享](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/g13.png?ssl=1)

### 七、回到我们实例，然后看看我们之前的实例是否都正常

![谷歌云 | 重新获取谷歌云300美金免费一年的方法 – Vedio Talk - VLOG、科技、生活、乐分享](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/g14.png?ssl=1) ![谷歌云 | 重新获取谷歌云300美金免费一年的方法 – Vedio Talk - VLOG、科技、生活、乐分享](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/g15.png?ssl=1)

### 八、再次回到结算，就会看到转至关联的结算账号，点击它

![谷歌云 | 重新获取谷歌云300美金免费一年的方法 – Vedio Talk - VLOG、科技、生活、乐分享](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/g16.png?ssl=1) ![谷歌云 | 重新获取谷歌云300美金免费一年的方法 – Vedio Talk - VLOG、科技、生活、乐分享](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/g17.png?ssl=1)

### 九、然后选择项目名称后面的下拉，选择更改结算账号，再设置账号

![谷歌云 | 重新获取谷歌云300美金免费一年的方法 – Vedio Talk - VLOG、科技、生活、乐分享](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/g19.png?ssl=1) ![谷歌云 | 重新获取谷歌云300美金免费一年的方法 – Vedio Talk - VLOG、科技、生活、乐分享](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/g18.png?ssl=1)

### 十、到此我们的300美金就全部到账设置完成了

![谷歌云 | 重新获取谷歌云300美金免费一年的方法 – Vedio Talk - VLOG、科技、生活、乐分享](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/01/g20.png?ssl=1)
