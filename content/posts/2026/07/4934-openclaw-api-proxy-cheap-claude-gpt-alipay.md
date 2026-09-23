---
title: "OpenClaw API 中转站：官方 1-3 折用 Claude Opus / GPT，国内直连支付宝充值"
slug: "openclaw-api-proxy-cheap-claude-gpt-alipay"
source_id: "4934"
canonical_url: "https://jiami.dog/4934.html"
date_local: "2026-07-30T13:53:20"
date_published: "2026-07-30T05:53:20Z"
date_modified_local: "2026-07-30T14:00:47"
date_modified: "2026-07-30T06:00:47Z"
draft: false
featured_image_url: "https://jiami.dog/wp-content/uploads/2026/07/4423E5C.png"
featured_image_alt: "4423E5C"
categories:
  - "资源攻略"
tags: []
---

# OpenClaw API 中转站：官方 1-3 折用 Claude Opus / GPT，国内直连支付宝充值

> 本文同步自 [jiami.dog 官方原文](https://jiami.dog/4934.html)，以官网版本为准。

找到一家靠谱的 AI API 中转站：490 块充 1200 刀额度，Claude Opus 4.8、GPT 5.6 全都有，国内直连，支付宝、微信直接充。官方链路直连，没掺水、没降智、没偷换模型，请求过去返回什么就是什么。我自己的 OpenClaw / Claude Code 都已经切过来了，Extended Thinking 正常开启。

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2026/07/4423E5C.png?resize=1570%2C1183&ssl=1)

注册链接：[**https://openclaw-api.com**](https://openclaw-api.com/register?aff=BMTXSWJ5)

## 核心优势

- **价格杀手**：官方价 1-3 折。充 490 元人民币 = 1200 美元额度（6 亿 token），按官方价算省了 8000+ 元
- **国内直连**：base URL 国内 CDN 加速，不需要翻墙，支付宝/微信人民币充值
- **50+ 模型一个 key 搞定**：Claude Opus 4.8/4.7/4.6、Sonnet 5/4.6、GPT 5.6/5.5/5.4、Grok 4.5，改个 model id 就切换
- **双协议兼容**：OpenAI Chat Completions + Anthropic Messages 都支持
- **Extended Thinking**：Claude 系列支持深度思考模式，budget\_tokens 可拉满 128k
- **余额永不过期**：充多少用多少，没有有效期
- **零运维**：不用自己部署 new-api/one-api，不用绑外币卡，邮箱注册即用
- **适配主流工具**：Claude Code、Codex、CC-Switch、TRAE、WorkBuddy、OpenClaw 一键接入

## 接入配置（JSON）

### Claude Opus 4.6（推荐，带深度思考）

```
{
  "model": "claude-opus-4-6",
  "base_url": "https://openclaw-api.com/v1",
  "api_key": "你的key"
}
```

### GPT 5.5

```
{
  "model": "gpt-5.5",
  "base_url": "https://openclaw-api.com/v1",
  "api_key": "你的key"
}
```

### Anthropic 原生格式（Claude Code 等）

```
{
  "base_url": "https://openclaw-api.com",
  "api_key": "你的key"
}
```

## Claude Code 设置命令

```
export ANTHROPIC_BASE_URL=https://openclaw-api.com
export ANTHROPIC_API_KEY=你的key
```

## 注意事项

- OpenAI 格式用 `https://openclaw-api.com/v1`
- Anthropic 格式用 `https://openclaw-api.com`
- 模型名直接写官方名（claude-opus-4-6、gpt-5.5 等），不需要加前缀

## 注册入口

直达注册：**[https://openclaw-api.com](https://openclaw-api.com/register?aff=BMTXSWJ5)**
