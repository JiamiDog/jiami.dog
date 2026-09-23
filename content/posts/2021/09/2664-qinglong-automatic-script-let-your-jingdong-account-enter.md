---
title: "青龙自动脚本：让您的每个京东账号年入几千块"
slug: "qinglong-automatic-script-let-your-jingdong-account-enter"
source_id: "2664"
canonical_url: "https://jiami.dog/2664.html"
date_local: "2021-09-23T01:05:39"
date_published: "2021-09-22T17:05:39Z"
date_modified_local: "2021-09-23T01:05:40"
date_modified: "2021-09-22T17:05:40Z"
draft: false
featured_image_url: "https://jiami.dog/wp-content/uploads/2021/09/20210908193451.png"
featured_image_alt: "青龙面板的定时任务列表，显示了多个京东相关脚本的任务名称、状态和操作选项。"
categories:
  - "资源攻略"
tags:
  - "docker"
  - "青龙"
---

# 青龙自动脚本：让您的每个京东账号年入几千块

> 本文同步自 [jiami.dog 官方原文](https://jiami.dog/2664.html)，以官网版本为准。

![青龙面板+JS自动脚本：每个京东账号年入几千块](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/09/20210908193451.png?ssl=1)

最近被朋友不断安利这个薅羊毛的玩意！昨天抽空也试了下果然很给力：只要一个弱服务器就能挂很多京东账号自动薅羊毛。

> 博主粗糙算了下每个京东账号每天收入。不考虑互助奖励（还不会玩互助池），单纯签到做任务京豆大概2、3块钱，京东极速版微信提现每天可以1块左右，东东农场隔几天就可获得免费水果，还有东东工厂制造实物等等。一年下来还不得收入好几千？要是多挂几个账号，想着就美！

这里简单记录下关键操作，不懂的可以找博主咨询（联系方式自寻）或者在博客留言！

## 一、安装[青龙](https://jiami.dog/tag/qinglong "青龙")面板

仓库地址 <https://github.com/whyour/qinglong>
安装步骤 <https://github.com/whyour/qinglong/blob/develop/INSTALL.md>

## 二、青龙面板添加定时任务

定时任务前辈们已经帮我们做好了，一键添加就完事了，都不要手动一个个加。

### 【JS自动脚本】推荐

查看[docker](https://jiami.dog/tag/docker "docker")容器名可以在服务器命令窗口输入docker container ls命令。博主这里的docker容器名字是qinglong\_web\_1
![docker container ls](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/09/20210908203249.png?ssl=1)

### **推荐1**：

仓库地址 <https://github.com/zero205/JD_tencent_scf>

#### 安装步骤

##### 方式1

在服务器命令窗口输入

```
docker exec -it qinglong_web_1 ql repo https://ghproxy.com/https://github.com/zero205/JD_tencent_scf.git "jd_|jx_|getJDCookie" "backUp|icon" "^jd[^_]|USER|sendNotify|sign_graphics_validate|JDJR" "main"
```

##### 方式2

在青龙面板新建定时任务，名称随意，定时规则填0，命令填

```
ql repo https://ghproxy.com/https://github.com/zero205/JD_tencent_scf.git "jd_|jx_|getJDCookie" "backUp|icon" "^jd[^_]|USER|sendNotify|sign_graphics_validate|JDJR" "main"
```

#### **推荐2**：

仓库地址：<https://github.com/smiek2221/scripts>

##### 方式1

在服务器命令窗口输入

```
docker exec -it qinglong_web_1 ql repo https://github.com/smiek2221/scripts.git "jd_|gua_" "" "ZooFaker_Necklace.js|JDJRValidator_Pure.js|sign_graphics_validate.js"
```

##### 方式2

在青龙面板新建定时任务，名称随意，定时规则填0，命令填

```
ql repo https://github.com/smiek2221/scripts.git "jd_|gua_" "" "ZooFaker_Necklace.js|JDJRValidator_Pure.js|sign_graphics_validate.js"
```

#### **更多推荐**：

更多【JS自动脚本】待探索！

## 三、青龙面板创建环境变量

这里是通过环境变量告诉JS脚本我们京东账号的信息。zero205的开源项目中给了很详细的获取京东账号的cookie的教程
1. [**浏览器获取京东cookie教程**](https://github.com/zero205/JD_tencent_scf/blob/main/backUp/GetJdCookie.md)
2. [**插件获取京东cookie教程**](https://github.com/zero205/JD_tencent_scf/blob/main/backUp/GetJdCookie2.md)
3. **扫码自动获取并录入cookie** （好像）属于京东的漏洞，方法现已失效
为了让脚本跑起来，这里只要添加一个变量就可以：变量名JD\_COOKIE，变量内容

```
pt_key=AAA;pt_pin=BBB;&pt_key=CCC;pt_pin=DDD;&pt_key=EEE;pt_pin=FFF;
```

![变量JD_COOKIE](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/09/20210908203453.png?ssl=1)
AAA，BBB，…，FFF替换为获取到的值！这里只挂了三个京东账号，如果要挂更多账号，只要编辑变量JD\_COOKIE的内容继续以&符号分割往后加cookie就可以了！

## 四、青龙面板修改配置文件

主要是添加“通知推送”相关，将相关通知推送到微信，Telegram或者钉钉等即时聊天工具上。博主配置了“Push Plus”，步骤很简单这里不赘述了。

## 五、最后

感谢开源项目的大佬们！感谢京东爸爸的羊毛！最后，小伙伴们且薅且珍惜！

---

## 继续阅读与讨论

- 分类：[资源攻略](../../../categories/ziyuan-gonglue.md)
- 主题：[docker](../../../tags/docker.md), [青龙](../../../tags/青龙.md)
- [在官网参与本文评论](https://jiami.dog/2664.html#jiami-giscus-comments)
- [浏览 GitHub 文章评论区](https://github.com/JiamiDog/jiami.dog/discussions/categories/article-comments)
- [返回全部文章](../../../INDEX.md)
