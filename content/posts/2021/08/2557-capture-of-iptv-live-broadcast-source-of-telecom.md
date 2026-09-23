---
title: "电信IPTV直播源抓取"
slug: "capture-of-iptv-live-broadcast-source-of-telecom"
source_id: "2557"
canonical_url: "https://jiami.dog/2557.html"
date_local: "2021-08-25T16:24:54"
date_published: "2021-08-25T08:24:54Z"
date_modified_local: "2021-08-25T16:26:22"
date_modified: "2021-08-25T08:26:22Z"
draft: false
featured_image_url: "https://jiami.dog/wp-content/uploads/2021/08/1629879894-6d722827c916d6924a8ecd81bae92911-1.png"
featured_image_alt: "IPTV直播源抓取软件界面，显示多行IP地址和端口信息"
categories:
  - "资源攻略"
tags:
  - "iptv"
  - "运营商"
---

# 电信IPTV直播源抓取

> 本文同步自 [jiami.dog 官方原文](https://jiami.dog/2557.html)，以官网版本为准。

![IPTV直播源抓取软件界面，显示多行IP地址和端口信息](https://jiami.dog/wp-content/uploads/2021/08/1629879894-6d722827c916d6924a8ecd81bae92911-1.png)

## 环境准备

- 电信IPTV机顶盒
- 支持openwrt和U盘的路由器（抓取的包时间长会很大，有可能几百MB）
- Wireshark

## 抓取步骤

- 将电信IPTV盒子连接到路由器的LAN口
- 配置盒子，使盒子处于观看电视频道状态待用
- 获取电信盒子IP（本次抓取ip为192.168.1.10）
- ssh登录路由器执行命令

| ``` 1
 2
 3 ``` | ``` # 进入u盘挂载目录，根据实际情况选择
 cd /tmp/mnt/disk/
 tcpdump -i br0  src host 192.168.1.10 -w ./target.cap ``` |
| --- | --- |

- 执行完命令后开始将电视机顶盒换台，把所以需要抓取的电视台都换一遍
- 换台完毕后ssh客户端CTRL+C结束抓取
- scp或者使用Samba服务拷贝target.cap到本地
- 通过Wireshark打开文件分析
- 输入过滤信息rtsp，导出过滤结果，其中Info信息里的PLAY地址即为IPTV直播地址，可以通过播放器直接播放验证![1](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/08/1629879894-6d722827c916d6924a8ecd81bae92911-2.png?ssl=1)

![2](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/08/1629879895-7d889e11cbb53bef242efab6689cd42a-1.png?ssl=1)
