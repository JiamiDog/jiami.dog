# 加密狗 · JiamiDog

[jiami.dog](https://jiami.dog/) 的官方 GitHub 主页与公开文章镜像。

- 官网：[https://jiami.dog/](https://jiami.dog/)
- Agent / MCP 入口：[https://jiami.dog/mcp](https://jiami.dog/mcp)
- AI 阅读入口：[https://jiami.dog/llms.txt](https://jiami.dog/llms.txt)
- 全部镜像文章：[content/INDEX.md](content/INDEX.md)
- 机器可读索引：[data/articles.json](data/articles.json)

> WordPress 官网是唯一发布源和权威版本。本仓库每天从官网公开接口拉取一次，只镜像已发布内容；正文或元数据不一致时，以官网为准。

## 最新文章

<!-- AUTO:ARTICLES:START -->

已自动镜像 **184** 篇公开文章。

- 2026-09-23 [长期美国手机号怎么选？2026 年 Tello、Ultra PayGo、Airalo 对比](content/posts/2026/09/5157-long-term-us-phone-number-guide-2026.md) · [官网原文](https://jiami.dog/5157.html)
- 2026-08-05 [我在网赚圈做斑竹的经历](content/posts/2026/08/5077-bandwagonhost-justmysocks-vps-hosting-experience.md) · [官网原文](https://jiami.dog/5077.html)
- 2026-07-30 [OpenClaw API 中转站：官方 1\-3 折用 Claude Opus / GPT，国内直连支付宝充值](content/posts/2026/07/4934-openclaw-api-proxy-cheap-claude-gpt-alipay.md) · [官网原文](https://jiami.dog/4934.html)
- 2023-11-24 [ShareASale广告联盟推广者注册指南](content/posts/2023/11/4877-shareasale-advertising-alliance-promoter-registration-guide.md) · [官网原文](https://jiami.dog/4877.html)
- 2023-11-24 [Google Ads 账号类型说明（个人号，企业号，代理号）](content/posts/2023/11/4874-google-ads-account-type-description-personal-number.md) · [官网原文](https://jiami.dog/4874.html)
- 2023-07-06 [my\.id来自印度尼西亚免费域名以及邮箱服务](content/posts/2023/07/4858-my-id-comes-from-indonesias-free-domain-name-and-email.md) · [官网原文](https://jiami.dog/4858.html)
- 2023-06-24 [万豪会员新福利，可以直接获得赫兹租车公司高级会籍](content/posts/2023/06/4849-new-benefits-for-marriott-members-can-directly-obtain.md) · [官网原文](https://jiami.dog/4849.html)
- 2023-04-28 [日本网盘！永久45G，速度超快，支持 WebDav 协议的 InfiniCloud](content/posts/2023/04/4832-japanese-netdisk-permanent-45g-ultra-fast-infinicloud.md) · [官网原文](https://jiami.dog/4832.html)
- 2023-04-25 [AdSense，Admob，Google Play开发者使用W9信息免税教程](content/posts/2023/04/4818-adsense-adnob-google-play-developer-use-w9-information.md) · [官网原文](https://jiami.dog/4818.html)
- 2023-04-03 [最近ChatGPT封账号太严重，ChatGPT解封攻略步骤](content/posts/2023/04/4760-recently-chatgpt-account-closure-has-been-too-serious.md) · [官网原文](https://jiami.dog/4760.html)

[查看全部文章 →](content/INDEX.md)

<!-- AUTO:ARTICLES:END -->

## 仓库结构

```text
content/posts/       按 年/月 存放的公开文章 Markdown
content/INDEX.md     全量文章导航
data/articles.json  供 Agent、MCP 和程序读取的结构化索引
data/sync-state.json 连续完整抓取与安全删除状态
scripts/             确定性同步程序（Python + 固定版 markdownify）
.github/workflows/   每日同步与手动同步工作流
```

## 同步原则

1. 只读取无需登录的公开内容接口，不保存 WordPress 密码、令牌或 Cookie。
2. 查询固定带 `status=publish`，并再次校验每条记录的 `status=publish` 与 `type=post`；不访问 pages、草稿或定时文章。
3. 以来源文章的稳定 ID 更新文件；只有连续两次完整抓取都缺失时才删除本地镜像，避免瞬时漏页误删。
4. 输出不包含“本次运行时间”等易变字段。同一份来源数据重复运行不会制造提交。
5. 同步器只能改动 `README.md` 的自动生成区、`content/posts/`、`content/INDEX.md`、`data/articles.json` 与 `data/sync-state.json`。

## 本地验证

```bash
python -m pip install --requirement requirements.txt
python -m unittest discover -s tests -v
python scripts/sync_content.py --repository-root .
```

同步器固定读取 WordPress 的公开 posts REST 接口：`https://jiami.dog/wp-json/wp/v2/posts`。它以每页 100 条、ID 升序抓取全部分页，并核对 `X-WP-Total`、`X-WP-TotalPages`、页数、数量和唯一 ID。它不会读取或镜像 WordPress pages。

HTML 正文由固定版本 `markdownify==1.2.3` 转为 GitHub Markdown；图片、表格与链接会保留，iframe 会先转换成带标题的普通链接。分类、标签与题图来自 WordPress `_embedded` 数据。

## 内容与安全边界

本仓库不得出现草稿、私密文章、后台路径、用户数据、访问日志、API 密钥、WordPress 凭据、联盟后台数据或未公开运营资料。安全问题请按 [SECURITY.md](SECURITY.md) 私下报告，不要把敏感信息写进公开 Issue。

## 版权

除非文件另有明确说明，本仓库内容与代码均适用 [LICENSE](LICENSE)。公开可读不代表授权转载或再许可。
