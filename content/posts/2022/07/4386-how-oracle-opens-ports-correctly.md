---
title: "甲骨文如何正确开放端口"
slug: "how-oracle-opens-ports-correctly"
source_id: "4386"
canonical_url: "https://jiami.dog/4386.html"
date_local: "2022-07-24T18:42:32"
date_published: "2022-07-24T10:42:32Z"
date_modified_local: "2022-07-24T19:14:31"
date_modified: "2022-07-24T11:14:31Z"
draft: false
featured_image_url: "https://jiami.dog/wp-content/uploads/2022/07/6ef620c66cd8a5fae9b98dbce3439bb9.png"
featured_image_alt: "甲骨文云安全组入站规则编辑界面，显示源CIDR设置为0.0.0.0/0和协议类型为所有协议。"
categories:
  - "资源攻略"
tags:
  - "甲骨文"
---

# 甲骨文如何正确开放端口

> 本文同步自 [jiami.dog 官方原文](https://jiami.dog/4386.html)，以官网版本为准。

## 一、进入自己的实例，设置子网

![甲骨文如何正确开放端口](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/07/fb0bc1f3fa88897584e838b875433f18.png?ssl=1)

![甲骨文如何正确开放端口](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/07/a6ce6dcddac3fc3b32f9bd47ac43d866.png?ssl=1)

开放所有端口，当然你也可以设置需要开放的端口，我这里是所有开放

![甲骨文如何正确开放端口](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/07/6ef620c66cd8a5fae9b98dbce3439bb9.png?ssl=1)

## 二、删除、关闭、打开各自系统的无用附件、防火墙、端口及规则

### Ubuntu系统下：

```
开放所有端口
iptables -P INPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT
iptables -F
Ubuntu镜像默认设置了Iptable规则，关闭它
apt-get purge netfilter-persistent
reboot
或者强制删除
rm -rf /etc/iptables && reboot
```

### Centos系统下：

```
删除多余附件
systemctl stop oracle-cloud-agent
systemctl disable oracle-cloud-agent
systemctl stop oracle-cloud-agent-updater
systemctl disable oracle-cloud-agent-updater
停止firewall
systemctl stop firewalld.service
禁止firewall开机启动
systemctl disable firewalld.service
```

---

## 继续阅读与讨论

- 分类：[资源攻略](../../../categories/ziyuan-gonglue.md)
- 主题：[甲骨文](../../../tags/甲骨文.md)
- [在官网参与本文评论](https://jiami.dog/4386.html#jiami-giscus-comments)
- [浏览 GitHub 文章评论区](https://github.com/JiamiDog/jiami.dog/discussions/categories/article-comments)
- [返回全部文章](../../../INDEX.md)
