---
title: "使用脚本自动抢 Oracle ARM 服务器，并使用 Telegram 机器人通知"
slug: "use-the-script-to-automatically-grab-the-oracle-arm-server"
source_id: "3896"
canonical_url: "https://jiami.dog/3896.html"
date_local: "2022-02-27T16:46:23"
date_published: "2022-02-27T08:46:23Z"
date_modified_local: "2022-02-27T17:34:21"
date_modified: "2022-02-27T09:34:21Z"
draft: false
featured_image_url: "https://jiami.dog/wp-content/uploads/2022/02/1645954196-20220227172605.png"
featured_image_alt: "终端窗口显示Terraform版本信息，提示当前版本已过时。"
categories:
  - "资源攻略"
tags:
  - "Telegram"
  - "机器人"
  - "甲骨文"
---

# 使用脚本自动抢 Oracle ARM 服务器，并使用 Telegram 机器人通知

> 本文同步自 [jiami.dog 官方原文](https://jiami.dog/3896.html)，以官网版本为准。

### 需要用到的

- 一台 vps 服务器
- Terraform
- oci-cli

  #### 一、安装 Terraform

CODE

| ``` wget https://releases.hashicorp.com/terraform/0.15.5/terraform_0.15.5_linux_amd64.zip ``` |
| --- |

**解压，并移动文件 terraform 到 /usr/bin 目录**

CODE

| ``` unzip terraform_0.15.5_linux_amd64.zipmv terraform /usr/bin ``` |
| --- |

**使用以下命令查看版本**

CODE

| ``` terraform version ``` |
| --- |

**显示如下则安装成功**

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/1645954196-20220227172605.png?resize=616%2C111&ssl=1)

#### 二、安装 oci-cli 工具

**使用以下命令安装 oci-cli 工具**

CODE

| ``` bash -c "$(curl –L https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh)" ``` |
| --- |

**一直回车即可****当出现:**

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/1645954199-20220227172618.png?resize=607%2C47&ssl=1)

### **这个时候，是在提示你输入 y 回车，会自动添加环境变量之后又是一直回车。出现如下提示表示安装成功。可以用：`oci -v` 查询版本**

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/1645954201-20220227172633.png?resize=877%2C175&ssl=1)

#### 三、复制用户和租户的 ocid

**[甲骨文](https://jiami.dog/tag/oracle "甲骨文")后台右上角 — 用户设置 — 点击用户以及租户，在信息栏中有我们需要的 ID，分别点击复制，可以保存在记事本备份好**

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/1645954201-20220227172646.png?resize=1427%2C542&ssl=1)

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/1645954202-20220227172702.png?resize=1430%2C601&ssl=1)

#### 四、配置 cli

**输入如下代码开始配置，配置的路径默认在 root 目录**

CODE

| ``` oci setup config ``` |
| --- |

**具体配置看下面**

CODE

| ``` Enter a location for your config [/root/.oci/config]: Enter a user OCID: #输入你的用户OCIDEnter a tenancy OCID: #输入你的租户OCIDEnter a region by index or name(e.g.1: ap-chiyoda-1, 2: ap-chuncheon-1, 3: ap-hyderabad-1, 4: ap-melbourne-1, 5: ap-mumbai-1,6: ap-osaka-1, 7: ap-seoul-1, 8: ap-sydney-1, 9: ap-tokyo-1, 10: ca-montreal-1,11: ca-toronto-1, 12: eu-amsterdam-1, 13: eu-frankfurt-1, 14: eu-zurich-1, 15: me-dubai-1,16: me-jeddah-1, 17: sa-santiago-1, 18: sa-saopaulo-1, 19: uk-cardiff-1, 20: uk-gov-cardiff-1,21: uk-gov-london-1, 22: uk-london-1, 23: us-ashburn-1, 24: us-gov-ashburn-1, 25: us-gov-chicago-1,26: us-gov-phoenix-1, 27: us-langley-1, 28: us-luke-1, 29: us-phoenix-1, 30: us-sanjose-1): 9  #这里选择你的区域Do you want to generate a new API Signing RSA key pair? (If you decline you will be asked to supply the path to an existing key.) [Y/n]: y  #输入y生成公钥Enter a directory for your keys to be created [/root/.oci]: Enter a name for your key [oci_api_key]: Public key written to: /root/.oci/oci_api_key_public.pemEnter a passphrase for your private key (empty for no passphrase): Private key written to: /root/.oci/oci_api_key.pemFingerprint: Config written to /root/.oci/config     If you haven't already uploaded your API Signing public key through the    console, follow the instructions on the page linked below in the section    'How to upload the public key':    https://docs.cloud.oracle.com/Content/API/Concepts/apisigningkey.htm#How2 ``` |
| --- |

