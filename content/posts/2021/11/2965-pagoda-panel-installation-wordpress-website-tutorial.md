---
title: "宝塔面板安装WordPress网站教程"
slug: "pagoda-panel-installation-wordpress-website-tutorial"
source_id: "2965"
canonical_url: "https://jiami.dog/2965.html"
date_local: "2021-11-17T20:42:27"
date_published: "2021-11-17T12:42:27Z"
date_modified_local: "2021-11-17T20:42:28"
date_modified: "2021-11-17T12:42:28Z"
draft: false
featured_image_url: "https://jiami.dog/wp-content/uploads/2021/11/1637151893-20211117191532-1.png"
featured_image_alt: "宝塔面板推荐安装LNMP和LAMP环境选项界面"
categories:
  - "资源攻略"
tags:
  - "wordpress"
  - "wordpress建站"
  - "域名"
  - "数据库"
  - "数码"
---

# 宝塔面板安装WordPress网站教程

> 本文同步自 [jiami.dog 官方原文](https://jiami.dog/2965.html)，以官网版本为准。

### 安装网站环境

---

成功进入宝塔面板后，会提示安装LNMP运行环境

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/11/1637151893-20211117191532-1.png?resize=651%2C419&ssl=1)

LNMP即Nginx、MySQL和PHP，这些环境是运行WordPress程序必不可少的。推荐使用PHP7以上版本，其他保持默认即可，推荐使用编译安装，耐心等待，可以在左上角查看进度。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/11/1637151949-20211117202515-1.png?resize=633%2C586&ssl=1)

### 必要的安全设置

---

为了提高安全性，建议修改面板的别名、默认端口、安全入口、面板用户和密码。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/11/1637151993-20211117202616-1.png?resize=880%2C808&ssl=1)

不建议修改并发线程，不建议添加[域名](https://jiami.dog/tag/domain-names "域名")和授权IP，以免出现访问不了面板的情况，其他的保持默认即可。

### 建立WordPress网站

宝塔面板有一键部署WordPress网站插件，但是版本较老，后期进入WordPress后台得升级。手动部署需要到WordPress官网下载最新的安装程序，还可以保证安全性。下面介绍的也会是手动建立站点，其实并没有很复杂。

#### 添加站点

---

在宝塔界面找到网站，点击添加站点，会出现以下界面：

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/11/1637152050-20211117202702-1.png?resize=638%2C561&ssl=1)

域名根据实际情况填写，如果是国内空间，则域名必须备案，国外空间则不需要，一般写一个顶级域名和一个www二级域名即可，比如www.jiami.dog，jiami.dog，搭建阶段可以也用云服务器的公网IP代替。

FTP可以选择不创建，后面可以用宝塔面板的文件管理。

[数据库](https://jiami.dog/tag/database "数据库")选择MySQL，会提示输入用户名名称和密码，自动建立与用户名同名的数据库

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/11/1637152129-20211117202810-1.png?resize=616%2C115&ssl=1)

PHP版本选择你安装的PHP版本，我安装的是PHP7.2，建议安装版本不低于7。

点击提交，会提示站点创建成功，并显示数据库用户名和密码，这里不用刻意去记录，可以在宝塔的数据库管理界面再次查看。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/11/1637152144-20211117202825-1.png?resize=626%2C245&ssl=1)

站点创建完成之后，可以通过公网IP或你绑定的域名测试一下，在浏览器输入公网IP或你绑定的域名即可，如果成功，会显示以下页面：

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/11/1637152229-20211117202930-1.png?resize=704%2C377&ssl=1)

到这里，网站的基本架构已经搭建完成了，下面要做的就是安装WordPress网站程序。

#### 下载WordPress安装程序

---

到[WordPress中文官网](https://cn.wordpress.org/)下载最新的中文安装包，一定要选择tar.gz格式

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/11/1637152250-20211117202944-1.png?resize=725%2C534&ssl=1)

下载完成后需要将安装程序上传到刚刚建立的网站目录下，进入宝塔面板首页，找到你刚刚创建的网站目录

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/11/1637152280-20211117203003-1.png?resize=588%2C420&ssl=1)

