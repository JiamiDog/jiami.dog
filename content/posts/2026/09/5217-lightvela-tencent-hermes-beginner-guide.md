---
title: "腾讯出品 LightVela 新手教程：在微信、QQ 里用自己的云端智能体"
slug: "lightvela-tencent-hermes-beginner-guide"
source_id: "5217"
canonical_url: "https://jiami.dog/5217.html"
date_local: "2026-09-28T23:11:08"
date_published: "2026-09-28T15:11:08Z"
date_modified_local: "2026-09-28T23:11:08"
date_modified: "2026-09-28T15:11:08Z"
draft: false
featured_image_url: "https://jiami.dog/wp-content/uploads/2026/09/lightvela-channels-v1.0-2026-09-28.png"
featured_image_alt: "LightVela 通道配置页，展示微信、QQ、企业微信、钉钉和飞书，QQ 已连接"
categories:
  - "资源攻略"
tags:
  - "AI智能体"
  - "Hermes Agent"
  - "LightVela"
  - "新手教程"
  - "腾讯轻量云"
---

# 腾讯出品 LightVela 新手教程：在微信、QQ 里用自己的云端智能体

> 本文同步自 [jiami.dog 官方原文](https://jiami.dog/5217.html)，以官网版本为准。

我已经把 [LightVela](https://jiami.dog/tag/lightvela "LightVela") 的 QQ 通道接上了。

本文的官网和注册入口使用我的邀请链接。通过这些入口注册或消费，我可能获得平台奖励或返利，具体以各平台规则为准。

这次想写的，不是又一个“注册之后就能改变人生”的 AI 推荐。我的读者大多在国内，有人打不开 ChatGPT，有人还没用上 Claude。你让他先买服务器、装环境、配一堆接口，他可能连第一步都不想动了。

腾讯出品的 [**LightVela**](https://jiami.dog/lightvela)，值得从这个角度看看：能不能少折腾部署，先在熟悉的微信、QQ 里用上自己的云端智能体？

可以从它开始。但别把开通账号当成学会了。下面按新手实际要走的顺序来，一直到它交出第一份有用的结果。

![LightVela 通道配置页，展示微信、QQ、企业微信、钉钉和飞书，QQ 已连接](https://i0.wp.com/jiami.dog/wp-content/uploads/2026/09/lightvela-channels-v1.0-2026-09-28.png?resize=2118%2C716&ssl=1)

我的 LightVela 通道页面，QQ 已连接。新手可以先接一个自己常用的聊天通道，完成一次真实任务后再增加其他通道。

## LightVela 是什么？和腾讯、Hermes 有什么关系

[LightVela 官网（我的推荐入口）](https://jiami.dog/lightvela)的[官方介绍](https://lightvela.com/about)明确写着：产品由[腾讯轻量云](https://jiami.dog/tag/%e8%85%be%e8%ae%af%e8%bd%bb%e9%87%8f%e4%ba%91 "腾讯轻量云")团队出品，目前提供 [Hermes Agent](https://jiami.dog/tag/hermes-agent "Hermes Agent") 托管服务。

你不用自己租一台 VPS，再去安装 Hermes。平台替你维护云端运行环境，你配置智能体、模型和聊天通道。这和在自己服务器上安装、拿到服务器管理权限，是两种用法。

Hermes 是执行任务的智能体；GPT、Claude 或其他模型负责理解和生成；微信、QQ 是你给它发消息、收结果的入口。LightVela 把这些东西接起来，并提供托管、记忆和定时任务等功能。

它不是把 ChatGPT 原样搬进 QQ，也不能保证复制某个产品的全部能力。“云端运行”表示不用让自己的电脑一直开着，不是无限用量、永不故障。

这篇教程分两段：先用平台可用的模型积分跑通，再给需要 GPT、Claude 的人配置自定义模型。暂时用不上中转站，就先不买。

## 开通之前，先算清 LightVela 的费用

按 [2026 年 9 月 28 日的官方套餐说明](https://lightvela.com/docs/plans)，Launch 标准月价 45 元，带少量体验积分；Launch AI 标准月价 68 元，包含每月 4500 模型积分。两者的云端环境都是 2 核、8GB 内存。

当前文档写新用户首购 Launch、Launch AI 可以免费体验一个月，首页也展示了一个月与 4500 积分。开通时仍要看你自己的订阅页：活动有没有、首期多少钱、续费多少钱，以那里为准。旧教程里的“14 天”别拿来直接套。

费用要分开看：

| 你用什么 | 要看哪笔费用 | 新手容易误解的地方 |
| --- | --- | --- |
| LightVela 云端智能体 | 平台套餐、有效期和续费价 | 免费体验不等于永久免费 |
| 平台自带模型 | 套餐内模型积分及消耗记录 | 4500 积分不是固定 4500 次聊天 |
| 自定义模型 | 第三方 API 账户的套餐或扣费 | 接上 Key 不等于上游免费 |

新手先选有可用模型积分的方式，试一个小任务。以后确认只用自有 Key，再比较普通版是否更合适。长上下文、工具调用、重试都会改变模型开销，不能凭“我一天只发几条消息”就断言很便宜。

还有个实际问题：试用结束忘了续费怎么办？官方说明是到期约一天后暂停权益，数据从到期日起保留 14 天，之后释放且不可恢复；目前为手动续费，不自动扣款。重要文件自己留一份，别等暂停后才想起。

## 第 1 步：注册 LightVela，创建第一个智能体

从 [LightVela 注册入口](https://jiami.dog/lightvela)进入官网，选 QQ 或微信登录，按订阅页要求完成实名认证、核对套餐，再跟着引导创建第一个智能体。

名字随你，例如“我的工作助理”。等页面显示它已经可用，再去下一步。不是点了创建就算部署完成。

这里有两个容易踩的坑。QQ 登录和微信登录会生成不同的 LightVela 账号，数据不互通，选定一种就固定用它。认证资料只填官网的认证表单，不要发给机器人，更别丢进群里。具体流程可对照[官方快速开始](https://lightvela.com/docs/quickstart)与[账号说明](https://lightvela.com/docs/account)。

网页里先发一句简短的中文消息，确认能回复。如果套餐有可用积分，先用它，不用急着注册另外两家。

## 第 2 步：接入 QQ 或微信，先完成一件小事

进入智能体的“通道”页面。上面的截图能看到微信、QQ、企业微信、钉钉、飞书，我的 QQ 已显示“已连接”。这不表示五个通道都已经替你测试过。

个人使用就先接一个。点 QQ 或微信的“连接”，按当前页面提示扫码授权；若显示 App ID、Secret 方式，那是另一套机器人配置，不要凭空填数字，也不要把登录密码填进去。

连接后，从选定的聊天软件发一条消息，看它是不是真的回到了同一个聊天窗口。网页能聊、QQ 收不到，要先查通道，不要马上重买模型额度。

按[官方微信接入说明](https://lightvela.com/docs/configuration/channel-wechat)，微信目前只支持一对一，不支持群聊。[QQ 群策略](https://lightvela.com/docs/configuration/channel-qq)默认允许群成员 @ 触发对话。刚开始先用私聊，不然大家轮流试一句，你的额度也跟着跑。

然后做一件你原本就要做的事。比如拿三款产品的公开参数，整理一张选购表。下面这张任务卡可以整段复制，参数接在它后面；这是第一次使用，不需要联网，也不用给它任何账户权限。

```
::ILANG::v5.0
[TYPE:task][PROJECT:lightvela_first_result][LANG:zh]
::MODULE{TASK}
  [INPUT] 我会在这张任务卡后提供三款产品的公开参数和我的选购条件
  [DO] 只根据我提供的材料 整理名称 价格 适用场景 限制的对照表
  [DO] 信息没有提供就写未提供 不编造价格规格测试结果
  [DO] 根据我的条件推荐一个选择 说明理由和仍需确认的问题
  [MUST] 不联网 不登录 不购买 不创建定时任务 不处理密码或身份资料
::MODULE{ACCEPTANCE}
  [DO] 表后列出推荐依据对应的原始参数 让我逐项核对
  [MUST] 材料不足以推荐时直接说明缺什么 不假装已经测试产品
::ILANG::COMPLETE::
```

读完结果，检查它有没有编价格、有没有漏掉你在意的条件。如果你没提供尺寸，它能说“未提供”，比一本正经地猜一个数字更有用。

到这里，你已经有了能在聊天软件里帮你处理材料的助理。后面接 GPT、Claude，是换模型，不是从头再买一遍服务器。

## 第 3 步：想用 GPT、Claude，再准备自定义模型

我这次的分工是：GPT 用 [CodeGo](https://jiami.dog/codego)；Claude 我更倾向于 [APIKEY](https://jiami.dog/apikey) 这一路。我自己付费使用过，提供的订单截图里有多笔已完成订单，不是只看了宣传页就来推荐。

但花过钱能证明购买经历，证明不了模型永远“满血”、不会替换、以后一定稳定。有人把不同通道都叫“逆向 Claude”，公开说明却还有第三方、Max、官渠等分组，不能一概而论。选的是哪个组，允许怎么用，才是你要核对的。

下面三个是我的邀请入口，通过它们注册或消费，我可能得到平台奖励或返利，具体以各站规则为准。你按需求选，不用一次把三家都充上。

- [LightVela：开通云端智能体](https://jiami.dog/lightvela)
- [CodeGo：本文采用的 GPT 接入路线](https://jiami.dog/codego)
- [APIKEY.FUN：本文讨论的 Claude 接入路线](https://jiami.dog/apikey)

APIKEY 网站页头显示 APIKEY.FAN，邀请入口在 .fun 域名，接口地址又在 .fan，别拿注册页当 API 地址。

更要看的是它的[公开支持地区](https://apikey.fun/legal/supported-regions)：列表里没有中国大陆。我个人用过，不等于每位大陆读者都符合它的服务条件。充值前确认你的账户地区、所选分组是否支持 LightVela 外接；没确认就先用平台自带模型，不提供虚报地区的办法。

### CodeGo 的 299 元和 2300 USD，到底是什么

![用户于 2026 年 9 月 28 日提供的 CodeGo 套餐页截图，展示 299 元 Ultra 月卡和 1.9 元新人体验卡](https://i0.wp.com/jiami.dog/wp-content/uploads/2026/09/codego-plan-snapshot-v1.0-2026-09-28.png?resize=2312%2C1923&ssl=1)

这是我在 2026 年 9 月 28 日提供的 CodeGo 套餐页面。图中的美元额度属于平台内部计费口径，不是可提现美元，也不是 OpenAI 官方账户余额；体验卡和团购活动不是永久优惠，价格、资格与有效期以购买页面为准。

我的页面截图里，Ultra 月卡标价 299 元，基础额度 2300 USD，有效期一个月；新人体验卡显示 1.9 元、15 USD、一天，而且截图已达到购买上限。

2300 USD 是站内记账额度，不是你拿到 2300 美元现金，也不是 OpenAI 官方账户余额。实际能做多少事，要看分组、模型、输入输出、倍率和有效期。截图里的活动到了你注册时可能已经变了。

新手找当前最小可用的套餐，确认有目标模型、允许你的用途，再试跑。先不用照抄我的 299 元月卡。

## 第 4 步：填写 Base URL、协议和 API Key

登录中转站控制台，打开左侧“API 密钥”页面，按页面提示创建 Key。确认它的分组包含你要调用的模型，且允许外接智能体。然后回到 LightVela 的模型设置，选“自定义模型”。

![LightVela 自定义模型配置表单，包含 Provider 名称、Base URL、兼容协议、API Key 和模型用途](https://i0.wp.com/jiami.dog/wp-content/uploads/2026/09/lightvela-custom-model-v1.0-2026-09-28.png?resize=2109%2C1149&ssl=1)

自定义模型要分别填写接口地址、兼容协议和 API Key。图中的 api.example.com 只是占位示例，不能照抄；API Key 应只填进配置栏，不要发给聊天窗口。

这几个字段不是一回事：Provider 名称是你自己给配置起的名字；Base URL 是服务地址；兼容协议是双方沟通的接口格式；API Key 是中转站给这次调用使用的密钥。

Key 只填配置页的专用输入框，不要发给助理让它“帮我记着”，不要晒出带 Key 的截图。下面这些地址本身不是秘密，可以照着核对。

| 本文路线 | 兼容协议 | Base URL |
| --- | --- | --- |
| CodeGo GPT，按其 Hermes 文档起步 | OpenAI Chat Completions | `https://codegoai.com/v1` |
| CodeGo GPT，Key 与模型明确支持 Responses 时 | OpenAI Responses | `https://codegoai.com/v1` |
| APIKEY Claude，选择允许外接的组 | Anthropic Messages | `https://api.apikey.fan` |

这张表按[CodeGo 的 Hermes 文档](https://codegoai.com/docs#hermes)和[APIKEY 的 Hermes 文档](https://apikey.fun/docs#Hermes)核对。注意：CodeGo GPT 这里带 `/v1`，APIKEY Claude 选 Anthropic Messages 时填根地址，不带 `/v1`。别把完整的 `/chat/completions` 或 `/messages` 填进 Base URL。

![LightVela 兼容协议下拉菜单，显示 OpenAI Chat Completions、Anthropic Messages 和 OpenAI Responses](https://i0.wp.com/jiami.dog/wp-content/uploads/2026/09/lightvela-protocol-options-v1.0-2026-09-28.png?resize=2402%2C1320&ssl=1)

兼容协议不是随便选的。根据供应商文档匹配接口地址和协议，再获取可用模型、检测状态。截图中的模型名称仅反映当时的配置，不是模型身份验证。

上面的配置截图里有三个协议选项，界面提供选项不等于每个上游模型都能完成同一种工具任务。[OpenAI 官方说明](https://developers.openai.com/api/docs/guides/migrate-to-responses)也区分 Chat Completions 与 Responses 的工具和输出格式；模型能回话，不代表同一接法一定适合智能体执行任务。

按下面顺序填，不要一次改五处：

1. Provider 名称填“CodeGo GPT”或“APIKEY Claude”，方便以后辨认。
2. 按表填写地址，选择对应协议。
3. 粘贴该站创建的 Key，点“获取可用模型”。
4. 从当前 Key 返回的列表选模型，点“检测模型状态”。不要因为旧截图写了某个名字就硬填。我的截图里是 `gpt-6-sol`，它只是那次配置的模型路由名。
5. 新增配置先选“仅添加”，点“确认配置”保存。回模型列表，保留原来的配置，把新模型临时设为主模型再试任务。通过并核对调用日志后保留，不通过就切回原模型。只添加不切换，任务成功也可能是原模型的功劳。

APIKEY 的公开 API 文档没有明确保证模型列表接口。获取不到列表，不等于你可以随便填一个 Claude 名字：先核对 Key 分组，再问服务商是否支持 LightVela 获取模型。当前界面不让选，就先停在这里，保留原来的可用模型。

Claude 分组里如果看到“仅限 CC”，不要默认拿来外接 LightVela。选择明确允许外接、支持 Anthropic Messages、包含目标模型的组。便宜但用途不对，买了也没用。

检测和试跑也可能消耗额度，先小额测试。这里是公开文档和截图核对后的接入说明，不是对两家所有套餐的付费端到端测试。接口、分组变动时，以当前页面和实际任务结果为准。

## 第 5 步：别只测一句“你好”，让它真的交付

能返回绿色提示，说明基础连接往前走了一步。接下来，用选定的主模型在 QQ 或微信里回复一次，再测一个需要实际读取公开网页的小任务。

把这张卡复制进去。它只处理一份公开说明，不登录、不付款，也不让它自行扩展成每天跑的任务。

```
::ILANG::v5.0
[TYPE:task][PROJECT:lightvela_public_page_test][LANG:zh]
::MODULE{TASK}
  [INPUT] 公开页面https://lightvela.com/docs/plans
  [DO] 只读取这一页 查找Launch AI的标准月价与新用户试用说明
  [DO] 用三行中文给出结果 页面标注更新日期与可打开的来源链接
  [MUST] 不登录 不买套餐 不创建定时任务 不添加收费工具或扩展访问其他网站
  [MUST] 不重复自动重试 读取失败直接说明错误 不用记忆内容冒充本次抓取
::MODULE{ACCEPTANCE}
  [DO] 明确报告这次是否实际读取页面 取不到更新日期就写未取得
  [MUST] 没有工具或读取权限就报告不能完成 不编造已联网证据
::ILANG::COMPLETE::
```

打开它引用的页面，看价格和日期是否对得上。如果它根本没有拿到页面，却说“我查到了”，这次就没过。

再去中转站的使用记录找这次调用，核对时间、模型路由和扣费。记录里显示的名称能帮助你核对配置，但不是底层模型真伪鉴定。

如果短聊天能回复，工具任务却失败，检查模型是否支持工具调用及当前协议。CodeGo 文档也提供 Responses 接口，可在 Key、模型和 LightVela 都支持的前提下测试；不要无限重试，重试可能照样扣费。

| 遇到什么 | 先查哪里 |
| --- | --- |
| 401、Key 无效 | Key 是否复制完整、来自正确服务商、仍有效；不把错误截图里的 Key 公开 |
| 403、模型不可用 | Key 分组权限、允许用途、地区及模型 ID |
| 404、找不到接口 | 协议和 Base URL 是否对应，是否误加或重复拼了 /v1 |
| 429、额度不足、超时 | 套餐有效期、余额、频率限制及服务商状态，停止连续重试 |
| 网页有回复，QQ 没收到 | 通道连接和目标聊天；不是所有问题都在模型 |

## 能用了，再设置提醒和定时任务

想让它早上主动提醒你，可以从固定通知开始。按[官方定时任务说明](https://lightvela.com/docs/configuration/automation/)，通知任务按固定正文发送，不调用模型；“每天找新闻、读完再总结”属于智能任务，会调用模型。两者别混了。

在定时任务页选通知类型，写清目标聊天、北京时间和固定正文。例如每天 9:30 提醒“检查昨天的广告花费”。先试跑一次，确认手机收到消息，再留作每天运行。

设置保存成功，还不能叫自动化成功。执行历史有记录、消息真的送到，才算这一步完成。新闻研究、文件处理之类任务先手动跑通，确认结果和消耗值得，再定时。

## 几个新手经常问的问题

### 要先购买 ChatGPT Plus 或 Claude 会员吗？

本文自定义模型路线用的是中转站提供的 API Key，不把 ChatGPT、Claude 官网会员当作配置前提。你仍需满足平台和服务商的账号、地区与用途条件；有官网会员也不会自动给这家中转站增加余额。

### 微信、QQ 能直接用，数据就只在腾讯吗？

不是。消息经过聊天通道和 LightVela；接自定义模型后，还会发送给所选模型服务商及其上游。腾讯托管也不是腾讯给这两家中转站背书。[LightVela 隐私政策](https://lightvela.com/privacy-policy/)写明了配置第三方服务时的数据共享，第三方另有自己的政策。密码、身份证、客户名单、完整合同和支付资料，别拿来做第一次实验。

### 以后要不要再买 VPS？

只想用自己的托管助理，目前这条路线不要求单独买 VPS。如果你以后要自己控制部署、备份和网关，那是另一件事，可以看之前的[WorkBuddy + Sub2API 零基础教程](https://jiami.dog/5201.html)。这次先别给自己加一套运维工作。

我更想让新手先走到这里：在 QQ 或微信里发出一个清楚的任务，拿到能检查、能使用的结果，知道它花了什么钱。

把这件小事做好，比第一天就集齐所有模型有用。

---

## 继续阅读与讨论

- 分类：[资源攻略](../../../categories/ziyuan-gonglue.md)
- 主题：[AI智能体](../../../tags/ai智能体.md), [Hermes Agent](../../../tags/hermes-agent.md), [LightVela](../../../tags/lightvela.md), [新手教程](../../../tags/新手教程.md), [腾讯轻量云](../../../tags/腾讯轻量云.md)
- [在官网参与本文评论](https://jiami.dog/5217.html#jiami-giscus-comments)
- [浏览 GitHub 文章评论区](https://github.com/JiamiDog/jiami.dog/discussions/categories/article-comments)
- [返回全部文章](../../../INDEX.md)
