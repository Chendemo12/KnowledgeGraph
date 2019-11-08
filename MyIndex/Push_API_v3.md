

# Push API v3

这是 Push API 最近的版本。

相比于 API v2 版本，v3 版本的改进为：

+  完全基于 https，不再提供 http 访问；
+  使用 HTTP Basic Authentication 的方式做访问授权。这样整个 API 请求可以使用常见的 HTTP 工具来完成，比如：curl，浏览器插件等；
+  推送内容完全使用 JSON 的格式；
+  支持的功能有所改进：支持多 tag 的与或操作；可单独发送通知或者自定义消息，也可同时推送通知与自定义消息；windows phone 目前只有通知。

## 推送概述

### 功能说明

向某单个设备或者某设备列表推送一条通知、或者消息。
推送的内容只能是 JSON 表示的一个推送对象。

### 调用地址

https://api.jpush.cn/v3/push

如果创建的极光应用分配的北京机房，并且 API 调用方的服务器也位于北京，则比较适合调用极光北京机房的 API，可以提升一定的响应速度。

通过极光 Web 控制台 “应用设置” -> "应用信息" 中可以看到应用所在机房。如果应用所在地为北京机房，同时会给出各 API 的调用地址。

北京机房 Push API 调用地址： https://bjapi.push.jiguang.cn/v3/push

详细对应关系见 “应用信息” 中 “服务器所在地” 后的信息。

### 请求示例

```
curl --insecure -X POST -v https://api.jpush.cn/v3/push -H "Content-Type: application/json" -u "7d431e42dfa6a6d693ac2d04:5e987ac6d2e04d95a9d8f0d1" -d '{"platform":"all","audience":"all","notification":{"alert":"Hi,JPush !","android":{"extras":{"android-key1":"android-value1"}},"ios":{"sound":"sound.caf","badge":"+1","extras":{"ios-key1":"ios-value1"}}}}'

> POST /v3/push HTTP/1.1
> Authorization: Basic N2Q0MzFlNDJkZmE2YTZkNjkzYWMyZDA0OjVlOTg3YWM2ZDJlMDRkOTVhOWQ4ZjBkMQ==
```

### 返回示例

```
< HTTP/1.1 200 OK
< Content-Type: application/json
{"sendno":"18","msg_id":"1828256757"}
```

## 调用验证

HTTP Header（头）里加一个字段（Key/Value 对）：

```
Authorization: Basic base64_auth_string
```

其中 base64_auth_string 的生成算法为：base64 (appKey:masterSecret)
即，对 appKey 加上冒号，加上 masterSecret 拼装起来的字符串，再做 base64 转换。

## 推送对象

一个推送对象，以 JSON 格式表达，表示一条推送相关的所有信息。

| 关键字       | 选项 | 含义                                                         |
| :----------- | :--- | :----------------------------------------------------------- |
| platform     | 必填 | 推送平台设置                                                 |
| audience     | 必填 | 推送设备指定                                                 |
| notification | 可选 | 通知内容体。是被推送到客户端的内容。与 message 一起二者必须有其一，可以二者并存 |
| message      | 可选 | 消息内容体。是被推送到客户端的内容。与 notification 一起二者必须有其一，可以二者并存 |
| sms_message  | 可选 | 短信渠道补充送达内容体                                       |
| options      | 可选 | 推送参数                                                     |
| cid          | 可选 | 用于防止 api 调用端重试造成服务端的重复推送而定义的一个标识符。 |

### 示例与说明

```
{
    "cid": "8103a4c628a0b98974ec1949-711261d4-5f17-4d2f-a855-5e5a8909b26e",
    "platform": "all",
    "audience": {
        "tag": [
            "深圳",
            "北京"
        ]
    },
    "notification": {
        "android": {
            "alert": "Hi, JPush!",
            "title": "Send to Android",
            "builder_id": 1,
            "large_icon": "http://www.jiguang.cn/largeIcon.jpg",
            "intent": {
                "url": "intent:#Intent;component=com.jiguang.push/com.example.jpushdemo.SettingActivity;end",
            },
            "extras": {
                "newsid": 321
            }
        },
        "ios": {
            "alert": "Hi, JPush!",
            "sound": "default",
            "badge": "+1",
            "thread-id": "default"
            "extras": {
                "newsid": 321
            }
        }
    },
    "message": {
        "msg_content": "Hi,JPush",
        "content_type": "text",
        "title": "msg",
        "extras": {
            "key": "value"
        }
    },
    "sms_message":{
       "temp_id":1250,
       "temp_para":{
            "code":"123456"
       },
        "delay_time":3600,
        "active_filter":false
    },
    "options": {
        "time_to_live": 60,
        "apns_production": false,
        "apns_collapse_id":"jiguang_test_201706011100"
    }
}
```

## platform：推送平台

JPush 当前支持 Android, iOS, Windows Phone 三个平台的推送。其关键字分别为："android", "ios", "winphone"。

如果目标平台为 iOS 平台，推送 Notification 时需要在 options 中通过 apns_production 字段来设定推送环境。True 表示推送生产环境，False 表示要推送开发环境； 如果不指定则为推送生产环境；一次只能推送给一个环境。



推送到所有平台：

```
{ "platform" : "all" }
```

指定特定推送平台：

```
{ "platform" : ["android", "ios"] }
```

## audience：推送目标

推送设备对象，表示一条推送可以被推送到哪些设备列表。确认推送设备对象，JPush 提供了多种方式，比如：别名、标签、注册 ID、分群、广播等。

### all

如果要发广播（全部设备），则直接填写 “all”。

### 推送目标

广播外的设备选择方式，有如下几种：

| 关键字          | 类型       | 含义        | 说明                                                         | 备注                                                         |
| :-------------- | :--------- | :---------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| tag             | JSON Array | 标签 OR     | 数组。多个标签之间是 OR 的关系，即取并集。                   | 用标签来进行大规模的设备属性、用户属性分群。 一次推送最多 20 个。有效的 tag 组成：字母（区分大小写）、数字、下划线、汉字、特殊字符 @!#$&*+=.\|￥。限制：每一个 tag 的长度限制为 40 字节。（判断长度需采用 UTF-8 编码） |
| tag_and         | JSON Array | 标签 AND    | 数组。多个标签之间是 AND 关系，即取交集。                    | 注意与 tag 区分。一次推送最多 20 个。                        |
| tag_not         | JSON Array | 标签 NOT    | 数组。多个标签之间，先取多标签的并集，再对该结果取补集。     | 一次推送最多 20 个。                                         |
| alias           | JSON Array | 别名        | 数组。多个别名之间是 OR 关系，即取并集。                     | 用别名来标识一个用户。一个设备只能绑定一个别名，但多个设备可以绑定同一个别名。一次推送最多 1000 个。有效的 alias 组成：字母（区分大小写）、数字、下划线、汉字、特殊字符 @!#$&*+=.\|￥。限制：每一个 alias 的长度限制为 40 字节。（判断长度需采用 UTF-8 编码） |
| registration_id | JSON Array | 注册 ID     | 数组。多个注册 ID 之间是 OR 关系，即取并集。                 | 设备标识。一次推送最多 1000 个。客户端集成 SDK 后可获取到该值。 |
| segment         | JSON Array | 用户分群 ID | 在页面创建的用户分群的 ID。定义为数组，但目前限制一次只能推送一个。 | 目前限制是一次只能推送一个。                                 |
| abtest          | JSON Array | A/B Test ID | 在页面创建的 A/B 测试的 ID。定义为数组，但目前限制是一次只能推送一个。 | 目前限制一次只能推送一个。                                   |



以上几种类型至少需要有其一。如果值数组长度为 0，表示该类型不存在。

这几种类型可以并存，多项的隐含关系是 AND，即取几种类型结果的交集。

例如：

