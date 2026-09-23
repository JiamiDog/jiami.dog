---
title: "手把手教你发行自己的加密货币"
slug: "teach-you-to-issue-your-own-cryptocurrency"
source_id: "2317"
canonical_url: "https://jiami.dog/2317.html"
date_local: "2021-08-16T17:10:03"
date_published: "2021-08-16T09:10:03Z"
date_modified_local: "2021-08-16T17:32:42"
date_modified: "2021-08-16T09:32:42Z"
draft: false
featured_image_url: "https://jiami.dog/wp-content/uploads/2021/08/1629104212-1a32a1fd7c2b97d6048d94ad9d1f1508.png"
featured_image_alt: "以太坊智能合约部署界面，显示合约代码、参数输入和交易确认。"
categories:
  - "资源攻略"
tags:
  - "数字货币"
---

# 手把手教你发行自己的加密货币

> 本文同步自 [jiami.dog 官方原文](https://jiami.dog/2317.html)，以官网版本为准。

![以太坊智能合约部署界面，显示合约代码、参数输入和交易确认。](https://jiami.dog/wp-content/uploads/2021/08/1629104212-1a32a1fd7c2b97d6048d94ad9d1f1508.png)

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/08/1629105005-ccb23e749bbc7af86701c7af800b905b.png?resize=768%2C348&ssl=1)

手把手教你发行自己的加密货币

空气币的发行过程极为简单，这里就开个文章给大家介绍下如何发行。

本教程前置要求：

1.会魔法上网（爬梯子），这里不懂的话建议直接关闭本页面。

2.需要十几元的以太坊（发行成本，本文链接测试网络，0成本）

3.需要一个MetaMask钱包

文中使用到的一些地址：

编辑器：<https://remix.ethereum.org>

Metamask钱包：<https://metamask.io>

以太坊测试币获取地址：<https://faucet.metamask.io>

以太坊代币代码：<https://github.com/ConsenSys/Tokens/tree/fdf687c69d998266a95f15216b1955a4965a0a6d/contracts/eip20>

以太坊官方ERC-20 标准：<https://eips.ethereum.org/EIPS/eip-20>

## 发行成本

本文因为测试发行，所以是0成本。

实际发行的话也就几十块。

## 和交易所上的币有什么不同？

举例：最近（2021年5月）玩币的应该都听说过shib（柴犬币/屎币），这个币在上交易所之前也是在SWAP等去中心化交易所玩的，上面别人通过搜索他的合约地址可以找到shib，然后可以用其他的币来兑换shib。

我们这篇文章讲的就是创建币种并且写入区块链中，别人也可以通过我们的合约地址来兑换币。

有想法的可以找小交易所上市交易。目前交易所上很多币都是这么个情况。当然你要会忽悠，创建一个币不难，难的是卖出去。

**以下是教程正文**

## 1.安装MetaMask钱包

Metamask钱包：<https://metamask.io>

## 2.在MetaMask获取测试ETH币

这里因为是写教程所以我们就不使用真实ETH币来操作了。如果你要发行自己的币，就自己转入真实ETH币即可。

MetaMask钱包可以连接测试网络，专门给我们测试用的，里面余额等信息都是假的。我们在测试网络中可以获取虚拟的ETH币。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/08/1629105006-3e406153dac86e76fbcd1714a3cf0219.png?ssl=1)

点“购买”

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/08/1629105007-de65586a1e04145dc3e99972075f0422.png?ssl=1)

下面有添加测试币的按钮

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/08/1629105007-de65586a1e04145dc3e99972075f0422.png?ssl=1)

会跳到一个网站。

![](https://i0.wp.com/pic4.zhimg.com/v2-b9eabbdaa05d12da22e6e1fb52613317_b.png?ssl=1)

网站里点击“request 1 ether from faucet”就自动给我们发1个测试ETH币。到账速度很快，几乎十几秒。没到账就多等一会。

## 3.创建加密货币代码

代码？？？我不会啊怎么办？

没关系，以太区块链官方有现成的代码可以使用。我们复制过去就可以了。

打开地址

<https://github.com/ConsenSys/Tokens/tree/fdf687c69d998266a95f15216b1955a4965a0a6d/contracts/eip20>

如下图，有两个文件。EIP20.sol和EIP20Interface.sol

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/08/1629105007-b29254535a4db07c3f53d3672ad231ff.png?ssl=1)

我们先不管他。继续下一步

## 4.部署智能合约

打开以太坊智能合约语言在线编辑器：http://remix.ethereum.org

