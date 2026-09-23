---
title: "苹果手机下载 TikTok 旧版本安装包教程"
slug: "apple-download-tiktok-old-version-installation-package"
source_id: "4174"
canonical_url: "https://jiami.dog/4174.html"
date_local: "2022-03-16T12:43:28"
date_published: "2022-03-16T04:43:28Z"
date_modified_local: "2022-03-16T12:44:38"
date_modified: "2022-03-16T04:44:38Z"
draft: false
featured_image_url: "https://jiami.dog/wp-content/uploads/2022/03/9a7a96c497834c6e9e2b37ec1d9b6ed1.png"
featured_image_alt: "爱思助手界面显示iTunes版本信息及下载按钮"
categories:
  - "资源攻略"
tags:
  - "TIKTOK"
---

# 苹果手机下载 TikTok 旧版本安装包教程

> 本文同步自 [jiami.dog 官方原文](https://jiami.dog/4174.html)，以官网版本为准。

目前苹果手机能在国内免拔卡使用的 TikTok 版本只有 21.1.0 版本，而 App Store 是高于 21.1.0 版本，本次教程就是解决如何下载 TikTok 旧版本安装包。

## **前期准备**

准备美区苹果账号，如果没有可以自行注册，参考内容：[国内注册美区苹果账号及充值方法教程](https://jiami.dog/4012.html "国内注册美区苹果账号及充值方法教程")

下载安装爱思助手，注意只安装爱思助手，提示安装 iTunes Srore 驱动不进行安装，因为需要旧版

下载安装 Fiddler4 网络抓包调试工具。

开启网络代理，要下载网络稳定的[订阅节点](https://jiami.dog/jms/)或其他客户端。

## **操作步骤**

1、打开爱思助手，点击“智能刷机”，找到“其他工具”，下载 iTunes（最后一个支持应用商城的版本），如果你安装了最新版本的 iTunes 驱动，先卸载掉，在安装旧版 iTunes 驱动，如下图：

```
# 如果爱思助手无法下载旧版本iTunes驱动，可通过以下地址安装
https://secure-appldnld.apple.com/itunes12/091-87819-20180912-69177170-B085-11E8-B6AB-C1D03409AD2A6/iTunes64Setup.exe
https://secure-appldnld.apple.com/itunes12/091-33626-20170922-F51D3530-A003-11E7-8324-03D19A97A551/iTunes64Setup.exe
```

![通过爱思助手安装旧版iTunes](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/03/9a7a96c497834c6e9e2b37ec1d9b6ed1.png?ssl=1)

2、打开 iTunes 界面，在“账号”内点击“登录”，输入提前准备的美区苹果账号，验证手机号后成功登录，注意：国内账号无法进行下载，请确认您的账号为美区或其他海外账号，如下图：

![登录美区苹果账号到iTunes](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/03/f309d51d930268e0f31077b8f035e189.png?ssl=1)

3、然后我们在 iTunes 界面右上角的搜索框搜索“tiktok”，搜索出来不要着急点击 获取 或者 下载，切记，如下图：

![在iTunes搜索TIKTOK应用](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/03/945331a415ce3d663cec3ed75b8a17b2.png?ssl=1)

4、然后我们打开下载安装好的 Fiddler4 网络抓包调试工具，进行配置安装 HTTPS 证书，点击“Tools”选择“Options…”，进入后选择“HTTPS”，勾选“Decrypt HTTPS traffic”，弹出 HTTPS 证书安装提示，YES，全部选择是，如下图：

**注意：**如果没有弹出证书提示，那么手动选择左边“Actions”框内的的第一个选择“Trust Root Certificate”进行安装。

![进行配置Fiddler4的选择](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/03/a7452e31da21b91b542897ef0afcf8b6.png?ssl=1)

5、完成以上步骤后，还需要勾选“Check for certificate revocation”，然后点击“OK”，这样就算是配置完成 HTTPS 证书了，如下图：

![Fiddler4安装HTTPS证书](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/03/0fdf999762e1e86f5cc43ff82290fab4.png?ssl=1)

6、证书配置完成后，我们需要运行代码，在左下角黑色输入框输入 bpu MZBuy.woa ，输入完成看到结果后，如下图：

```
bpu MZBuy.woa
```

![开始对iTunes下载抓包](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/03/769ccf91b9af123275c49d342ca46034.png?ssl=1)

7、接着返回 iTunes 搜索“tiktok”的结果页面，点击 TikTok 的“获取”按钮，如下图：

![在iTunes内获取TIKTOK下载地址](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/03/0a4196c63943c610b1321f1dc0b3e2fe.png?ssl=1)

8、返回 Fiddler4 界面，找到“p54-buy.itunes.apple.com”选择，点击“Inspectors”，选择“TextView”，将“<string>847108070</string>”替换成一下版本号，替换完成后点击绿色“Run to Completion”确认，如下图：

```
21.1.0版本ID：844024073
21.1.0版本ID：843972181
```

![在Fiddler4内替换TIKTOK版本号](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/03/54cdf3fc9292165e3bea4ae5b3b3189a.png?ssl=1)

9、完成上一步后，就会在右上角提示下载，如果无法下载，检查UDP是否开启代理，确认代理没有问题，关闭 iTunes 和 Fiddler 程序，从第三步重新开始，多尝试几回，你就会成功下载，如下图：

![下载旧版tiktok成功](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/03/60a291857f0955e546e92860bba5347a.png?ssl=1)

10、下载完成后，在 iTunes 更新选项内，右键 TikTok 图标，选择在 Windows 资源管理器中显示，然后我们将其复制到桌面，文件名为：TikTok 21.1.0.ipa，如下图：

![导出TikTok 21.1.0安装包](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/03/cc8b320b3c668c2fbf9a31db9d65105e.png?ssl=1)

11、在你的 App Store 上登录刚才用的美区苹果账号，用数据线连接电脑，打开爱思助手“信任手机”，在“我的设备”应用游戏内导入安装包“TikTok 21.1.0.ipa”，如下图：

![导入TIKTOK旧版安装包](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/03/d037f2b6f4199a133a85d89b3f4797b4.png?ssl=1)

## **最后总结**

点击 TikTok 的“获取”按钮后，或许你会因为不熟练导致下载失败，多尝试几次就可以了，关闭 iTunes 和 Fiddler 程序，从第三步重新开始，相信自己。

然后还有一点就是，网络节点代理，不仅仅只是TCP协议代理，如果你是路由器使用订阅地址，那么TCP选择节点后UDP选择与TCP一直即可，桌面客户端的开启全局模式。