"audience" : { "tag" : [ "tag1", "tag2" ], "tag_and" : [ "tag3", "tag4"], "tag_not" : [ "tag5", "tag6"] }

先计算 "tag" 字段的结果 **tag1或tag2=A**;

再计算 "tag_and" 字段的结果 **tag3且tag4=B**;

再计算 "tag_not" 字段的结果 **非(tag5或tag6)=C**

"audience" 的最终结果为 **A且B且C** 。



### 示例

+  推送给全部（广播）：

```
{
   "platform": "all",
   "audience" : "all",
   "notification" : {
      "alert" : "Hi, JPush!",
      "android" : {}, 
      "ios" : {
         "extras" : { "newsid" : 321}
      }
   }
}
```

+  推送给多个标签（只要在任何一个标签范围内都满足）：在深圳、广州、或者北京

```
{
    "audience" : {
        "tag" : [ "深圳", "广州", "北京" ]
    }
}
```

+  推送给多个标签（需要同时在多个标签范围内）：在深圳并且是 “女”

```
{
    "audience" : {
        "tag_and" : [ "深圳", "女" ]
    }
}
```

+  推送给多个别名：

```
{
    "audience" : {
        "alias" : [ "4314", "892", "4531" ]
    }
}
```

+  推送给多个注册 ID：

```
{
    "audience" : {
        "registration_id" : [ "4312kjklfds2", "8914afd2", "45fdsa31" ]
    }
}
```

+  可同时推送指定多类推送目标：在深圳或者广州，并且是 “女” “会员”

```
{
    "audience" : {
        "tag" : [ "深圳", "广州" ],
        "tag_and" : [ "女", "会员"]
    }
}
```

## notification：通知

“通知” 对象，是一条推送的实体内容对象之一（另一个是 “消息”），是会作为 “通知” 推送到客户端的。
其下属属性包含 4 种，3 个平台属性，以及一个 "alert" 属性。

### alert

通知的内容在各个平台上，都可能只有这一个最基本的属性 "alert"。
这个位置的 "alert" 属性（直接在 notification 对象下），是一个快捷定义，各平台的 alert 信息如果都一样，则可不定义。如果各平台有定义，则覆盖这里的定义。

```
{
    "notification" : {
        "alert" : "Hello, JPush!"
    }
}
```

上面定义的 notification 对象，将被推送到 "platform" 指定的多个平台，并且其通知 alert 信息都一样。

### android

Android 平台上的通知，JPush SDK 按照一定的通知栏样式展示。

支持的字段有：