进入此目录会看到如下文件列表，这是宝塔创建站点时的默认主页和404页面，删除即可，.htaccess和.user.ini如果你不懂，就不要动。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/11/1637152438-20211117203234-1.png?resize=484%2C246&ssl=1)

#### 上传WordPress安装程序

---

在你的网站目录下，点击上传，将你刚刚下载的WordPress程序上传，上传成功后是这个样子的：

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/11/1637152453-20211117203245-1.png?resize=675%2C270&ssl=1)

#### 解压WordPress压缩包

---

这一步可以使用命令行操作或使用宝塔面板操作，如果使用面板解压，那么解压后的目录权限默认是www用户的。如果使用命令解压，不要忘记把目录所属组更改为www用户，并把权限设置为755。

鼠标移上WordPress压缩包，右侧会出现工具栏，选择解压，在弹出的界面再次选择解压即可，解压完成后文件列表会是这样：

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/11/1637152471-20211117203307-1.png?resize=530%2C246&ssl=1)

进入[wordpress](https://jiami.dog/tag/wordpress "wordpress")目录，全选所有文件，点击复制或剪切，然后返回到站点目录，选择粘贴所有，你的站点目录一定要是这个样子的：

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/11/1637152523-20211117203447-1.png?resize=828%2C626&ssl=1)

之后就可以删除wordpress目录和wordpress压缩包，现在已经没用了。到此就完成了WordPress安装的准备工作。

#### 运行WordPress安装程序

---

浏览器输入域名或公网IP，可以看到WordPress的安装程序页面，出现这个页面说明你之前做的都没问题。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/11/1637152546-20211117203502-1.png?resize=800%2C530&ssl=1)

在开始之前，我们需要找到之前创建的MySQL数据库用户名和密码，在宝塔面板-数据库中可以看到

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/11/1637152698-20211117203724-1.png?resize=773%2C187&ssl=1)

回到WordPress安装页面，点击现在就开始，填入你的数据库名称、用户名和密码，其他项目保持默认即可。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/11/1637152715-20211117203739-1.png?resize=781%2C523&ssl=1)

如果信息都正确的话，点击提交会出现以下页面：

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/11/1637152788-20211117203910-1.png?resize=760%2C828&ssl=1)

输入站点标题、用户名、密码和电子邮件，同时勾选“建议搜索引擎不索引本站点”，因为在网站建设初期不需要搜索引擎收录，后期可以改，点击“安装WordPress”，安装完成之后会出现以下界面：

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/11/1637152803-20211117203922-1.png?resize=765%2C429&ssl=1)

你可以选择登录或者在浏览器输入你的域名或公网IP，出现以下类似的网页就说明站点搭建成功了。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/11/1637152853-20211117204022-1.png?resize=822%2C451&ssl=1)

### 设置伪静态和固定链接

这一步尤其重要，正确设置伪静态和固定链接可以保证网站被正常访问，顺序一定不要搞错了，先在宝塔设置伪静态规则，再设置WordPress固定链接，否则可能导致除首页之外的任何页面都访问不了。

#### 设置伪静态规则

---

打开宝塔面板，找到你的站点，点击设置，找到伪静态，选择WordPress

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/11/1637152873-20211117204034-1.png?resize=686%2C528&ssl=1)

#### 设置固定链接

---

进入WordPress后台管理界面，找到设置-固定链接，我们使用自定义结构，用文章ID作为链接地址。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/11/1637152922-20211117204139-1.png?resize=819%2C133&ssl=1)

### 结束语

---

搭建一个网站的步骤还是挺多的，好在有这么多好用的工具来帮助我们建站，除了安装宝塔面板，没有输入一行命令就这么快速地搭建一个网站，真是太赞了。在此过程中要有足够的耐心，看起来容易，但是做起来，还是挺费时间的，希望各位胆大心细，出现问题不要惊慌，检查步骤即可，最坏情况删掉重新再来也不是麻烦事。
