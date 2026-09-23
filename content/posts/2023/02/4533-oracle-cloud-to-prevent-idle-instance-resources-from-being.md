---
title: "甲骨文云(Oracle Cloud)防止被清理闲置实例资源保活教程"
slug: "oracle-cloud-to-prevent-idle-instance-resources-from-being"
source_id: "4533"
canonical_url: "https://jiami.dog/4533.html"
date_local: "2023-02-11T15:07:29"
date_published: "2023-02-11T07:07:29Z"
date_modified_local: "2023-02-11T15:07:56"
date_modified: "2023-02-11T07:07:56Z"
draft: false
featured_image_url: "https://jiami.dog/wp-content/uploads/2023/02/b1dfde9f6f719f208e04723102110fbc.jpg"
featured_image_alt: "Oracle Cloud控制台仪表板，显示“服务链接”和“访问所有OCI服务”按钮。"
categories:
  - "资源攻略"
tags:
  - "甲骨文"
---

# 甲骨文云(Oracle Cloud)防止被清理闲置实例资源保活教程

> 本文同步自 [jiami.dog 官方原文](https://jiami.dog/4533.html)，以官网版本为准。

从发了[白嫖甲骨文云服务器](https://jiami.dog/3807.html "申请Oracle Cloud永久免费服务+300美元试用额度")文章后，到现在已经3年多了。

从最初的AMD服务器，到现在的高配ARM服务器。这一波[甲骨文](https://jiami.dog/tag/oracle "甲骨文")云确实非常良心了！！

由于确实好多童鞋闲置计算实例资源，甲骨文最近一直在酝酿清理闲置资源方式，这次终于出详细规则了！

大家要注意了！要使用率不高可能会回收实例哦~~~

## 历史公告

2022年11月16日 官方突然新增说明：

*从 2022 年 11 月 24 日开始，您闲置的 Always Free 计算实例可能会停止。 详细了解此过程以及如何重启您的实例。 您还可以随时升级您的帐户以避免中断。*

*仅限未付费的免费套餐帐户。Idle Always未付费免费套餐帐户的免费资源可以随时回收，恕不另行通知。回收包括停止或终止等操作。*

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2023/02/b1dfde9f6f719f208e04723102110fbc.jpg?resize=631%2C248&ssl=1)

但是21年11月19号 该说明突然又消失了。

就在23年1月底 又再次出现类似的说明。

## 最新公告

空闲计算实例的回收

Idle Always Free计算实例可能会被 Oracle 回收。如果在 7 天内满足以下条件，则 Oracle 会将虚拟机和裸机计算实例视为空闲：

- 95%时间CPU利用率低于10%
- 网络利用率低于10%
- 内存利用率低于 10% （仅适用于A1 形状）（ARM实例）

公告地址：https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier\_topic-Always\_Free\_Resources.htm

这次公告说明明确了具体回收闲置资源的规则！看来这次是玩真的了。

下面纯个人看法，目前官方未提供详细解释

按照官方说明来看，CPU / 网络 / 内存 都不符合要求会回收计算实例，账号不影响，回收后应该能再开新实例。

## 保活方法

### 开源仓库

就在甲骨文悄悄发这个消息后，有大佬已经提供了保活的代码了！

开源仓库：<https://github.com/layou233/NeverIdle>

简要步骤：（仓主提供了一键脚本，我没有测试）

- # 服务器安装 wget screen
- yum install -y wget screen
- # 下载编译后的可执行文件
- # AMD服务器
- wget <https://github.com/layou233/NeverIdle/releases/download/0.1/NeverIdle-linux-amd64> -O NeverIdle
- # ARM
- wget <https://github.com/layou233/NeverIdle/releases/download/0.1/NeverIdle-linux-arm64> -O NeverIdle
- # 修改文件权限
- chmod 777 NeverIdle
- # 使用screen运行程序
- screen -R baohuo
- # 启动程序
- ./NeverIdle -c 2h -m 2 -n 4h
- # 挂起screen 按 Ctrl+A+D
- #再次进入screen
- screen -R baohuo

展开

命令参数：

```
./NeverIdle -c 2h -m 2 -n 4h
```

其中：

-c 指启用 CPU 定期浪费，后面跟随每次浪费的间隔时间。
如每 12 小时 23 分钟 34 秒浪费一次，则为 12h23m34s。按照格式填。

-m 指启用浪费的内存量，后面是一个数字，单位为 GiB。
启动后会占用对应量的内存，并且保持不会释放，直到手动杀死进程。

-n 指启用网络定期浪费，后面跟随每次浪费的间隔时间。
格式同 CPU。会定期执行一次 Ookla Speed Test（还会输出结果哦！）

### Shell脚本

- 一键脚本
- curl https://keeporacle.pages.dev/ -o keeporacle.sh && chmod +x keeporacle.sh && ./keeporacle.sh
- 或
- wget https://keeporacle.pages.dev/ -O keeporacle.sh && chmod +x keeporacle.sh && ./keeporacle.sh

博主没有测试！

### lookbusy

lookbusy 自己搜索部署方式

- lookbusy -c 50 # 占用所有 CPU 核心各 50%
- lookbusy -c 50 -n 2 # 占用两个 CPU 核心各 50%
- lookbusy -c 50–80 -r curve # 占用所有 CPU 核心在 50%-80% 左右浮动
- lookbusy -c 0 -m 128MB -M 1000 # 每 1000 毫秒，循环释放并分配 128MB 内存
- lookbusy -c 0 -d 1GB -b 1MB -D 10 # 每 10 毫秒，循环进行 1MB 磁盘写入，临时文件不超过 1GB

### 计算圆周率

- nohup echo “scale=99999999;4\*a(1)” | bc -lq > /dev/null &
- nohup cpulimit -l 30 -p 22489 >/dev/null &
- scale那个代表小数点后的位数，数越大计算时间越长
- -l 那里可以控制cpu使用率0-200
- -p 那里写程序的PID，通过top命令查找，或者 ps -aux | grep bc

博主没有测试！

## 最后总结

再好的保活教程也不如自己真实使用！建议大家别浪费云服务器多多利用起来！

---

## 继续阅读与讨论

- 分类：[资源攻略](../../../categories/ziyuan-gonglue.md)
- 主题：[甲骨文](../../../tags/甲骨文.md)
- [在官网参与本文评论](https://jiami.dog/4533.html#jiami-giscus-comments)
- [浏览 GitHub 文章评论区](https://github.com/JiamiDog/jiami.dog/discussions/categories/article-comments)
- [返回全部文章](../../../INDEX.md)