| 关键字       | 类型        | 选项 | 含义                    | 说明                                                         |
| :----------- | :---------- | :--- | :---------------------- | :----------------------------------------------------------- |
| alert        | string      | 必填 | 通知内容                | 这里指定了，则会覆盖上级统一指定的 alert 信息；内容可以为空字符串，则表示不展示到通知栏。 |
| title        | string      | 可选 | 通知标题                | 如果指定了，则通知里原来展示 App 名称的地方，将展示成这个字段。 |
| builder_id   | int         | 可选 | 通知栏样式 ID           | Android SDK 可[设置通知栏样式](https://docs.jiguang.cn/jpush/client/Android/android_api/#api_8)，这里根据样式 ID 来指定该使用哪套样式，android 8.0 开始建议采用 [NotificationChannel 配置](https://docs.jiguang.cn/jpush/client/Android/android_api/#notificationchannel)。 |
| channel_id   | String      | 可选 | android 通知 channel_id | 不超过 1000 字节，Android 8.0 开始可以进行 [NotificationChannel 配置](https://docs.jiguang.cn/jpush/client/Android/android_api/#notificationchannel)，这里根据 channel ID 来指定通知栏展示效果。 |
| priority     | int         | 可选 | 通知栏展示优先级        | 默认为 0，范围为 -2～2。                                     |
| category     | string      | 可选 | 通知栏条目过滤或排序    | 完全依赖 rom 厂商对 category 的处理策略                      |
| style        | int         | 可选 | 通知栏样式类型          | 默认为 0，还有 1，2，3 可选，用来指定选择哪种通知栏样式，其他值无效。有三种可选分别为 bigText=1，Inbox=2，bigPicture=3。 |
| alert_type   | int         | 可选 | 通知提醒方式            | 可选范围为 -1～7 ，对应 Notification.DEFAULT_ALL = -1 或者 Notification.DEFAULT_SOUND = 1, Notification.DEFAULT_VIBRATE = 2, Notification.DEFAULT_LIGHTS = 4 的任意 “or” 组合。默认按照 -1 处理。 |
| big_text     | string      | 可选 | 大文本通知栏样式        | 当 style = 1 时可用，内容会被通知栏以大文本的形式展示出来。支持 api 16 以上的 rom。 |
| inbox        | JSONObject  | 可选 | 文本条目通知栏样式      | 当 style = 2 时可用， json 的每个 key 对应的 value 会被当作文本条目逐条展示。支持 api 16 以上的 rom。 |
| big_pic_path | string      | 可选 | 大图片通知栏样式        | 当 style = 3 时可用，可以是网络图片 url，或本地图片的 path，目前支持 .jpg 和 .png 后缀的图片。图片内容会被通知栏以大图片的形式展示出来。如果是 http／https 的 url，会自动下载；如果要指定开发者准备的本地图片就填 sdcard 的相对路径。支持 api 16 以上的 rom。 |
| extras       | JSON Object | 可选 | 扩展字段                | 这里自定义 JSON 格式的 Key / Value 信息，以供业务使用。      |
| large_icon   | string      | 可选 | 通知栏大图标            | 图标路径可以是以 http 或 https 开头的网络图片，如：http:jiguang.cn/logo.png , 图标大小不超过 30 k; 也可以是位于 drawable 资源文件夹的图标路径，如：R.drawable.lg_icon； 如果有此字段值，推送一定走极光自有通道下发。 |
| intent       | JSON Object | 可选 | 指定跳转页面            | 使用 intent 里的 url 指定点击通知栏后跳转的目标页面； 如果有此字段值，推送一定走极光自有通道下发。 |



```
{
    "notification" : {
        "android" : {
             "alert" : "hello, JPush!", 
             "title" : "JPush test", 
             "builder_id" : 3, 
             "style":1  // 1,2,3
             "alert_type":1 // -1 ~ 7
             "big_text":"big text content",
             "inbox":JSONObject,
             "big_pic_path":"picture url",
             "priority":0, // -2~2
             "category":"category str",
             "large_icon": "http://www.jiguang.cn/largeIcon.jpg",
           "intent": {
                "url": "intent:#Intent;component=com.jiguang.push/com.example.jpushdemo.SettingActivity;end",
            },
             "extras" : {
                  "news_id" : 134, 
                  "my_key" : "a value"
             }
        }
    }
}
```

### iOS

iOS 平台上 APNs 通知结构。
该通知内容会由 JPush 代理发往 Apple APNs 服务器，并在 iOS 设备上在系统通知的方式呈现。
该通知内容满足 APNs 的规范，支持的字段如下：

| 关键字            | 类型                  | 选项 | 含义                   | 说明                                                         |
| :---------------- | :-------------------- | :--- | :--------------------- | :----------------------------------------------------------- |
| alert             | string 或 JSON Object | 必填 | 通知内容               | 这里指定内容将会覆盖上级统一指定的 alert 信息；内容为空则不展示到通知栏。支持字符串形式也支持官方定义的[ alert payload](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/PayloadKeyReference.html) 结构，在该结构中包含 title 和 subtitle 等官方支持的 key |
| sound             | string 或 JSON Object | 可选 | 通知提示声音或警告通知 | 普通通知： string 类型，如果无此字段，则此消息无声音提示；有此字段，如果找到了指定的声音就播放该声音，否则播放默认声音，如果此字段为空字符串，iOS 7 为默认声音，iOS 8 及以上系统为无声音。说明：JPush 官方 SDK 会默认填充声音字段，提供另外的方法关闭声音，详情查看各 SDK 的源码。 告警通知： JSON Object , 支持官方定义的[ payload](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/generating_a_remote_notification#2990112) 结构，在该结构中包含 critical 、name 和 volume 等官方支持的 key . |
| badge             | int                   | 可选 | 应用角标               | 如果不填，表示不改变角标数字，否则把角标数字改为指定的数字；为 0 表示清除。JPush 官方 SDK 会默认填充 badge 值为 "+1", 详情参考：[badge +1](http://blog.jpush.cn/ios_apns_badge_plus/) |
| content-available | boolean               | 可选 | 推送唤醒               | 推送的时候携带 "content-available":true 说明是 Background Remote Notification，如果不携带此字段则是普通的 Remote Notification。详情参考：[Background Remote Notification](https://docs.jiguang.cn/jpush/client/iOS/ios_new_fetures/#ios-7-background-remote-notification) |
| mutable-content   | boolean               | 可选 | 通知扩展               | 推送的时候携带 ”mutable-content":true 说明是支持 iOS10 的 UNNotificationServiceExtension，如果不携带此字段则是普通的 Remote Notification。详情参考：[UNNotificationServiceExtension](https://docs.jiguang.cn/jpush/client/iOS/ios_new_fetures/#ios-10-service-extension) |
| category          | string                | 可选 |                        | IOS 8 才支持。设置 APNs payload 中的 "category" 字段值       |
| extras            | JSON Object           | 可选 | 附加字段               | 这里自定义 Key /value 信息，以供业务使用。                   |
| thread-id         | string                | 可选 | 通知分组               | ios 的远程通知通过该属性来对通知进行分组，同一个 thread-id 的通知归为一组。 |



iOS 通知 JPush 要转发给 APNs 服务器。APNs 协议定义通知长度为 2048 字节。

JPush 因为需要重新组包，并且考虑一点安全冗余，要求 "iOS":{ } 及大括号内的总体长度不超过：2000 个字节。JPush 使用 utf-8 编码，所以一个汉字占用 3 个字节长度。



**服务端发送消息串**

```
{
    "notification" : {
         "ios" : {
                 "alert" : "hello, JPush!", 
                 "sound" : "sound.caf", 
                 "badge" : 1, 
                 "extras" : {
                      "news_id" : 134, 
                      "my_key" : "a value"
                 }
            }
       }
}                
```

**客户端收到 apns**

```
{
    "_j_msgid" = 813843507;
    aps =     {
        alert = "hello,JPush!";
        badge = 1;
        sound = "sound.caf";
    };
    "my_key" = "a value";
    "news_id" = 134;
}
```

### winphone

Windows Phone 平台上的通知。
该通知由 JPush 服务器代理向微软的 MPNs 服务器发送，并在 Windows Phone 客户端的系统通知栏上展示。
该通知满足 MPNs 的相关规范。当前 JPush 仅支持 toast 类型：

| 关键字     | 类型        | 选项 | 含义               | 说明                                                         |
| :--------- | :---------- | :--- | :----------------- | :----------------------------------------------------------- |
| alert      | string      | 必填 | 通知内容           | 会填充到 toast 类型 text2 字段上。这里指定了，将会覆盖上级统一指定的 alert 信息；内容为空则不展示到通知栏。 |
| title      | string      | 可选 | 通知标题           | 会填充到 toast 类型 text1 字段上。                           |
| _open_page | string      | 可选 | 点击打开的页面名称 | 点击打开的页面。会填充到推送信息的 param 字段上，表示由哪个 App 页面打开该通知。可不填，则由默认的首页打开。 |
| extras     | JSON Object | 可选 | 扩展字段           | 作为参数附加到上述打开页面的后边。                           |



```
    {
        "notification" : {
            "winphone" : {
                 "alert" : "hello, JPush!", 
                 "title" : "Push Test", 
                 "_open_page" : "/friends.xaml", 
                 "extras" : {
                      "news_id" : 134, 
                      "my_key" : "a value"
                 }
            }
        }
    }
```

## message：自定义消息

应用内消息。或者称作：自定义消息，透传消息。
此部分内容不会展示到通知栏上，JPush SDK 收到消息内容后透传给 App。需要 App 自行处理。
iOS 在推送应用内消息通道（非 APNS）获取此部分内容，即需 App 处于前台。Windows Phone 暂时不支持应用内消息。

消息包含如下字段：

| 关键字       | 类型        | 选项 | 含义                |
| :----------- | :---------- | :--- | :------------------ |
| msg_content  | string      | 必填 | 消息内容本身        |
| title        | string      | 可选 | 消息标题            |
| content_type | string      | 可选 | 消息内容类型        |
| extras       | JSON Object | 可选 | JSON 格式的可选参数 |



```
Android 1.6.2 及以下版本 接收 notification 与 message 并存（即本次 api 调用同时推送通知和消息）的离线推送， 只能收到通知部分，message 部分没有透传给 App。

Android 1.6.3 及以上 SDK 版本已做相应调整，能正常接收同时推送通知和消息的离线记录。

iOS 1.7.3 及以上的版本才能正确解析 v3 的 message，但是无法解析 v2 推送通知同时下发的应用内消息。
```

## sms_message：短信补充

温馨提示：

\1. 使用短信业务，会产生额外的运营商费用，具体请咨询商务，联系电话：400-612-5955，商务 QQ：800024881

\2. 短信由签名和正文内容两部分组成。应运营商规定，签名和正文内容需审核。参考 [名词解释](https://docs.jiguang.cn/jsms/guideline/jsms_terminology/)

\3. 签名设置参考 [《控制台操作指南》之签名设置](https://docs.jiguang.cn/jsms/guideline/JSMS_consoleguide/#_9) 和 [短信签名 API](https://docs.jiguang.cn/jsms/server/rest_api_jsms_sign/) 。

\4. 自 2018 年 3 月起，短信补充的开发者必须提交正文内容模板，审核通过后即可使用。因此推送时需要填写 temp_id（如果模版有设置参数则需要填写 temp_para）。参考 [《控制台操作指南》之模板设置](https://docs.jiguang.cn/jsms/guideline/JSMS_consoleguide/#_12) 和 [短信模板 API](https://docs.jiguang.cn/jsms/server/rest_api_jsms_templates/) 。


sms_message 用于设置短信推送内容以及短信发送的延迟时间。

开发者需要先把用户的手机号码与设备的 registrationID 匹配。绑定方法：[服务端 - Device - 更新设备](https://docs.jiguang.cn/jpush/server/push/rest_api_v3_device/#_3) ; [Android API - 设置手机号码](https://docs.jiguang.cn/jpush/client/Android/android_api/#_61) ; [iOS API - 设置手机号码](https://docs.jiguang.cn/jpush/client/iOS/ios_api/#_151)；

与原有 JSON 业务协议相匹配，消息有如下字段信息：

| 关键字        | 类型    | 选项 | 说明                                                         |
| :------------ | :------ | :--- | :----------------------------------------------------------- |
| delay_time    | int     | 必填 | 单位为秒，不能超过 24 小时。设置为 0，表示立即发送短信。该参数仅对 android 和 iOS 平台有效，Winphone 平台则会立即发送短信。 |
| signid        | int     | 选填 | 签名 ID，该字段为空则使用应用默认签名。                      |
| temp_id       | long    | 必填 | 短信补充的内容模板 ID。没有填写该字段即表示不使用短信补充功能。 |
| temp_para     | JSON    | 可选 | 短信模板中的参数。                                           |
| active_filter | boolean | 可选 | active_filter 字段用来控制是否对补发短信的用户进行活跃过滤，默认为 true ，做活跃过滤；为 false，则不做活跃过滤； |

## options：可选参数

推送可选项。

当前包含如下几个可选项：

| 关键字            | 类型    | 选项 | 含义                  | 说明                                                         |
| :---------------- | :------ | :--- | :-------------------- | :----------------------------------------------------------- |
| sendno            | int     | 可选 | 推送序号              | 纯粹用来作为 API 调用标识，API 返回时被原样返回，以方便 API 调用方匹配请求与返回。值为 0 表示该 messageid 无 sendno，所以字段取值范围为非 0 的 int. |
| time_to_live      | int     | 可选 | 离线消息保留时长 (秒) | 推送当前用户不在线时，为该用户保留多长时间的离线消息，以便其上线时再次推送。默认 86400 （1 天），最长 10 天。设置为 0 表示不保留离线消息，只有推送当前在线的用户可以收到。该字段对 iOS 的 Notification 消息无效。 |
| override_msg_id   | long    | 可选 | 要覆盖的消息 ID       | 如果当前的推送要覆盖之前的一条推送，这里填写前一条推送的 msg_id 就会产生覆盖效果，即：1）该 msg_id 离线收到的消息是覆盖后的内容；2）即使该 msg_id Android 端用户已经收到，如果通知栏还未清除，则新的消息内容会覆盖之前这条通知；覆盖功能起作用的时限是：1 天。如果在覆盖指定时限内该 msg_id 不存在，则返回 1003 错误，提示不是一次有效的消息覆盖操作，当前的消息不会被推送；该字段仅对 Android 有效。 |
| apns_production   | boolean | 可选 | APNs 是否生产环境     | True 表示推送生产环境，False 表示要推送开发环境；如果不指定则为推送生产环境。但注意，JPush 服务端 SDK 默认设置为推送 “开发环境”。该字段仅对 iOS 的 Notification 有效。 |
| apns_collapse_id  | string  | 可选 | 更新 iOS 通知的标识符 | APNs 新通知如果匹配到当前通知中心有相同 apns-collapse-id 字段的通知，则会用新通知内容来更新它，并使其置于通知中心首位。collapse id 长度不可超过 64 bytes。 |
| big_push_duration | int     | 可选 | 定速推送时长 (分钟)   | 又名缓慢推送，把原本尽可能快的推送速度，降低下来，给定的 n 分钟内，均匀地向这次推送的目标用户推送。最大值为 1400。未设置则不是定速推送。 |

## cid：推送唯一标识符

### 调用地址

GET https://api.jpush.cn/v3/push/cid[?count=n[&type=xx]]

### 功能说明

cid 是用于防止 api 调用端重试造成服务端的重复推送而定义的一个推送参数。

用户使用一个 cid 推送后，再次使用相同的 cid 进行推送，则会直接返回第一次成功推送的结果，不会再次进行推送。

CID 的有效期为 1 天。CID 的格式为：{appkey}-{uuid}

在使用 cid 之前，必须通过接口获取你的 cid 池。获取时 type=push 或者不传递 type 值。

### 调用示例

**Request Header**

```
curl --insecure -X GET -v https://api.jpush.cn/v3/push/cid?count=3 -H "Content-Type: application/json" -u "2743204aad6fe2572aa2d8de:e674a3d0fd42a53b9a58121c"
GET /v3/push/cid?count=3
Authorization: Basic (base64 auth string)
Content-Type: text/plain
Accept: application/json
```

**Request Params**

```
count
    可选参数。数值类型，不传则默认为 1。范围为 [1, 1000]
type
    可选参数。CID 类型。取值：push（默认），schedule
```

**Response Header**

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

 Response Data  

{
 "cidlist":[
 "8103a4c628a0b98994ec1949-128eeb45-471c-49f3-b442-a05c20c9ed56",
 "8103a4c628a0b98994ec1949-6e44d7f1-89f5-48a8-bec4-e359c15b13e5",
 "8103a4c628a0b98994ec1949-47e0a960-ce67-4e71-94ce-b4b9e8813af0"
 ]
}
```

**Response Params**

```
cidlist
    cid 列表
```

## Group Push API：应用分组推送

### 调用地址

POST https://api.jpush.cn/v3/grouppush

### 功能说明

该 API 用于为开发者在 portal 端创建的应用分组创建推送。

groupkey 可以在创建的分组信息中获取，使用起来同 appkey 类似，但在使用的时候前面要加上 “group-” 前缀。

**注**：暂不支持 option 中 override_msg_id 的属性；分组推送仅在官网支持设置定时，调 Schedule API 时不支持。

### 调用示例

```
curl --insecure -X POST -v https://api.jpush.cn/v3/grouppush -H "Content-Type: application/json" -u "group-e4c938578ee598be517a2243:71d1dc4dae126674ed386b7b" -d '{"platform":["android"],"audience":"all","notification":{"android":{"alert":"notification content","title":"notification title"}},"message":{"msg_content":"message content"}}'
```

## 批量单推（VIP 专属接口）

### 调用地址

POST https://api.jpush.cn/v3/push/batch/regid/single 
POST https://api.jpush.cn/v3/push/batch/alias/single

**注**：/v3/push/batch/regid/single 针对的是 RegID 方式批量单推，/v3/push/batch/alias/single 针对的是 Alias 方式批量单推

### 功能说明

如果您在给每个用户的推送内容都不同的情况下，可以使用此接口。

如需要开通此接口，请联系：[商务客服](https://www.jiguang.cn/accounts/business_contact?fromPage=push_doc)

### 调用说明

使用此接口前，您需要配合使用 [cid: 推送唯一标识符](https://docs.jiguang.cn/jpush/server/push/rest_api_v3_push/#cid) 接口提前获取到 cid 池，获取时 type=push 或者不传递 type 值；获取到 cid 值后，传递参数格式如下：

```
{"pushlist":{
    "cid值1":{     
        ...
    },
    "cid值2":{     
        ...
    },
    ...
}}
```

### 调用示例

**Request Header**

>  POST /v3/push/batch/regid/single HTTP/1.1 Authorization: Basic N2Q0MzFlNDJkZmE2YTZkNjkzYWMyZDA0OjVlOTg3YWM2ZDJlMDRkOTVhOWQ4ZjBkMQ==

或者

>  POST /v3/push/batch/alias/single HTTP/1.1 Authorization: Basic N2Q0MzFlNDJkZmE2YTZkNjkzYWMyZDA0OjVlOTg3YWM2ZDJlMDRkOTVhOWQ4ZjBkMQ==

**Request Params**

```
pushlist
    必填参数。JSON类型
cid值
    必填参数。JSON类型，取值：push（默认），JSON Value部分具体字段参考下面表格说明
```

| 关键字       | 选项 | 含义                                                         |
| :----------- | :--- | :----------------------------------------------------------- |
| platform     | 必填 | 推送平台设置                                                 |
| target       | 必填 | 推送设备指定。 如果是调用 RegID 方式批量单推接口（/v3/push/batch/regid/single），那此处就是指定 regid 值； 如果是调用 Alias 方式批量单推接口（/v3/push/batch/alias/single），那此处就是指定 alias 值。 |
| notification | 可选 | 通知内容体。是被推送到客户端的内容。与 message 一起二者必须有其一，可以二者并存 |
| message      | 可选 | 消息内容体。是被推送到客户端的内容。与 notification 一起二者必须有其一，可以二者并存 |
| sms_message  | 可选 | 短信渠道补充送达内容体                                       |
| options      | 可选 | 推送参数                                                     |

完整参数示例：

```
{"pushlist":{
    "cid1":{     
        "platform": "all",
        "target": "aliasvalue1",       // 此处填写的是regid值或者alias值
        "notification": {
            ...    // 省略参数同push api部分
        },
        "message": {
            ...   // 省略参数同push api部分
        },
        "sms_message":{
            ...  // 省略参数同push api部分
        },
        "options": {
            ...  // 省略参数同push api部分
        }
    },
    "cid2":{     
        "platform": "all",
        "target": "aliasvalue2",       // 此处填写的是regid值或者alias值
        "notification": {
            ...
        },
        "message": {
            ...
        },
        "sms_message":{
            ...
        },
        "options": {
            ...
        }
    },
    ...
}}
```

**Response**

成功返回：

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

Success Response Data
{
    "cid1"：{
        "msg_id":134123478
    },
    "cid1"：{
        "msg_id":134123478,
        "error":{
            "code":1011,
            "message":"****"
        }
    },
    "cid3"：{
        "error":{
            "code":1009,
            "message":"****"
        }
    },
    ...
}
```

失败返回：

```
HTTP/1.1 400 OK
Content-Type: application/json; charset=utf-8

 Failed Response Data 
{
    "error":{
        "message":"Authen failed",
        "code":1004
    }
}
```

## 推送校验 API

### 调用地址

POST https://api.jpush.cn/v3/push/validate

### 功能说明

该 API 只用于验证推送调用是否能够成功，与推送 API 的区别在于：不向用户发送任何消息。 其他字段说明：同推送 API。

## 调用返回

| Code | 描述                           | 详细解释                                                     | HTTP Status Code |
| :--- | :----------------------------- | :----------------------------------------------------------- | :--------------- |
| 1000 | 系统内部错误                   | 服务器端内部逻辑错误，请稍后重试。                           | 500              |
| 1001 | 只支持 HTTP Post 方法          | 不支持 Get 方法。                                            | 405              |
| 1002 | 缺少了必须的参数               | 必须改正，检查要求必填的参数是否未写                         | 400              |
| 1003 | 参数值不合法                   | 必须改正。参数不合法的情况如：Audience 参数中 tag，alias，registration_id 有空值；单发指定的 registration_id 非法或者格式错误。 | 400              |
| 1004 | 验证失败                       | 必须改正。检查 Appkey 与 MasterSecret，详情请看：[调用验证](https://docs.jiguang.cn/jpush/server/push/rest_api_v3_push/#_5) | 401              |
| 1005 | 消息体太大                     | 必须改正。 Android 平台 Notification+Message 长度限制为 4000 字节； iOS Notification 中 “iOS”:{ } 及大括号内的总体长度不超过：2000 个字节（包括自定义参数和符号），iOS 的 Message 部分长度不超过 4000 字节； WinPhone 平台 Notification 长度限制为 1000 字节 | 400              |
| 1008 | app_key 参数非法               | 必须改正，请仔细对比你所传的 Appkey 是否与应用信息中的一致，是否多了空格 | 400              |
| 1009 | 推送对象中有不支持的 key       | 必须改正，提示：Android 属性不支持 sound 字段；是否将 content-available 错误地写为 content_available，builder_id 错误地写为 build_id；除文档中指定的字段外，还需传递自定义的 key 请在 extras 中填写。 | 400              |
| 1011 | 没有满足条件的推送目标         | 请检查是否有设备满足 audience 的目标条件（别名与标签是否设置成功）；若客户端未完成 SDK 集成，服务端先做测试，需下载 demo 安装到手机上再做推送；第一次集成成功，若采用广播推送请等待 10 分钟。 | 400              |
| 1012 | 符合当前条件的推送已超过限制   | 定速推送超过限制                                             | 400              |
| 1020 | 只支持 HTTPS 请求              | 必须改正                                                     | 404              |
| 1030 | 内部服务超时                   | 稍后重试，若多次重试无法成功，请联系 support@jpush.cn        | 503              |
| 2002 | API 调用频率超出该应用的限制   | 注意[ API 频率控制](https://docs.jiguang.cn/jpush/server/push/server_overview/#api_1)，可联系极光商务或技术支持开通更高的 API 调用频率 | 429              |
| 2003 | 该应用 appkey 已被限制调用 API | 联系技术支持查明限制原因和寻求帮助                           | 403              |
| 2004 | 无权限执行当前操作             | 必须改正。当前调用 API 的源 ip 地址不在该应用的 ip 白名单中，请在官网应用设置中配置 IP 白名单。 | 403              |
| 2005 | 信息发送量超出合理范围。       | 检测到目标用户累计发送消息量过大，超过合理的使用范围，需要检查业务逻辑或者联系技术支持。 | 403              |
| 2006 | 非 VIP 用户。                  | 接口只针对 VIP 用户开放。                                    | 403              |
| 2007 | 无权调用此接口。               | 请联系商务开通使用权限。                                     | 403              |

## 参考

+  HTTP 返回码：[HTTP-Status-Code](https://docs.jiguang.cn/jpush/server/push/http_status_code/)

+  获取推送送达 API：[Report-API](https://docs.jiguang.cn/jpush/server/push/rest_api_v3_report)

+  老版本 Push API：[Push API v2](https://docs.jiguang.cn/jpush/server/old/rest_api_v2_push)

+  HTTP 规范参考：[HTTP 基本认证](http://zh.wikipedia.org/zh/HTTP基本认证)

+  Apple APNs 规范：[Apple Push Notification Service](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1)

+  Microsoft MPNs 规范：[Push notifications for Windows Phone 8](http://msdn.microsoft.com/en-us/library/windowsphone/develop/ff402558(v=vs.105).aspx)

   



# JPush API Python Client

## 概述

这是 JPush REST API 的 Python 版本封装开发包，是由极光推送官方提供的，一般支持最新的 API 功能。

对应的 REST API 文档：<https://docs.jiguang.cn/jpush/server/push/server_overview/>

## 兼容版本

+  Python 2.7
+  Python 3

## 环境配置

pip 方式：

```
sudo pip install jpush
```

easy_install 方式：

```
sudo easy_install jpush
```

使用源码方式：

```
sudo python setup.py install
```

## 代码样例

>  代码样例在 jpush-api-python-client 中的 examples 文件夹中，[点击查看所有 examples ](https://github.com/jpush/jpush-api-python-client/tree/master/examples) 。

>  以下片断来自项目代码里的文件：jpush-api-python-client 中的 examples/push_examples  目录下的 example_all.py

>  这个样例演示了消息推送，日志设置，异常处理。

```python
_jpush = jpush.JPush(app_key, master_secret)
push = _jpush.create_push()
# if you set the logging level to "DEBUG",it will show the debug logging.
_jpush.set_logging("DEBUG")
push.audience = jpush.all_
push.notification = jpush.notification(alert="hello python jpush api")
push.platform = jpush.all_
try:
    response=push.send()
except common.Unauthorized:
    raise common.Unauthorized("Unauthorized")
except common.APIConnectionException:
    raise common.APIConnectionException("conn error")
except common.JPushFailure:
    print ("JPushFailure")
except:
    print ("Exception")
```

## 日志说明

logging level 默认的是 WARNING ，为了方便调试建议设置为 DEBUG
设置方法为：

```
_jpush.set_logging("DEBUG")
```

## 异常说明

+  Unauthorized
   +  AppKey，Master Secret 错误，验证失败必须改正。
+  APIConnectionException
   +  包含错误的信息：比如超时，无网络等情况。
+  JPushFailure
   +  请求出错，参考业务返回码。

## HTTP 状态码

参考文档：<http://docs.jiguang.cn/jpush/server/push/http_status_code/>

Push v3 API 状态码 参考文档：<http://docs.jiguang.cn/jpush/server/push/rest_api_v3_push/>　

Report API  状态码 参考文档：<http://docs.jiguang.cn/jpush/server/push/rest_api_v3_report/>

Device API 状态码 参考文档：<http://docs.jiguang.cn/jpush/server/push/rest_api_v3_device/>

Push Schedule API 状态码 参考文档：<http://docs.jiguang.cn/jpush/server/push/rest_api_push_schedule/>　

[Release页面](https://github.com/jpush/jpush-api-python-client/releases) 有详细的版本发布记录与下载。



## 初始化

实例化JPush对象

```
_jpush = jpush.JPush(app_key, master_secret)
```

参数说明

>  app_key  https://www.jpush.cn/ 控制台获取

>  master_secret  https://www.jpush.cn/ 控制台获取

返回值

>  JPush 实例



## Push api

### 初始化push对象

```
push = _jpush.create_push()
```

参数说明 （无）

返回值

>  push 实例

#### audience 设置

##### tag 设置

```
tag(*tags)
```

参数说明

tags 例如：tag("tag1", "tag2")

返回值

>  payload 字典

##### tag_and 设置

```
tag_and(*tag_ands)
```

参数说明

tags 例如：tag_and("tag1", "tag2")

返回值

>  payload 字典

##### tag_not 设置

```
tag_not(*tag_nots)
```

参数说明

tags 例如：tag_not("tag1", "tag2")

返回值

>  payload 字典

##### alias 设置

```
alias(*alias)
```

参数说明

alias 例如：alias("alias1", "alias2")

返回值

>  payload 字典

##### registration_id 设置

```
registration_id(*reg_ids)
```

参数说明

registration_id 例如：tag("registration_id1", "registration_id2")

返回值

>  payload 字典

##### 推送目标说明

推送设备对象，表示一条推送可以被推送到哪些设备列表。确认推送设备对象，JPush 提供了多种方式，比如：别名、标签、注册ID、分群、广播等。

+  all

如果要发广播（全部设备），则直接填写 “all”。

+  推送目标

广播外的设备选择方式，有如下几种：

<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr bgcolor="#D3D3D3">
			<th >关键字</th>
			<th >含义</th>
			<th >类型</th>
			<th >说明</th>
			<th >备注</th>
		</tr>
		<tr >
			<td>tag</td>
			<td>JSON Array</td>
			<td>标签</td>
			<td>数组。多个标签之间是 OR 的关系，即取并集。 </td>
			<td>用标签来进行大规模的设备属性、用户属性分群。 一次推送最多 20 个。<ul style="margin-bottom: 0;"><li>有效的 tag 组成：字母（区分大小写）、数字、下划线、汉字。</li><li>限制：每一个 tag 的长度限制为 40 字节。（判断长度需采用UTF-8编码）</li></td>
		</tr>
		<tr >
			<td>tag_and</td>
			<td>JSON Array</td>
			<td>标签AND</td>
			<td>数组。多个标签之间是 AND 关系，即取交集。</td>
			<td>注册与 tag 区分。一次推送最多 20 个。</td>
		</tr>
		<tr >
			<td>alias</td>
			<td>JSON Array</td>
			<td>别名</td>
			<td>数组。多个别名之间是 OR 关系，即取并集。</td>
			<td>用别名来标识一个用户。一个设备只能绑定一个别名，但多个设备可以绑定同一个别名。一次推送最多 1000 个。<ul style="margin-bottom: 0;"><li>有效的 alias 组成：字母（区分大小写）、数字、下划线、汉字。</li><li>限制：每一个 alias 的长度限制为 40 字节。（判断长度需采用UTF-8编码）</li></td>
		</tr>
		<tr >
			<td>registration_id</td>
			<td>JSON Array</td>
			<td>注册ID</td>
			<td>数组。多个注册ID之间是 OR 关系，即取并集。</td>
			<td>设备标识。一次推送最多 1000 个。</td>
		</tr>
	</table>
</div>



#### notification 设置

```
notification(alert=None, ios=None, android=None, winphone=None)
```

参数说明

+  alert

>  通知的内容在各个平台上，都可能只有这一个最基本的属性 "alert"。
>  这个位置的 "alert" 属性（直接在 notification 对象下），是一个快捷定义，各平台的 alert 信息如果都一样，则可不定义。如果各平台有定义，则覆盖这里的定义。

+  ios

>  ios payload 字典 查看 [ios payload](https://github.com/jpush/jpush-api-python-client/blob/master/docs/push/push.md#ios-payload)

+  android

>  android payload 字典 查看 [android payload](https://github.com/jpush/jpush-api-python-client/blob/master/docs/push/push.md#android-payload)

返回值

>  notification payload

##### ios payload

```
ios(alert=None, badge='+1', sound=None， content_available=False, mutable_content=False, category=None, extras=None, sound_disable=False, thread_id=None):

```

参数说明

<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th >关键字</th>
			<th >类型</th>
			<th width="6%">选项</th>
			<th width="20%">含义</th>
			<th >说明</th>
		</tr>
		<tr >
			<td>alert</td>
			<td>string</td>
			<td>必填</td>
			<td width="20%">通知内容</td>
			<td>
			这里指定内容将会覆盖上级统一指定的 alert 信息；内容为空则不展示到通知栏。支持字符串形式也支持官方定义的 alert payload 结构，在该结构中包含 title 和 subtitle 等官方支持的 key
			</td>
		</tr>
		<tr >
			<td>sound</td>
			<td>string</td>
			<td>可选</td>
			<td width="20%">通知提示声音</td>
			<td>
			普通通知： string类型，如果无此字段，则此消息无声音提示；有此字段，如果找到了指定的声音就播放该声音，否则播放默认声音，如果此字段为空字符串，iOS 7 为默认声音，iOS 8 及以上系统为无声音。说明：JPush 官方 SDK 会默认填充声音字段，提供另外的方法关闭声音，详情查看各 SDK 的源码。
			告警通知： JSON Object ,支持官方定义的 payload 结构，在该结构中包含 critical 、name 和 volume 等官方支持的 key
			</td>
		</tr>
		<tr >
			<td>badge</td>
			<td>int</td>
			<td>可选</td>
			<td width="20%">应用角标</td>
			<td>如果不填，表示不改变角标数字；否则把角标数字改为指定的数字；为 0 表示清除。JPush 官方 API Library(SDK) 会默认填充badge值为"+1",详情参考：<a href="http://blog.jpush.cn/ios_apns_badge_plus/">badge +1</a></td>
		</tr>
		<tr >
			<td>content-available</td>
			<td>boolean</td>
			<td>可选</td>
			<td width="20%">推送唤醒</td>
			<td>推送的时候携带"content-available":true 说明是 Background Remote Notification，如果不携带此字段则是普通的Remote Notification。详情参考：<a href="../../client/iOS/ios_new_fetures/#ios-7-background-remote-notification">Background Remote Notification</a></td>
		</tr>
		<tr >
			<td>mutable-content</td>
			<td>boolean</td>
			<td>可选</td>
			<td width="20%">通知扩展</td>
			<td>推送的时候携带 ”mutable-content":true 说明是支持iOS10的UNNotificationServiceExtension，如果不携带此字段则是普通的 Remote Notification。详情参考：<a href="../../client/IOS/ios_new_fetures/#ios-10-service-extension">UNNotificationServiceExtension</a></td>
		</tr>
		<tr >
			<td>category</td>
			<td>string</td>
			<td>可选</td>
			<td width="20%"> </td>
			<td>IOS8才支持。设置APNs payload中的"category"字段值</td>
		</tr>
		<tr >
			<td>thread-id</td>
			<td>string</td>
			<td>可选</td>
			<td width="20%">通知分组</td>
			<td>ios 的远程通知通过该属性来对通知进行分组，同一个 thread-id 的通知归为一组。</td>
		</tr>
		<tr >
			<td>extras</td>
			<td>JSON Object</td>
			<td>可选</td>
			<td width="20%">扩展字段</td>
			<td>这里自定义 Key/value 信息，以供业务使用。</td>
		</tr>
	</table>
</div>

返回值

>  ios payload 字典

##### android payload

```
android(alert, title=None, builder_id=None, extras=None, priority=None, category=None, style=None, alert_type=None, big_text=None, inbox=None, big_pic_path=None, large_icon=None, intent=None)

```

参数说明

<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th >关键字</th>
			<th >类型</th>
			<th width="6%" >选项</th>
			<th >含义</th>
			<th >说明</th>
		</tr>
		<tr >
			<td>alert</td>
			<td>string</td>
			<td>必填</td>
			<td>通知内容</td>
			<td>这里指定了，则会覆盖上级统一指定的 alert 信息；内容可以为空字符串，则表示不展示到通知栏。</td>
		</tr>
		<tr >
			<td>title</td>
			<td>string</td>
			<td>可选</td>
			<td>通知标题</td>
			<td>如果指定了，则通知里原来展示 App名称的地方，将展示成这个字段。</td>
		</tr>
		<tr >
			<td>builder_id</td>
			<td>int</td>
			<td>可选</td>
			<td>通知栏样式ID</td>
			<td>Android SDK 可设置通知栏样式，这里根据样式 ID 来指定该使用哪套样式。</td>
		</tr>
		<tr >
			<td>extras</td>
			<td>JSON Object</td>
			<td>可选</td>
			<td>扩展字段</td>
			<td>这里自定义 JSON 格式的 Key/Value 信息，以供业务使用。</td>
		</tr>
	</table>
</div>



返回值

>  android payload 字典

#### message 设置

```
message(msg_content, title=None, content_type=None, extras=None)

```

参数说明

<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th width="10%">关键字</th>
			<th width="8%">类型</th>
			<th width="6%">选项</th>
			<th>含义</th>
		</tr>
		<tr >
			<td>msg_content</td>
			<td>string</td>
			<td>必填</td>
			<td>消息内容本身</td>
		</tr>
		<tr >
			<td>title</td>
			<td>string</td>
			<td>可选</td>
			<td>消息标题</td>
		</tr>
		<tr >
			<td>content_type</td>
			<td>string</td>
			<td>可选</td>
			<td>消息内容类型</td>
		</tr>
		<tr >
			<td>extras</td>
			<td>JSON Object</td>
			<td>可选</td>
			<td>JSON 格式的可选参数</td>
		</tr>
	</table>
</div>

返回值

>  message payload

#### smsmessage 设置

```
smsmessage(content,delay_time)

```

+  参数说明

<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th width="10%">关键字</th>
			<th width="8%">类型</th>
			<th width="6%">选项</th>
			<th>示例</th>
		</tr>
		<tr >
			<td>content</td>
			<td>string</td>
			<td>必填</td>
			<td>不能超过480个字符。"你好,JPush"为8个字符。超过67个字符的内容（含签名）会被拆分成多条短信下发。</td>
		</tr>
		<tr >
			<td>delay_time</td>
			<td>int</td>
			<td>必填</td>
			<td>单位为秒，不能超过24小时。设置为0，表示立即发送短信。该参数仅对android平台有效，iOS 和 Winphone平台则会立即发送短信</td>
		</tr>
	</table>
</div>

+  返回值

>  smsmessage payload

#### platform 设置

```
platform(*types)

```

+  参数说明

JPush 当前支持 Android, iOS, Windows Phone 三个平台的推送。其关键字分别为："android", "ios","winphone"。

+  返回值

>  platform tuple

#### options 设置

```
options(options)

```

+  参数说明

<div class="table-d" align="center" >
	<table border="1" width = "100%">
		<tr  bgcolor="#D3D3D3" >
			<th >关键字</th>
			<th >类型</th>
			<th width="6%">选项</th>
			<th >含义</th>
			<th >说明</th>
		</tr>
		<tr >
			<td>sendno</td>
			<td>int</td>
			<td>可选</td>
			<td>推送序号</td>
			<td>纯粹用来作为 API 调用标识，API 返回时被原样返回，以方便 API 调用方匹配请求与返回。</td>
		</tr>
		<tr >
			<td>time_to_live</td>
			<td>int</td>
			<td>可选</td>
			<td>离线消息保留时长(秒)</td>
			<td>推送当前用户不在线时，为该用户保留多长时间的离线消息，以便其上线时再次推送。默认 86400 （1 天），最长 10 天。设置为 0 表示不保留离线消息，只有推送当前在线的用户可以收到。</td>
		</tr>
		<tr >
			<td>override_msg_id</td>
			<td>long</td>
			<td>可选</td>
			<td>要覆盖的消息ID</td>
			<td>如果当前的推送要覆盖之前的一条推送，这里填写前一条推送的 msg_id 就会产生覆盖效果，即：1）该 msg_id 离线收到的消息是覆盖后的内容；2）即使该 msg_id Android 端用户已经收到，如果通知栏还未清除，则新的消息内容会覆盖之前这条通知；覆盖功能起作用的时限是：1 天。如果在覆盖指定时限内该 msg_id 不存在，则返回 1003 错误，提示不是一次有效的消息覆盖操作，当前的消息不会被推送。</td>
		</tr>
		<tr >
			<td>apns_production</td>
			<td>boolean</td>
			<td>可选</td>
			<td>APNs是否生产环境</td>
			<td>True 表示推送生产环境，False 表示要推送开发环境；如果不指定则为推送生产环境。JPush 官方 API LIbrary (SDK) 默认设置为推送 “开发环境”。</td>
		</tr>
		<tr >
			<td>big_push_duration</td>
			<td>int</td>
			<td>可选</td>
			<td>定速推送时长(分钟)</td>
			<td>又名缓慢推送，把原本尽可能快的推送速度，降低下来，给定的n分钟内，均匀地向这次推送的目标用户推送。最大值为1400.未设置则不是定速推送。</td>
		</tr>
	</table>
</div>

+  返回值

>  options 字典





## 实例：

### 1. 程序结构

```python
__init__.py
admin_example.py
device_example.py
group_push_example.py
push_example.py
report_example.py
schedule_example.py
zone_example.py
```

### 2. —init—.py

```python
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import jpush

from .conf import app_key, master_secret, dev_key, dev_secret

from . import device_example
from . import push_example
from . import report_example
from . import schedule_example
from . import group_push_example
from . import admin_example
from . import zone_example

__all__ = [
    device_example,
    push_example,
    report_example,
    schedule_example,
    group_push_example,
    admin_example,
    zone_example,
]

```



### 3.admin_example.py

```python
from . import jpush, dev_key, dev_secret

admin = jpush.Admin(dev_key, dev_secret)
admin.set_logging("DEBUG")

def create_app():
    response = admin.create_app('aaa', 'cn.jpush.app')
    return response

def delete_app(app_key):
    response = admin.delete_app(app_key)
    return response

```



### 4.device_example.py

```python
from . import jpush, app_key, master_secret

_jpush = jpush.JPush(app_key, master_secret)
_jpush.set_logging("DEBUG")
device = _jpush.create_device()

def alias_user():
    alias = "alias1"
    platform = "android,ios"
    device.get_aliasuser(alias, platform)

def ctrl_tag():
    reg_id = '090c1f59f89'
    entity = jpush.device_tag("")
    device.set_deviceinfo(reg_id, entity)

def get_device():
    reg_id = '090c1f59f89'
    device.get_deviceinfo(reg_id)

def delete_alias():
    alias = "alias1"
    platform = "android,ios"
    device.delete_alias(alias, platform)

def delete_tag():
    tag = "ddd"
    platform = "android,ios"
    device.delete_tag(tag, platform)

def check_tag():
    tag = "ddd"
    registration_id = '090c1f59f89'
    device.check_taguserexist(tag, registration_id)

def tag_list():
    device.get_taglist()

def tag_update_user():
    tag = "ddd"
    entity = jpush.device_regid(jpush.add("090c1f59f89"))
    device.update_tagusers(tag, entity)

def update_device():
    reg_id = '1507bfd3f7c466c355c'
    entity = jpush.device_tag(jpush.add("ddd", "tageee"))
    result=device.set_devicemobile(reg_id, entity)
    print (result.status_code)
    print (result.payload)

def update_device_mobile():
    reg_id = '1507bfd3f7c466c355c'
    entity = jpush.device_mobile("18588232140")
    device.set_devicemobile(reg_id, entity)

def get_device_status():
    reg_id = '1507bfd3f7c466c355c'
    device.get_device_status(reg_id)

```



### 5.group_push_example.py

```python
from . import jpush
from jpush import common

group_key = u'xxxxxx'
group_secret = u'xxxxxx'

group = jpush.GroupPush(group_key, group_secret)
group.set_logging("DEBUG")

def all():
    push = group.create_push()
    push.audience = jpush.all_
    push.notification = jpush.notification(alert="!hello python jpush api")
    push.platform = jpush.all_
    try:
        response=push.send()
    except common.Unauthorized:
        raise common.Unauthorized("Unauthorized")
    except common.APIConnectionException:
        raise common.APIConnectionException("conn")
    except common.JPushFailure:
        print ("JPushFailure")
    except:
        print ("Exception")

```



### 6.push_example.py

```python
from . import jpush, app_key, master_secret

_jpush = jpush.JPush(app_key, master_secret)
_jpush.set_logging("DEBUG")

def alias():
    push = _jpush.create_push()
    alias=["alias1", "alias2"]
    alias1={"alias": alias}
    print(alias1)
    push.audience = jpush.audience(
        jpush.tag("tag1", "tag2"),
        alias1
    )

    push.notification = jpush.notification(alert="Hello world with audience!")
    push.platform = jpush.all_
    print (push.payload)
    push.send()

def all():
    push = _jpush.create_push()
    push.audience = jpush.all_
    push.notification = jpush.notification(alert="!hello python jpush api")
    push.platform = jpush.all_
    try:
        response=push.send()
    except common.Unauthorized:
        raise common.Unauthorized("Unauthorized")
    except common.APIConnectionException:
        raise common.APIConnectionException("conn")
    except common.JPushFailure:
        print ("JPushFailure")
    except:
        print ("Exception")

def audience():
    push = _jpush.create_push()

    push.audience = jpush.audience(
                jpush.tag("tag1", "tag2"),
                jpush.alias("alias1", "alias2")
            )


    push.notification = jpush.notification(alert="Hello world with audience!")
    push.platform = jpush.all_
    print (push.payload)
    push.send()


def notification():
    push = _jpush.create_push()

    push.audience = jpush.all_
    push.platform = jpush.all_

    ios = jpush.ios(alert="Hello, IOS JPush!", sound="a.caf", extras={'k1':'v1'})
    android = jpush.android(alert="Hello, Android msg", priority=1, style=1, alert_type=1,big_text='jjjjjjjjjj', extras={'k1':'v1'})

    push.notification = jpush.notification(alert="Hello, JPush!", android=android, ios=ios)

    # pprint (push.payload)
    result = push.send()

def options():
    push = _jpush.create_push()
    push.audience = jpush.all_
    push.notification = jpush.notification(alert="Hello, world!")
    push.platform = jpush.all_
    push.options = {"time_to_live":86400, "sendno":12345,"apns_production":True}
    push.send()

def platfrom_msg():
    push = _jpush.create_push()
    push.audience = jpush.all_
    ios_msg = jpush.ios(alert="Hello, IOS JPush!", badge="+1", sound="a.caf", extras={'k1':'v1'})
    android_msg = jpush.android(alert="Hello, android msg")
    push.notification = jpush.notification(alert="Hello, JPush!", android=android_msg, ios=ios_msg)
    push.message=jpush.message("content",extras={'k2':'v2','k3':'v3'})
    push.platform = jpush.all_
    push.send()


def silent():
    push = _jpush.create_push()
    push.audience = jpush.all_
    ios_msg = jpush.ios(alert="Hello, IOS JPush!", badge="+1", extras={'k1':'v1'}, sound_disable=True)
    android_msg = jpush.android(alert="Hello, android msg")
    push.notification = jpush.notification(alert="Hello, JPush!", android=android_msg, ios=ios_msg)
    push.platform = jpush.all_
    push.send()


def sms():
    push = _jpush.create_push()
    push.audience = jpush.all_
    push.notification = jpush.notification(alert="a sms message from python jpush api")
    push.platform = jpush.all_
    push.smsmessage=jpush.smsmessage("a sms message from python jpush api",0)
    print (push.payload)
    push.send()

def validate():
    push = _jpush.create_push()
    push.audience = jpush.all_
    push.notification = jpush.notification(alert="Hello, world!")
    push.platform = jpush.all_
    push.send_validate()

```



### 7. report_example.py

```python
from . import jpush, app_key, master_secret

_jpush = jpush.JPush(app_key, master_secret)
_jpush.set_logging("DEBUG")
report=_jpush.create_report()

def messages():
    report.get_messages("3289406737")

def receivede():
    report.get_received("3289406737")

def users():
    report.get_users("DAY","2016-04-10","3")

def status():
    report.get_status_messages('3289406737', ['xxx'])

```



### 8.schedule_example.py

```python
from . import jpush, app_key, master_secret

_jpush = jpush.JPush(app_key, master_secret)
_jpush.set_logging("DEBUG")
schedule = _jpush.create_schedule()

def delete_schedule():
    schedule.delete_schedule("e9c553d0-0850-11e6-b6d4-0021f652c102")

def get_schedule():
    schedule.get_schedule_by_id("e9c553d0-0850-11e6-b6d4-0021f652c102")

def get_schedule_list():
    schedule.get_schedule_list("1")

def post_schedule():
    push = _jpush.create_push()
    push.audience = jpush.all_
    push.notification = jpush.notification(alert="Hello, world!")
    push.platform = jpush.all_
    push=push.payload

    trigger=jpush.schedulepayload.trigger("2016-07-17 12:00:00")
    schedulepayload=jpush.schedulepayload.schedulepayload("name",True,trigger,push)
    result=schedule.post_schedule(schedulepayload)
    print (result.status_code)

def put_schedule():
    push = _jpush.create_push()
    push.audience = jpush.all_
    push.notification = jpush.notification(alert="Hello, world!")
    push.platform = jpush.all_
    push=push.payload

    trigger=jpush.schedulepayload.trigger("2016-05-17 12:00:00")
    schedulepayload=jpush.schedulepayload.schedulepayload("update a new name", True, trigger, push)
    schedule.put_schedule(schedulepayload,"17349f00-0852-11e6-91b1-0021f653c902")

```



### 9.zone_example.py

```python
from . import jpush, app_key, master_secret

def default():
    _jpush = jpush.JPush(app_key, master_secret)
    _jpush.set_logging("DEBUG")

    push = _jpush.create_push()
    push.audience = jpush.all_
    push.notification = jpush.notification(alert="!hello python jpush api")
    push.platform = jpush.all_
    try:
        response=push.send()
    except common.Unauthorized:
        raise common.Unauthorized("Unauthorized")
    except common.APIConnectionException:
        raise common.APIConnectionException("conn")
    except common.JPushFailure:
        print ("JPushFailure")
    except:
        print ("Exception")

def bj():
    _jpush = jpush.JPush(app_key, master_secret, zone = 'bj')
    _jpush.set_logging("DEBUG")

    push = _jpush.create_push()
    push.audience = jpush.all_
    push.notification = jpush.notification(alert="!hello python jpush api")
    push.platform = jpush.all_
    try:
        response=push.send()
    except common.Unauthorized:
        raise common.Unauthorized("Unauthorized")
    except common.APIConnectionException:
        raise common.APIConnectionException("conn")
    except common.JPushFailure:
        print ("JPushFailure")
    except:
        print ("Exception")

```



### 10. conf.py.simple

```
# please put your app_key and master_secret here
app_key = u'xxxxxx'
master_secret = u'xxxxxx'

dev_key = u'xxxxxx'
dev_secret = u'xxxxxx'

```

