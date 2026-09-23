---
title: "最简单的流程搭建Cloudreve V3：综合体验超好的自建云盘程序"
slug: "the-simplest-process-to-build-cloudrev-v3-a-self-built"
source_id: "2381"
canonical_url: "https://jiami.dog/2381.html"
date_local: "2021-08-20T16:38:52"
date_published: "2021-08-20T08:38:52Z"
date_modified_local: "2021-08-20T16:46:59"
date_modified: "2021-08-20T08:46:59Z"
draft: false
featured_image_url: "https://jiami.dog/wp-content/uploads/2021/08/1629448733-e10a6b33e4625313f6fe9779efee4efe.png"
featured_image_alt: "Cloudreve v3.0.0 服务启动日志，显示数据库连接、管理员账号初始化及运行模式等信息。"
categories:
  - "资源攻略"
tags:
  - "云盘"
---

# 最简单的流程搭建Cloudreve V3：综合体验超好的自建云盘程序

> 本文同步自 [jiami.dog 官方原文](https://jiami.dog/2381.html)，以官网版本为准。

![Cloudreve v3\.0\.0 服务启动日志，显示数据库连接、管理员账号初始化及运行模式等信息。](https://jiami.dog/wp-content/uploads/2021/08/1629448733-e10a6b33e4625313f6fe9779efee4efe.png)

很多很多的小[云盘](https://jiami.dog/tag/cloud-disk "云盘")用的都是这个程序，小麦云、白熊啥的，都是这个程序。不过以前用的是PHP版本的V2，个人版和商业版都很好用，个人用个人版完全足够，功能没差的，捐赠商业版是在多用户上体验更好一些。

# 前言

## 讲搭建之前先讲讲和这个项目相关的

这个云盘很复杂，但是其他的地方都有教程，我只讲讲最简单的搭建方式，讲讲容易踩坑的地方。根据我讲的走不会踩坑，我后期也会发视频。使用相关就根据云盘里面的提示自己摸索吧，离线下载也是外挂aria2，很简单。好像个人容量能超过VPS总硬盘量，这不知道是不是BUG，在细节你感觉一下，这个云盘真的很好用。

由于整个项目是用GO重写的，所以这里是重构进度：<https://forum.cloudreve.org/d/643>

这里是捐赠的版本和一般的个人免费版的差距：<https://docs.cloudreve.org/use/pro>

## 本教程的流程

我是按照官方的[快速开始](https://docs.cloudreve.org/getting-started/install) 做的流程，在已经有编译好的程序的情况下，快速开始比DOCKER还简单。

# 安装流程正式开始

## 1 获取 Cloudreve

在[GITHUB项目下载页](https://github.com/cloudreve/Cloudreve/releases)找到准备下载的项目，右键复制链接地址，一般咱们要下载的是cloudreve\_\*\*\*\*\*\_linux\_amd64.tar.gz这个文件的，直接右键复制链接地址。

## 2 下载程序包以及安装

在linux上下载东西一般用wget，我这次是默认装在默认文件夹的，也就是进了系统后没进入任何文件夹时的操作流程。

1 在linux上先输入 wget，wget后面留一个空格，然后把刚才复制的链接地址复制到空格后面，点击回车（报错wget发现不了的话自己去自己的系统怎么安装wget）如果没报错，最后在两个“”之间会提示你下载好的包的名字。

2 然后执行下列命令

```
#解压获取到的主程序
tar -zxvf  这里是你wget下载好压缩包的名字记得带上.zip

# 赋予执行权限
chmod +x ./cloudreve

# 启动 Cloudreve
./cloudreve
```

如果过程没问题这里应该是这样的

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/08/1629448733-e10a6b33e4625313f6fe9779efee4efe-2.png?ssl=1)

这里初步安装就搞定了，云盘也能进入。但是你会发现你ssh不能输入命令了，这是Ctrl+c发现会退出程序，云盘也进不去。不要慌，记下初始账号和密码，然后Ctrl+C退出，接下来咱们进行进程守护。

记下初始账号和密码！ 记下初始账号和密码！ 记下初始账号和密码！

## 3 进程守护

这里只讲第一种简单的方式，[第二种](https://docs.cloudreve.org/getting-started/install#supervisor)进作者教程自己看，我觉得第一种简单。

### Systemd

```
# 编辑配置文件
vim /usr/lib/systemd/system/cloudreve.service
```

将下文 `PATH_TO_CLOUDREVE` 更换为程序所在目录：

咱们这里因为是默认文件夹，PATH\_TO\_CLOUDREVE 改成root，如果你装在其他文件夹就改成其他文件夹的名字。

```
[Unit]
Description=Cloudreve
Documentation=https://docs.cloudreve.org
After=network.target
Wants=network.target

[Service]
WorkingDirectory=/PATH_TO_CLOUDREVE
ExecStart=/PATH_TO_CLOUDREVE/cloudreve
Restart=on-abnormal
RestartSec=5s
KillMode=mixed

StandardOutput=null
StandardError=syslog

[Install]
WantedBy=multi-user.target
```

```
# 更新配置
systemctl daemon-reload

# 启动服务
systemctl start cloudreve

# 设置开机启动
systemctl enable cloudreve
```

管理命令：

```
# 启动服务
systemctl start cloudreve

# 停止服务
systemctl stop cloudreve

# 重启服务
systemctl restart cloudreve

# 查看状态
systemctl status cloudreve
```

# 注意事项

- 如果你有宝塔等带防火墙的记得把5212端口放开
- 想绑定域名的话就反代，[作者的反代教程](https://docs.cloudreve.org/getting-started/install#fan-xiang-dai-li)，程序是自带web的，但是不能开启https，想挂载onedrive是需要开启HTTPS的，这里可以用宝塔反代，开启https也简单。我应该在博客刚创建的时候讲过宝塔如何反代。
- 具体的流程以及docker搭建可以去作者那里看，作者的文档：<https://docs.cloudreve.org/>

---

## 继续阅读与讨论

- 分类：[资源攻略](../../../categories/ziyuan-gonglue.md)
- 主题：[云盘](../../../tags/云盘.md)
- [在官网参与本文评论](https://jiami.dog/2381.html#jiami-giscus-comments)
- [浏览 GitHub 文章评论区](https://github.com/JiamiDog/jiami.dog/discussions/categories/article-comments)
- [返回全部文章](../../../INDEX.md)
