---
title: "美国 Stripe(香港 Stripe)成功申请并打通支付环节记录"
slug: "american-stripe-hong-kong-stripe-successfully-applied-for"
source_id: "2191"
canonical_url: "https://jiami.dog/2191.html"
date_local: "2021-08-11T19:57:12"
date_published: "2021-08-11T11:57:12Z"
date_modified_local: "2026-07-30T14:38:15"
date_modified: "2026-07-30T06:38:15Z"
draft: false
featured_image_url: "https://jiami.dog/wp-content/uploads/2021/08/1628683033-d664651ef9b8787bb8e973615ea85a20-1.png"
featured_image_alt: "Stripe支付国家列表和邮箱订阅面板"
categories:
  - "互联网金融"
tags:
  - "stripe"
  - "信用卡"
  - "银行"
---

# 美国 Stripe(香港 Stripe)成功申请并打通支付环节记录

> 本文同步自 [jiami.dog 官方原文](https://jiami.dog/2191.html)，以官网版本为准。

![Stripe支付国家列表和邮箱订阅面板](https://jiami.dog/wp-content/uploads/2021/08/1628683033-d664651ef9b8787bb8e973615ea85a20-1.png)

Stripe公司是由爱尔兰的两位兄弟创建的一家科技公司，致力于提供高效、简洁的互联网支付收款服务。宗旨:所有公司无论规模大小、无论是个人、还是创业公司、还是上市企业都可以用Stripe来收款和管理线上业务。

哪些人或企业、哪些业务场景需要用到Stripe网关进行收款

- 拥有个人网站想从事经营业务的同学(境外无需备案)
- 无法提供对公账户的创业小公司(国内支付需要企业开通对公账户收款)
- 在境外部署了跨境电子商务的个人或企业
- 对[信用卡](https://jiami.dog/tag/credit-card "信用卡")收款有明确需要的业务场景(可以拓展支付渠道和客户群体)
- 任何规模的公司或企业有支付收款需求

## 一、Stripe国际化支付网关简介

Stripe目前支持全球[42个国家](https://stripe.com/global)，很遗憾，和其他全球化的支付网关或[银行](https://jiami.dog/tag/bank "银行")账户一样，中国大陆依然不在支持清单之内。如果想从事跨境经营活动的同学，可以注册美国的Stripe账户或香港的Stripe账户来进行收款，以实现”曲线救国”的目的。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/08/1628683033-d664651ef9b8787bb8e973615ea85a20.png?resize=1980%2C1509&ssl=1)

根据官网介绍，目前全球有几百万的公司接入了Stripe的收款业务。其中比较出名的公司有如下几家，可以看到中国滴滴公司的影子。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/08/1628683033-c6a51441eb6b1ff588085ba3f2d735b8.png?resize=1980%2C682&ssl=1)

## 二、Stripe支付流程简析

总体上，整个支付流程很简洁，这也很符合Stripe的设计初衷——简单到让傻瓜都能使用。

1. 商户支付页面接入Stripe的js文件
2. 客户端将用户输入的信用卡信息或者其他银行卡信息(敏感信息)发送到 Stripe 服务器。
3. Stripe 服务器会对用户提交的信用卡信息进行检查校验，如果校验通过，则会返回一个token信息给客户端。
4. 客户端将token和订单信息发送到商家服务器。
5. 商家服务器会计算该订单的金额，并发送到Stripe服务器进行扣费。这里需要注意是，订单的金额是由后台计算决定的，不是由前端告知后台的。没有人会直接让客户决定商品的价格。
6. Stripe返回交易结果给商家服务器端。
7. 商家服务将交易结果返回给客户端。

值得一提的是，在支付后台可以看到每笔订单的交易细节，可以回溯到每个交易节点，这点值得点赞。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/08/1628683034-719eefa99ea1d56e3706f62e6c45462b.png?resize=1980%2C1014&ssl=1)

## 三、美区Stripe注册实战

注册美区Stripe所需要准备的材料

1. 美国电话卡
2. 美国银行账户(P卡美国社区联邦储蓄账户、或者美国银行发行的其他借记卡)
3. 美国手机号[Google voice](https://jiami.dog/2032.html)
4. 中国护照
5. 美国[SSN或EIN](https://jiami.dog/2116.html)
   6. [美国信件地址](https://jiami.dog/88.html): 注册Stripe时需要填写的美国地址可直接使用银行地址，也可以使用你购买的虚拟信箱地址。

1. 进入美区[stripe](https://jiami.dog/tag/stripe "stripe")的官方注册网站，点击注册，填写常规个人信息，个人信息一定要如实填写，很多人搞虚假的信息弄巧成拙，最终导致被封号。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/08/1628683035-b03d7688abfb52cd4f1403d20d2a2160.png?resize=1920%2C997&ssl=1)

1. 进入到SSN号码填写环节时，可以先随便写个尾号，比如8888，可以验证通过。等账户成功下发后，Stripe官方会进入SSN的审核期，会发邮件提示你的SSN号码不匹配，需要你重新提交资料验证(该部分内容后面再讨论)

3.开通支付方式，一般常见的几种支付方式如下:

- Cards，也就是最核心的信用卡支付方式，支持Visa、Master、American Express、Discover、Diners Club、JCB等机构发行的卡片
- ACH Credit Transfer. 支持美国用户在美国银行账户之间通过ACH方式转账
- Alipay，支付宝国际版。用户支付成功后，资金进入stripe的支付宝账户，支持提现至个人银行卡账户。交易汇率按照国际汇率进行实时更新
- ApplePay, 苹果支付，接入过程稍微繁琐一点。
- WechatPay， 微信支付，微信支付只是beta版本，需要用户自己做定制。stripe官方发文，根据美国政策规定，2020年9月20日，已经无法通过stripe接收微信付款。随后政府又放开了监管政策，目前又可以使用了。不推荐使用，会影响业务交易的稳定性。![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/08/1628683035-3a3fb043253a5324d8e010e9c9450232.png?resize=2522%2C802&ssl=1)

## 四、美区Stripe如何进行Tax税务认证

关于税务信息认证。税务信息认证是Stripe支付的核心关键点所在，这点也基本上挡住了90%的中国卖家账户。可以使用ITIN税务信息或者EIN税务信息进行认证，可以参考我之前写的文章《[成功申请美国EIN税号，ITIN/EIN/SSN等税务识别号的区别](https://jiami.dog/2116.html)》

刚开通的未认证的美区Stripe是可以进行交易的，但是大概有效期是一个月左右。然后官方会发邮件提醒你进行税务认证，否则账户会受到限制，影响正常的业务交易流程。官方的提示邮件如下，并对支持的认证资料类型做了详细说明:

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/08/1628683036-c02492765d2eb3e476bbebbd78c67865.png?resize=1980%2C1002&ssl=1)

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/08/1628683036-55ceb9f4ebe1fc5d4d1aa062e3f737c9.png?resize=1920%2C993&ssl=1)

这里由于我之前申请过美国的EIN税号，所以使用EIN号码来进行认证，认证通过后的信息如下，在Tax information后面会有个绿色的verified状态信息。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/08/1628683037-8fef68ea296da2f6e8c0a0e42b00c852.png?resize=2540%2C1344&ssl=1)

## 五、美区Stripe如何绑定银行卡收款

完成相关认证服务后，需要在后台绑定你的银行卡信息。在settings–》business information栏目里面填写相关账户信息

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/08/1628683037-3c4f3c3a925323bd241ce6a93ffd956c.png?resize=1980%2C802&ssl=1)

推荐的美国银行卡种类

- 针对国内用户，推荐使用[Velo华美银行办法的借记卡](https://jiami.dog/2181.html)
- 其他美国银行机构发行的借记卡也可以
- TransferWise申请到的美国银行卡
- Payonner颁发的美国虚拟银行账户(交易退款环节会失败，如果交易有频繁的退款行为，不推荐使用)
- WorldFirst颁发的美国虚拟银行账户(交易退款环节会失败，如果交易有频繁的退款行为，不推荐使用)

银行账户通过后就可以开始正常交易了，如下是测试账户的交易信息统计。在payments信息栏中可以看到每一笔详细的交易订单情况，还是很直接的。整个交易过程一目了然。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/08/1628683037-3038a4212080215bc1a31eb4ae8e263b.png?resize=2514%2C946&ssl=1)

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/08/1628683037-e6ccdcd26727d2f4373b73cef588c76c.png?resize=2506%2C828&ssl=1)

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2021/08/1628683038-0c9398cfaca696e48f94297e8b5e60da.png?resize=2520%2C1258&ssl=1)

不过有几点值得注意:

- 对于没有美国本土银行账户的朋友，可以使用Transferwise或者Payonner或者worldfirst开设的虚拟账户绑定进行收款。这里有个很大的Bug: 如果你的交易业务涉及到退款纠纷等，Stripe的官方需要在你的银行卡内扣款，如果是W卡或者P卡颁发的虚拟账户，就会导致扣款失败。以P卡为例，允许扣款的最低额度是50美金，这就显得很蛋疼了。
- 建议还是绑定正规的美国本土银行进行收款，防止上文中所提的问题，账户受到审核

## 六、美区Stripe交易手续费分析

1.银行卡或数字钱包。征收2.9% +$USD0.3

包含Visa、Master、American Express、Discover、Diners Club、JCB、ApplePay、GooglePay、银联卡

2.本地银行转账。征收0.8%，5美金封顶。

包含用 ACH 借记、ACH 贷记或电汇方式，安全地接收大额付款或定期付款

1. 提款周期: 正常的周期在提款日期起，一般在7天内到达个人账户。如果希望入账实时滚动，快速回款。可以将后台的支付周期改为每天，这样，stripe会每天自动的将余额打款到你的银行账户。

## 七、Stripe账户被封号的常见原因及分析

Stripe的风控机制还是很先进的，具体的原理不得而知。但是总结了很多封号的原因，其中最核心的一点就是，stripe判断你的账户成为了高风险账户。导致账户被判为高风险的因素有很多，常见的有如下几种

1.网站的经营内容不合规，比如: 为了躲避审核，你在网站首页搞得很正规，结果内页隐藏了N个层级卖充气娃娃，导致stripe二审或三审的时候被发现了。你说封还是不封呢？

2.交易欺诈。这里涉及到卖家和买家双方的行为。

其中，对于卖家而言，故意买黑卡信用卡，自己进行虚假交易；对于买家而言，故意在卖家的店铺进行骚操作，包括:买黑卡刷记录，同一IP高频次交易

1. 发生大量的拒付款信息。涉及到拒付款的因素有很多，常见的为: 金额不符、信用卡未经授权、货物未收到等

4.交易失败，导致交易失败的因素有很多，比如信用卡的信息错误、过期，黑卡交易等

5.交易风险，比如非法盗刷信用卡等，这里就不展开做深入的讨论了。

## **八、美区Stripe账户和港区Stripe账户有什么区别**

总体上讲，申请流程基本一样。最大的区别就是港区stripe监管力度比美区stripe小很多，不需要提供tax税务认证

所需要的注册材料为:

1. 香港手机号
2. 香港银行账户(拍住赏绑定的香港银联账户，Payoneer或者Worldfirst分配的香港银行账户)
3. 护照照片
4. 香港地址(可以直接用如上虚拟银行的地址)

另外，港区的Stripe支持添加绑定多个银行账户。

其他的流程细节部分基本大同小异

## **九、一个Stripe账户是否可以绑定多家商店(网站)进行收款**

做生意的基本上都不会把鸡蛋放到一个篮子里，所以一般手上可能有几个店铺或网站，那么能不能将一个账户绑定到所有的店铺进行收款呢？

Stripe的官方并没有禁止这种行为，官方表明一个Stripe账户是可以管理多家店铺的。绑定方式为，在主账户的后台添加子账户，进行统一管理。但是Stripe官方更加建议将不同的独立业务绑定单独的Stripe账号。这样做有几个好处:

- 单独的税法和法人信息。每个帐户只能与一个企业的税号和法人实体相关联。如果您经营的多个企业具有单独的税号信息（例如，单独的法人实体），则必须为每个企业创建其他帐户。
- 独特的声明描述符和公共业务信息。将相同的Stripe帐户用于单独的业务可能会造成混乱，因为两者使用的公共业务信息相同。例如，从您的公司“ XYZ”购买商品的客户可能会在其对帐单上看到来自您的公司“ ABC”的费用，有可能引起纠纷。每个其他帐户都有其自己的公共信息，以准确描述您的业务和付款。
- 更轻松的报告和对帐。分开您的企业处理的付款，可以更轻松地找到付款，创建和导出报告，以及将付款与您的银行帐户进行对帐。
- 支付到单独的银行帐户。每个其他帐户都可以将单独的银行帐户用于付款（尽管您可以根据需要使用同一银行帐户）。
- 防止账户牵连。这是很重要的，如果多家店铺或网站绑定在一个相同的Stripe账户主体下，若有一个店铺的拒单率出奇的高，那么可能导致整个账户被停用，从而牵连到其他店铺的正常业务。

---

## 继续阅读与讨论

- 分类：[互联网金融](../../../categories/hulianwang-jinrong.md)
- 主题：[stripe](../../../tags/stripe.md), [信用卡](../../../tags/信用卡.md), [银行](../../../tags/银行.md)
- [在官网参与本文评论](https://jiami.dog/2191.html#jiami-giscus-comments)
- [浏览 GitHub 文章评论区](https://github.com/JiamiDog/jiami.dog/discussions/categories/article-comments)
- [返回全部文章](../../../INDEX.md)
