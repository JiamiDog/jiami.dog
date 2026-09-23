---
title: "VPS 添加 WARP 解锁NetFlix（奈飞）"
slug: "vps-adds-warp-to-unlock-netflix"
source_id: "3786"
canonical_url: "https://jiami.dog/3786.html"
date_local: "2022-02-26T20:50:58"
date_published: "2022-02-26T12:50:58Z"
date_modified_local: "2022-02-27T15:31:58"
date_modified: "2022-02-27T07:31:58Z"
draft: false
featured_image_url: "https://jiami.dog/wp-content/uploads/2022/02/5421c3aa2f3c795c01890a5b56fee1d3.png"
featured_image_alt: "VPS添加WARP解锁Netflix的终端操作界面，包含安装前、安装后及刷新IP的命令行步骤。"
categories:
  - "资源攻略"
tags:
  - "netflix"
---

# VPS 添加 WARP 解锁NetFlix（奈飞）

> 本文同步自 [jiami.dog 官方原文](https://jiami.dog/3786.html)，以官网版本为准。

## 前言

cloudflare 一直以来提供了十分优秀且免费的服务，希望不要被滥用。

此文是使用 warp 来达到奈飞解锁的目的的。该方法还请自用，请勿用于解锁服务贩卖等。

## 安装 Warp

GitHub 地址：https://github.com/fscarmen/warp

该一键脚本可能是最快且最完善的 warp 一键安装脚本

一键脚本：

CODE

| ``` wget -N https://cdn.jsdelivr.net/gh/fscarmen/warp/menu.sh && bash menu.sh [option] [lisence] ``` |
| --- |

运行后选择 2 简体中文，然后一般是纯 ipv4 添加 ipv6warp，所以选 1（根据自己情况选择）。

如果有 warp + 的 license 可以输入，没有的话跳过即可，使用普通的 warp 服务。

还会让你选择 ipv4 和 ipv6 的优先级别，一般选择 3 保持系统默认即可。

可以输入 `warp h` 查看该脚本的帮助菜单。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/5421c3aa2f3c795c01890a5b56fee1d3.png?resize=1696%2C1123&ssl=1)

### 手动安装 warp

如果担心出问题可以使用手动安装

## 解锁奈飞

更换 warp 的脚本很多，但是要说哪个更好用很难，这个挺看几率的，特别是香港、新加坡这些热门地区

GitHub 地址们：

<https://github.com/luoxue-bot/warp_auto_change_ip>

<https://github.com/acacia233/Project-WARP-Unlock>

<https://github.com/GeorgeXie2333/Project-WARP-Unlock>

### Dnsmasq

如果 VPS 性能配置还不错，可以使用 dnsmasq 处理，用一键脚本：

CODE

| ``` curl -sL https://raw.githubusercontent.com/acacia233/Project-WARP-Unlock/main/run.sh | bash ``` |
| --- |

该脚本的改进版：

CODE

| ``` curl -sL https://raw.githubusercontent.com/GeorgeXie2333/Project-WARP-Unlock/main/run.sh | bash ``` |
| --- |

改进版的 arm 一键脚本：

CODE

| ``` curl -sL https://raw.githubusercontent.com/GeorgeXie2333/Project-WARP-Unlock/main/run_arm.sh | bash ``` |
| --- |

### 刷 IP

只是更换 warp ip 的刷 ip 脚本：

原版脚本：

CODE

| ``` wget https://github.com/luoxue-bot/warp_auto_change_ip/raw/main/warp_change_ip.sh && chmod +x warp_change_ip.sh && ./warp_change_ip.sh ``` |
| --- |

如果用了上面的一键安装 warp 脚本，可以输入 `warp i` 自动刷 warp ip，该脚本的 `warp i` 也是改进自上面的原版脚本。

改版脚本 2：

CODE

| ``` wget https://github.com/GeorgeXie2333/Project-WARP-Unlock/raw/main/warp_change_ip.sh && chmod +x warp_change_ip.sh && ./warp_change_ip.sh ``` |
| --- |

#### 挂 Screen 后台

可以新建个 screen 挂在后台一直自动刷 IP，否则关闭 ssh 窗口就会断开该程序了。

CODE

| ``` screen -S warp ``` |
| --- |

运行脚本，然后按 `ctrl + a + d` 退出 screen 窗口。

返回该窗口

CODE

| ``` screen -r warp ``` |
| --- |

结束该窗口： `ctrl + d`

更多 screen 安装和使用教程可见这里

## 更换为 warp team

WARP 默认分配到的通道是共享的通道，很多用户被挤在一起，导致网速变得越来越差。

这时候有两种方法。一种是使用 WARP+，而另外一种就是使用 CloudFlare Teams 的专属通道

