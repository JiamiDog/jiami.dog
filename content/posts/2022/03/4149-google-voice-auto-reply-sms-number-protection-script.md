---
title: "Google Voice 自动回复短信保号脚本"
slug: "google-voice-auto-reply-sms-number-protection-script"
source_id: "4149"
canonical_url: "https://jiami.dog/4149.html"
date_local: "2022-03-06T16:23:08"
date_published: "2022-03-06T08:23:08Z"
date_modified_local: "2026-07-30T14:38:17"
date_modified: "2026-07-30T06:38:17Z"
draft: false
featured_image_url: "https://jiami.dog/wp-content/uploads/2022/03/e5ba2ec464a6226e0da721517583bb04.png"
featured_image_alt: "Google Voice设置页面，显示“将短信转发到电子邮件”选项已开启。"
categories:
  - "资源攻略"
tags:
  - "Google Voice"
  - "谷歌"
---

# Google Voice 自动回复短信保号脚本

> 本文同步自 [jiami.dog 官方原文](https://jiami.dog/4149.html)，以官网版本为准。

自从搞了 [Google Voice](https://jiami.dog/2032.html) 虚拟号码，时不时的就要去发短信，搞不好就忘记了，已经让回收了个炸弹号，挺可惜的，[保号也就是说可以长期的能够使用它并不被谷歌回收](https://jiami.dog/4745.html)，下面我们就借助 GmailApp 实现 [Google Voice](https://jiami.dog/tag/google-voice "Google Voice") 自动回复短信脚本，方法比较简单，但愿能保住有需要的人。

[Google Voice 号码回收中文版规则里写的是3个月不活动](https://jiami.dog/4533.html)，就会回收 Google Voice 号码，明显是与英文版有所出处，Google Voice 号码回收中文版规则里写的是3个月不收发短信，也不接打语音就视为死号，然后会被[谷歌](https://jiami.dog/tag/google "谷歌")回收。

## **设置步骤**

1、登入 Google Voice，在 Google Voice 设置里面把“将消息转发到电子邮件”打开，如下图：

![设置将短信转发到电子邮箱](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/03/e5ba2ec464a6226e0da721517583bb04.png?ssl=1)

2、登入谷歌 Gmail 邮箱，在设置里选择“过滤器和屏蔽的地址” –> “创建新的过滤器” –> 在发件人处填写 “@txt.voice.google.com”点击“创建过滤器”，如下图：

![gmail创建新的过滤器](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/03/60dd737868866e89871aaf51a76975ad.png?ssl=1)

3、点击“创建过滤器”后，在弹出的对话框点击“选择标签” –> “新建标签”，输入标签名为“**autoreply**”，点击创建即可，如下图：

![创建过滤器设置标签](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/03/f425a47104378aa48c033d708ee83049.png?ssl=1)

4、点击“创建”后，在页面勾选“跳过收件箱”，创建完新标签默认勾选应用标签，然后直接点击“创建过滤器”，如下图：

![完成创建过滤器](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/03/5f16b6c87f04f3294206ad3677478937.png?ssl=1)

5、接着登录 Google Drive（也就是谷歌网盘），单击左上角的“新建”在“更多”里选择 Google App Script，如在图：

![新建Google App Script](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/03/42a9acac7e2966cc8d8cb15976d62ea3.png?ssl=1)

6、点击图片旁边修改重命名为“**autoReplier**”，并将复制下面的代码替换现有的代码内，完全替换以前的开始语句，如下图：

![复制代码并重命名](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/03/9658fc499250f10246f6fe5b988ec5c9.png?ssl=1)

Bash

```
  function autoReplier() {
var labelObj = GmailApp.getUserLabelByName('autoreply');
var gmailThreads;
var messages;
var messagecount;
var sender;
var num = 9;  //设置连续自动回复邮件的次数（为防止两人都是自动回复，当发送次数达到 9 时将不自动回复）。
var hours = 12;  //过了多少小时后又可以自动回复。
try {
for (var gg = 0; gg < labelObj.getUnreadCount(); gg++) {
gmailThreads = labelObj.getThreads()[gg];
messages = gmailThreads.getMessages();
messagecount = gmailThreads.getMessageCount();
//console.log(messages[messagecount - 9].getDate() + "  time");
for (var ii = 0; ii < messages.length; ii++) {
if (messages[ii].isUnread()) {
msg = messages[ii].getPlainBody();
sender = messages[ii].getFrom();
array = [
["弱水三千，只取一瓢"],
["情不知所起，一往而深"],
["有钱买房住别墅，没钱买房先首付"],
["衣带渐宽终不悔，为伊消得人憔悴"],
["Zblog，中国最好的博客程序 -- 曹彧繎"]
];
var j = Math.floor(Math.random() * (array.length));
var temp = array[j];
if (messagecount < num){
MailApp.sendEmail(sender, "Auto Reply", temp);
}else if( (messages[messagecount - 1].getDate().getTime() - messages[messagecount - num].getDate().getTime()) > hours * 60 * 60 * 1000 ){
MailApp.sendEmail(sender, "Auto Reply", "Hi, 您好！我们已经发了好几条信息了，可以停下来休息休息一下了！本短信由 Google Apps Script 自动发出。");
}
messages[ii].markRead();
messages[ii].moveToTrash();
}
}
}
} catch (err) {
console.error('for loop error: ' + e);
}
}
```

7、然后进行保存，再单击“调试”会提示你授权，你按提示授权即可，[如果中途提示此应用未经 Google 验证](https://jiami.dog/4760.html)，直接点击高级，转至autoReplier(不安全)，如下图：

![提示不安全](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/03/d61c406c95ae69994a014609a7ef20b9.png?ssl=1)

8、然后再次点击“调试”，如果没有任何提示说明脚本没有错误，我们点击左面闹钟进行设置触发器，主要设置触发器时间类型和间隔分钟数，如果不清楚，直接参考下图：

![设置触发器](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/03/c880e79c828518b2c5a7bf5634084679.png?ssl=1)

9、给星巴克号码 22122 发短信，内容为“JOIN”，也就是订阅内容，每月2条，顺便测试，如果成功就会自动回复脚本里的内容，如下图：

![测试短信自动回复脚本](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/03/b8e0a643abc471830f86e6f60209fe87.png?ssl=1)

## **最后总结**

订阅短信目前最稳定，最安心的也就是星巴克的了，其他的你要是想测试也可以，不过为了保险起见，还是一并把星巴克短信订阅了。

如果出现 ReferenceError: e is not defined at autoReplier(代码:38:42) 错误，请重新复制以下代码进行保存，脚本安全可靠，不会出现锁号冻结的情况，放心使用。

如果你会经常更换IP地址或发送垃圾短信，使用脚本会出现禁封，申诉话术：因个人编写自动回复信息脚本，并未做出违法谷歌协议，希望谷歌审核团队审核，解封几率99%。

---

## 继续阅读与讨论

- 分类：[资源攻略](../../../categories/ziyuan-gonglue.md)
- 主题：[Google Voice](../../../tags/google-voice.md), [谷歌](../../../tags/谷歌.md)
- [在官网参与本文评论](https://jiami.dog/4149.html#jiami-giscus-comments)
- [浏览 GitHub 文章评论区](https://github.com/JiamiDog/jiami.dog/discussions/categories/article-comments)
- [返回全部文章](../../../INDEX.md)
