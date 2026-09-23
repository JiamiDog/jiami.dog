---
title: "GCP，Oralce，AWS开启 root 登录"
slug: "gcp-oracle-aws-enable-root-login"
source_id: "3805"
canonical_url: "https://jiami.dog/3805.html"
date_local: "2022-02-26T20:53:59"
date_published: "2022-02-26T12:53:59Z"
date_modified_local: "2026-07-30T14:38:17"
date_modified: "2026-07-30T06:38:17Z"
draft: false
featured_image_url: "https://jiami.dog/wp-content/uploads/2022/02/214ab7b6eebf2a4719c0e5c6cc914606.png"
featured_image_alt: "四个云服务提供商的标志：Azure、AWS、Google Cloud Platform 和 Oracle Cloud Infrastructure。"
categories:
  - "资源攻略"
tags:
  - "甲骨文"
---

# GCP，Oralce，AWS开启 root 登录

> 本文同步自 [jiami.dog 官方原文](https://jiami.dog/3805.html)，以官网版本为准。

![四个云服务提供商的标志：Azure、AWS、Google Cloud Platform 和 Oracle Cloud Infrastructure。](https://jiami.dog/wp-content/uploads/2022/02/214ab7b6eebf2a4719c0e5c6cc914606.png)

## AWS vs AZURE vs GCP vs Oracle - TechBull - Medium

## 主要思路

大同小异，修改 `sshd——config` 文件，把里面的 `PasswordAuthentication` 和 `PermitRootLogin` 都改成 Yes

[修改 SSH 配置文件 /etc/ssh/sshd\_config](https://jiami.dog/4386.html)

CODE

| ``` vi /etc/ssh/sshd_config ``` |
| --- |

找到 PermitRootLogin 和 PasswordAuthentication

CODE

| ``` # Authentication: LoginGraceTime 120 PermitRootLogin yes //默认为no，需要开启root用户访问改为 yesStrictModes yes   # Change to no to disable tunnelled clear text passwords PasswordAuthentication yes //默认为no，改为yes开启密码登陆 ``` |
| --- |

重启 SSH 服务
Ubuntu/debian 适用

CODE

| ``` /etc/init.d/ssh restart ``` |
| --- |

Centos 7 适用

CODE

| ``` systemctl restart sshd.service ``` |
| --- |

## 方便起见

CODE

| ``` sudo sed -i 's/^#\?PermitRootLogin.*/PermitRootLogin yes/g' /etc/ssh/sshd_config; ``` |
| --- |


CODE

| ``` sudo sed -i 's/^#\?PasswordAuthentication.*/PasswordAuthentication yes/g' /etc/ssh/sshd_config; ``` |
| --- |


CODE

| ``` sudo service sshd restart ``` |
| --- |
