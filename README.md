# ikuuu每日签到

这个脚本只适合这一个机场😥😥😥😥，当时只是自己拿来用，就写个这一个机场的。我又写了一个通用的（机场只要Powered by SSPANEL就可以，），请移步<a href = 'https://github.com/bighammer-link/jichang_checkin'>此处</a>
## 推送
  该脚本采用的是server酱的推送方式

# 部署过程
 
1. 右上角Fork此仓库
2. 然后到`Settings`→`Secrets and variables`→`Actions` 新建以下参数：

| 参数   | 是否必须  | 内容  | 
| ------------ | ------------ | ------------ |
| EMAIL  | 是  | 账号邮箱  |
| PASSWD | 是  | 账号密码  |
| WXPUSHER  | 否  | Sever酱推送全链接  |

3. 到`Actions`中创建一个workflow，运行一次，以后每天项目都会自动运行。
4. 最后，可以到Run sign查看签到情况，同时也会也会将签到详情推送到Sever酱。
