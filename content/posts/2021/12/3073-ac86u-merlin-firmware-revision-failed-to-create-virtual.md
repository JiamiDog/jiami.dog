---
title: "AC86U 梅林改版固件虚拟内存创建失败，提示USB磁盘读写速度不满足要求"
slug: "ac86u-merlin-firmware-revision-failed-to-create-virtual"
source_id: "3073"
canonical_url: "https://jiami.dog/3073.html"
date_local: "2021-12-24T18:31:07"
date_published: "2021-12-24T10:31:07Z"
date_modified_local: "2021-12-24T18:34:53"
date_modified: "2021-12-24T10:34:53Z"
draft: false
featured_image_url: "https://jiami.dog/wp-content/uploads/2021/12/WX20211202-095415.9z7ntbhdxs8.png"
featured_image_alt: "路由器固件虚拟内存创建失败的命令行日志"
categories:
  - "资源攻略"
tags:
  - "梅林固件"
  - "虚拟内存"
---

# AC86U 梅林改版固件虚拟内存创建失败，提示USB磁盘读写速度不满足要求

> 本文同步自 [jiami.dog 官方原文](https://jiami.dog/3073.html)，以官网版本为准。

事由：使用koolshare的软件中心[虚拟内存](https://jiami.dog/tag/virtual-memory "虚拟内存")插件创建swap内存，提示USB磁盘读速度不低于10M/s，写速度不低于30M/s

> USB磁盘[/dev/sdb]的读写速度太低，不符合插件要求!
> 【虚拟内存】插件要求USB磁盘设备读取不低于20MB/s，写入速度不低于为30MB/s，此测试速度和USB磁盘实际速度可能有一定差别，以上读写速度仅供参考!

在同等测试条件下，RT-AC86U，RT-AX88U等机型的flash读为10MB/s，写为30MB/s

附图：原版插件安装提示

![原版插件安装提示](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/12/WX20211202-095415.9z7ntbhdxs8.png?resize=822%2C443&ssl=1)

解决方法：
先使用ssh工具进入路由器后台
方法：先在路由器后台开启ssh登录，然后用xshell、putty等软件登录，用户名密码就是网页端后台的用户密码

![开启SSh](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/12/2.2mr07zoft5a0.png?resize=915%2C610&ssl=1)开启SSh

附上xshell的新建连接设置

![xshell](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/12/3.693b3jebfio0.png?resize=664%2C637&ssl=1)xshell

执行一下命令

```
sed -i '7,8c R_LIMIT=20nW_LIMIT=20' /koolshare/scripts/swap_make.sh
```

解释一下，就是把创建swap分区的U盘速度限制调整至可用值，值可设置成自己想设置的值（保证外设能达到的水准，不行就往低了调）

![执行命令](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/12/4.74p98sgagj40.png?resize=729%2C95&ssl=1)

![成功创建](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/12/5.51ue8i70unk0.png?resize=777%2C425&ssl=1)

执行完成，再次进入软件中心，即可正常创建虚拟内存

![成功挂载](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/12/6.70xdjvyzwew0.png?resize=742%2C525&ssl=1)

---

## 继续阅读与讨论

- 分类：[资源攻略](../../../categories/ziyuan-gonglue.md)
- 主题：[梅林固件](../../../tags/梅林固件.md), [虚拟内存](../../../tags/虚拟内存.md)
- [在官网参与本文评论](https://jiami.dog/3073.html#jiami-giscus-comments)
- [浏览 GitHub 文章评论区](https://github.com/JiamiDog/jiami.dog/discussions/categories/article-comments)
- [返回全部文章](../../../INDEX.md)
