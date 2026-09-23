---
title: "YOUTUBE-DL 安装及油管视频下载使用教程"
slug: "youtube-dl-installation-and-tubing-video-download-tutorial"
source_id: "4729"
canonical_url: "https://jiami.dog/4729.html"
date_local: "2023-03-15T15:50:54"
date_published: "2023-03-15T07:50:54Z"
date_modified_local: "2023-03-15T15:51:07"
date_modified: "2023-03-15T07:51:07Z"
draft: false
featured_image_url: "https://jiami.dog/wp-content/uploads/2023/03/40a8f49526cf204f6f71d01e436580c7.png"
featured_image_alt: "Python 3.8.5 (64-bit) 安装界面，突出显示“Add Python 3.8 to PATH”选项。"
categories:
  - "资源攻略"
tags:
  - "python"
  - "youtube-dl"
---

# YOUTUBE-DL 安装及油管视频下载使用教程

> 本文同步自 [jiami.dog 官方原文](https://jiami.dog/4729.html)，以官网版本为准。

强大的视频下载工具 [youtube-dl](https://jiami.dog/tag/youtube-dl "youtube-dl") 项目由 Ricardo Garcia 创建于2008年，源代码由 Python 编写，托管在 GitHub 上，最初仅支持 YouTube，但随着项目的发展，也开始支持其他视频网站，优势在于使用简单、功能齐全、体积小巧，但唯一遗憾的是国内使用需要开启代理，不多说了直接进入正题。

## **使用方法**

1、该脚本源代码基于 Python 编写，就需要安装 Python 2.7 或 3.2 以上版本，这里推荐腾讯软件下载，安装程序务必勾选“Add [python](https://jiami.dog/tag/python "python") to PATH”，仅运行脚本无其他需求直接选择“Install Now”，如下图：

```
#Python下载地址
https://pc.qq.com/search.html#!keyword=python
```

![通过腾讯软件下载python](https://i0.wp.com/jiami.dog/wp-content/uploads/2023/03/40a8f49526cf204f6f71d01e436580c7.png?ssl=1)

2、在安装了 Python 后，按 Win+R 键打开运行，输入cmd，再输入以下提供的命令，即可自动下载安装 youtube-dl 工具，以下命令都是运行安装 youtube-dl 的命令，只是第二条为安装 youtube-dl 并更新，如下图：

```
#直接安装 youtube-dl
pip install youtube-dl
#更新安装 youtube-dl
pip install --upgrade youtube-dl
```

![通过命令安装youtube-dl](https://i0.wp.com/jiami.dog/wp-content/uploads/2023/03/15e62d0d1e0fa932a77d5eaf569714c2.png?ssl=1)

3、接着安装 FFmpeg 组件，通过以下地址下载，解压到某个位置，右键“我的电脑”-“属性”-“高级系统设置”-“环境变量(N)”，在用户变量内找到 PATH 添加 FFmpeg 解压目录里的Bin文件夹路径，设置完成运行cmd，输入命令 ffmpeg 运行，查看是否安装成功，如下图：

```
#FFmpeg组件下载
https://github.com/BtbN/FFmpeg-Builds/releases
#查看是否安装成功
ffmpeg
```

![在系统上配置FFmpeg组件](https://i0.wp.com/jiami.dog/wp-content/uploads/2023/03/6b630ac0f56d2b4b5eae1d92845eba6c.png?ssl=1)

4、然后就可以制作懒人脚本了，桌面新建记事本（或使用：notepad 命令），复制粘贴以下代码，另存为 youtube.bat，要注意“另存为”时，将右下角编码“UTF-8”更改为“ANSI”，否则运行时会乱码，脚本代码如下：

```
@echo off
:start
set /p dir=请输入保存路径：
set dir=%dir:/=\%
pushd %dir%
if /i not %dir%==%cd% goto :start
echo 保存路径：%cd%
:download
set /p input=请输入视频链接：
set input=%input:&=^^^&%
youtube-dl -F %input%
if errorlevel 1 goto :download
set /p code=请输入视频格式编号：
youtube-dl -f %code% %input%
goto :download
```

5、在使用 youtube.bat 之前需要开启网络代理，接着运行制作好的 .bat 懒人脚本，执行后会提示请输入视频保存路径，填写路径如：D:\程序缓存，接着就会提示输入 YouTube 或 其他视频 链接，如下图：

![运行脚本设置下载路径和视频地址](https://i0.wp.com/jiami.dog/wp-content/uploads/2023/03/efa32474f05b257f5075dae8340ee6f5.png?ssl=1)

6、由于懒人脚本内使用了 **-F**，会输出不同质量的组合，需要自己挑选想要的视频、音频组合方案（后面会说到关于视频、音频编码问题），然后填写对应的组合序号，如：单独下载视频 136，单独下载音频 140，合并下载音视频 136+140，如下图：

![填写视频、音频组合序号方案](https://i0.wp.com/jiami.dog/wp-content/uploads/2023/03/1affc2e3773f9141102ff93fbf95f936.png?ssl=1)

7、输入完成对应的组合序号后就需要耐心等待下载完成了，感觉下载慢可在 youtube-dl 那一行后加上 –proxy “你的代理服务器地址”，完成如下图：

![通过youtube-dl下载完成油管视频](https://i0.wp.com/jiami.dog/wp-content/uploads/2023/03/071f4cd9109a0b7b4caedf3370910bce.png?ssl=1)

## **关于编码**

**视频编码**

**avc1：**也就是 h264 的格式，一般现在经常使用的格式，许多 up主 也是以这种格式上传的。

**webm：**内封的是 vp9 格式，属于 Google 为了避免 h265 的高额费用开发的自有格式，在大部分时候是比avc1要小一些的。

**av01：**比较新的格式，后缀也是 mp4，但目前阶段基本没法硬解，同等清晰度下生成的文件比较小。

**best：**下载 youtube-dl 自认为最好的版本，然而并没有什么卵用。

**音频编码**

在利于封装的原则下，avc1 和 av01 首选 m4a，最后生成的是 mp4 文件，webm 对应 opus 音频。

需要注意的是 Youtube 在处理 m4a 音频时，16kHz 以上有“剃头”现象。

## **最后说明**

视频列中有“video only”标识的，需要同时下载音频轨，安装 FFmpeg 组件是为了正常合并 webm 格式，FFmpeg 组件需要大于 3.4.2 版本，建议保持最新。

输入命令“pip install –upgrade youtube-dl”可检查更新组件，youtube-dl 也适用于其他网站，经常使用 youtube-dl 下载视频，建议保存最新版本，如有问题请留言。