![](https://i0.wp.com/pic4.zhimg.com/v2-252ec085a8a8e8365a31d831237a4b8b_b.png?ssl=1)

下面有导入Github代码的地方。

我们复制EIP20.sol和EIP20Interface.sol的代码地址。

EIP20.sol：
<https://github.com/ConsenSys/Tokens/blob/fdf687c69d998266a95f15216b1955a4965a0a6d/contracts/eip20/EIP20.sol>

EIP20Interface.sol：
<https://github.com/ConsenSys/Tokens/blob/fdf687c69d998266a95f15216b1955a4965a0a6d/contracts/eip20/EIP20Interface.sol>

填入编辑器并点击OK就导入了。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/08/1629105008-b7bf2d9b9fc3f786d553198f6e736e95.png?ssl=1)

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/08/1629105009-b6c9d4ae0596614064a1901eb73cf6ba.png?ssl=1)

然后我们开始编译代码

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/08/1629105010-839b177b3048dc67363c0b9c4258275e.png?ssl=1)

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/08/1629105010-ef4315b5d0f36eeb819506e99415fc38.png?ssl=1)

这里不需要修改东西，直接点下面的Compile EIP20.sol按钮即可。

然后是部署代码

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/08/1629105011-b46117828112bbfaa9fd030cc47abc62.png?ssl=1)

这里的ENVIRONMENT我们选择第二个INjectrd Web3,这时候会连接我们的MetaMask钱包。并在编译器显示余额。

然后下面的GAS LIMIT和VALUE不用修改。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/08/1629105011-899556bb8e9b2117892eb042f1301d85.png?ssl=1)

接着下面就是我们发行的币一些参数了。

INITIALAMOUNT：币的发行总量（这里假如我们发行一亿个币，我们写了100000000后还要再加DECIMALUNITS个0（DECIMALUNITS设置的小数点后4位就加4个0，设置的10位就要加10个0））
TOKENNAME：币全名
DECIMALUNITS：小数点后显示几位
TOKENSYMBOL：币的简写（比如比特币是BTC，以太币是ETH）

本文参数：

INITIALAMOUNT：1000000000000000000000000
TOKENNAME：cheshirex
DECIMALUNITS：10
TOKENSYMBOL：rex

**PS：**下图截图DECIMALUNITS的值有误，应该写个数字10，我写了10个0.

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/08/1629105012-d759957c39e8aaa6fee6ed6e5aabf4f2.png?ssl=1)

然后点击下面的橙色按钮transact即可。

点击后钱包会弹出窗口，并显示本次发币的费用。确认即可。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/08/1629105012-2d4d773c27f7ea95b7980f1e2d753441.png?ssl=1)

然后编辑器中会开始部署代码。等待两分钟，显示有个绿色对勾就完成了。如下图

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/08/1629105014-3ac1d06cfaad1b8e665defdc9854c6e6.png?ssl=1)

## 5.查看发行货币的信息

打开我们的钱包，下面查看“活动”

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/08/1629105014-64aab03bb70f6607828224239b110bf5.png?ssl=1)

点击最上面的活动。

并在以太坊浏览器中查看

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/08/1629105014-3c53bab3bd48ca8b78e75665b99745dd.png?ssl=1)

会显示刚才的交易信息

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/08/1629105015-80c15c4016ea979c14f13d7e5c548b03.png?ssl=1)

## 6.将发行的货币添加到钱包

复制我们上一步图片里的新发型加密货币地址。

并在MetaMask钱包测试网络中点击添加代币。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/08/1629105015-95df0297fe60c26f93bb00136a2d6781.png?ssl=1)

填入我们复制的加密货币地址。会显示出代币信息。下一步添加即可。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/08/1629105016-6c5c6929866c6ec0e5c1f911669a67ea.png?ssl=1)

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/08/1629105016-6bff3a15ceb283c76d35d12c79eccd88.png?ssl=1)

好了，我们已经有一百万亿rex币了。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/08/1629105017-37ce6822255e4f8204c44b4523644316.png?ssl=1)

---

## 继续阅读与讨论

- 分类：[资源攻略](../../../categories/ziyuan-gonglue.md)
- 主题：[数字货币](../../../tags/数字货币.md)
- [在官网参与本文评论](https://jiami.dog/2317.html#jiami-giscus-comments)
- [浏览 GitHub 文章评论区](https://github.com/JiamiDog/jiami.dog/discussions/categories/article-comments)
- [返回全部文章](../../../INDEX.md)
