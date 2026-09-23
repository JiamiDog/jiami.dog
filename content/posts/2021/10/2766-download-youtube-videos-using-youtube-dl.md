---
title: "使用youtube-dl下载YouTube视频"
slug: "download-youtube-videos-using-youtube-dl"
source_id: "2766"
canonical_url: "https://jiami.dog/2766.html"
date_local: "2021-10-11T18:29:51"
date_published: "2021-10-11T10:29:51Z"
date_modified_local: "2026-07-30T14:38:14"
date_modified: "2026-07-30T06:38:14Z"
draft: false
featured_image_url: "https://jiami.dog/wp-content/uploads/2021/10/YouTube.jpg"
featured_image_alt: "YouTube标志，下方有“Broadcast Yourself”标语。"
categories:
  - "资源攻略"
tags:
  - "youtube"
---

# 使用youtube-dl下载YouTube视频

> 本文同步自 [jiami.dog 官方原文](https://jiami.dog/2766.html)，以官网版本为准。

![YouTube](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/10/YouTube.jpg?resize=620%2C359&ssl=1 "使用youtube-dl下载YouTube视频")

[youtube-dl](https://youtube-dl.org/)是一个使用python编写的脚本，可以下载热门视频网站的视频。在Linux系统下可以一健下载Youtube、Youku、Tudou等热门网站的视频，甚至是一些XXX站的视频下载，如YouPorn、XVideos等。下面介绍使用方法。

**1、环境确认**
[youtube](https://jiami.dog/tag/youtube "youtube")-dl需要Python 2.6以上的版本。因此需要先确认安装的Python版本。默认CentOS6.x是安装了2.6.6。通过以下命令可以查看版本：
python –version

若是CentOS5.x，则需要编译安装新版本。参考《[CentOS 6.4安装Python2.7.5](https://teddysun.com/215.html)》，在CentOS5.x下编译安装步骤是一样的。

**2、下载安装**
youtube-dl直接下载最新版到/usr/local/bin/目录下并赋予权限即可使用。命令：

```
wget http://youtube-dl.org/latest/youtube-dl -O /usr/local/bin/youtube-dl
chmod a+x /usr/local/bin/youtube-dl
```

**3、用法**
使用帮助命令查看其用法：

```
youtube-dl -h
```

一些常用的参数：

```
youtube-dl --list-extractors  #查看支持网站列表
youtube-dl -U  #程序升级
youtube-dl --get-format URL #获取视频格式
youtube-dl -F URL #获取所有格式（目前仅支持YouTube），例如：
youtube-dl -F http://www.youtube.com/watch?v=n-BXNXvTvV4
[youtube] Setting language
[youtube] n-BXNXvTvV4: Downloading video webpage
[youtube] n-BXNXvTvV4: Downloading video info webpage
[youtube] n-BXNXvTvV4: Extracting video information
Available formats:
37      :       mp4     [1080x1920]
46      :       webm    [1080x1920]
22      :       mp4     [720x1280]
45      :       webm    [720x1280]
35      :       flv     [480x854]
44      :       webm    [480x854]
34      :       flv     [360x640]
18      :       mp4     [360x640]
43      :       webm    [360x640]
5       :       flv     [240x400]
36      :       3gp     [240x320]
17      :       3gp     [144x176]
137     :       mp4     [1080p] (DASH Video)
136     :       mp4     [720p] (DASH Video)
135     :       mp4     [480p] (DASH Video)
134     :       mp4     [360p] (DASH Video)
133     :       mp4     [240p] (DASH Video)
160     :       mp4     [192p] (DASH Video)
141     :       mp4     [256k] (DASH Audio)
172     :       webm    [256k] (DASH Audio)
140     :       mp4     [128k] (DASH Audio)
171     :       webm    [128k] (DASH Audio)
139     :       mp4     [48k] (DASH Audio)

youtube-dl -f format URL #下载指定格式的视频，这里以下载1080p原画质量的视频格式为例:
youtube-dl -f 137 http://www.youtube.com/watch?v=n-BXNXvTvV4
```

**补充说明：**
我在VPS上试了试，下载YouTube的1080p速度飞快，几百兆的视频几乎瞬间搞定。下载回来重命名一下，放到Apache的htdoc目录里，再用百度或迅雷的离线下载拖回来，如此收藏YouTube视频易如反掌。

[针对Youtube将1080P格式的视频和音频分离的问题](https://jiami.dog/4729.html), 解决办法为:

在机器上安装avconv或者ffmpeg, 然后使用参数,让youtube-dl自动下载最优的视频和音频, 下载完毕后会自动调用ffmpeg将视频和音频进行merge, 默认合并成一个mkv格式的视频.

```
sudo apt install ffmpeg

youtube-dl -f bestvideo+bestaudio https://www.youtube.com/watch?v=phbaY0fusaQ
```

发现了一个基于youtube-dl的GUI版本, 地址是<https://github.com/MrS0m30n3/youtube-dl-gui>, 这下也可以直接在Windows上面使用了.

发现使用上面的命令下载回来的视频是webm格式的, 也是很奇怪, 经过一阵搜索, 发现了如下有用命令

```
youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' url
```

```
youtube-dl --merge-output-format mp4 -f bestvideo+bestaudio url
```