**复制生成的公钥，使用以下命令获取公钥**

CODE

| ``` cat /root/.oci/oci_api_key_public.pem ``` |
| --- |

把显示出来的内容复制，并且添加到甲骨文后台 — 用户设置 — 资源 —API 秘钥 — 添加 API 秘钥

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/1645954203-20220227172722.png?resize=1920%2C888&ssl=1)

CODE

| ``` oci iam availability-domain list ``` |
| --- |

**提示以下内容则是配置正确**

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/1645954205-20220227172735.png?resize=772%2C167&ssl=1)

#### 五、Terraform 环境初始化

##### 1、我们先获取甲骨文的 Terraform 脚本

**点击 创建 VM 实例**

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/1645954205-20220227172749.png?resize=1474%2C663&ssl=1)

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/1645954206-20220227172804.png?resize=1920%2C888&ssl=1)

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/1645954208-20220227172819.png?resize=1920%2C883&ssl=1)

**一直下一步**

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/1645954209-20220227172832.png?resize=1403%2C835&ssl=1)

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/1645954223-20220227172846.png?resize=1918%2C881&ssl=1)

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/1645954224-20220227172901.png?resize=101%2C105&ssl=1)

##### 2、配置 Terraform

**使用以下命令创建 Terraform 运行目录**

CODE

| ``` cd /opt/mkdir terraform-learning && cd terraform-learning ``` |
| --- |

**将刚刚解压到桌面的 main.tf 文件 上传到这个目录**

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/1645954225-20220227172914.png?resize=853%2C305&ssl=1)

**将目录设置为 Terraform 运行目录**

CODE

| ``` terraform init ``` |
| --- |

**以上完成后，开始创建任务，用命令：（注意还是在 /opt/terraform-learning）**

CODE

| ``` terraform apply ``` |
| --- |

**执行完上面命令之后，会提示输入 yes**

![](https://i0.wp.com/jiami.dog/wp-content/uploads/2022/02/1645954226-20220227172927.png?resize=1047%2C608&ssl=1)

**上图还能看到 API 返回 Error Message: Out of host capacity, 提示主机容量不足，下面就用脚本来不停刷就行了**

#### 六、部署脚本

**终于可以部署脚本来抢服务器了，请先获取 telegram 账号 id，并且关注通知[机器人](https://jiami.dog/tag/robot "机器人") @oracle\_message\_botTG id 请通过 @userinfobot 机器人获取在 root 目录下新建一个 terraform.sh**

CODE

| ``` cd /rootvi terraform.sh ``` |
| --- |

**写入以下内容**

CODE

| ``` #!/bin/bash path='/opt/terraform-learning/'FIND_FILE="/root/terraform.log" #日志文件位置FIND_STR="Apply complete!"cd $path &&while truedo    echo 'yes' | terraform apply -lock=false    sleep 1sdoneif [ grep -c "$FIND_STR" $FIND_FILE -ne '20' ];then    curl --location --request POST 'https://api.telegram.org/bot2124631392:AAHtVpEm7KRWo6ulYNG_Zbz98irpmTSIf8o/sendMessage' \--form 'text=服务器创建成功！' \--form 'chat_id=你的tg id' \--form 'parse_mode=markdown'pkill terraform    exit 0fi ``` |
| --- |

**给 Shell 脚本赋予执行权限：**

CODE

| ``` chmod +x terraform.sh ``` |
| --- |

**使用以下命令后台执行脚本**

CODE

| ``` nohup ./terraform.sh >> terraform.log 2>&1  & ``` |
| --- |

##### 如何结束脚本？

**使用以下命令结束脚本**

CODE

| ``` pkill terraform ``` |
| --- |

###