可以查看这个教程申请和使用 warp team 功能

### 获取 WARP Teams 的配置文件

打开 Android Studio 官网

点击中间的 Download Android Studio，进行下载安装包

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/c90e958f9edacc67ce5201302080f760.png?resize=2048%2C1139&ssl=1)

依据提示进行安装

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/17a0e42108f8cf76c8b6607ec6323a04.png?resize=1602%2C1257&ssl=1)

打开 Android Studio，等待下载一些配置文件。由于我这里已经安装过了，卸载重装复现不了，故不上图演示了

进入主页

点击 More Actions 里面的 AVD Manager

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/dcecf7406acc4c9d46d6e79c0b2e6689.png?resize=998%2C776&ssl=1)

点击 Create Virtual Device

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/22a1c5313e035a9dfc8041ced643c1ac.png?resize=1598%2C1255&ssl=1)

设备选择一定要选下图的平板，然后点击 Next

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/5b7cabfa1b50949c6e6351b28df43424.png?resize=1998%2C1587&ssl=1)

系统镜像选 Lollipop，点 Next

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/3cb505b678ebea83bef7f0dd97beb6a5.png?resize=1998%2C1587&ssl=1)

名字随便输入一个，点击 Finish 完成创建

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/e408cb4cfea12be7d004aba4a8fb0189.png?resize=1998%2C1587&ssl=1)

启动虚拟机

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/4bbead1212d64f7b5dc2567f4e123a3d.png?resize=1598%2C1255&ssl=1)

打开 Android SDK Platform Tools 的官网，点击下载适用于 Windows 的 SDK Platform-Tools

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/249ce0d0c19a574f2cf18772a1645da5.png?resize=2048%2C1139&ssl=1)

解压到电脑的任意一个位置

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/ac9eae1451268c041e7fdad28848ac04.png?resize=2048%2C1081&ssl=1)

从此处下载 1.1.1.1 APP 的 APK 文件，然后复制到 Android SDK Platform Tools 的程序目录下

右键，选择在 Windows 终端中打开

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/d5f3960940e3bdc66157b8543fa9632c.png?resize=2048%2C1081&ssl=1)

输入 `adb.exe devices` 命令检查 SDK 是否正确识别到虚拟机

输入以下命令在虚拟机安装 warp

CODE

| ``` adb.exe install "xxxx.apk" ``` |
| --- |

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/10d245451d7a7837af632ff9818edde2.png?resize=2048%2C1112&ssl=1)

打开真全局模式（例如：Clash 的 TUN 模式），并打开 WARP APP

切换为 team 账户，具体教程见此处

在虚拟机内连接 WARP

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/d999b8eeb500adbf1d991522b8625f5d.png?resize=2048%2C1112&ssl=1)

输入以下命令提取 WARP Teams 的配置文件

CODE

| ``` adb pull /data/data/com.cloudflare.onedotonedotonedotone/shared_prefs/com.cloudflare.onedotonedotonedotone_preferences.xml ``` |
| --- |

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/2238cd8471de7f0ed77fce438ae3bb91.png?resize=2048%2C1293&ssl=1)

关闭虚拟机，打开配置文件

复制 `PublicKey`、`PrivateKey`，`Endpoint` 地址和 IP 地址

![PS: 本文的配置文件格式是为了方便展示用，实际的配置文件不是这样](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/139cb8132941498743114f1256b0e516.png?ssl=1)

PS: 本文的配置文件格式是为了方便展示用，实际的配置文件不是这样

### VPS 启用 WARP Teams

SSH 登录至自己的 VPS

文件管理器打开 `/etc/wireguard` 目录，找到 `wgcf.conf` 文件，备份一份到本地

打开 `wgcf.conf` 文件

编辑，替换相对应的 `PublicKey`、`PrivateKey`，`Endpoint` 地址和 IP 地址

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/686530ed1a8c15a2b92481beb7a164d2.png?resize=2048%2C1293&ssl=1)

VPS 内重新启动 WARP

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/01d6568ddc901ef5c693a361b6d97abe.png?resize=966%2C347&ssl=1)

使用以下命令查询 WARP 状态，如返回 warp=plus 即为成功

CODE

| ``` curl -s4m4 https://www.cloudflare.com/cdn-cgi/trace | grep warp | sed "s/warp=//g" ``` |
| --- |

该过程视频教程（MisakaNo 制作）： https://www.bilibili.com/video/BV1gU4y1K7of?p=1&share\_medium=iphone&share\_plat=ios&share\_session\_id=18DB1799-F06C-42FF-8647-E2A3322B37A3&share\_source=COPY&share\_tag=s\_i&timestamp=1639369745&unique\_k=3xHUpod
