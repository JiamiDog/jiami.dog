# 参与 JiamiDog 社区

感谢你帮助 JiamiDog 改进公开文章镜像与同步工具。

## 先选择正确的入口

| 你的事项 | 应该提交到哪里 |
| --- | --- |
| 评论某篇文章、交流经验 | GitHub Discussions 的“文章评论”分类 |
| 提问、寻求使用帮助 | GitHub Discussions 的“问答”分类 |
| 指出文章观点或事实可能有误、提出内容建议 | GitHub Discussions 的“纠错与建议”分类 |
| 已发布文章没有同步、镜像内容残缺、页面渲染错误或元数据错误 | GitHub Issues |
| 安全漏洞、凭据或个人数据问题 | 按 [SECURITY.md](SECURITY.md) 私密报告 |

请勿用 Issue 发表一般评论、咨询服务、投稿文章或讨论观点。我们会把不属于可执行镜像故障的 Issue 引导到 Discussions。

## 内容源与镜像边界

[jiami.dog](https://jiami.dog/) 上已发布的 WordPress 文章是正文的唯一权威来源。本仓库是公开、只读的 GitHub 镜像：

- 文章观点或事实需要修订时，应先在 Discussions 说明；确认后由维护者修改 WordPress 正文，再由同步任务更新仓库。
- 不要直接修改 `content/posts/`、`content/INDEX.md`、`data/articles.json`、`data/sync-state.json` 或 README 中的自动生成区块。
- 如果源站正确而镜像错误，请提交 Issue，并同时提供源站地址和镜像地址。
- 本仓库不接受未发布草稿、用户数据、流量日志、联盟账户资料或内部运营材料。

## 提交 Issue

1. 先搜索现有 Issues 与 Discussions，避免重复。
2. 打开源站文章，确认问题不是源站正文自身的问题。
3. 选择对应的 Issue 表单，填写可复现步骤、实际结果和期望结果。
4. 可以附截图，但必须遮盖令牌、Cookie、邮箱、订单号和其他私人信息。

只要问题可复现且属于同步、渲染或元数据范围，即使暂时不知道技术原因，也欢迎报告。

## 提交代码或文档改进

Pull Request 主要用于同步程序、测试、工作流、社区文档和模板。请保持改动单一、可审核，并说明：

- 要解决的问题；
- 为什么不会改变 WordPress 的权威来源地位；
- 采用了哪些验证；
- 是否影响自动生成文件或每日同步。

修改 Python 同步逻辑时，至少运行：

```bash
python -m unittest discover -s tests -v
```

请勿在 Pull Request 中加入密钥、Cookie、WordPress 凭据、私有接口响应或无授权内容。

## 自动化与人工复核

社区机器人可以自动欢迎、做初步分类、核对公开文章引用，并提示缺失或冲突的信息。机器人不会自动关闭或删除讨论与 Issue，也不会删除正常评论、封禁用户、裁定争议、修改 WordPress 正文或处理安全报告。对自动化结果有异议时，请在原讨论或 Issue 中说明，维护者会人工复核。

参与本社区即表示你同意遵守 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)。
