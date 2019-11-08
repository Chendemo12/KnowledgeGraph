# [Pushbullet API](https://docs.pushbullet.com/#pushbullet-api)

Pushbullet 的 API 使开发人员能够在 Pushbullet 基础架构上构建。我们的目标是提供一个完整的 API，使任何东西都能进入 Pushbullet 网络。

这对我们很重要，因为我们相信所有东西，不仅仅是智能手机和电脑，都应该能够实时交换信息。以下是您可以使用 Pushbullet 构建的一些内容：

+  有一个网站，并希望提供推送通知？我们已经构建了您需要的一切。
+  想为我们尚未正式支持的平台构建 Pushbullet 客户端吗？你需要的一切都在这里。
+  在家庭自动化系统上工作？Pushbullet 可以让一切都在聊天。
+  使用传感器并想要将消息发送到另一台设备？Pushbullet 正是您所需要的。
+  管理 IT / 服务器并希望获得更新和警报，无论您身在何处或使用何种设备？Pushbullet 让它变得简单。

[查看此 ProgrammableWeb 文章，了解有关 Pushbullet 和此 API 的更多介绍](http://www.programmableweb.com/news/pushbullet-releases-new-and-improved-api/2014/05/21)。

![img](https://docs.pushbullet.com/fleur.png)

### [第](https://docs.pushbullet.com/#sections)

+  [API](https://docs.pushbullet.com/#api-quick-start) - 使用 Pushbullet 服务器发送 / 接收推送。
+  [iPhone 扩展程序](https://docs.pushbullet.com/#iphone-extensions) - 通过您的应用程序或网页与 iPhone 应用程序进行交互。
+  [更改日志](https://docs.pushbullet.com/#changelog) - API 的最新更改。

### [问题 / 意见](https://docs.pushbullet.com/#problemsfeedback)

如果您有任何疑问，请随意将它们发布到 [Stack Overflow 上](http://stackoverflow.com/questions/tagged/pushbullet)的[pushbullet标签](http://stackoverflow.com/questions/tagged/pushbullet)。我们监控此标签并尽快回复。

对于其他一切（包括不正确的事情或对这些文档的建议更改），请随时通过[api@pushbullet.com](mailto:api@pushbullet.com)与我们联系。

![img](https://docs.pushbullet.com/fleur.png)

# [ API 快速入门](https://docs.pushbullet.com/#api-quick-start)

我们的所有示例都使用大多数系统上已有的curl命令行工具。

+  如果你使用 Mac，它应该已经安装，只需打开终端应用程序并运行它。
+  如果您使用的是 Linux，则应该已经安装，只需打开控制台并运行它即可。
+  在 Windows 上，您必须在[此处](https://docs.pushbullet.com/curl_745_0_ssl.zip)或从[curl 下载页面](http://curl.haxx.se/download.html#Win32)下载它。

Pushbullet API 允许您发送 / 接收推送，并执行官方 Pushbullet 客户端可以执行的所有操作。要访问 API，您需要一个访问令牌，以便服务器知道您是谁。您可以从 “ [帐户设置”](https://www.pushbullet.com/#settings/account)页面获取一个。

获得该访问令牌后，您可以使用它来使用 Pushbullet API 访问您的 Pushbullet 帐户：

######  示例：获取当前用户

 请求

```
curl --header'访问令牌：<your_access_token_here>'\
     https://api.pushbullet.com/v2/users/me
```

 响应

```
{ 
  “创造” ： 1.381092887398433e + 09 ，
  “电子邮件” ： “ elon@teslamotors.com ” ，
  “email_normalized” ：“  elon@teslamotors.com ” ，“鉴定者” ：“ujpah72o0” ，“图片网址” ：“HTTPS：/ /static.pushbullet.com/missing-image/55a7dc-45" ，“max_upload_size” ：2.62144e + 07 ，“修饰的” ：1.441054560741007e + 09 ，“姓名” ：“伊隆麝香” }
   
   
   
   
   
```

# [ API 概述](https://docs.pushbullet.com/#api-overview)

## [ 要求](https://docs.pushbullet.com/#requests)

API 通过https://api.pushbullet.com接受 HTTPS 请求。所有 POST 请求必须使用[JSON](http://en.wikipedia.org/wiki/JSON)正文，并将 Content-Type 标头设置为application / json。大多数编程语言都有一些方法将对象编码为 JSON，建议使用内置库，因为它可以正确处理换行符和引号。

#### [ 认证](https://docs.pushbullet.com/#authentication)

要对 API 进行身份验证，请在Access-Token：<your_access_token_here>等标头中使用您的访问令牌。您可以在 “ [帐户设置”](https://www.pushbullet.com/#settings)页面上找到您的访问令牌。请注意，此密钥可以完全访问您的帐户，因此请勿将其全部发布到互联网上。

如果您创建的应用程序代表其他用户使用 Pushbullet API（例如，以该用户身份发送推送通知），请使用[OAuth](https://docs.pushbullet.com/#oauth)获取该用户的访问令牌。在开发过程中使用您自己的访问令牌可以使您不必在以后设置 OAuth。

您可以从任何应用程序发出请求，但如果您这样做可能取决于您是在编写脚本还是使用编程语言。如果您有终端和[curl](http://curl.haxx.se/download.html)实用程序，则可以从命令行执行请求。

######  示例：获取当前用户

 请求

```
curl --header'访问令牌：<your_access_token_here>'\
     https://api.pushbullet.com/v2/users/me
```

 响应

```
{ 
  “创造” ： 1.381092887398433e + 09 ，
  “电子邮件” ： “ elon@teslamotors.com ” ，
  “email_normalized” ：“  elon@teslamotors.com ” ，“鉴定者” ：“ujpah72o0” ，“图片网址” ：“HTTPS：/ /static.pushbullet.com/missing-image/55a7dc-45" ，“max_upload_size” ：2.62144e + 07 ，“修饰的” ：1.441054560741007e + 09 ，“姓名” ：“伊隆麝香” }
   
   
   
   
   
```

因为我们允许 CORS 请求，所以您可以从任何浏览器发出请求（您可以点击运行按钮或将此代码复制并粘贴到您的 javascript 控制台中）：

## [ 回应](https://docs.pushbullet.com/#responses)

响应总是[JSON](http://en.wikipedia.org/wiki/JSON)。密钥要么存在非空值，要么完全不存在于响应中。空值为：null，false，“”，[]和{}。 [删除的对象](https://docs.pushbullet.com/#deleted-objects)将仅具有标识，活动，创建和修改的键，因为已删除所有其他属性并且现在为空值。

###### [示例：API 响应](https://docs.pushbullet.com/#example-api-response)

```
{ 
  “创造” ： 1.35794175382879e + 09 ，
  “电子邮件” ： “ elon@teslamotors.com ” ，
  “email_normalized” ：“  elon@teslamotors.com ” ，“iDEN的” ：“ujpah72o0sjAoRtnM0jc” ，“修饰的” ：1.39932599218423e + 09 }
   
   
```

#### [ HTTP 状态代码](https://docs.pushbullet.com/#http-status-codes)

+  200 OK - 一切都按预期工作。
+  400 错误请求 - 通常这是因为缺少必需参数。
+  401 Unauthorized - 未提供有效的访问令牌。
+  403 Forbidden - 访问令牌对该请求无效。
+  404 Not Found - 请求的项目不存在。
+  429 请求太多 - 您对服务器发出过多请求的速度[有限](https://docs.pushbullet.com/#ratelimiting)。
+  5XX 服务器错误 - 在 Pushbullet 方面出现问题。如果此错误来自中间服务器，则它可能不是有效的 JSON。

#### [ 错误](https://docs.pushbullet.com/#errors)

错误响应（任何非 200 错误代码）包含有关发生的错误类型的信息。响应 JSON 将具有包含以下字段的error属性：

+  type - 引用此类错误的机器可读代码。无论是INVALID_REQUEST的客户端错误或服务器对服务器端错误。
+  消息 - （大多数）人类可读的错误消息。
+  param - （可选）有时在 invalid_request 错误期间出现，说明请求中的哪个参数导致错误。
+  cat - 某种 ASCII cat 来抵消接收错误消息的痛苦。

###### [ 示例：错误响应](https://docs.pushbullet.com/#example-error-response)

```
{ 
  “error” ： { 
    “cat” ： “〜（= ^‥^）” ，
    “message” ： “无法找到资源。” ，
    “type” ： “invalid_request” 
  } 
}
```

Pushbullet 服务器的错误将具有此 JSON 主体。中间服务器或托管基础结构的错误可能不会，因此您应该能够将非 JSON 响应作为一般错误处理。

## [ 对象](https://docs.pushbullet.com/#objects)

可以创建，修改，列出和删除对象（例如[推送](https://docs.pushbullet.com/#push)和[设备](https://docs.pushbullet.com/#device)）。

对象上出现的所有时间戳都是自纪元以来的浮点秒，也称为[Unix 时间](http://en.wikipedia.org/wiki/Unix_time)。

对列表对象的所有调用（list- *）都接受active，limit和cursor参数。

#### [ 引导](https://docs.pushbullet.com/#bootstrapping)

默认情况下，列出任何类型的对象都将返回已删除的对象（这对于同步很有用）。当您获得初始对象列表时，您可能只想获取活动对象列表。要仅获取活动对象，请在请求中将active设置为true。

#### [ 分页](https://docs.pushbullet.com/#pagination)

列出对象时，如果在响应中收到游标，则表示结果在多个页面上。要请求下一页结果，请在下一个请求中将此光标用作参数光标。每次列出对象集合时，它们可能是多个页面（对象总是先返回最新的对象）。您可以在任何返回对象列表的调用上指定limit参数，以在每个页面上获得较少数量的对象。默认（最大）限制为 500，包括已删除的对象。

#### [ 同步变更](https://docs.pushbullet.com/#syncing-changes)

对列表对象的所有调用都接受modified_after属性（[时间戳](http://en.wikipedia.org/wiki/Unix_time)）。将返回自该时间以来修改的任何对象，最近最先修改。该modified_after参数应该是最新的修改从服务器返回的对象值（不信任本地计算机的时间戳，因为它通常是不一样的值作为服务器）。

#### [ 删除的对象](https://docs.pushbullet.com/#deleted-objects)

当您使用modified_after时间戳查询以将更改的对象同步到设备时，您需要知道对象是否已被删除，以便您可以在本地删除它。已删除的对象将具有active = false，并且返回的对象中将缺少除iden，created，modified和active之外的所有属性。列出对象时，默认情况下会显示已删除的对象。

#### [ 调整图像大小](https://docs.pushbullet.com/#resizing-images)

[推送](https://docs.pushbullet.com/#push)具有image_url属性，可以通过设置查询参数来调整其大小。要使用此功能，请将= s <pixels>添加到网址的末尾。

###### [示例：调整图像大小](https://docs.pushbullet.com/#example-resize-an-image)

调整图像大小，使最长边不超过 100 像素

之前



[https://lh3.googleusercontent.com/kR7yrU5ioduH9D0LGM1qr6GAPxFv6gybYmIvQwxwhvIkDj_hJA1GrwP4pqOn5wW5Hawp-kvNGWEHch4AAo6aiUGcug
![img](https://lh3.googleusercontent.com/kR7yrU5ioduH9D0LGM1qr6GAPxFv6gybYmIvQwxwhvIkDj_hJA1GrwP4pqOn5wW5Hawp-kvNGWEHch4AAo6aiUGcug)](https://lh3.googleusercontent.com/kR7yrU5ioduH9D0LGM1qr6GAPxFv6gybYmIvQwxwhvIkDj_hJA1GrwP4pqOn5wW5Hawp-kvNGWEHch4AAo6aiUGcug)

后



[https://lh3.googleusercontent.com/kR7yrU5ioduH9D0LGM1qr6GAPxFv6gybYmIvQwxwhvIkDj_hJA1GrwP4pqOn5wW5Hawp-kvNGWEHch4AAo6aiUGcug=s100
![img](https://lh3.googleusercontent.com/kR7yrU5ioduH9D0LGM1qr6GAPxFv6gybYmIvQwxwhvIkDj_hJA1GrwP4pqOn5wW5Hawp-kvNGWEHch4AAo6aiUGcug=s100)](https://lh3.googleusercontent.com/kR7yrU5ioduH9D0LGM1qr6GAPxFv6gybYmIvQwxwhvIkDj_hJA1GrwP4pqOn5wW5Hawp-kvNGWEHch4AAo6aiUGcug=s200)

该IMAGE_URL应该与结尾的域名托管.googleusercontent.com。如果域不以此结束，则不应尝试使用查询参数调整图像大小。除了推送之外的对象具有image_url属性，但它们不一定以相同的方式调整大小。

### [ 向后兼容性](https://docs.pushbullet.com/#backwards-compatibility)

我们尝试仅对现有的公共 API 调用进行向后兼容的更改。这意味着我们不应该更改现有调用的含义，并且我们只会添加而不是从 API 返回的对象中删除键。添加密钥被认为是向后兼容的更改。

### [ 范围](https://docs.pushbullet.com/#limits)

#### [Ratelimiting](https://docs.pushbullet.com/#ratelimiting)

当您向 API 发出请求时，您将在响应中收到以下标题：

```
X-Ratelimit-Limit：32768
X-Ratelimit-Remaining：32765
X-Ratelimit-Reset：1432447070
```

这些告诉你速率限制是什么，剩余多少以及何时重置（[Unix 时间内的](http://en.wikipedia.org/wiki/Unix_time)整数秒）。这些单位是一种通用的 “成本” 数字。请求成本为 1，数据库操作成本为 4. 因此，读取 500 会导致成本大约为 500 个数据库操作 + 1 个请求 = 500 * 4 + 1 = 2001. 您可以通过更改X-Ratelimit-Remaining来查看请求的成本。两个请求。

#### [推极限](https://docs.pushbullet.com/#push-limit)

免费帐户（没有专业版订阅）每月限制为 500 次推送。在发送推送时，结束将导致错误。

![img](https://docs.pushbullet.com/fleur.png)

# [ 指南](https://docs.pushbullet.com/#guides)

## [ 的 OAuth2](https://docs.pushbullet.com/#oauth2)

### [概观](https://docs.pushbullet.com/#overview)

OAuth 允许您访问用户的 Pushbullet 帐户，或者使用浏览器通过他们的 Pushbullet 帐户进行身份验证。

OAuth 是大多数网站使用的标准身份验证程序，以下是它的工作原理：

1. 您，应用开发者，使用 Pushbullet [注册您的应用](https://www.pushbullet.com/create-client)（称为 “OAuth 客户端”）
2. 使用您在应用程序中生成的 URL（您可以在 “ [创建客户端”](https://www.pushbullet.com/create-client)页面上看到示例），将用户发送到 Pushbullet 站点。网址的一个参数是重定向网址，用户在完成授权您的应用时将被发送到该网址。
3. 用户通过单击 “允许” 按钮来授权您的应用程序。
4. 用户被重定向到您之前提供的重定向网址，通常是您的网站或您的应用。

以下是图片的粗略表现：

[![img](https://docs.pushbullet.com/oauth.png)](https://docs.pushbullet.com/oauth.png)

### [入门](https://docs.pushbullet.com/#getting-started)

首先，在[Create Client](https://www.pushbullet.com/create-client)页面上创建一个客户端（注册您的应用程序）。对于此页面上的示例，客户端如下所示：

##### 示例客户端

```
{ 
  “CLIENT_ID” ： “YW7uItOzxPFx8vJ4” ，
  “client_secret” ： “MmA98EDg0pjr4fZw” ，“
  鉴定者” ： “ujpah72o0sjAoRtnM0jc” ，“
  图片网址” ： “http://www.catpusher.com/logo.png” ，“
  名” ： “ Cat Pusher“ ，
  ”redirect_uri“ ： ”http://www.catpusher.com/auth_complete“ ，
  ”website_url“ ： ”http://www.catpusher.com“ 
}
```

### [获取访问令牌](https://docs.pushbullet.com/#getting-an-access-token)

创建客户端后，您可以使用以下参数将用户发送到<https://www.pushbullet.com/authorize>：

+  client_id - client_id来注册您的客户端
+  redirect_uri - 授权完成后要将用户重定向到的 URL。路径部分必须与为客户端提供的路径部分匹配，可以动态设置查询字符串。
+  response_type - “代码”（如果您有服务器）或 “令牌”（如果您的应用完全在客户端上）

##### 示例网址

```
https://www.pushbullet.com/authorize?client_id=YW7uItOzxPFx8vJ4&redirect_uri=http%3A%2F%2Fwww.catpusher.com%2Fauth_complete&response_type=code
```

注意：您的应用的 “ [创建客户端”](https://www.pushbullet.com/create-client)页面上有一个示例 url（“oauth test url”）。

当用户被发送到此页面时，他们可以授权或拒绝您的应用程序。如果他们选择拒绝，他们会被重定向到 redirect_uri，参数为 “error = access_denied”。

如果他们选择授权，则有两个可能的后续步骤，具体取决于 response_type 的值：

#### [对于客户端应用程序：response_type = token](https://docs.pushbullet.com/#for-client-side-apps-responsetypetoken)

用户被重定向到 redirect_uri，其 url 片段为 “access_token = <access_token>”。如果您有运行嵌入式 Web 浏览器的客户端应用程序，则可以将 redirect_uri 配置为 “https://www.pushbullet.com/login-success”，然后在授权调用中使用此 redirect_uri。

##### 示例网址

```
https://www.pushbullet.com/authorize?client_id=YW7uItOzxPFx8vJ4&redirect_uri=https%3A%2F%2Fwww.pushbullet.com%2Flogin-success&response_type=token
```

##### 示例重定向

```
https://www.pushbullet.com/login-success#access_token=o.RUe7IZgC6384GrI1
```

#### [对于具有服务器的应用程序：response_type = code](https://docs.pushbullet.com/#for-apps-with-servers-responsetypecode)

如果您有服务器，则可以使用此 response_type，它可能比客户端更安全，因为客户端永远不会看到实际的访问令牌。在此模式下，用户将使用参数 “code = <code>” 重定向到 redirect_uri。

##### 示例网址

```
https://www.pushbullet.com/authorize?client_id=YW7uItOzxPFx8vJ4&redirect_uri=http%3A%2F%2Fwww.catpusher.com%2Fauth_complete&response_type=code
```

##### 示例重定向

```
http://www.catpusher.com/auth_complete?code=RUe7IZgC6384GrI1
```

然后，您的服务器使用以下参数将 POST 请求发送到<https://api.pushbullet.com/oauth2/token>：

+  grant_type - 设置为 “authorization_code”
+  client_id - client_id来注册您的客户端
+  client_secret - client_secret来注册您的客户端
+  代码 - 重定向的代码

######  示例：将代码转换为访问令牌

 请求

```
curl --header'访问令牌：<your_access_token_here>'\
     --header'Content-Type：application / json'\
     --data-binary'{“client_id”：“YW7uItOzxPFx8vJ4”，“client_secret”：“MmA98EDg0pjr4fZw”，“code”：“RUe7IZgC6384GrI1”，“grant_type”：“authorization_code”}'
     --request POST \
     https://api.pushbullet.com/oauth2/token
```

 响应

```
{ 
  “access_token” ： “a6FJVAA0LVJKrT8k” ，
  “token_type” ： “Bearer” 
}
```

如果需要为请求存储额外状态，可以在 redirect_uri 的末尾添加额外的查询参数。例如，如果您将客户端的redirect_uri设置为http://www.catpusher.com/auth_complete，那么当您构建将用户发送到 Pushbullet 的 URL 时，您可以指定redirect_uri = http：//www.catpusher.com / auth_complete？state = zhk2KJ3SAAS3q1。当用户完成授权您的应用程序时，他们最终会访问http://www.catpusher.com/auth_complete?state=zhk2KJ3SAAS3q1&code=RUe7IZgC6384GrI1。

### [使用您的访问令牌](https://docs.pushbullet.com/#using-your-access-token)

现在您已拥有访问令牌，您可以以该用户身份访问 Pushbullet。只需将access_token与您的请求一起包含在 HTTP Basic Auth 中作为用户名，或者将Access-Token标头设置为access_token。确保将access_token保存在安全的地方，它允许访问您的用户帐户！

######  示例：获取当前用户

 请求

```
curl --header'访问令牌：<your_access_token_here>'\
     https://api.pushbullet.com/v2/users/me
```

 响应

```
{ 
  “创造” ： 1.381092887398433e + 09 ，
  “电子邮件” ： “ elon@teslamotors.com ” ，
  “email_normalized” ：“  elon@teslamotors.com ” ，“鉴定者” ：“ujpah72o0” ，“图片网址” ：“HTTPS：/ /static.pushbullet.com/missing-image/55a7dc-45" ，“max_upload_size” ：2.62144e + 07 ，“修饰的” ：1.441054560741007e + 09 ，“姓名” ：“伊隆麝香” }
   
   
   
   
   
```

该的 access_token没有一组到期时间，但可能会在未来的某个时候到期。如果删除客户端，则所有现有令牌都将失效。

![img](https://docs.pushbullet.com/fleur.png)

## [ 端到端加密](https://docs.pushbullet.com/#end-to-end-encryption)

我们支持[通知镜像，通用复制和粘贴以及 SMS](https://blog.pushbullet.com/2015/08/11/end-to-end-encryption/)的端到端加密。我们使用客户端对称加密。没有密钥被发送到服务器，甚至没有公钥，这从安全的角度来看特别好。

加密主要用于[短暂的](https://docs.pushbullet.com/#ephemerals)。如果在 Pushbullet 客户端中启用它，则只要使用支持端到端加密的任何功能，就应该能够在[流](https://docs.pushbullet.com/#stream)上看到加密消息。

#### [ 密钥生成](https://docs.pushbullet.com/#key-generation)

密钥是从用户提供的密码创建的，并通过

PBKDF2

传递：

+  伪随机函数：[HMAC-SHA256](https://en.wikipedia.org/wiki/Hash-based_message_authentication_code)
+  密码：用户提供的用于加密的密码在用户拥有的所有 Pushbullet 设备上必须相同
+  Salt：当前用户的用户标识，例如up0snaKOsn
+  迭代次数：30,000
+  派生密钥长度：256 位

###### [ 代码示例：生成加密 / 解密密钥](https://docs.pushbullet.com/#code-sample-generate-an-encryptiondecryption-key)

此示例使用 javascript [Forge 库](https://github.com/digitalbazaar/forge)





var  pseudorandom_function  **=**  forge 。md 。sha256 。create （）;

var  password  **=**  “hunter2” ;

var  salt  **=**  “up0snaKOsn” ;

var  iterations  **=**  30000 ;

var  derived_key_length_bytes  **=**  32 ;  // 256 位

var  key  **=**  forge 。pkcs5 。pbkdf2 （

  密码，

  盐，

  迭代，

  derived_key_length_bytes ，

  pseudorandom_function

)

// 编码到 base64，这样我们就可以轻松打印密钥了

//（通常是二进制，无法打印）

var  base64_key  **=**  btoa （key ）;

控制台。log （“base64_key：” ， base64_key ）;









跑

#### [ 加密](https://docs.pushbullet.com/#encryption)

要加密消息，请使用[AES-256](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)和[GCM 身份验证](https://en.wikipedia.org/wiki/Galois/Counter_Mode)。AES-256 使用 PBKDF2 输出的 256 位密钥。要加密，您需要生成一个 96 位的初始化向量（这用于启动加密过程，这不是秘密）。带有 GCM 的 AES-256 输出将是加密消息（任意长度）和 128 位标记。此加密邮件的编码如下所示：

```
encoded_message =“1”+ tag + initialization_vector + encrypted_message
```

的1 个前缀是指示编码的版本的版本号。当encoded_message被放入 JSON 时，它必须是[base64 编码的，](https://en.wikipedia.org/wiki/Base64)因为 JSON 无法处理二进制数据。

###### [ 代码示例：加密消息](https://docs.pushbullet.com/#code-sample-encrypt-a-message)

此示例使用 javascript [Forge 库](https://github.com/digitalbazaar/forge)





// 将密钥从 base64 转换为二进制

VAR  键 **=**  细胞（“1sW28zp7CWv5TtGjlQpDHHG4Cbr9v36fG5o4f74LsKg =” ）;

var  initialization_vector  **=**  forge 。随机的。getBytes （12 ）;  // 96 位

var  message  **=**  “喵！” ;



var  cipher  **=**  forge 。密码。createCipher （'AES-GCM' ， key ）;

密码。start （{ “iv” ： initialization_vector }）;

密码。更新（伪造。UTIL 。createBuffer （伪造。UTIL 。encodeUtf8 （消息）））;

密码。完成（）;



var  tag  **=**  cipher 。模式。标签。getBytes （）;

var  encrypted_message  **=**  cipher 。输出。getBytes （）;



var  encoded_message  **=**  “1”  **+**  tag  **+**  initialization_vector  **+**  encrypted_message ;

var  base64_encoded_message  **=**  btoa （encoded_message ）;

控制台。log （“base64_encoded_message：” ， base64_encoded_message ）;









跑

#### [ 解密](https://docs.pushbullet.com/#decryption)

如果您可以加密邮件，则解密邮件非常简单。您需要将encoded_message解码为标记，initialization_vector和encrypted_message。

###### [ 代码示例：解密加密的消息](https://docs.pushbullet.com/#code-sample-decrypt-an-encrypted-message)

此示例使用 javascript [Forge 库](https://github.com/digitalbazaar/forge)





VAR  键 **=**  细胞（“1sW28zp7CWv5TtGjlQpDHHG4Cbr9v36fG5o4f74LsKg =” ）;

VAR  encoded_message  **=**  细胞（“MSfJxxY5YdjttlfUkCaKA57qU9SuCN8 + ZhYg / xieI + lDnQ ==” ）;



var  version  **=**  encoded_message 。SUBSTR （0 ， 1 ）;

var  tag  **=**  encoded_message 。SUBSTR （1 ， 16 ）;  // 128 位

var  initialization_vector  **=**  encoded_message 。SUBSTR （17 ， 12 ）;  // 96 位

var  encrypted_message  **=**  encoded_message 。substr （29 ）;



**if**  （version  **！=**  “1” ） {

  **抛出** “无效版本”

}



var  decipher  **=**  forge 。密码。createDecipher （'AES-GCM' ， key ）;

破译。开始（{

​    'iv' ： initialization_vector ，

​    ' 天 ' ： 天

});

破译。更新（伪造。UTIL 。createBuffer （encrypted_message ））;

破译。完成（）;



var  message  **=**  decipher 。输出。toString （'utf8' ）;

控制台。log （“message：” ， message ）;

​    









跑

确保您的加密库使用错误的标记检查标记参数的有效性，并验证您是否收到某种错误。您还必须丢弃任何不带前缀 1 的encoded_message，因为将来这些编码将是不同的，不兼容的编码。

#### [ 加密短暂格式](https://docs.pushbullet.com/#encrypted-ephemeral-format)

一个看起来像这样的短暂：

```
{ 
  “push” ： { 
    “data” ： { 
      “key1” ： “value1” ，
      “key2” ： “value2” 
    } 
  } ，
  “type” ： “push” 
}
```

加密时会看起来像这样：

```
{ 
  “push” ： { 
    “ciphertext” ： “MXAdvN64uXWtLXCRaqYHEtGhiogR1VHyXX21Lpjp4jv3v + JWygMBA9Wp5npbQdfeZAgOZI + JT3y3pbmq + OrKXrK1rg ==” ，
    “encrypted” ： true 
  } ，
  “type” ： “push” 
}
```

当密文是base64_encoded_message从[加密的例子](https://docs.pushbullet.com/#encryption-example)。

如果您解码密文，那么您将获得以下 javascript 对象：

```
{ 
  “key1” ： “value1” ，
  “key2” ： “value2” 
}
```

![img](https://docs.pushbullet.com/fleur.png)

# [ 实时事件流](https://docs.pushbullet.com/#realtime-event-stream)

### 连接到流

您可以通过创建安全的 websocket 连接（wss：//）来连接到 websocket 以获取帐户 wss：//stream.pushbullet.com/websocket/ <your_access_token_here>

**直播 jsFiddle 示例**

连接后，如果发送任何[短暂](https://docs.pushbullet.com/#ephemerals)或[推送](https://docs.pushbullet.com/#push)，您将定期看到type =“nop”消息以及其他类型的消息。

#### 流消息

所有消息都是带有类型键的[JSON](http://en.wikipedia.org/wiki/JSON)对象。

#### 类型

+  type =“nop” - 每 30 秒发送一次，确认连接处于活动状态。

+  type =“tickle”

    \- 告诉你服务器上有什么变化。该

   子类型

   属性告诉你发生了什么变化。

   +  subtype =“push” - 更改 /v2 / 推送资源。
   +  subtype =“device” - 对 /v2 /devices 资源的更改。

+  type =“push” - 一个新的推动。推送数据是在从一个对象可用的推键。注意：这仅用于[Ephemerals](https://docs.pushbullet.com/#ephemerals)（例如镜像通知）而不是正常推送（例如您看到的那些）[list-pushes](https://docs.pushbullet.com/#list-pushes)）。正常推送仅产生痒，而不是这些消息。

##### 示例消息

```
{ 
  “type” ： “nop” 
}
{ 
  “subtype” ： “push” ，
  “type” ： “tickle” 
}
{ 
  “push” ： { 
    “cat” ： “meow” 
  } ，
  “type” ： “push” 
}
```

#### 推送消息类型

与消息类型 =“推”将包含由密钥映射到数据对象推。此处根据其内部类型记录此对象。

+  type =“mirror” - 此推送是从 Android 设备镜像的通知。
+  type =“dismissal” - 此推送是通知的解雇消息。

##### 示例通知镜像

```
{ 
  “push” ： { 
    “application_name” ： “Pushbullet” ，
    “body” ： “如果你在计算机上看到这个，镜像正在运行！\ n” ，
    “已创建” ： 1.39935096416497e + 09 ，
    “dismissable” ： true ，
    “icon” ： “iVBORw0KGgoAAAANSUhEBgUzC42AAAADNElEQVRo \ ng == \ n” ，
    “ iden” ： “1e443556ba3217c” ，
    “notification_id” ： “ -  8” ，
    “notification_tag” ： null ，
    “package_name” ： “com.pushbullet.android” ，
    “receiver_email” ： “ elon @teslamotors.com ” ，
    “receiver_email_normalized” ： “ elon @teslamotors.com ” ，
    “receiver_iden” ： “ujpah72o0” ，
    “sender_email” ： “ elon @teslamotors.com ” ，
    “sender_email_normalized” ： “ elon @ teslamotors.com “ ，
    ”sender_iden“ ： ”ujpah72o0“ ，
    ”source_device_iden“ ： ”ujpah72o0sjAoRtnM0jc“ ，
    ”标题“ ： ”镜像测试“ ，
    ”类型“ ： “镜子” 
  } ，
  “类型” ： “推” 
}
```

##### 示例通知解除

```
{ 
  “push” ： { 
    “created” ： 1.39935096622458e + 09 ，
    “ iden ” ： “1e443556ba3217c” ，
    “notification_id” ： “ -  8” ，
    “notification_tag” ： null ，
    “package_name” ： “com.pushbullet.android” ，
    “receiver_email” ： “ elon@teslamotors.com ” ，
    “receiver_email_normalized” ： “ elon @teslamotors.com ” ，
    “receiver_iden” ： “ujpah72o0“ ，
    ”sender_email“ ： ”elon@teslamotors.com “ ，
    ”sender_email_normalized“ ： ” elon @teslamotors.com “ ，
    ”sender_iden“ ： ”ujpah72o0“ ，
    ”source_device_iden“ ： ”ujpah72o0sjAoRtnM0jc“ ，
    ”type“ ： ”dismissal“ 
  } ，
  ”type“ ： ”push“ “ 
}
```

### 反应痒痒

当您收到挠痒信息时，表示类型子类型的资源已更改。这是您更新该资源的提示。这是推送类型的示例：

收到此消息后：

```
{ 
  “subtype” ： “push” ，
  “type” ： “tickle” 
}
```

请求自上次收到它们以来发生过更改的推送：

```
获取 https://api.pushbullet.com/v2/pushes?modified_after=1399008037.849
```

然后将这些更新合并到推送历史的本地副本中。

**注意：**在发出更新请求时，最好使用最近修改的本地推送修改时间戳。这将使响应保持小而快。此外，不要信任本地计算机的当前时间戳，因为它不可避免地与服务器的时间戳不同。使用您在推送对象上看到的最新时间戳。由于推送是在最近修改的第一次返回时返回的，因此这将是您从任何调用中获得的第一次推送[列表推送](https://docs.pushbullet.com/#list-pushes)。

![img](https://docs.pushbullet.com/fleur.png)

# [ 短命植物](https://docs.pushbullet.com/#ephemerals)

您可以向帐户中的所有设备发送名为 “ephemerals” 的任意 JSON 消息。短暂存储的时间很短（如果有的话）并直接发送到设备。因为它们是直接发送的，所以没有像创建或更新推送或其他对象那样的 “痒” 消息，JSON 消息直接出现在流中。

Pushbullet 应用程序使用短暂的通知镜像和通用复制 / 粘贴。

与某些其他 HTTP 端点不同，由于其 JSON 结构，不支持短暂的 POST 参数。

### 发送一个短暂的

#### 参数

+  type - 必须设置为push，这是目前唯一的短暂类型。
+  push - 任意 JSON 对象。

######  示例：发送短暂的

 请求

```
curl --header'访问令牌：<your_access_token_here>'\
     --header'Content-Type：application / json'\
     --data-binary'{“push”：{“cat”：“meow”}，“type”：“push”}'\
     --request POST \
     https://api.pushbullet.com/v2/ephemerals
```

 响应

```
{}
```

除非出现错误，否则 Ephemerals 会使用空 JSON 对象进行响应。

## [ 发送短信](https://docs.pushbullet.com/#send-sms)

您可以通过向手机发送短暂消息来发送手机短信。

#### 短信短暂

+  type - 推送发送短信。

+  推送

    \- 有关要发送的 SMS 的信息

   +  type - messaging_extension_reply用于发送 SMS。
   +  package_name - com.pushbullet.android用于发送短信
   +  source_user_iden - 发送此消息的用户的用户标识。
   +  target_device_iden - 与应发送 SMS 的电话对应的设备的标识。
   +  conversation_iden - 发送短信的电话号码。
   +  message - 要发送的 SMS 消息。

##### 例

```
{ 
  “push” ： { 
    “conversation_iden” ： “+1 303 555 1212” ，
    “message” ： “你好！” ，
    “package_name” ： “com.pushbullet.android” ，
    “source_user_iden” ： “ujpah72o0” ，
    “target_device_iden” ： “ujpah72o0sjAoRtnM0jc” ，
    “type” ： “messaging_extension_reply” 
  } ，
  “type” ： “push” 
}
```

## [ 镜像通知](https://docs.pushbullet.com/#mirrored-notifications)

镜像通知是从 Android 设备（当前是镜像通知的唯一来源）发送到其他设备的通知。要测试这些，您可以进入 Android 应用程序的设置屏幕，并在收听流时点击 “发送测试通知” 按钮。

### [通知短暂](https://docs.pushbullet.com/#notification-ephemeral)

+  type - 推送镜像通知。

+  推送

    \- 有关通知的信息

   +  型 - 反射镜对镜像通知。
   +  icon - [Base64](http://en.wikipedia.org/wiki/Base64)编码的 JPEG 图像，用作推送的图标。
   +  title - 通知的标题。
   +  body - 通知的正文。
   +  source_user_iden - 发送此消息的用户的用户标识。
   +  source_device_iden - 发送此消息的设备的标识。
   +  application_name - 创建通知的应用程序的名称。
   +  不允许 - 如果通知可以被驳回，则为真。
   +  package_name - 发出通知的包，用于更新 / 解除现有通知。
   +  notification_id - 更新 / 解除现有通知时使用的通知 ID。
   +  notification_tag - 更新 / 解除现有通知时使用的通知标记。
   +  has_root - 手机已植根。
   +  client_version - 发送此消息的应用程序的客户端版本。

##### 例

```
{ 
  “push” ： { 
    “application_name” ： “Pushbullet” ，
    “body” ： “如果你在计算机上看到这个，Android到PC通知正在运行！\ n” ，
    “client_version” ： 125 ，
    “dismissable” ： true ，
    “has_root” ： false ，
    “icon” ： “（base64_encoded_jpeg）” ，
    “notification_id” ： “ -  8” ，
    “notification_tag” ： null ，
    “package_name” ： “com.pushbullet.android” ，
    “source_device_iden”： “ujpah72o0sjAoRtnM0jc” ，
    “source_user_iden” ： “ujpah72o0” ，
    “title” ： “镜像测试” ，
    “类型” ： “镜像” 
  } ，
  “类型” ： “推送” 
}
```

### [解雇短暂](https://docs.pushbullet.com/#dismissal-ephemeral)

+  type - “推”通知解雇。

+  推

    \- 关于解雇的信息。

   +  类型 - 通知解雇的“解雇”。
   +  package_name - 设置为镜像通知的package_name字段。
   +  notification_id - Set to the notification_id field from the mirrored notification.
   +  notification_tag - Set to the notification_tag field from the mirrored notification.
   +  source_user_iden - Set to the source_user_iden field from the mirrored notification.

##### EXAMPLE

```
{ 
  “push” ： { 
    “notification_id” ： “ -  8” ，
    “notification_tag” ： null ，
    “package_name” ： “com.pushbullet.android” ，
    “source_user_iden” ： “ujpah72o0” ，
    “type” ： “dismissal” 
  } ，
  “type” ： “push” 
}
```

######  示例：解除通知

 请求

```
curl --header'访问令牌：<your_access_token_here>'\
     --header'Content-Type：application / json'\
     --data-binary'{“push”：{“notification_id”：“ -  8”，“notification_tag”：null，“package_name”：“com.pushbullet.android”，“source_user_iden”：“ujpah72o0”，“type” ：“解雇”}，“类型”：“推”}'\
     --request POST \
     https://api.pushbullet.com/v2/ephemerals
```

 响应

```
{}
```

## [ 通用复制 / 粘贴](https://docs.pushbullet.com/#universal-copypaste)

Pushbullet 应用程序可以监控剪贴板并在每次用户复制新文本选择时发送消息，将其发送到所有用户的设备，可以将其复制到系统剪贴板或以其他方式提供给用户。

#### 将字符串复制到剪贴板

#### 属性

+  type - 推送剪贴板消息。

+  push

    \- 有关剪贴板消息的信息。

   +  type - 剪贴板消息的剪辑。
   +  body - 要复制到剪贴板的文本。
   +  source_user_iden - 发送此消息的用户的标识。
   +  source_device_iden - 发送此消息的设备的标识。

#### 例

```
{ 
  “push” ： { 
    “body” ： “http://www.google.com” ，
    “source_device_iden” ： “ujpah72o0sjAoRtnM0jc” ，
    “source_user_iden” ： “ujpah72o0” ，
    “type” ： “clip” 
  } ，
  “type” ： “推” 
}
```

######  示例：发送剪贴板内容

 请求

```
curl --header'访问令牌：<your_access_token_here>'\
     --header'Content-Type：application / json'\
     --data-binary'{“push”：{“body”：“http://www.google.com”，“source_device_iden”：“ujpah72o0sjAoRtnM0jc”，“source_user_iden”：“ujpah72o0”，“type”：“clip “}，”类型“：”推“}'\
     --request POST \
     https://api.pushbullet.com/v2/ephemerals
```

 响应

```
{}
```

![img](https://docs.pushbullet.com/fleur.png)

# [ iPhone 扩展程序](https://docs.pushbullet.com/#iphone-extensions)

### [ Pushbullet URL Handler](https://docs.pushbullet.com/#pushbullet-url-handler)

iPhone 应用程序有一个 url 处理程序，pushbullet：//可用于组合推送，如下所示：

```
  pushbullet：//排版=笔记和身体=你好
```

compose是目前唯一的选择，但可以构造一些推送类型（确保 urlencode 任何参数）：

```
  pushbullet：// compose？type = link＆url = https％3A％2F％2Fwww.pushbullet.com 
  pushbullet：// compose？type = address＆address = 850％20Bryant％20St
```

现在只支持type =“note”和type =“link”（它们的参数与 in 中相同）[create-push](https://docs.pushbullet.com/#create-push)）。

### [ 在 Pushbullet 中打开](https://docs.pushbullet.com/#open-in-pushbullet)

如果使用[UIDocumentInteractionController](https://developer.apple.com/library/ios/documentation/FileManagement/Conceptual/DocumentInteraction_TopicsForIOS/Articles/PreviewingandOpeningItems.html#//apple_ref/doc/uid/TP40010410-SW1)预览文件，当用户为大多数文件类型选择 “Open In ...” 时，Pushbullet 应显示在应用程序列表中。

如果用户选择了 Pushbullet 应用程序，则应该打开应用程序，并使用附加提供的文件的type =“file”推送新的撰写窗口。

### [ 反馈](https://docs.pushbullet.com/#feedback)

请通过 [ios@pushbullet.com](mailto:ios@pushbullet.com) 告诉我们您的想法

![img](https://docs.pushbullet.com/fleur.png)

# [ 聊](https://docs.pushbullet.com/#chat)

每当您向某人发送消息或从他们那里收到消息并且您与其他用户之间没有现有聊天时，就会创建聊天。

| 领域               | 类型   | 描述                                                         |
| :----------------- | :----- | :----------------------------------------------------------- |
| 鉴定者             | 串     | 此对象的唯一标识符**示例：**“ujpah72o0sjAoRtnM0jc”           |
| 活性               | 布尔   | 如果项目已被删除，则为 false**示例：**true                   |
| 创建               | 浮动   | 以浮点秒为单位的创建时间（[unix 时间戳](https://en.wikipedia.org/wiki/Unix_time)）**示例：**1.381092887398433e + 09 |
| 改性               | 浮动   | 浮点时间的最后修改时间（[unix 时间戳](https://en.wikipedia.org/wiki/Unix_time)）**示例：**1.441054560741007e + 09 |
| 静音               | 布尔   | 如果为true，则不会显示此聊天的通知**Example:** false         |
| with               | object | The user or email that the chat is with                      |
| ↳ email            | string | Email address of the person**Example:** "carmack@idsoftware.com" |
| ↳ email_normalized | string | Canonical email address of the person**Example:** "carmack@idsoftware.com" |
| ↳ iden             | string | If this is a user, the iden of that user**Example:** "ujlMns72k" |
| ↳ image_url        | string | Image to display for the person**Example:** "https://dl.pushbulletusercontent.com/foGfub1jtC6yYcOMACk1AbHwTrTKvrDc/john.jpg" |
| ↳ type             | string | "email" or "user"**Example:** "user"                         |
| ↳ name             | string | Name of the person**Example:** "John Carmack"                |

#####  Example

```
{
  "active": true,
  "created": 1.412047948579029e+09,
  "iden": "ujpah72o0sjAoRtnM0jc",
  "modified": 1.412047948579031e+09,
  "with": {
    "email": "carmack@idsoftware.com",
    "email_normalized": "carmack@idsoftware.com",
    "iden": "ujlMns72k",
    "image_url": "https://dl.pushbulletusercontent.com/foGfub1jtC6yYcOMACk1AbHwTrTKvrDc/john.jpg",
    "name": “John Carmack” ，
    “type” ： “user” 
  } 
}
```



## [ 列表，聊天](https://docs.pushbullet.com/#list-chats)

获取属于当前用户的聊天列表。如果您有大量的聊天记录，则需要使用[分页](https://docs.pushbullet.com/#pagination)。

#####  呼叫

```
获取https://api.pushbullet.com/v2/chats
```

#####  请求

没有

#####  响应

| 领域 | 类型    | 描述                                                         |
| :--- | :------ | :----------------------------------------------------------- |
| 猫   | [] 聊天 | 数组 [聊天](https://docs.pushbullet.com/#chat)对象与最近修改过的第一个一起排序 |

#####  例

 请求

```
curl --header'访问令牌：<your_access_token_here>'\
     https://api.pushbullet.com/v2/chats
```

 响应

```
{ 
  “聊天” ： [ 
    { 
      “活性” ： 真，
      “创建” ： 1.412047948579029e + 09 ，
      “iDEN的” ： “ujpah72o0sjAoRtnM0jc” ，“
      修饰的” ： 1.412047948579031e + 09 ，
      “同” ： { 
        “电子邮件” ： “ 卡马克@ idsoftware.com “ ”email_normalized“ ：” carmack@idsoftware.com “ ，”鉴定者“ ：”ujlMns72k“ ，”图片网址“：
         
         
         “https://dl.pushbulletusercontent.com/foGfub1jtC6yYcOMACk1AbHwTrTKvrDc/john.jpg” ，“
        名” ： “约翰·卡马克” ，
        “类型” ： “用户” 
      } 
    } 
  ] 
}
```



## [ 创建聊天](https://docs.pushbullet.com/#create-chat)

与其他用户或电子邮件地址创建聊天（如果尚不存在）。

#####  呼叫

```
POST https://api.pushbullet.com/v2/chats
```

#####  请求

| 领域     | 类型 | 描述                                                         |
| :------- | :--- | :----------------------------------------------------------- |
| 电子邮件 | 串   | 创建聊天的人的电子邮件（不一定是 Pushbullet 用户）**示例：**“ carmack@idsoftware.com ” |

#####  响应

[聊天](https://docs.pushbullet.com/#chat)对象

#####  例

 请求

```
curl --header'访问令牌：<your_access_token_here>'\
     --header'Content-Type：application / json'\
     --data-binary'{“email”：“ carmack@idsoftware.com ”}'
     --request POST \
     https://api.pushbullet.com/v2/chats
```

 响应

```
{
  "active": true,
  "created": 1.412047948579029e+09,
  "iden": "ujpah72o0sjAoRtnM0jc",
  "modified": 1.412047948579031e+09,
  "with": {
    "email": "carmack@idsoftware.com",
    "email_normalized": "carmack@idsoftware.com",
    "iden": "ujlMns72k",
    "image_url": "https://dl.pushbulletusercontent.com/foGfub1jtC6yYcOMACk1AbHwTrTKvrDc/john.jpg",
    "name": “John Carmack” ，
    “type” ： “user” 
  } 
}
```



## [ 更新聊天](https://docs.pushbullet.com/#update-chat)

更新现有聊天对象。

#####  呼叫

```
POST https://api.pushbullet.com/v2/chats/{iden}
```

#####  请求

| 领域 | 类型 | 描述                                                   |
| :--- | :--- | :----------------------------------------------------- |
| 静音 | 布尔 | 如果将授权静音，则为true，否则为取消静音**示例：**true |

#####  响应

[聊天](https://docs.pushbullet.com/#chat)对象

#####  例

 请求

```
curl --header'访问令牌：<your_access_token_here>'\
     --header'Content-Type：application / json'\
     --data-binary'{“muted”：true}'\
     --request POST \
     https://api.pushbullet.com/v2/chats/ujpah72o0sjAoRtnM0jc
```

 响应

```
{ 
  “活性” ： 真，
  “创建” ： 1.412047948579029e + 09 ，
  “iDEN的” ： “ujpah72o0sjAoRtnM0jc”，
  “modified” ： 1.412094382919271e + 09 ，
  “muted” ： true ，
  “with” ： { 
    “email” ： “ carmack @ idsoftware.com “ ”email_normalized“ ：” carmack@idsoftware.com “ ，”鉴定者“ ：”ujlMns72k“ ，”图片网址“：
     
     
     “https://dl.pushbulletusercontent.com/foGfub1jtC6yYcOMACk1AbHwTrTKvrDc/john.jpg” ，“
    名” ： “约翰·卡马克” ，
    “类型” ： “用户” 
  } 
}
```



## [ 删除聊天](https://docs.pushbullet.com/#delete-chat)

删除聊天对象。

#####  呼叫

```
删除https://api.pushbullet.com/v2/chats/{iden}
```

#####  请求

没有

#####  响应

没有

#####  例

 请求

```
curl --header'访问令牌：<your_access_token_here>'\
     - 请求删除\
     https://api.pushbullet.com/v2/chats/ujpah72o0sjAoRtnM0jc
```

 响应

```
{}
```



![img](https://docs.pushbullet.com/fleur.png)

# [ 设备](https://docs.pushbullet.com/#device)

| 领域               | 类型 | 描述                                                         |
| :----------------- | :--- | :----------------------------------------------------------- |
| 鉴定者             | 串   | 此对象的唯一标识符**示例：**“ujpah72o0sjAoRtnM0jc”           |
| 活性               | 布尔 | 如果项目已被删除，则为 false**示例：**true                   |
| 创建               | 浮动 | 以浮点秒为单位的创建时间（[unix 时间戳](https://en.wikipedia.org/wiki/Unix_time)）**示例：**1.381092887398433e + 09 |
| 改性               | 浮动 | 浮点时间的最后修改时间（[unix 时间戳](https://en.wikipedia.org/wiki/Unix_time)）**示例：**1.441054560741007e + 09 |
| 图标               | 串   | 用于此设备的图标可以是任意字符串。常用的值有：“桌面”，“浏览器”，“网站”，“笔记本电脑”，“平板电脑”，“手机”，“手表”，“系统”**示例：**“ios” |
| 昵称               | 串   | 显示设备时使用的名称**示例：**“Elon Musk 的 iPhone”          |
| generated_nickname | 布尔 | 如果昵称是从制造商和模型字段自动生成的（仅用于某些 Android 手机），则为 true**示例：**true |
| 生产厂家           | 串   | 该设备的制造商**示例：**“Apple”                              |
| 模型               | 串   | 设备型号**示例：**“iPhone 5s（GSM）”                         |
| APP_VERSION        | INT  | 设备上安装的 Pushbullet 应用程序的版本**示例：**8623         |
| 指纹               | 串   | 设备的字符串指纹，供应用程序使用以避免重复设备。价值是特定于平台的。**示例：**“nLN19IRNzS5xidPF + X8mKGNRpQo2X6XBgyO30FL6OiQ =” |
| key_fingerprint    | 串   | 设备端到端加密密钥的指纹，用于确定当前设备（基于其自己的密钥指纹）将能够与哪些设备通信。**示例：**“5ae6ec7e1fe681861b0cc85c53accc13bf94c11db7461a2808903f7469bfda56” |
| push_token         | 串   | 特定于平台的推送令牌。如果您要制作自己的设备，请将其留空，然后您可以在[实时事件流](https://docs.pushbullet.com/#realtime-event-stream)上收听[事件](https://docs.pushbullet.com/#realtime-event-stream)。**示例：**“production：f73be0ee7877c8c7fa69b1468cde764f” |
| has_sms            | 串   | 真如果设备有短信功能，目前只有真正为TYPE =“机器人”的装置**示例：**true |
| 类型               | 串   | DEPRECATED，改为使用图标字段。设备类型，可以是任意字符串。常用的值有：“android”，“chrome”，“firefox”，“ios”，“windows”，“stream”，“safari”，“mac”，“opera”，“website” |
| 类                 | 串   | DEPRECATED，类型的旧名称                                     |
| 可推               | 布尔 | DEPRECATED，用于部分初始化的type =“android”设备              |

#####  例

```
{ 
  “活性” ： 真，
  “APP_VERSION” ： 8623 ，
  “创建” ： 1.412047948579029e + 09 ，
  “iDEN的” ： “ujpah72o0sjAoRtnM0jc” ，“
  制造商” ： “苹果” ，
  “模型” ： “iPhone 5S（GSM）” ，
  “修改” ： 1.412047948579031e + 09 ，
  “昵称” ： “Elon Musk的iPhone” ，
  “push_token” ： “生产：f73be0ee7877c8c7fa69b1468cde764f” 
}
```



## [ 清单的设备](https://docs.pushbullet.com/#list-devices)

获取属于当前用户的设备列表。如果您有大量设备，则需要使用[分页](https://docs.pushbullet.com/#pagination)。

#####  呼叫

```
获取https://api.pushbullet.com/v2/devices
```

#####  请求

没有

#####  响应

| 领域 | 类型    | 描述                                                         |
| :--- | :------ | :----------------------------------------------------------- |
| 设备 | [] 设备 | 数组 订购的[设备](https://docs.pushbullet.com/#device)对象最近修改过的第一个 |

#####  例

 请求

```
curl --header'访问令牌：<your_access_token_here>'\
     https://api.pushbullet.com/v2/devices
```

 响应

```
{ 
  “设备” ： [ 
    { 
      “活动” ： 真实的，
      “APP_VERSION” ： 8623 ，
      “创造” ： 1.412047948579029e + 09 ，
      “鉴定者” ： “ujpah72o0sjAoRtnM0jc” ，“
      制造商” ： “苹果” ，
      “模式” ： “iPhone 5s（GSM）“ ，
      ”修改“ ： 1.412047948579031e + 09 ，
      ”昵称“ ： ”Elon Musk的iPhone“ ，
      ”push_token“ ： ”制作：f73be0ee7877c8c7fa69b1468cde764f“ 
    } 
  ] 
}
```



## [ 创建设备](https://docs.pushbullet.com/#create-device)

创建一个新设备。

#####  呼叫

```
POST https://api.pushbullet.com/v2/devices
```

#####  请求

| 领域        | 类型 | 描述                                                         |
| :---------- | :--- | :----------------------------------------------------------- |
| 昵称        | 串   | 显示设备时使用的名称**示例：**“Elon Musk 的 iPhone”          |
| 模型        | 串   | 设备型号**示例：**“iPhone 5s（GSM）”                         |
| 生产厂家    | 串   | 该设备的制造商**示例：**“Apple”                              |
| push_token  | 串   | 特定于平台的推送令牌。如果您要制作自己的设备，请将其留空，然后您可以在[实时事件流](https://docs.pushbullet.com/#realtime-event-stream)上收听[事件](https://docs.pushbullet.com/#realtime-event-stream)。**示例：**“production：f73be0ee7877c8c7fa69b1468cde764f” |
| APP_VERSION | INT  | 设备上安装的 Pushbullet 应用程序的版本**示例：**8623         |
| 图标        | 串   | 用于此设备的图标可以是任意字符串。常用的值有：“桌面”，“浏览器”，“网站”，“笔记本电脑”，“平板电脑”，“手机”，“手表”，“系统”**示例：**“ios” |
| has_sms     | 串   | 真如果设备有短信功能，目前只有真正为TYPE =“机器人”的装置**示例：**true |

#####  响应

[设备](https://docs.pushbullet.com/#device)对象

#####  例

 请求

```
curl --header'访问令牌：<your_access_token_here>'\
     --header'Content-Type：application / json'\
     --data-binary'{“app_version”：8623，“manufacturer”：“Apple”，“model”：“iPhone 5s（GSM）”，“昵称”：“Elon Musk的iPhone”，“push_token”：“制作： f73be0ee7877c8c7fa69b1468cde764f“}'\
     --request POST \
     https://api.pushbullet.com/v2/devices
```

 响应

```
{ 
  “活性” ： 真，
  “APP_VERSION” ： 8623 ，
  “创建” ： 1.412047948579029e + 09 ，
  “iDEN的” ： “ujpah72o0sjAoRtnM0jc” ，“
  制造商” ： “苹果” ，
  “模型” ： “iPhone 5S（GSM）” ，
  “修改” ： 1.412047948579031e + 09 ，
  “昵称” ： “Elon Musk的iPhone” ，
  “push_token” ： “生产：f73be0ee7877c8c7fa69b1468cde764f” 
}
```



## [ 更新设备](https://docs.pushbullet.com/#update-device)

更新现有设备。

#####  呼叫

```
POST https://api.pushbullet.com/v2/devices/{iden}
```

#####  请求

| 领域        | 类型 | 描述                                                         |
| :---------- | :--- | :----------------------------------------------------------- |
| 昵称        | 串   | 显示设备时使用的名称**示例：**“Elon Musk 的 iPhone”          |
| 模型        | 串   | 设备型号**示例：**“iPhone 5s（GSM）”                         |
| 生产厂家    | 串   | 该设备的制造商**示例：**“Apple”                              |
| push_token  | 串   | 特定于平台的推送令牌。如果您要制作自己的设备，请将其留空，然后您可以在[实时事件流](https://docs.pushbullet.com/#realtime-event-stream)上收听[事件](https://docs.pushbullet.com/#realtime-event-stream)。**示例：**“production：f73be0ee7877c8c7fa69b1468cde764f” |
| APP_VERSION | INT  | 设备上安装的 Pushbullet 应用程序的版本**示例：**8623         |
| 图标        | 串   | 用于此设备的图标可以是任意字符串。常用的值有：“桌面”，“浏览器”，“网站”，“笔记本电脑”，“平板电脑”，“手机”，“手表”，“系统”**示例：**“ios” |
| has_sms     | 串   | 真如果设备有短信功能，目前只有真正为TYPE =“机器人”的装置**示例：**true |

#####  响应

[设备](https://docs.pushbullet.com/#device)对象

#####  例

 请求

```
curl --header'访问令牌：<your_access_token_here>'\
     --header'Content-Type：application / json'\
     --data-binary'{“昵称”：“工作电话”}'\
     --request POST \
     https://api.pushbullet.com/v2/devices/ujpah72o0sjAoRtnM0jc
```

 响应

```
{ 
  “活性” ： 真，
  “APP_VERSION” ： 8623 ，
  “创建” ： 1.412047948579029e + 09 ，
  “iDEN的” ： “ujpah72o0sjAoRtnM0jc” ，“
  制造商” ： “苹果” ，
  “模型” ： “iPhone 5S（GSM）” ，
  “已修改” ： 1.412094382919271e + 09 ，
  “昵称” ： “工作电话” ，
  “push_token” ： “生产：f73be0ee7877c8c7fa69b1468cde764f” 
}
```



## [ 删除设备](https://docs.pushbullet.com/#delete-device)

Delete a device.

#####  Call

```
DELETE https://api.pushbullet.com/v2/devices
```

#####  Request

none

#####  Response

none

#####  Example

 Request

```
curl --header 'Access-Token: <your_access_token_here>' \
     --request DELETE \
     https://api.pushbullet.com/v2/devices/ujpah72o0sjAoRtnM0jc
```

 Response

```
{}
```



![img](https://docs.pushbullet.com/fleur.png)

# [ Push](https://docs.pushbullet.com/#push)

A Push.

| Field                     | Type   | Description                                                  |
| :------------------------ | :----- | :----------------------------------------------------------- |
| iden                      | string | Unique identifier for this object**Example:** "ujpah72o0sjAoRtnM0jc" |
| active                    | bool   | false if the item has been deleted**Example:** true          |
| created                   | float  | Creation time in floating point seconds ([unix timestamp](https://en.wikipedia.org/wiki/Unix_time))**Example:** 1.381092887398433e+09 |
| modified                  | float  | Last modified time in floating point seconds ([unix timestamp](https://en.wikipedia.org/wiki/Unix_time))**Example:** 1.441054560741007e+09 |
| type                      | string | Type of the push, one of "note", "file", "link".**Example:** "note" |
| dismissed                 | bool   | true if the push has been dismissed by any device or if any device was active when the push was received**Example:** false |
| guid                      | string | Unique identifier set by the client, used to identify a push in case you receive it from /v2/everything before the call to /v2/pusheshas completed. This should be a unique value. Pushes with guidset are mostly idempotent, meaning that sending another push with the same guid is unlikely to create another push (it will return the previously created push).**Example:** "993aaa48567d91068e96c75a74644159" |
| direction                 | string | Direction the push was sent in, can be "self", "outgoing", or "incoming"**Example:** "self" |
| sender_iden               | string | User iden of the sender**Example:** "ujpah72o0"              |
| sender_email              | string | Email address of the sender**Example:** "elon@teslamotors.com" |
| sender_email_normalized   | string | Canonical email address of the sender**Example:** "elon@teslamotors.com" |
| sender_name               | string | Name of the sender**Example:** "Elon Musk"                   |
| receiver_iden             | string | User iden of the receiver**Example:** "ujpah72o0"            |
| receiver_email            | string | Email address of the receiver**Example:** "elon@teslamotors.com" |
| receiver_email_normalized | string | Canonical email address of the receiver**Example:** "elon@teslamotors.com" |
| target_device_iden        | string | 目标设备的设备标识，如果发送到单个设备**示例：**“ujpah72o0sjAoRtnM0jc” |
| source_device_iden        | 串     | 发送设备的设备标识。可选择在创建推送时由发件人设置**示例：**“ujpah72o0sjAoRtnM0jc” |
| CLIENT_ID                 | 串     | 如果推送是由客户端创建的，则设置为该客户端的标识。**示例：**“ujpah72o0sjAoRtnM0jc” |
| channel_iden              | 串     | 如果推送是由通道创建的，则设置为该通道的标识**示例：**“ujpah72o0sjAoRtnM0jc” |
| awake_app_guids           | [] 串  | 在发送推送时唤醒应用程序的 guid 列表（客户端标识符，而不是推送时的guid字段）。如果此列表的长度 > 0，则解雇将设置为true，并且唤醒应用程序必须决定如何处理通知**示例：**[“web-2d8cdf2a2b9b”，“web-cdb2313c74e”] |
| 标题                      | 串     | 推动的标题，用于所有类型的推动**示例：**“太空旅行创意”       |
| 身体                      | 串     | 推动体，用于所有类型的推动**示例：**“太空升降机，火星超级环，空间模型 S（模型空间？）” |
| 网址                      | 串     | URL 字段，用于type =“link”推送**示例：**“http://www.teslamotors.com/” |
| 文件名                    | 串     | 文件名，用于type =“file”推送**示例：**“john.jpg”             |
| 文件类型                  | 串     | 文件 mime 类型，用于type =“file”推送**示例：**“image / jpeg” |
| FILE_URL                  | 串     | 文件下载 URL，用于type =“file”推送**示例：**“https://dl.pushbulletusercontent.com/foGfub1jtC6yYcOMACk1AbHwTrTKvrDc/john.jpg” |
| IMAGE_URL                 | 串     | 如果 file_type 与 image / * 匹配，则在type =“file”上显示用于此推送的图像的 URL**示例：**“https://lh3.googleusercontent.com/mrrz35lLbiYAz8ejkJcpdsYhN3tMEXXxj93k_gQPin4GfdDjVy2Bj26pOGrpFQmAM7OFBHcDfdMjrScg3EUIJrgJeY” |
| IMAGE_WIDTH               | INT    | 图像宽度（以像素为单位），仅在设置了image_url 时才会出现**示例：**322 |
| IMAGE_HEIGHT              | INT    | 图像的高度（以像素为单位），仅在设置了image_url 时才会出现**示例：**484 |

#####  例

```
{ 
  “active” ： true ，
  “body” ： “Space Elevator，Mars Hyperloop，Space Model S（Model Space？）” ，
  “created” ： 1.412047948579029e + 09 ，
  “direction” ： “self” ，
  “ dismissed ” ： false ，
  “ iden ” ： “ujpah72o0sjAoRtnM0jc” ，
  “modified” ： 1.412047948579031e + 09 ，
  “receiver_email” ： “ elon @teslamotors.com ” ，
  “receiver_email_normalized” ： “ elon@teslamotors.com ” ，
  "receiver_iden": "ujpah72o0",
  "sender_email": "elon@teslamotors.com",
  "sender_email_normalized": "elon@teslamotors.com",
  "sender_iden": "ujpah72o0",
  "sender_name": "Elon Musk",
  "title": "Space Travel Ideas",
  "type": "note"
}
```



## [ list-pushes](https://docs.pushbullet.com/#list-pushes)

Request push history.

#####  Call

```
GET https://api.pushbullet.com/v2/pushes
```

#####  Request

| Field          | Type    | Description                                                  |
| :------------- | :------ | :----------------------------------------------------------- |
| modified_after | string  | Request pushes modified after this timestamp**Example:** 1.4e+09 |
| active         | string  | Don't return deleted pushes**Example:** true                 |
| cursor         | string  | Cursor for getting multiple pages of pushes, see [Pagination](https://docs.pushbullet.com/#pagination)**Example:** "3eae6fa796b06b51b7bd6ad824b9b63b" |
| limit          | integer | Limit on the number of results returned, see [Pagination](https://docs.pushbullet.com/#pagination)**Example:** 10 |

#####  Response

| Field  | Type   | Description                                                  |
| :----- | :----- | :----------------------------------------------------------- |
| pushes | []Push | Array of [ Push](https://docs.pushbullet.com/#push) objects ordered with most recently modified first |

#####  Example

 Request

```
curl --header 'Access-Token: <your_access_token_here>' \
     --data-urlencode active="true" \
     --data-urlencode modified_after="1.4e+09" \
     --get \
     https://api.pushbullet.com/v2/pushes
```

 Response

```
{
  "pushes": [
    {
      "active": true,
      "body": "Space Elevator, Mars Hyperloop, Space Model S (Model Space?)",
      "created": 1.412047948579029e+09,
      "direction": "self",
      "dismissed": false,
      "iden": "ujpah72o0sjAoRtnM0jc",
      "modified": 1.412047948579031e+09,
      "receiver_email": "elon@teslamotors.com",
      "receiver_email_normalized": "elon@teslamotors.com",
      "receiver_iden": "ujpah72o0",
      "sender_email": "elon@teslamotors.com",
      "sender_email_normalized": "elon@teslamotors.com",
      "sender_iden": "ujpah72o0",
      "sender_name": "Elon Musk",
      "title": "Space Travel Ideas",
      "type": "note"
    }
  ]
}
```



## [ create-push](https://docs.pushbullet.com/#create-push)

Send a push to a device or another person.

#### [Target Parameters](https://docs.pushbullet.com/#target-parameters)

Each push has a target, if you don't specify a target, we will broadcast it to all of the user's devices. Only one target may be specified.

+  device_iden - Send the push to a specific device. Appears as target_device_iden on the push. You can find this using the [/v2/devices](https://docs.pushbullet.com/#devices) call.
+  email - Send the push to this email address. If that email address is associated with a Pushbullet user, we will send it directly to that user, otherwise we will fallback to sending an email to the email address (this will also happen if a user exists but has no devices registered).
+  channel_tag - Send the push to all subscribers to your channel that has this tag.
+  client_iden - Send the push to all users who have granted access to your OAuth client that has this iden.

#### [Parameters for different types of pushes](https://docs.pushbullet.com/#parameters-for-different-types-of-pushes)

+  Note
   +  type - Set to note
   +  title - The note's title.
   +  body - The note's message.
+  Link
   +  type - Set to link
   +  title - The link's title.
   +  body - A message associated with the link.
   +  url - The url to open.
+  File
   +  type - Set to file
   +  body - A message to go with the file.
   +  file_name - The name of the file.
   +  file_type - The MIME type of the file.
   +  file_url - The url for the file. See [pushing files](https://docs.pushbullet.com/#pushing-files) for how to get a file_url

### [Push a file](https://docs.pushbullet.com/#push-a-file)

Pushing files is a two-part process: first the file needs to be uploaded, then a push needs to be sent for that file.

To upload a new file, use [ upload-request](https://docs.pushbullet.com/#upload-request).

Once the file has been uploaded, set the file_name, file_url, and file_typereturned in the response to the upload request as the parameters for a new push with type="file".

#####  Call

```
POST https://api.pushbullet.com/v2/pushes
```

#####  Request

| Field              | Type   | Description                                                  |
| :----------------- | :----- | :----------------------------------------------------------- |
| type               | string | Type of the push, one of "note", "file", "link".**Example:** "note" |
| title              | string | Title of the push, used for all types of pushes**Example:** "Space Travel Ideas" |
| body               | string | Body of the push, used for all types of pushes**Example:** "Space Elevator, Mars Hyperloop, Space Model S (Model Space?)" |
| url                | string | URL field, used for type="link" pushes**Example:** "http://www.teslamotors.com/" |
| file_name          | string | File name, used for type="file" pushes**Example:** "john.jpg" |
| file_type          | string | File mime type, used for type="file" pushes**Example:** "image/jpeg" |
| file_url           | string | File download url, used for type="file" pushes**Example:** "https://dl.pushbulletusercontent.com/foGfub1jtC6yYcOMACk1AbHwTrTKvrDc/john.jpg" |
| source_device_iden | string | Device iden of the sending device. Optional.**Example:** "ujpah72o0sjAoRtnM0jc" |
| device_iden        | string | Device iden of the target device, if sending to a single device. Appears as target_device_iden on the push.**Example:** "ujpah72o0sjAoRtnM0jc" |
| client_iden        | string | Client iden of the target client, sends a push to all users who have granted access to this client. The current user must own this client.**Example:** "ujpah72o0sjAoRtnM0jc" |
| channel_tag        | string | Channel tag of the target channel, sends a push to all people who are subscribed to this channel. The current user must own this channel. |
| email              | string | Email address to send the push to. If there is a pushbullet user with this address, they get a push, otherwise they get an email.**Example:** "elon@teslamotors.com" |
| guid               | string | Unique identifier set by the client, used to identify a push in case you receive it from /v2/everything before the call to /v2/pusheshas completed. This should be a unique value. Pushes with guidset are mostly idempotent, meaning that sending another push with the same guid is unlikely to create another push (it will return the previously created push).**Example:** "993aaa48567d91068e96c75a74644159" |

#####  Response

[ Push](https://docs.pushbullet.com/#push) object

#####  Example

 Request

```
curl --header 'Access-Token: <your_access_token_here>' \
     --header 'Content-Type: application/json' \
     --data-binary '{"body":"Space Elevator, Mars Hyperloop, Space Model S (Model Space?)","title":"Space Travel Ideas","type":"note"}' \
     --request POST \
     https://api.pushbullet.com/v2/pushes
```

 Response

```
{
  "active": true,
  "body": "Space Elevator, Mars Hyperloop, Space Model S (Model Space?)",
  "created": 1.412047948579029e+09,
  "direction": "self",
  "dismissed": false,
  "iden": "ujpah72o0sjAoRtnM0jc",
  "modified": 1.412047948579031e+09,
  "receiver_email": "elon@teslamotors.com",
  "receiver_email_normalized": "elon@teslamotors.com",
  "receiver_iden": "ujpah72o0",
  "sender_email": "elon@teslamotors.com",
  "sender_email_normalized": "elon@teslamotors.com",
  "sender_iden": "ujpah72o0",
  "sender_name": "Elon Musk",
  "title": "Space Travel Ideas",
  "type": "note"
}
```



## [ update-push](https://docs.pushbullet.com/#update-push)

Update a push.

#####  Call

```
POST https://api.pushbullet.com/v2/pushes/{iden}
```

#####  Request

| Field     | Type | Description                                                  |
| :-------- | :--- | :----------------------------------------------------------- |
| dismissed | bool | Marks a push as having been dismissed by the user, will cause any notifications for the push to be hidden if possible.**Example:** true |

#####  Response

[ Push](https://docs.pushbullet.com/#push) object

#####  Example

 Request

```
curl --header 'Access-Token: <your_access_token_here>' \
     --header 'Content-Type: application/json' \
     --data-binary '{"dismissed":true}' \
     --request POST \
     https://api.pushbullet.com/v2/pushes/ujpah72o0sjAoRtnM0jc
```

 Response

```
{ 
  “active” ： true ，
  “body” ： “Space Elevator，Mars Hyperloop，Space Model S（Model Space？）” ，
  “created” ： 1.412047948579029e + 09 ，
  “direction” ： “self” ，
  “ dismissed ” ： true ，
  “ iden ” ： “ujpah72o0sjAoRtnM0jc” ，
  “modified” ： 1.412094382919271e + 09 ，
  “receiver_email” ： “ elon @teslamotors.com ” ，
  “receiver_email_normalized” ： “ elon@teslamotors.com ” ，
  “receiver_iden” ： “ujpah72o0” ，
  “sender_email” ： “ elon@teslamotors.com ” ，
  “sender_email_normalized” ： “ elon@teslamotors.com ” ，
  “sender_iden” ： “ujpah72o0” ，
  “sender_name” ： “Elon Musk” ，
  “ title“ ： ”Space Travel Ideas“ ，
  ”type“ ： ”note“ 
}
```



## [ 删除推](https://docs.pushbullet.com/#delete-push)

删除推送。

#####  呼叫

```
删除https://api.pushbullet.com/v2/pushes/{iden}
```

#####  请求

没有

#####  响应

没有

#####  例

 请求

```
curl --header'访问令牌：<your_access_token_here>'\
     - 请求删除\
     https://api.pushbullet.com/v2/pushes/ujpah72o0sjAoRtnM0jc
```

 响应

```
{}
```



## [ 删除 - 全推](https://docs.pushbullet.com/#delete-all-pushes)

删除属于当前用户的所有推送。此调用是异步的，在调用返回后将删除推送。

#####  呼叫

```
删除https://api.pushbullet.com/v2/pushes
```

#####  请求

没有

#####  响应

没有

#####  例

 请求

```
curl --header'访问令牌：<your_access_token_here>'\
     - 请求删除\
     https://api.pushbullet.com/v2/pushes
```

 响应

```
{}
```



![img](https://docs.pushbullet.com/fleur.png)

# [ 订阅](https://docs.pushbullet.com/#subscription)

订阅频道以接收推送到该频道的任何更新。

可以[在网站](https://www.pushbullet.com/my-channels)上[创建](https://www.pushbullet.com/my-channels)频道。每个频道都有一个唯一的标签来识别它。当您推送到频道时，订阅该频道的所有人都将获得推送。

要推送到频道，请使用channel_tag参数[ 创建推](https://docs.pushbullet.com/#create-push)

| 领域          | 类型   | 描述                                                         |
| :------------ | :----- | :----------------------------------------------------------- |
| 鉴定者        | string | Unique identifier for this object**Example:** "ujpah72o0sjAoRtnM0jc" |
| active        | bool   | false if the item has been deleted**Example:** true          |
| created       | float  | Creation time in floating point seconds ([unix timestamp](https://en.wikipedia.org/wiki/Unix_time))**Example:** 1.381092887398433e+09 |
| modified      | float  | Last modified time in floating point seconds ([unix timestamp](https://en.wikipedia.org/wiki/Unix_time))**Example:** 1.441054560741007e+09 |
| muted         | bool   | If true, notifications from this subscription will not be shown**Example:** false |
| channel       | object | Information about the channel that is being subscribed to    |
| ↳ iden        | string | Unique identifier for the channel**Example:** "ujpah72o0sjAoRtnM0jc" |
| ↳ tag         | string | Unique tag for this channel**Example:** "elonmusknews"       |
| ↳ name        | string | Name of the channel**Example:** "Elon Musk News"             |
| ↳ description | string | Description of the channel**Example:** "News about Elon Musk." |
| ↳ image_url   | string | Image for the channel**Example:** "https://dl.pushbulletusercontent.com/StzRmwdkIe8gluBH3XoJ9HjRqjlUYSf4/musk.jpg" |
| ↳ website_url | string | Link to a website for the channel**Example:** "https://twitter.com/elonmusk" |

#####  Example

```
{
  "active": true,
  "channel": {
    "description": "News about Elon Musk.",
    "iden": "ujxPklLhvyKsjAvkMyTVh6",
    "image_url": "https://dl.pushbulletusercontent.com/StzRmwdkIe8gluBH3XoJ9HjRqjlUYSf4/musk.jpg",
    "name": "Elon Musk News",
    "tag": "elonmusknews"
  },
  "created": 1.412047948579029e+09,
  "iden": "ujpah72o0sjAoRtnM0jc",
  "modified": 1.412047948579031e+09，
  “静音” ： 假
}
```



## [ 列表订阅](https://docs.pushbullet.com/#list-subscriptions)

获取属于当前用户的订阅列表。如果您有大量订阅，则需要使用[分页](https://docs.pushbullet.com/#pagination)。

#####  呼叫

```
获取https://api.pushbullet.com/v2/subscriptions
```

#####  请求

没有

#####  响应

| 领域 | 类型    | 描述                                                         |
| :--- | :------ | :----------------------------------------------------------- |
| 订阅 | [] 订阅 | 数组 [订购](https://docs.pushbullet.com/#subscription)对象最近修改的第一个[订购](https://docs.pushbullet.com/#subscription)对象 |

#####  例

 请求

```
curl --header'访问令牌：<your_access_token_here>'\
     https://api.pushbullet.com/v2/subscriptions
```

 响应

```
{ 
  “subscriptions” ： [ 
    { 
      “active” ： true ，
      “channel” ： { 
        “description” ： “有关Elon Musk的新闻。” ，
        “ iden ” ： “ujxPklLhvyKsjAvkMyTVh6” ，
        “image_url” ： “https://dl.pushbulletusercontent.com/StzRmwdkIe8gluBH3XoJ9HjRqjlUYSf4/musk.jpg” ，
        “name” ： “Elon Musk News” ，
        “tag” ： “elonmusknews” 
      } ，
      “创造” ： 1.412047948579029e + 09 ，
       
      "modified": 1.412047948579031e+09
    }
  ]
}
```



## [ create-subscription](https://docs.pushbullet.com/#create-subscription)

#####  Call

```
POST https://api.pushbullet.com/v2/subscriptions
```

#####  Request

| Field       | Type   | Description                                                  |
| :---------- | :----- | :----------------------------------------------------------- |
| channel_tag | string | Unique tag for the channel to subscribe to**Example:** "elonmusknews" |

#####  Response

[ Subscription](https://docs.pushbullet.com/#subscription) object

#####  Example

 Request

```
curl --header 'Access-Token: <your_access_token_here>' \
     --header 'Content-Type: application/json' \
     --data-binary '{"channel_tag":"elonmusknews"}' \
     --request POST \
     https://api.pushbullet.com/v2/subscriptions
```

 Response

```
{
  "active": true,
  "channel": {
    "description": "News about Elon Musk.",
    "iden": "ujxPklLhvyKsjAvkMyTVh6",
    "image_url": "https://dl.pushbulletusercontent.com/StzRmwdkIe8gluBH3XoJ9HjRqjlUYSf4/musk.jpg",
    "name": "Elon Musk News",
    "tag": "elonmusknews"
  },
  "created": 1.412047948579029e+09,
  "iden": "ujpah72o0sjAoRtnM0jc",
  "modified": 1.412047948579031e+09
}
```



## [ 更新订阅](https://docs.pushbullet.com/#update-subscription)

#####  呼叫

```
POST https://api.pushbullet.com/v2/subscriptions/{iden}
```

#####  请求

| 领域 | 类型 | 描述                                                         |
| :--- | :--- | :----------------------------------------------------------- |
| 静音 | 布尔 | 如果要取消订阅，则为true;如果取消静音，则为 false**示例：**true |

#####  响应

[订阅](https://docs.pushbullet.com/#subscription)对象

#####  例

 请求

```
curl --header'访问令牌：<your_access_token_here>'\
     --header'Content-Type：application / json'\
     --data-binary'{“muted”：true}'\
     --request POST \
     https://api.pushbullet.com/v2/subscriptions/ujpah72o0sjAoRtnM0jc
```

 响应

```
{ 
  “active” ： true ，
  “channel” ： { 
    “description” ： “有关Elon Musk的新闻。” ，
    “ iden ” ： “ujxPklLhvyKsjAvkMyTVh6” ，
    “image_url” ： “https://dl.pushbulletusercontent.com/StzRmwdkIe8gluBH3XoJ9HjRqjlUYSf4/musk.jpg” ，
    “name” ： “Elon Musk News” ，
    “tag” ： “elonmusknews” 
  } ，
  “created” ： 1.412047948579029e + 09 ，
  “ iden ” ： “
   ，
  “静音” ： 真实
}
```



## [ 删除订阅](https://docs.pushbullet.com/#delete-subscription)

取消订阅频道。

#####  呼叫

```
删除https://api.pushbullet.com/v2/subscriptions/{iden}
```

#####  请求

没有

#####  响应

[订阅](https://docs.pushbullet.com/#subscription)对象

#####  例

 请求

```
curl --header'访问令牌：<your_access_token_here>'\
     - 请求删除\
     https://api.pushbullet.com/v2/subscriptions/ujpah72o0sjAoRtnM0jc
```

 响应

```
{}
```



## [ 频道资讯](https://docs.pushbullet.com/#channel-info)

获取有关频道的信息。

#####  呼叫

```
获取https://api.pushbullet.com/v2/channel-info
```

#####  请求

| 领域             | 类型 | 描述                                         |
| :--------------- | :--- | :------------------------------------------- |
| 标签             | 串   | 获取信息的频道标记**示例：**“elonmusknews”   |
| no_recent_pushes | 布尔 | 不显示最近的推送，默认为 false**示例：**true |

#####  响应

| 领域             | 类型   | 描述                                                         |
| :--------------- | :----- | :----------------------------------------------------------- |
| 鉴定者           | 串     | 频道的唯一标识符**Example:** "ujpah72o0sjAoRtnM0jc"          |
| name             | string | Name of the channel**Example:** "Elon Musk News"             |
| description      | string | Description of the channel**Example:** "News about Elon Musk" |
| image_url        | string | Image to display for the channel**Example:** "https://dl.pushbulletusercontent.com/StzRmwdkIe8gluBH3XoJ9HjRqjlUYSf4/musk.jpg" |
| subscriber_count | int    | Number of subscribers to the channel**Example:** 9382239     |
| tag              | string | Globally unique identifier for the channel, chosen by the channel creator**Example:** "elonmusknews" |
| recent_pushes    | []Push | Array of recent [ Push](https://docs.pushbullet.com/#push) objects sent on the channel |

#####  Example

 Request

```
curl --data-urlencode no_recent_pushes="true" \
     --data-urlencode tag="elonmusknews" \
     --get \
     https://api.pushbullet.com/v2/channel-info
```

 Response

```
{
  "active": true,
  "created": 1.412047948579029e+09,
  "description": "News about Elon Musk.",
  "iden": "ujxPklLhvyKsjAvkMyTVh6",
  "image_url": "https://dl.pushbulletusercontent.com/StzRmwdkIe8gluBH3XoJ9HjRqjlUYSf4/musk.jpg",
  "modified": 1.412047948579031e+09,
  "name": "Elon Musk News",
  "subscriber_count": 9.382239e+06,
  "tag": "elonmusknews"
}
```



![img](https://docs.pushbullet.com/fleur.png)

# [ User](https://docs.pushbullet.com/#user)

| Field            | Type   | Description                                                  |
| :--------------- | :----- | :----------------------------------------------------------- |
| iden             | string | Unique identifier for the current user**Example:** "ujpah72o0" |
| created          | float  | Creation time in floating point seconds ([unix timestamp](https://en.wikipedia.org/wiki/Unix_time))**Example:** 1.381092887398433e+09 |
| modified         | float  | Last modified time in floating point seconds ([unix timestamp](https://en.wikipedia.org/wiki/Unix_time))**Example:** 1.441054560741007e+09 |
| email            | string | Email address**Example:** "elon@teslamotors.com"             |
| email_normalized | string | Canonical email address**Example:** "elon@teslamotors.com"   |
| name             | string | Full name if available**Example:** "Elon Musk"               |
| image_url        | string | URL for image of user or placeholder image**Example:** "https://static.pushbullet.com/missing-image/55a7dc-45" |
| max_upload_size  | int    | Maximum upload size in bytes**示例：**26214400               |
| referred_count   | INT    | 此用户引用的用户数**示例：**2                                |
| referrer_iden    | 串     | 引用当前用户的用户的用户标识（如果已设置）**示例：**“ujlxm0aiz2” |

#####  例

```
{ 
  “创造” ： 1.381092887398433e + 09 ，
  “电子邮件” ： “ elon@teslamotors.com ” ，
  “email_normalized” ：“  elon@teslamotors.com ” ，“鉴定者” ：“ujpah72o0” ，“图片网址” ：“HTTPS：/ /static.pushbullet.com/missing-image/55a7dc-45" ，“max_upload_size” ：2.62144e + 07 ，“修饰的” ：1.441054560741007e + 09 ，“姓名” ：“伊隆麝香” }
   
   
   
   
   
```



## [ 获得用户](https://docs.pushbullet.com/#get-user)

获取当前登录的用户。

#####  呼叫

```
获取https://api.pushbullet.com/v2/users/me
```

#####  请求

没有

#####  响应

[用户](https://docs.pushbullet.com/#user)对象

#####  例

 请求

```
curl --header'访问令牌：<your_access_token_here>'\
     https://api.pushbullet.com/v2/users/me
```

 响应

```
{ 
  “创造” ： 1.381092887398433e + 09 ，
  “电子邮件” ： “ elon@teslamotors.com ” ，
  “email_normalized” ：“  elon@teslamotors.com ” ，“鉴定者” ：“ujpah72o0” ，“图片网址” ：“HTTPS：/ /static.pushbullet.com/missing-image/55a7dc-45" ，“max_upload_size” ：2.62144e + 07 ，“修饰的” ：1.441054560741007e + 09 ，“姓名” ：“伊隆麝香” }
   
   
   
   
   
```



![img](https://docs.pushbullet.com/fleur.png)

# [ 上传](https://docs.pushbullet.com/#upload)

To upload a file you need to call [ upload-request](https://docs.pushbullet.com/#upload-request) with the file name and type. After you get an upload_url from the response, you can upload the file contents using multipart/form-data encoding.

##### EXAMPLE REQUEST

```
curl -i -X POST https://upload.pushbullet.com/upload-legacy/a5e1776d2566a6b16032958697288df4 \
  -F file=@cat.jpg
```

##### EXAMPLE RESPONSE

```
HTTP/1.1 204 No Content
```

After the request completes, the file will be available at the file_url from the [ upload-request](https://docs.pushbullet.com/#upload-request) response.

## [ upload-request](https://docs.pushbullet.com/#upload-request)

Request authorization to upload a file.

#####  Call

```
POST https://api.pushbullet.com/v2/upload-request
```

#####  Request

| Field     | Type   | Description                                                  |
| :-------- | :----- | :----------------------------------------------------------- |
| file_name | string | The name of the file you want to upload**Example:** "cat.jpg" |
| 文件类型  | 串     | 文件的 MIME 类型**示例：**“image / jpeg”                     |

#####  响应

| 领域       | 类型 | 描述                                                         |
| :--------- | :--- | :----------------------------------------------------------- |
| 文件名     | 串   | 将用于文件的文件名（可能会从原始file_name 中截断。           |
| 文件类型   | 串   | 将用于文件的文件类型（可能与提供的文件类型不同 [上传请求](https://docs.pushbullet.com/#upload-request)。 |
| FILE_URL   | 串   | 上传文件后可用的 URL。                                       |
| UPLOAD_URL | 串   | 将文件 POST 到的 URL。必须使用multipart / form-data编码发布该文件。 |
| 数据       | 宾语 | 弃用                                                         |

#####  例

 请求

```
curl --header'访问令牌：<your_access_token_here>'\
     --header'Content-Type：application / json'\
     --data-binary'{“file_name”：“cat.jpg”，“file_type”：“image / jpeg”}'\
     --request POST \
     https://api.pushbullet.com/v2/upload-request
```

 响应

```
{ 
  “FILE_NAME” ： “cat.jpg” ，
  “FILE_TYPE” ：“ 图像/ JPEG” ，
  “FILE_URL” ： “https://dl.pushbulletusercontent.com/034f197bc6c37cac3cc03542659d458b/cat.jpg” ，
  “UPLOAD_URL” ： “HTTPS： //upload.pushbullet.com/upload-legacy/a5e1776d2566a6b16032958697288df4“ 
}
```



![img](https://docs.pushbullet.com/fleur.png)

# [ 更新日志](https://docs.pushbullet.com/#changelog)

#### [2015 年 1 月 28 日](https://docs.pushbullet.com/v15)

・删除已永久弃用的地址和列表推送。

#### [2015 年 12 月 18 日](https://docs.pushbullet.com/v14)

・修复了窗户的卷曲链接。

#### [2015 年 11 月 4 日](https://docs.pushbullet.com/v13)

・删除了 Android 扩展部分，因为已经替换为 Android Wear 集成，不再需要 Android 扩展。

#### [2015 年 9 月 11 日](https://docs.pushbullet.com/v12)

・文档的新风格。

・删除了联系人呼叫，因为官方应用程序不再是用户联系人。这些已被替换为[聊天](https://docs.pushbullet.com/#chat)对象。

#### [2015 年 8 月 24 日](https://docs.pushbullet.com/v11)

・添加了一个运行按钮来执行 javascript 片段。

#### [2015 年 8 月 18 日](https://docs.pushbullet.com/v10)

・添加了[端到端加密中的加密信息](https://docs.pushbullet.com/#end-to-end-encryption)。

・添加了新的 auth 标头Access-Token to [Requests](https://docs.pushbullet.com/#requests)，删除了旧版 auth 标头的提及。

・从[调整图像大小中](https://docs.pushbullet.com/#resizing-images)删除了过时的信息。

#### [2015 年 5 月 23 日](https://docs.pushbullet.com/v9)

・添加了有关[限速的](https://docs.pushbullet.com/#ratelimiting)信息。

#### [2015 年 4 月 13 日](https://docs.pushbullet.com/v8)

・添加了使用短命的[发送短信](https://docs.pushbullet.com/#send-sms)。

・更新了[调整大小图像](https://docs.pushbullet.com/#resizing-images)以提及新的调整大小方法并删除旧方法。

#### [2015 年 3 月 10 日](https://docs.pushbullet.com/v7)

・删除了[提到的 HTTP Basic Auth](https://docs.pushbullet.com/#getting-started)，它比设置 Authorization 标头更令人困惑。

#### [2015 年 2 月 20 日](https://docs.pushbullet.com/v6)

・添加了有关[向后兼容性的说明](https://docs.pushbullet.com/#backwards-compatibility)。

#### [2015 年 2 月 16 日](https://docs.pushbullet.com/v5)

・添加了[删除所有推送](https://docs.pushbullet.com/#delete-all-pushes)的调用。







# [Pushbullet API](https://docs.pushbullet.com/#pushbullet-api)

Pushbullet's API enables developers to build on the Pushbullet infrastructure. Our goal is to provide a full API that enables anything to tap into the Pushbullet network.

This is important to us because we believe everything, not just smartphones and computers, should be able to exchange information in real time. Here are some of the things you can build with Pushbullet:

+  Have a website and want to offer push notifications? We've built everything you need.
+  Want to build a Pushbullet client for a platform we don't officially support yet? Everything you need is here.
+  Working on a home automation system? Pushbullet can get everything chatting.
+  Working with sensors and want to send messages to another device? Pushbullet is just what you need.
+  Manage IT/servers and want to get updates and alerts no matter where you are or what device you're using? Pushbullet makes it easy.

[Check out this ProgrammableWeb article for a longer introduction to Pushbullet and this API](http://www.programmableweb.com/news/pushbullet-releases-new-and-improved-api/2014/05/21).

![img](https://docs.pushbullet.com/fleur.png)

### [Sections](https://docs.pushbullet.com/#sections)

+  [API](https://docs.pushbullet.com/#api-quick-start) - Send/receive pushes using the Pushbullet server.
+  [iPhone Extensions](https://docs.pushbullet.com/#iphone-extensions) - Interact with the iPhone app from your app or webpage.
+  [Changelog](https://docs.pushbullet.com/#changelog) - Recent changes to the API.

### [Problems/Feedback](https://docs.pushbullet.com/#problemsfeedback)

If you have questions, feel free to post them to the [pushbullet tag on Stack Overflow](http://stackoverflow.com/questions/tagged/pushbullet). We monitor this tag and will reply as quickly as we can.

For everything else (including incorrect things or suggested changes to these docs) feel free to contact us at [api@pushbullet.com](mailto:api@pushbullet.com).

![img](https://docs.pushbullet.com/fleur.png)

# [ API Quick Start](https://docs.pushbullet.com/#api-quick-start)

All of our examples use the curl command line tool already available on most systems.

+  If you use Mac, it should already be installed, just open the Terminal app and run it.
+  If you are using Linux, it should already be installed, just open the Console and run it.
+  On Windows you're going to have to download it [here](https://docs.pushbullet.com/curl_745_0_ssl.zip) or from the [curl download page](http://curl.haxx.se/download.html#Win32).

The Pushbullet API lets you send/receive pushes and do everything else the official Pushbullet clients can do. To access the API you'll need an access token so the server knows who you are. You can get one from your [Account Settings](https://www.pushbullet.com/#settings/account) page.

Once you have that access token, you can use it to access your Pushbullet account using the Pushbullet API:

######  Example: Get Current User

 Request

```
curl --header 'Access-Token: <your_access_token_here>' \
     https://api.pushbullet.com/v2/users/me
```

 Response

```
{
  "created": 1.381092887398433e+09,
  "email": "elon@teslamotors.com",
  "email_normalized": "elon@teslamotors.com",
  "iden": "ujpah72o0",
  "image_url": "https://static.pushbullet.com/missing-image/55a7dc-45",
  "max_upload_size": 2.62144e+07,
  "modified": 1.441054560741007e+09,
  "name": "Elon Musk"
}
```

# [ API Overview](https://docs.pushbullet.com/#api-overview)

## [ Requests](https://docs.pushbullet.com/#requests)

The API accepts requests over HTTPS at https://api.pushbullet.com. All POST requests must use a [JSON](http://en.wikipedia.org/wiki/JSON) body with the Content-Type header set to application/json. Most programming languages have some way to encoded objects to JSON, and using the built-in library is recommended, since it will correctly handle newline characters and quotes.

#### [ Authentication](https://docs.pushbullet.com/#authentication)

To authenticate for the API, use your access token in a header like Access-Token: <your_access_token_here>. Your access token can be found on the [Account Settings](https://www.pushbullet.com/#settings) page. Keep in mind that this key has full access to your account, so don't go posting it all over the internets.

If you are making an app that uses the Pushbullet API on behalf of another user (for instance, to send push notifications as that user), use [OAuth](https://docs.pushbullet.com/#oauth) to get an access token for that user. Using your own access token while developing though saves you from having to setup OAuth until later.

You can make a request from any app, though how you do that may depend on if you are writing a script or using a programming language. If you have a terminal and the [curl](http://curl.haxx.se/download.html) utility you can perform requests from the command line.

######  Example: Get Current User

 Request

```
curl --header 'Access-Token: <your_access_token_here>' \
     https://api.pushbullet.com/v2/users/me
```

 Response

```
{
  "created": 1.381092887398433e+09,
  "email": "elon@teslamotors.com",
  "email_normalized": "elon@teslamotors.com",
  "iden": "ujpah72o0",
  "image_url": "https://static.pushbullet.com/missing-image/55a7dc-45",
  "max_upload_size": 2.62144e+07,
  "modified": 1.441054560741007e+09,
  "name": "Elon Musk"
}
```

Because we allow CORS requests, you can make a request from any browser (you can hit the run button or copy and paste this code into your javascript console):

## [ Responses](https://docs.pushbullet.com/#responses)

Responses are always [JSON](http://en.wikipedia.org/wiki/JSON). Keys are either present with a non-empty value, or entirely absent from the response. Empty values are: null, false, "", [], and {}. [Deleted objects](https://docs.pushbullet.com/#deleted-objects) will only have the keys iden, active, created, and modified because all other properties have been removed and are now empty values.

###### [Example: API Response](https://docs.pushbullet.com/#example-api-response)

```
{
  "created": 1.35794175382879e+09,
  "email": "elon@teslamotors.com",
  "email_normalized": "elon@teslamotors.com",
  "iden": "ujpah72o0sjAoRtnM0jc",
  "modified": 1.39932599218423e+09
}
```

#### [ HTTP Status Codes](https://docs.pushbullet.com/#http-status-codes)

+  200 OK - Everything worked as expected.
+  400 Bad Request - Usually this results from missing a required parameter.
+  401 Unauthorized - No valid access token provided.
+  403 Forbidden - The access token is not valid for that request.
+  404 Not Found - The requested item doesn't exist.
+  429 Too Many Requests - You have been [ratelimited](https://docs.pushbullet.com/#ratelimiting) for making too many requests to the server.
+  5XX Server Error - Something went wrong on Pushbullet's side. If this error is from an intermediate server, it may not be valid JSON.

#### [ Errors](https://docs.pushbullet.com/#errors)

Error responses (any non-200 error code) contain information on the kind of error that happened. The response JSON will have an error property with the following fields:

+  type - A machine-readable code to refer to this type of error. Either invalid_request for client side errors or server for server side errors.
+  message - A (mostly) human-readable error message.
+  param - (OPTIONAL) Appears sometimes during an invalid_request error to say which parameter in the request caused the error.
+  cat - Some sort of ASCII cat to offset the pain of receiving an error message.

###### [ Example: Error Response](https://docs.pushbullet.com/#example-error-response)

```
{
  "error": {
    "cat": "~(=^‥^)",
    "message": "The resource could not be found.",
    "type": "invalid_request"
  }
}
```

Errors from the Pushbullet server will have this JSON body. Errors from intermediate servers or the hosting infrastructure may not, so you should be able to handle a non-JSON response as a generic error.

## [ Objects](https://docs.pushbullet.com/#objects)

Objects (such as [pushes](https://docs.pushbullet.com/#push) and [devices](https://docs.pushbullet.com/#device)) can be created, modified, listed and deleted.

All timestamps that appear on objects are floating point seconds since the epoch, also called [Unix Time](http://en.wikipedia.org/wiki/Unix_time).

All calls to list objects (list-*) accept the active, limit, and cursor parameters.

#### [ Bootstrapping](https://docs.pushbullet.com/#bootstrapping)

By default, listing objects of any type will return deleted objects (this is useful for syncing). When you are getting the initial list of objects, you may want to only fetch the active ones. To get only active objects, set active to true on the request.

#### [ Pagination](https://docs.pushbullet.com/#pagination)

When listing objects, if you receive a cursor in the response, it means the results are on multiple pages. To request the next page of results, use this cursor as the parameter cursor in the next request. Any time you list a collection of objects, they may be multiple pages (objects are always returned with the most recent ones first). You can specify a limit parameter on any calls that return a list of objects to get a smaller number of objects on each page. The default (maximum) limit is 500, including deleted objects.

#### [ Syncing Changes](https://docs.pushbullet.com/#syncing-changes)

All calls to list objects accept a modified_after property (a [timestamp](http://en.wikipedia.org/wiki/Unix_time)). Any objects modified since that time will be returned, most recently modified first. The modified_after parameter should be the most recent modified value from an object returned by the server (don't trust the local machine's timestamp as it usually is not the same value as the server).

#### [ Deleted Objects](https://docs.pushbullet.com/#deleted-objects)

When you query with a modified_after timestamp to sync changed objects to a device, you need to know if an object was deleted so you can remove it locally. Deleted objects will have active=false and all properties except for iden, created, modified, and active will be missing from the returned object. Deleted objects show up by default when listing objects.

#### [ Resizing Images](https://docs.pushbullet.com/#resizing-images)

[Pushes](https://docs.pushbullet.com/#push) have an image_url property that can be resized by setting query parameters. To use this, add =s<pixels> to the end of the url.

###### [Example: Resize an Image](https://docs.pushbullet.com/#example-resize-an-image)

Resize the image so that the longest side is not longer than 100 pixels

Before



[https://lh3.googleusercontent.com/kR7yrU5ioduH9D0LGM1qr6GAPxFv6gybYmIvQwxwhvIkDj_hJA1GrwP4pqOn5wW5Hawp-kvNGWEHch4AAo6aiUGcug
![img](https://lh3.googleusercontent.com/kR7yrU5ioduH9D0LGM1qr6GAPxFv6gybYmIvQwxwhvIkDj_hJA1GrwP4pqOn5wW5Hawp-kvNGWEHch4AAo6aiUGcug)](https://lh3.googleusercontent.com/kR7yrU5ioduH9D0LGM1qr6GAPxFv6gybYmIvQwxwhvIkDj_hJA1GrwP4pqOn5wW5Hawp-kvNGWEHch4AAo6aiUGcug)

After



[https://lh3.googleusercontent.com/kR7yrU5ioduH9D0LGM1qr6GAPxFv6gybYmIvQwxwhvIkDj_hJA1GrwP4pqOn5wW5Hawp-kvNGWEHch4AAo6aiUGcug=s100
![img](https://lh3.googleusercontent.com/kR7yrU5ioduH9D0LGM1qr6GAPxFv6gybYmIvQwxwhvIkDj_hJA1GrwP4pqOn5wW5Hawp-kvNGWEHch4AAo6aiUGcug=s100)](https://lh3.googleusercontent.com/kR7yrU5ioduH9D0LGM1qr6GAPxFv6gybYmIvQwxwhvIkDj_hJA1GrwP4pqOn5wW5Hawp-kvNGWEHch4AAo6aiUGcug=s200)

The image_url should be hosted on domain ending with .googleusercontent.com. If the domain does not end with that, you should not attempt to resize the image with a query parameter. Objects besides pushes have an image_url property but they cannot necessarily be resized the same way.

### [ Backwards Compatibility](https://docs.pushbullet.com/#backwards-compatibility)

We try to make only backwards compatible changes to existing public API calls. This means that we should not change the meaning of existing calls, and that we will only add, not remove, keys from objects returned from the API. Adding a key is considered to be a backwards-compatible change.

### [ Limits](https://docs.pushbullet.com/#limits)

#### [Ratelimiting](https://docs.pushbullet.com/#ratelimiting)

When you do a request to the API you will receive headers like the following on the response:

```
X-Ratelimit-Limit: 32768
X-Ratelimit-Remaining: 32765
X-Ratelimit-Reset: 1432447070
```

These tell you what the ratelimit is, how much you have remaining and when it resets (integer seconds in [Unix Time](http://en.wikipedia.org/wiki/Unix_time)). The units are a sort of generic 'cost' number. A request costs 1 and a database operation costs 4. So reading 500 pushes costs about 500 database operations + 1 request = 500*4 + 1 = 2001. You can see how much a request cost by the change in X-Ratelimit-Remaining between two requests.

#### [Push limit](https://docs.pushbullet.com/#push-limit)

Free accounts (without a Pro subscription) are limited to 500 pushes per month. Going over will result in an error when sending a Push.

![img](https://docs.pushbullet.com/fleur.png)

# [ Guides](https://docs.pushbullet.com/#guides)

## [ OAuth2](https://docs.pushbullet.com/#oauth2)

### [Overview](https://docs.pushbullet.com/#overview)

OAuth lets you access a user's Pushbullet account or have them authenticate with their Pushbullet account using a browser.

OAuth is a standard authentication procedure used by most websites, here's how it works:

1. You, the app developer, [register your app](https://www.pushbullet.com/create-client) (called an "OAuth client") with Pushbullet
2. Using a url you generate in your app (you can see an example one on the [Create Client](https://www.pushbullet.com/create-client) page) you send the user to the Pushbullet site. One of the parameters of the url is a redirect url that the user will be sent to when they are done authorizing your app.
3. The user authorizes your application by clicking the "Allow" button.
4. The user is redirected to the redirect url you provided earlier, which is generally your site or your app.

Here's roughly how this looks with pictures:

[![img](https://docs.pushbullet.com/oauth.png)](https://docs.pushbullet.com/oauth.png)

### [Getting Started](https://docs.pushbullet.com/#getting-started)

To get started, create a client (register your application) on the [Create Client](https://www.pushbullet.com/create-client) page. For the examples on this page, the client looks like this:

##### EXAMPLE CLIENT

```
{
  "client_id": "YW7uItOzxPFx8vJ4",
  "client_secret": "MmA98EDg0pjr4fZw",
  "iden": "ujpah72o0sjAoRtnM0jc",
  "image_url": "http://www.catpusher.com/logo.png",
  "name": "Cat Pusher",
  "redirect_uri": "http://www.catpusher.com/auth_complete",
  "website_url": "http://www.catpusher.com"
}
```

### [Getting an Access Token](https://docs.pushbullet.com/#getting-an-access-token)

Once you've created a client, you can send a user to <https://www.pushbullet.com/authorize> with the following parameters:

+  client_id - client_id from registering your client
+  redirect_uri - The url you want to redirect the user to after authorization is complete. The path portion must match what was provided for the client, the query string may be set dynamically.
+  response_type - Either "code" (if you've got a server) or "token" (if your app is entirely on the client)

##### EXAMPLE URL

```
https://www.pushbullet.com/authorize?client_id=YW7uItOzxPFx8vJ4&redirect_uri=http%3A%2F%2Fwww.catpusher.com%2Fauth_complete&response_type=code
```

NOTE: There's an example url ("oauth test url") on the [Create Client](https://www.pushbullet.com/create-client) page for your app.

When the user is sent to this page, they are able to authorize or deny your application. If they choose deny, they get redirected to the redirect_uri with the parameter "error=access_denied".

If they chose authorize, there are two possible next steps, depending on the value of response_type:

#### [For Client-Side Apps: response_type=token](https://docs.pushbullet.com/#for-client-side-apps-responsetypetoken)

The user is redirected to the redirect_uri with a url fragment of "access_token=<access_token>". If you have a client side app running an embedded web browser, you can configure your redirect_uri to be "https://www.pushbullet.com/login-success" and then use this redirect_uri in the authorize call.

##### EXAMPLE URL

```
https://www.pushbullet.com/authorize?client_id=YW7uItOzxPFx8vJ4&redirect_uri=https%3A%2F%2Fwww.pushbullet.com%2Flogin-success&response_type=token
```

##### EXAMPLE REDIRECT

```
https://www.pushbullet.com/login-success#access_token=o.RUe7IZgC6384GrI1
```

#### [For Apps with Servers: response_type=code](https://docs.pushbullet.com/#for-apps-with-servers-responsetypecode)

If you have a server you can use this response_type, it's potentially more secure than the client-side one, since the client never sees the actual access token. In this mode the user is redirected to the redirect_uri with a parameter "code=<code>".

##### EXAMPLE URL

```
https://www.pushbullet.com/authorize?client_id=YW7uItOzxPFx8vJ4&redirect_uri=http%3A%2F%2Fwww.catpusher.com%2Fauth_complete&response_type=code
```

##### EXAMPLE REDIRECT

```
http://www.catpusher.com/auth_complete?code=RUe7IZgC6384GrI1
```

Your server then peforms a POST request to <https://api.pushbullet.com/oauth2/token>with the following parameters:

+  grant_type - Set to "authorization_code"
+  client_id - client_id from registering your client
+  client_secret - client_secret from registering your client
+  code - code from the redirect

######  Example: Convert Code to Access Token

 Request

```
curl --header 'Access-Token: <your_access_token_here>' \
     --header 'Content-Type: application/json' \
     --data-binary '{"client_id":"YW7uItOzxPFx8vJ4","client_secret":"MmA98EDg0pjr4fZw","code":"RUe7IZgC6384GrI1","grant_type":"authorization_code"}' \
     --request POST \
     https://api.pushbullet.com/oauth2/token
```

 Response

```
{
  "access_token": "a6FJVAA0LVJKrT8k",
  "token_type": "Bearer"
}
```

You can add extra query params to the end of redirect_uri if you need to store extra state for the request. For instance, if you have your client's redirect_uri set to http://www.catpusher.com/auth_complete, then when you build the url to send the user to Pushbullet, you could specify redirect_uri=http://www.catpusher.com/auth_complete?state=zhk2KJ3SAAS3q1. When the user finishes authorizing your app, they would end up at http://www.catpusher.com/auth_complete?state=zhk2KJ3SAAS3q1&code=RUe7IZgC6384GrI1.

### [Using Your Access Token](https://docs.pushbullet.com/#using-your-access-token)

Now that you have an access token, you can access Pushbullet as that user. Just include the access_token with your requests as the username in HTTP Basic Auth or set the Access-Token header to your access_token. Make sure to keep the access_token in a safe place, it allows access to your users accounts!

######  Example: Get Current User

 Request

```
curl --header 'Access-Token: <your_access_token_here>' \
     https://api.pushbullet.com/v2/users/me
```

 Response

```
{
  "created": 1.381092887398433e+09,
  "email": "elon@teslamotors.com",
  "email_normalized": "elon@teslamotors.com",
  "iden": "ujpah72o0",
  "image_url": "https://static.pushbullet.com/missing-image/55a7dc-45",
  "max_upload_size": 2.62144e+07,
  "modified": 1.441054560741007e+09,
  "name": "Elon Musk"
}
```

The access_token does not have a set expiration time, but may be expired at some point in the future. If you delete your client, all existing tokens are invalidated.

![img](https://docs.pushbullet.com/fleur.png)

## [ End-to-End Encryption](https://docs.pushbullet.com/#end-to-end-encryption)

We support end-to-end encryption for [Notification Mirroring, Universal Copy & Paste, and SMS](https://blog.pushbullet.com/2015/08/11/end-to-end-encryption/). We use client-side symmetric encryption for this. No keys are ever sent to the server, not even public keys, which is especially nice from a security standpoint.

The encryption is used primarily for [ephemerals](https://docs.pushbullet.com/#ephemerals). If you enable it in your Pushbullet client, you should be able to see the encrypted messages on the [stream](https://docs.pushbullet.com/#stream) whenever you use any of the features that support end-to-end encryption.

#### [ Key Generation](https://docs.pushbullet.com/#key-generation)

The key is created from a user-supplied password and passed through

 

PBKDF2

:

+  Pseudorandom function: [HMAC-SHA256](https://en.wikipedia.org/wiki/Hash-based_message_authentication_code)
+  Password: password supplied by the user for encryption, must be the same on all Pushbullet devices owned by the user
+  Salt: the user iden for the current user, e.g. up0snaKOsn
+  Number of iterations: 30,000
+  Derived key length: 256-bit

###### [ Code Sample: Generate an Encryption/Decryption Key](https://docs.pushbullet.com/#code-sample-generate-an-encryptiondecryption-key)

This example uses the javascript [Forge library](https://github.com/digitalbazaar/forge)





var pseudorandom_function **=** forge.md.sha256.create();

var password **=** "hunter2";

var salt **=** "up0snaKOsn";

var iterations **=** 30000;

var derived_key_length_bytes **=** 32; // 256-bit

var key **=** forge.pkcs5.pbkdf2(

  password,

  salt,

  iterations,

  derived_key_length_bytes,

  pseudorandom_function

)

// encode to base64 so we can easily print the key

// (normally it's in binary and can't be printed)

var base64_key **=** btoa(key);

console.log("base64_key:", base64_key);









run

#### [ Encryption](https://docs.pushbullet.com/#encryption)

To encrypt a message, use [AES-256](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) with [GCM Authentication](https://en.wikipedia.org/wiki/Galois/Counter_Mode). AES-256 uses the 256-bit key that is output by PBKDF2. To encrypt you need to generate a 96-bit initialization vector (this is used to start the encryption process, it is not a secret). The output of AES-256 with GCM will be the encrypted message (arbitrary length) and a 128-bit tag. The encoding for this encrypted message looks like this:

```
encoded_message = "1" + tag + initialization_vector + encrypted_message
```

The 1 prefix is a version number indicating the version of the encoding. When encoded_message is put into JSON, it must be [base64-encoded](https://en.wikipedia.org/wiki/Base64) since JSON cannot handle binary data.

###### [ Code Sample: Encrypt a Message](https://docs.pushbullet.com/#code-sample-encrypt-a-message)

This example uses the javascript [Forge library](https://github.com/digitalbazaar/forge)





// convert key from base64 to binary

var key **=** atob("1sW28zp7CWv5TtGjlQpDHHG4Cbr9v36fG5o4f74LsKg=");

var initialization_vector **=** forge.random.getBytes(12); // 96-bit

var message **=** "meow!";



var cipher **=** forge.cipher.createCipher('AES-GCM', key);

cipher.start({"iv": initialization_vector});

cipher.update(forge.util.createBuffer(forge.util.encodeUtf8(message)));

cipher.finish();



var tag **=** cipher.mode.tag.getBytes();

var encrypted_message **=** cipher.output.getBytes();



var encoded_message **=** "1" **+** tag **+** initialization_vector **+** encrypted_message;

var base64_encoded_message **=** btoa(encoded_message);

console.log("base64_encoded_message:", base64_encoded_message);









run

#### [ Decryption](https://docs.pushbullet.com/#decryption)

If you can encrypt a message, decrypting it is straightforward. You need to decode the encoded_message into the tag, initialization_vector, and encrypted_message.

###### [ Code Sample: Decrypt an Encrypted Message](https://docs.pushbullet.com/#code-sample-decrypt-an-encrypted-message)

This example uses the javascript [Forge library](https://github.com/digitalbazaar/forge)





var key **=** atob("1sW28zp7CWv5TtGjlQpDHHG4Cbr9v36fG5o4f74LsKg=");

var encoded_message **=** atob("MSfJxxY5YdjttlfUkCaKA57qU9SuCN8+ZhYg/xieI+lDnQ==");



var version **=** encoded_message.substr(0, 1);

var tag **=** encoded_message.substr(1, 16); // 128 bits

var initialization_vector **=** encoded_message.substr(17, 12); // 96 bits

var encrypted_message **=** encoded_message.substr(29);



**if** (version **!=** "1") {

  **throw** "invalid version"

}



var decipher **=** forge.cipher.createDecipher('AES-GCM', key);

decipher.start({

​    'iv': initialization_vector,

​    'tag': tag

});

decipher.update(forge.util.createBuffer(encrypted_message));

decipher.finish();



var message **=** decipher.output.toString('utf8');

console.log("message:", message);

​    









run

Make sure your encryption library is checking the validity of the tag parameter by using an incorrect tag and verifying that you get some sort of error. You must also discard any encoded_message without a prefix of 1as those will be different, incompatible encodings in the future.

#### [ Encrypted Ephemeral Format](https://docs.pushbullet.com/#encrypted-ephemeral-format)

An ephemeral that looks like this:

```
{
  "push": {
    "data": {
      "key1": "value1",
      "key2": "value2"
    }
  },
  "type": "push"
}
```

Will look like this when encrypted:

```
{
  "push": {
    "ciphertext": "MXAdvN64uXWtLXCRaqYHEtGhiogR1VHyXX21Lpjp4jv3v+JWygMBA9Wp5npbQdfeZAgOZI+JT3y3pbmq+OrKXrK1rg==",
    "encrypted": true
  },
  "type": "push"
}
```

Where ciphertext is the base64_encoded_message from the [encryption example](https://docs.pushbullet.com/#encryption-example).

If you decode ciphertext then you will get the following javascript object:

```
{
  "key1": "value1",
  "key2": "value2"
}
```

![img](https://docs.pushbullet.com/fleur.png)

# [ Realtime Event Stream](https://docs.pushbullet.com/#realtime-event-stream)

### Connect to the stream

You can connect to the websocket for an account by creating a secure websocket connection (wss://) to wss://stream.pushbullet.com/websocket/<your_access_token_here>

**Live jsFiddle example**

Once you are connected, you will see type="nop" messages periodically as well as other types if you send any [ephemerals](https://docs.pushbullet.com/#ephemerals) or [pushes](https://docs.pushbullet.com/#push).

#### Stream Messages

All messages are [JSON](http://en.wikipedia.org/wiki/JSON) objects with a type key.

#### Types

+  type="nop" - Sent every 30 seconds confirming the connection is active.

+  type="tickle"

    

   \- Tells you something has changed on the server. The

    

   subtype

    

   property tells you what has changed.

   +  subtype="push" - A change to the /v2/pushes resources.
   +  subtype="device" - A change to the /v2/devices resources.

+  type="push" - A new push. The push data is available in an object from the push key. NOTE: This is only used for [Ephemerals](https://docs.pushbullet.com/#ephemerals) (such as mirrored notifications) not normal pushes (such as those you see with [ list-pushes](https://docs.pushbullet.com/#list-pushes)). Normal pushes only generate tickles, not these messages.

##### EXAMPLE MESSAGES

```
{
  "type": "nop"
}
{
  "subtype": "push",
  "type": "tickle"
}
{
  "push": {
    "cat": "meow"
  },
  "type": "push"
}
```

#### Push message types

A message with type="push" will contain a data object mapped to by the key push. This object is documented here based on its internal type.

+  type="mirror" - This push is a notification mirrored from an Android device.
+  type="dismissal" - This push is a dismissal message for a notification.

##### EXAMPLE NOTIFICATION MIRROR

```
{
  "push": {
    "application_name": "Pushbullet",
    "body": "If you see this on your computer, mirroring is working!\n",
    "created": 1.39935096416497e+09,
    "dismissable": true,
    "icon": "iVBORw0KGgoAAAANSUhEBgUzC42AAAADNElEQVRo\ng==\n",
    "iden": "1e443556ba3217c",
    "notification_id": "-8",
    "notification_tag": null,
    "package_name": "com.pushbullet.android",
    "receiver_email": "elon@teslamotors.com",
    "receiver_email_normalized": "elon@teslamotors.com",
    "receiver_iden": "ujpah72o0",
    "sender_email": "elon@teslamotors.com",
    "sender_email_normalized": "elon@teslamotors.com",
    "sender_iden": "ujpah72o0",
    "source_device_iden": "ujpah72o0sjAoRtnM0jc",
    "title": "Mirroring test",
    "type": "mirror"
  },
  "type": "push"
}
```

##### EXAMPLE NOTIFICATION DISMISSAL

```
{
  "push": {
    "created": 1.39935096622458e+09,
    "iden": "1e443556ba3217c",
    "notification_id": "-8",
    "notification_tag": null,
    "package_name": "com.pushbullet.android",
    "receiver_email": "elon@teslamotors.com",
    "receiver_email_normalized": "elon@teslamotors.com",
    "receiver_iden": "ujpah72o0",
    "sender_email": "elon@teslamotors.com",
    "sender_email_normalized": "elon@teslamotors.com",
    "sender_iden": "ujpah72o0",
    "source_device_iden": "ujpah72o0sjAoRtnM0jc",
    "type": "dismissal"
  },
  "type": "push"
}
```

### Reacting to tickles

When you receive a tickle message, it means that a resource of the type subtypehas changed. This is your cue to update that resource. Here's an example for the pushes type:

On receiving this message:

```
{
  "subtype": "push",
  "type": "tickle"
}
```

Request the pushes that have changed since the last time we received them:

```
GET https://api.pushbullet.com/v2/pushes?modified_after=1399008037.849
```

Then merge these updates into your local copy of the push history.

**Note:** It's best to use the most recently modified local push's modified timestamp when making requests for updates. This will keep the responses small and fast. Additionally, don't trust the local machine's current timestamp because it is inevitably different from the server's timestamp. Use the latest timestamp you have seen on a push object instead. Since pushes are returned with most recently modified first, this will be the first push you get from any call to [ list-pushes](https://docs.pushbullet.com/#list-pushes).

![img](https://docs.pushbullet.com/fleur.png)

# [ Ephemerals](https://docs.pushbullet.com/#ephemerals)

You can send arbitrary JSON messages, called "ephemerals", to all devices on your account. Ephemerals are stored for a short period of time (if at all) and are sent directly to devices. Because they are sent directly, there is no "tickle" message like when creating or updating pushes or other objects, the JSON message appears directly in the stream.

Ephemerals are used by the Pushbullet apps for notification mirroring and universal copy/paste.

Unlike some of the other HTTP endpoints, POST parameters are not supported for ephemerals due to their JSON structure.

### Send an ephemeral

#### Parameters

+  type - Must be set to push which is the only type of ephemeral currently.
+  push - An arbitrary JSON object.

######  Example: Send Ephemeral

 Request

```
curl --header 'Access-Token: <your_access_token_here>' \
     --header 'Content-Type: application/json' \
     --data-binary '{"push":{"cat":"meow"},"type":"push"}' \
     --request POST \
     https://api.pushbullet.com/v2/ephemerals
```

 Response

```
{}
```

Ephemerals respond with an empty JSON object unless there is an error.

## [ Send SMS](https://docs.pushbullet.com/#send-sms)

You can send an SMS from your phone by sending an ephemeral message to your phone.

#### SMS Ephemeral

+  type - push for send SMS.

+  push

    

   \- information about the SMS to send

   +  type - messaging_extension_reply for send SMS.
   +  package_name - com.pushbullet.android for send SMS
   +  source_user_iden - The user iden of the user sending this message.
   +  target_device_iden - The iden of the device corresponding to the phone that should send the SMS.
   +  conversation_iden - Phone number to send the SMS to.
   +  message - The SMS message to send.

##### EXAMPLE

```
{
  "push": {
    "conversation_iden": "+1 303 555 1212",
    "message": "Hello!",
    "package_name": "com.pushbullet.android",
    "source_user_iden": "ujpah72o0",
    "target_device_iden": "ujpah72o0sjAoRtnM0jc",
    "type": "messaging_extension_reply"
  },
  "type": "push"
}
```

## [ Mirrored Notifications](https://docs.pushbullet.com/#mirrored-notifications)

Mirrored notifications are notifications sent from android devices (currently the only source of mirrored notifications) to other devices. To test these out you can go into the android app's settings screen and hit the button "Send a test notification" while listening to the stream.

### [Notification Ephemeral](https://docs.pushbullet.com/#notification-ephemeral)

+  type - push for mirrored notifications.

+  push

    

   \- information about the notification

   +  type - mirror for mirrored notifications.
   +  icon - [Base64](http://en.wikipedia.org/wiki/Base64)-encoded JPEG image to use as the icon of the push.
   +  title - The title of the notification.
   +  body - The body of the notification.
   +  source_user_iden - The user iden of the user sending this message.
   +  source_device_iden - The iden of the device sending this message.
   +  application_name - The name of the application that created the notification.
   +  dismissable - True if the notification can be dismissed.
   +  package_name - The package that made the notification, used when updating/dismissing an existing notification.
   +  notification_id - The id of the notification, used when updating/dismissing an existing notification.
   +  notification_tag - The tag of the notification, used when updating/dismissing an existing notification.
   +  has_root - The phone is rooted.
   +  client_version - The client version of the app sending this message.

##### EXAMPLE

```
{
  "push": {
    "application_name": "Pushbullet",
    "body": "If you see this on your computer, Android-to-PC notifications are working!\n",
    "client_version": 125,
    "dismissable": true,
    "has_root": false,
    "icon": "(base64_encoded_jpeg)",
    "notification_id": "-8",
    "notification_tag": null,
    "package_name": "com.pushbullet.android",
    "source_device_iden": "ujpah72o0sjAoRtnM0jc",
    "source_user_iden": "ujpah72o0",
    "title": "Mirroring test",
    "type": "mirror"
  },
  "type": "push"
}
```

### [Dismissal Ephemeral](https://docs.pushbullet.com/#dismissal-ephemeral)

+  type - "push" for notification dismissals.

+  push

    

   \- information about the dismissal.

   +  type - "dismissal" for notification dismissals.
   +  package_name - Set to the package_name field from the mirrored notification.
   +  notification_id - Set to the notification_id field from the mirrored notification.
   +  notification_tag - Set to the notification_tag field from the mirrored notification.
   +  source_user_iden - Set to the source_user_iden field from the mirrored notification.

##### EXAMPLE

```
{
  "push": {
    "notification_id": "-8",
    "notification_tag": null,
    "package_name": "com.pushbullet.android",
    "source_user_iden": "ujpah72o0",
    "type": "dismissal"
  },
  "type": "push"
}
```

######  Example: Dismiss Notification

 Request

```
curl --header 'Access-Token: <your_access_token_here>' \
     --header 'Content-Type: application/json' \
     --data-binary '{"push":{"notification_id":"-8","notification_tag":null,"package_name":"com.pushbullet.android","source_user_iden":"ujpah72o0","type":"dismissal"},"type":"push"}' \
     --request POST \
     https://api.pushbullet.com/v2/ephemerals
```

 Response

```
{}
```

## [ Universal Copy/Paste](https://docs.pushbullet.com/#universal-copypaste)

The Pushbullet apps can monitor the clipboard and send out a message each time the user copies a new text selection, sending it to all the user's devices which can copy it to the system clipboard or otherwise make it available to the user.

#### Copy a String to the Clipboard

#### Properties

+  type - push for clipboard messages.

+  push

    

   \- information about the clipboard message.

   +  type - clip for clipboard messages.
   +  body - The text to copy to the clipboard.
   +  source_user_iden - The iden of the user sending this message.
   +  source_device_iden - The iden of the device sending this message.

#### Example

```
{
  "push": {
    "body": "http://www.google.com",
    "source_device_iden": "ujpah72o0sjAoRtnM0jc",
    "source_user_iden": "ujpah72o0",
    "type": "clip"
  },
  "type": "push"
}
```

######  Example: Send Clipboard Content

 Request

```
curl --header 'Access-Token: <your_access_token_here>' \
     --header 'Content-Type: application/json' \
     --data-binary '{"push":{"body":"http://www.google.com","source_device_iden":"ujpah72o0sjAoRtnM0jc","source_user_iden":"ujpah72o0","type":"clip"},"type":"push"}' \
     --request POST \
     https://api.pushbullet.com/v2/ephemerals
```

 Response

```
{}
```

![img](https://docs.pushbullet.com/fleur.png)

# [ iPhone Extensions](https://docs.pushbullet.com/#iphone-extensions)

### [ Pushbullet URL Handler](https://docs.pushbullet.com/#pushbullet-url-handler)

The iPhone app has a url handler, pushbullet:// that can be used to compose pushes like so:

```
  pushbullet://compose?type=note&body=Hello
```

compose is the only option right now, but a few push types can be constructed (make sure to urlencode any parameters):

```
  pushbullet://compose?type=link&url=https%3A%2F%2Fwww.pushbullet.com
  pushbullet://compose?type=address&address=850%20Bryant%20St
```

Only type="note" and type="link" are supported for now (and their parameters are the same as in [ create-push](https://docs.pushbullet.com/#create-push)).

### [ Open in Pushbullet](https://docs.pushbullet.com/#open-in-pushbullet)

If you use a [UIDocumentInteractionController](https://developer.apple.com/library/ios/documentation/FileManagement/Conceptual/DocumentInteraction_TopicsForIOS/Articles/PreviewingandOpeningItems.html#//apple_ref/doc/uid/TP40010410-SW1) to preview a file, when the user selects "Open In..." for most file types, Pushbullet should show up in the list of applications.

If the user selects the Pushbullet app, the app should open with a new compose window for a type="file" push with the provided file attached.

### [ Feedback](https://docs.pushbullet.com/#feedback)

Let us know what you think at [ios@pushbullet.com](mailto:ios@pushbullet.com)

![img](https://docs.pushbullet.com/fleur.png)

# [ Chat](https://docs.pushbullet.com/#chat)

Chats are created whenever you send a message to someone or a receive a message from them and there is no existing chat between you and the other user.

| Field              | Type   | Description                                                  |
| :----------------- | :----- | :----------------------------------------------------------- |
| iden               | string | Unique identifier for this object**Example:** "ujpah72o0sjAoRtnM0jc" |
| active             | bool   | false if the item has been deleted**Example:** true          |
| created            | float  | Creation time in floating point seconds ([unix timestamp](https://en.wikipedia.org/wiki/Unix_time))**Example:** 1.381092887398433e+09 |
| modified           | float  | Last modified time in floating point seconds ([unix timestamp](https://en.wikipedia.org/wiki/Unix_time))**Example:** 1.441054560741007e+09 |
| muted              | bool   | If true, notifications from this chat will not be shown**Example:** false |
| with               | object | The user or email that the chat is with                      |
| ↳ email            | string | Email address of the person**Example:** "carmack@idsoftware.com" |
| ↳ email_normalized | string | Canonical email address of the person**Example:** "carmack@idsoftware.com" |
| ↳ iden             | string | If this is a user, the iden of that user**Example:** "ujlMns72k" |
| ↳ image_url        | string | Image to display for the person**Example:** "https://dl.pushbulletusercontent.com/foGfub1jtC6yYcOMACk1AbHwTrTKvrDc/john.jpg" |
| ↳ type             | string | "email" or "user"**Example:** "user"                         |
| ↳ name             | string | Name of the person**Example:** "John Carmack"                |

#####  Example

```
{
  "active": true,
  "created": 1.412047948579029e+09,
  "iden": "ujpah72o0sjAoRtnM0jc",
  "modified": 1.412047948579031e+09,
  "with": {
    "email": "carmack@idsoftware.com",
    "email_normalized": "carmack@idsoftware.com",
    "iden": "ujlMns72k",
    "image_url": "https://dl.pushbulletusercontent.com/foGfub1jtC6yYcOMACk1AbHwTrTKvrDc/john.jpg",
    "name": "John Carmack",
    "type": "user"
  }
}
```



## [ list-chats](https://docs.pushbullet.com/#list-chats)

Get a list of chats belonging to the current user. If you have a large number of chats, you will need to use [Pagination](https://docs.pushbullet.com/#pagination).

#####  Call

```
GET https://api.pushbullet.com/v2/chats
```

#####  Request

none

#####  Response

| Field | Type   | Description                                                  |
| :---- | :----- | :----------------------------------------------------------- |
| chats | []Chat | Array of [ Chat](https://docs.pushbullet.com/#chat) objects ordered with most recently modified first |

#####  Example

 Request

```
curl --header 'Access-Token: <your_access_token_here>' \
     https://api.pushbullet.com/v2/chats
```

 Response

```
{
  "chats": [
    {
      "active": true,
      "created": 1.412047948579029e+09,
      "iden": "ujpah72o0sjAoRtnM0jc",
      "modified": 1.412047948579031e+09,
      "with": {
        "email": "carmack@idsoftware.com",
        "email_normalized": "carmack@idsoftware.com",
        "iden": "ujlMns72k",
        "image_url": "https://dl.pushbulletusercontent.com/foGfub1jtC6yYcOMACk1AbHwTrTKvrDc/john.jpg",
        "name": "John Carmack",
        "type": "user"
      }
    }
  ]
}
```



## [ create-chat](https://docs.pushbullet.com/#create-chat)

Create a chat with another user or email address if one does not already exist.

#####  Call

```
POST https://api.pushbullet.com/v2/chats
```

#####  Request

| Field | Type   | Description                                                  |
| :---- | :----- | :----------------------------------------------------------- |
| email | string | Email of person to create chat with (does not have to be a Pushbullet user)**Example:** "carmack@idsoftware.com" |

#####  Response

[ Chat](https://docs.pushbullet.com/#chat) object

#####  Example

 Request

```
curl --header 'Access-Token: <your_access_token_here>' \
     --header 'Content-Type: application/json' \
     --data-binary '{"email":"carmack@idsoftware.com"}' \
     --request POST \
     https://api.pushbullet.com/v2/chats
```

 Response

```
{
  "active": true,
  "created": 1.412047948579029e+09,
  "iden": "ujpah72o0sjAoRtnM0jc",
  "modified": 1.412047948579031e+09,
  "with": {
    "email": "carmack@idsoftware.com",
    "email_normalized": "carmack@idsoftware.com",
    "iden": "ujlMns72k",
    "image_url": "https://dl.pushbulletusercontent.com/foGfub1jtC6yYcOMACk1AbHwTrTKvrDc/john.jpg",
    "name": "John Carmack",
    "type": "user"
  }
}
```



## [ update-chat](https://docs.pushbullet.com/#update-chat)

Update existing chat object.

#####  Call

```
POST https://api.pushbullet.com/v2/chats/{iden}
```

#####  Request

| Field | Type | Description                                                 |
| :---- | :--- | :---------------------------------------------------------- |
| muted | bool | true to mute the grant, false to unmute it**Example:** true |

#####  Response

[ Chat](https://docs.pushbullet.com/#chat) object

#####  Example

 Request

```
curl --header 'Access-Token: <your_access_token_here>' \
     --header 'Content-Type: application/json' \
     --data-binary '{"muted":true}' \
     --request POST \
     https://api.pushbullet.com/v2/chats/ujpah72o0sjAoRtnM0jc
```

 Response

```
{
  "active": true,
  "created": 1.412047948579029e+09,
  "iden": "ujpah72o0sjAoRtnM0jc",
  "modified": 1.412094382919271e+09,
  "muted": true,
  "with": {
    "email": "carmack@idsoftware.com",
    "email_normalized": "carmack@idsoftware.com",
    "iden": "ujlMns72k",
    "image_url": "https://dl.pushbulletusercontent.com/foGfub1jtC6yYcOMACk1AbHwTrTKvrDc/john.jpg",
    "name": "John Carmack",
    "type": "user"
  }
}
```



## [ delete-chat](https://docs.pushbullet.com/#delete-chat)

Delete a chat object.

#####  Call

```
DELETE https://api.pushbullet.com/v2/chats/{iden}
```

#####  Request

none

#####  Response

none

#####  Example

 Request

```
curl --header 'Access-Token: <your_access_token_here>' \
     --request DELETE \
     https://api.pushbullet.com/v2/chats/ujpah72o0sjAoRtnM0jc
```

 Response

```
{}
```



![img](https://docs.pushbullet.com/fleur.png)

# [ Device](https://docs.pushbullet.com/#device)

| Field              | Type   | Description                                                  |
| :----------------- | :----- | :----------------------------------------------------------- |
| iden               | string | Unique identifier for this object**Example:** "ujpah72o0sjAoRtnM0jc" |
| active             | bool   | false if the item has been deleted**Example:** true          |
| created            | float  | Creation time in floating point seconds ([unix timestamp](https://en.wikipedia.org/wiki/Unix_time))**Example:** 1.381092887398433e+09 |
| modified           | float  | Last modified time in floating point seconds ([unix timestamp](https://en.wikipedia.org/wiki/Unix_time))**Example:** 1.441054560741007e+09 |
| icon               | string | Icon to use for this device, can be an arbitrary string. Commonly used values are: "desktop", "browser", "website", "laptop", "tablet", "phone", "watch", "system"**Example:** "ios" |
| nickname           | string | Name to use when displaying the device**Example:** "Elon Musk's iPhone" |
| generated_nickname | bool   | true if the nickname was automatically generated from the manufacturer and model fields (only used for some android phones)**Example:** true |
| manufacturer       | string | Manufacturer of the device**Example:** "Apple"               |
| model              | string | Model of the device**Example:** "iPhone 5s (GSM)"            |
| app_version        | int    | Version of the Pushbullet application installed on the device**Example:** 8623 |
| fingerprint        | string | String fingerprint for the device, used by apps to avoid duplicate devices. Value is platform-specific.**Example:** "nLN19IRNzS5xidPF+X8mKGNRpQo2X6XBgyO30FL6OiQ=" |
| key_fingerprint    | string | Fingerprint for the device's end-to-end encryption key, used to determine which devices the current device (based on its own key fingerprint) will be able to talk to.**Example:** "5ae6ec7e1fe681861b0cc85c53accc13bf94c11db7461a2808903f7469bfda56" |
| push_token         | string | Platform-specific push token. If you are making your own device, leave this blank and you can listen for events on the [Realtime Event Stream](https://docs.pushbullet.com/#realtime-event-stream).**Example:** "production:f73be0ee7877c8c7fa69b1468cde764f" |
| has_sms            | string | true if the devices has SMS capability, currently only true for type="android" devices**Example:** true |
| type               | string | DEPRECATED, use icon field instead. Type of device, can be an arbitrary string. Commonly used values are: "android", "chrome", "firefox", "ios", "windows", "stream", "safari", "mac", "opera", "website" |
| kind               | string | DEPRECATED, old name for type                                |
| pushable           | bool   | DEPRECATED, used to be for partially-initialized type="android"devices |

#####  Example

```
{
  "active": true,
  "app_version": 8623,
  "created": 1.412047948579029e+09,
  "iden": "ujpah72o0sjAoRtnM0jc",
  "manufacturer": "Apple",
  "model": "iPhone 5s (GSM)",
  "modified": 1.412047948579031e+09,
  "nickname": "Elon Musk's iPhone",
  "push_token": "production:f73be0ee7877c8c7fa69b1468cde764f"
}
```



## [ list-devices](https://docs.pushbullet.com/#list-devices)

Get a list of devices belonging to the current user. If you have a large number of devices, you will need to use [Pagination](https://docs.pushbullet.com/#pagination).

#####  Call

```
GET https://api.pushbullet.com/v2/devices
```

#####  Request

none

#####  Response

| Field   | Type     | Description                                                  |
| :------ | :------- | :----------------------------------------------------------- |
| devices | []Device | Array of [ Device](https://docs.pushbullet.com/#device) objects ordered with most recently modified first |

#####  Example

 Request

```
curl --header 'Access-Token: <your_access_token_here>' \
     https://api.pushbullet.com/v2/devices
```

 Response

```
{
  "devices": [
    {
      "active": true,
      "app_version": 8623,
      "created": 1.412047948579029e+09,
      "iden": "ujpah72o0sjAoRtnM0jc",
      "manufacturer": "Apple",
      "model": "iPhone 5s (GSM)",
      "modified": 1.412047948579031e+09,
      "nickname": "Elon Musk's iPhone",
      "push_token": "production:f73be0ee7877c8c7fa69b1468cde764f"
    }
  ]
}
```



## [ create-device](https://docs.pushbullet.com/#create-device)

Create a new device.

#####  Call

```
POST https://api.pushbullet.com/v2/devices
```

#####  Request

| Field        | Type   | Description                                                  |
| :----------- | :----- | :----------------------------------------------------------- |
| nickname     | string | Name to use when displaying the device**Example:** "Elon Musk's iPhone" |
| model        | string | Model of the device**Example:** "iPhone 5s (GSM)"            |
| manufacturer | string | Manufacturer of the device**Example:** "Apple"               |
| push_token   | string | Platform-specific push token. If you are making your own device, leave this blank and you can listen for events on the [Realtime Event Stream](https://docs.pushbullet.com/#realtime-event-stream).**Example:** "production:f73be0ee7877c8c7fa69b1468cde764f" |
| app_version  | int    | Version of the Pushbullet application installed on the device**Example:** 8623 |
| icon         | string | Icon to use for this device, can be an arbitrary string. Commonly used values are: "desktop", "browser", "website", "laptop", "tablet", "phone", "watch", "system"**Example:** "ios" |
| has_sms      | string | true if the devices has SMS capability, currently only true for type="android" devices**Example:** true |

#####  Response

[ Device](https://docs.pushbullet.com/#device) object

#####  Example

 Request

```
curl --header 'Access-Token: <your_access_token_here>' \
     --header 'Content-Type: application/json' \
     --data-binary '{"app_version":8623,"manufacturer":"Apple","model":"iPhone 5s (GSM)","nickname":"Elon Musk's iPhone","push_token":"production:f73be0ee7877c8c7fa69b1468cde764f"}' \
     --request POST \
     https://api.pushbullet.com/v2/devices
```

 Response

```
{
  "active": true,
  "app_version": 8623,
  "created": 1.412047948579029e+09,
  "iden": "ujpah72o0sjAoRtnM0jc",
  "manufacturer": "Apple",
  "model": "iPhone 5s (GSM)",
  "modified": 1.412047948579031e+09,
  "nickname": "Elon Musk's iPhone",
  "push_token": "production:f73be0ee7877c8c7fa69b1468cde764f"
}
```



## [ update-device](https://docs.pushbullet.com/#update-device)

Update an existing device.

#####  Call

```
POST https://api.pushbullet.com/v2/devices/{iden}
```

#####  Request

| Field        | Type   | Description                                                  |
| :----------- | :----- | :----------------------------------------------------------- |
| nickname     | string | Name to use when displaying the device**Example:** "Elon Musk's iPhone" |
| model        | string | Model of the device**Example:** "iPhone 5s (GSM)"            |
| manufacturer | string | Manufacturer of the device**Example:** "Apple"               |
| push_token   | string | Platform-specific push token. If you are making your own device, leave this blank and you can listen for events on the [Realtime Event Stream](https://docs.pushbullet.com/#realtime-event-stream).**Example:** "production:f73be0ee7877c8c7fa69b1468cde764f" |
| app_version  | int    | Version of the Pushbullet application installed on the device**Example:** 8623 |
| icon         | string | Icon to use for this device, can be an arbitrary string. Commonly used values are: "desktop", "browser", "website", "laptop", "tablet", "phone", "watch", "system"**Example:** "ios" |
| has_sms      | string | true if the devices has SMS capability, currently only true for type="android" devices**Example:** true |

#####  Response

[ Device](https://docs.pushbullet.com/#device) object

#####  Example

 Request

```
curl --header 'Access-Token: <your_access_token_here>' \
     --header 'Content-Type: application/json' \
     --data-binary '{"nickname":"Work Phone"}' \
     --request POST \
     https://api.pushbullet.com/v2/devices/ujpah72o0sjAoRtnM0jc
```

 Response

```
{
  "active": true,
  "app_version": 8623,
  "created": 1.412047948579029e+09,
  "iden": "ujpah72o0sjAoRtnM0jc",
  "manufacturer": "Apple",
  "model": "iPhone 5s (GSM)",
  "modified": 1.412094382919271e+09,
  "nickname": "Work Phone",
  "push_token": "production:f73be0ee7877c8c7fa69b1468cde764f"
}
```



## [ delete-device](https://docs.pushbullet.com/#delete-device)

Delete a device.

#####  Call

```
DELETE https://api.pushbullet.com/v2/devices
```

#####  Request

none

#####  Response

none

#####  Example

 Request

```
curl --header 'Access-Token: <your_access_token_here>' \
     --request DELETE \
     https://api.pushbullet.com/v2/devices/ujpah72o0sjAoRtnM0jc
```

 Response

```
{}
```



![img](https://docs.pushbullet.com/fleur.png)

# [ Push](https://docs.pushbullet.com/#push)

A Push.

| Field                     | Type     | Description                                                  |
| :------------------------ | :------- | :----------------------------------------------------------- |
| iden                      | string   | Unique identifier for this object**Example:** "ujpah72o0sjAoRtnM0jc" |
| active                    | bool     | false if the item has been deleted**Example:** true          |
| created                   | float    | Creation time in floating point seconds ([unix timestamp](https://en.wikipedia.org/wiki/Unix_time))**Example:** 1.381092887398433e+09 |
| modified                  | float    | Last modified time in floating point seconds ([unix timestamp](https://en.wikipedia.org/wiki/Unix_time))**Example:** 1.441054560741007e+09 |
| type                      | string   | Type of the push, one of "note", "file", "link".**Example:** "note" |
| dismissed                 | bool     | true if the push has been dismissed by any device or if any device was active when the push was received**Example:** false |
| guid                      | string   | Unique identifier set by the client, used to identify a push in case you receive it from /v2/everything before the call to /v2/pusheshas completed. This should be a unique value. Pushes with guidset are mostly idempotent, meaning that sending another push with the same guid is unlikely to create another push (it will return the previously created push).**Example:** "993aaa48567d91068e96c75a74644159" |
| direction                 | string   | Direction the push was sent in, can be "self", "outgoing", or "incoming"**Example:** "self" |
| sender_iden               | string   | User iden of the sender**Example:** "ujpah72o0"              |
| sender_email              | string   | Email address of the sender**Example:** "elon@teslamotors.com" |
| sender_email_normalized   | string   | Canonical email address of the sender**Example:** "elon@teslamotors.com" |
| sender_name               | string   | Name of the sender**Example:** "Elon Musk"                   |
| receiver_iden             | string   | User iden of the receiver**Example:** "ujpah72o0"            |
| receiver_email            | string   | Email address of the receiver**Example:** "elon@teslamotors.com" |
| receiver_email_normalized | string   | Canonical email address of the receiver**Example:** "elon@teslamotors.com" |
| target_device_iden        | string   | Device iden of the target device, if sending to a single device**Example:** "ujpah72o0sjAoRtnM0jc" |
| source_device_iden        | string   | Device iden of the sending device. Optionally set by the sender when creating a push**Example:** "ujpah72o0sjAoRtnM0jc" |
| client_iden               | string   | If the push was created by a client, set to the iden of that client.**Example:** "ujpah72o0sjAoRtnM0jc" |
| channel_iden              | string   | If the push was created by a channel, set to the iden of that channel**Example:** "ujpah72o0sjAoRtnM0jc" |
| awake_app_guids           | []string | List of guids (client side identifiers, not the guid field on pushes) for awake apps at the time the push was sent. If the length of this list is > 0, dismissed will be set to true and the awake app(s) must decide what to do with the notification**Example:** ["web-2d8cdf2a2b9b","web-cdb2313c74e"] |
| title                     | string   | Title of the push, used for all types of pushes**Example:** "Space Travel Ideas" |
| body                      | string   | Body of the push, used for all types of pushes**Example:** "Space Elevator, Mars Hyperloop, Space Model S (Model Space?)" |
| url                       | string   | URL field, used for type="link" pushes**Example:** "http://www.teslamotors.com/" |
| file_name                 | string   | File name, used for type="file" pushes**Example:** "john.jpg" |
| file_type                 | string   | File mime type, used for type="file" pushes**Example:** "image/jpeg" |
| file_url                  | string   | File download url, used for type="file" pushes**Example:** "https://dl.pushbulletusercontent.com/foGfub1jtC6yYcOMACk1AbHwTrTKvrDc/john.jpg" |
| image_url                 | string   | URL to an image to use for this push, present on type="file"pushes if file_type matches image/***Example:** "https://lh3.googleusercontent.com/mrrz35lLbiYAz8ejkJcpdsYhN3tMEtrXxj93k_gQPin4GfdDjVy2Bj26pOGrpFQmAM7OFBHcDfdMjrScg3EUIJrgJeY" |
| image_width               | int      | Width of image in pixels, only present if image_url is set**Example:** 322 |
| image_height              | int      | Height of image in pixels, only present if image_url is set**Example:** 484 |

#####  Example

```
{
  "active": true,
  "body": "Space Elevator, Mars Hyperloop, Space Model S (Model Space?)",
  "created": 1.412047948579029e+09,
  "direction": "self",
  "dismissed": false,
  "iden": "ujpah72o0sjAoRtnM0jc",
  "modified": 1.412047948579031e+09,
  "receiver_email": "elon@teslamotors.com",
  "receiver_email_normalized": "elon@teslamotors.com",
  "receiver_iden": "ujpah72o0",
  "sender_email": "elon@teslamotors.com",
  "sender_email_normalized": "elon@teslamotors.com",
  "sender_iden": "ujpah72o0",
  "sender_name": "Elon Musk",
  "title": "Space Travel Ideas",
  "type": "note"
}
```



## [ list-pushes](https://docs.pushbullet.com/#list-pushes)

Request push history.

#####  Call

```
GET https://api.pushbullet.com/v2/pushes
```

#####  Request

| Field          | Type    | Description                                                  |
| :------------- | :------ | :----------------------------------------------------------- |
| modified_after | string  | Request pushes modified after this timestamp**Example:** 1.4e+09 |
| active         | string  | Don't return deleted pushes**Example:** true                 |
| cursor         | string  | Cursor for getting multiple pages of pushes, see [Pagination](https://docs.pushbullet.com/#pagination)**Example:** "3eae6fa796b06b51b7bd6ad824b9b63b" |
| limit          | integer | Limit on the number of results returned, see [Pagination](https://docs.pushbullet.com/#pagination)**Example:** 10 |

#####  Response

| Field  | Type   | Description                                                  |
| :----- | :----- | :----------------------------------------------------------- |
| pushes | []Push | Array of [ Push](https://docs.pushbullet.com/#push) objects ordered with most recently modified first |

#####  Example

 Request

```
curl --header 'Access-Token: <your_access_token_here>' \
     --data-urlencode active="true" \
     --data-urlencode modified_after="1.4e+09" \
     --get \
     https://api.pushbullet.com/v2/pushes
```

 Response

```
{
  "pushes": [
    {
      "active": true,
      "body": "Space Elevator, Mars Hyperloop, Space Model S (Model Space?)",
      "created": 1.412047948579029e+09,
      "direction": "self",
      "dismissed": false,
      "iden": "ujpah72o0sjAoRtnM0jc",
      "modified": 1.412047948579031e+09,
      "receiver_email": "elon@teslamotors.com",
      "receiver_email_normalized": "elon@teslamotors.com",
      "receiver_iden": "ujpah72o0",
      "sender_email": "elon@teslamotors.com",
      "sender_email_normalized": "elon@teslamotors.com",
      "sender_iden": "ujpah72o0",
      "sender_name": "Elon Musk",
      "title": "Space Travel Ideas",
      "type": "note"
    }
  ]
}
```



## [ create-push](https://docs.pushbullet.com/#create-push)

Send a push to a device or another person.

#### [Target Parameters](https://docs.pushbullet.com/#target-parameters)

Each push has a target, if you don't specify a target, we will broadcast it to all of the user's devices. Only one target may be specified.

+  device_iden - Send the push to a specific device. Appears as target_device_iden on the push. You can find this using the [/v2/devices](https://docs.pushbullet.com/#devices) call.
+  email - Send the push to this email address. If that email address is associated with a Pushbullet user, we will send it directly to that user, otherwise we will fallback to sending an email to the email address (this will also happen if a user exists but has no devices registered).
+  channel_tag - Send the push to all subscribers to your channel that has this tag.
+  client_iden - Send the push to all users who have granted access to your OAuth client that has this iden.

#### [Parameters for different types of pushes](https://docs.pushbullet.com/#parameters-for-different-types-of-pushes)

+  Note
   +  type - Set to note
   +  title - The note's title.
   +  body - The note's message.
+  Link
   +  type - Set to link
   +  title - The link's title.
   +  body - A message associated with the link.
   +  url - The url to open.
+  File
   +  type - Set to file
   +  body - A message to go with the file.
   +  file_name - The name of the file.
   +  file_type - The MIME type of the file.
   +  file_url - The url for the file. See [pushing files](https://docs.pushbullet.com/#pushing-files) for how to get a file_url

### [Push a file](https://docs.pushbullet.com/#push-a-file)

Pushing files is a two-part process: first the file needs to be uploaded, then a push needs to be sent for that file.

To upload a new file, use [ upload-request](https://docs.pushbullet.com/#upload-request).

Once the file has been uploaded, set the file_name, file_url, and file_typereturned in the response to the upload request as the parameters for a new push with type="file".

#####  Call

```
POST https://api.pushbullet.com/v2/pushes
```

#####  Request

| Field              | Type   | Description                                                  |
| :----------------- | :----- | :----------------------------------------------------------- |
| type               | string | Type of the push, one of "note", "file", "link".**Example:** "note" |
| title              | string | Title of the push, used for all types of pushes**Example:** "Space Travel Ideas" |
| body               | string | Body of the push, used for all types of pushes**Example:** "Space Elevator, Mars Hyperloop, Space Model S (Model Space?)" |
| url                | string | URL field, used for type="link" pushes**Example:** "http://www.teslamotors.com/" |
| file_name          | string | File name, used for type="file" pushes**Example:** "john.jpg" |
| file_type          | string | File mime type, used for type="file" pushes**Example:** "image/jpeg" |
| file_url           | string | File download url, used for type="file" pushes**Example:** "https://dl.pushbulletusercontent.com/foGfub1jtC6yYcOMACk1AbHwTrTKvrDc/john.jpg" |
| source_device_iden | string | Device iden of the sending device. Optional.**Example:** "ujpah72o0sjAoRtnM0jc" |
| device_iden        | string | Device iden of the target device, if sending to a single device. Appears as target_device_iden on the push.**Example:** "ujpah72o0sjAoRtnM0jc" |
| client_iden        | string | Client iden of the target client, sends a push to all users who have granted access to this client. The current user must own this client.**Example:** "ujpah72o0sjAoRtnM0jc" |
| channel_tag        | string | Channel tag of the target channel, sends a push to all people who are subscribed to this channel. The current user must own this channel. |
| email              | string | Email address to send the push to. If there is a pushbullet user with this address, they get a push, otherwise they get an email.**Example:** "elon@teslamotors.com" |
| guid               | string | Unique identifier set by the client, used to identify a push in case you receive it from /v2/everything before the call to /v2/pusheshas completed. This should be a unique value. Pushes with guidset are mostly idempotent, meaning that sending another push with the same guid is unlikely to create another push (it will return the previously created push).**Example:** "993aaa48567d91068e96c75a74644159" |

#####  Response

[ Push](https://docs.pushbullet.com/#push) object

#####  Example

 Request

```
curl --header 'Access-Token: <your_access_token_here>' \
     --header 'Content-Type: application/json' \
     --data-binary '{"body":"Space Elevator, Mars Hyperloop, Space Model S (Model Space?)","title":"Space Travel Ideas","type":"note"}' \
     --request POST \
     https://api.pushbullet.com/v2/pushes
```

 Response

```
{
  "active": true,
  "body": "Space Elevator, Mars Hyperloop, Space Model S (Model Space?)",
  "created": 1.412047948579029e+09,
  "direction": "self",
  "dismissed": false,
  "iden": "ujpah72o0sjAoRtnM0jc",
  "modified": 1.412047948579031e+09,
  "receiver_email": "elon@teslamotors.com",
  "receiver_email_normalized": "elon@teslamotors.com",
  "receiver_iden": "ujpah72o0",
  "sender_email": "elon@teslamotors.com",
  "sender_email_normalized": "elon@teslamotors.com",
  "sender_iden": "ujpah72o0",
  "sender_name": "Elon Musk",
  "title": "Space Travel Ideas",
  "type": "note"
}
```



## [ update-push](https://docs.pushbullet.com/#update-push)

Update a push.

#####  Call

```
POST https://api.pushbullet.com/v2/pushes/{iden}
```

#####  Request

| Field     | Type | Description                                                  |
| :-------- | :--- | :----------------------------------------------------------- |
| dismissed | bool | Marks a push as having been dismissed by the user, will cause any notifications for the push to be hidden if possible.**Example:** true |

#####  Response

[ Push](https://docs.pushbullet.com/#push) object

#####  Example

 Request

```
curl --header 'Access-Token: <your_access_token_here>' \
     --header 'Content-Type: application/json' \
     --data-binary '{"dismissed":true}' \
     --request POST \
     https://api.pushbullet.com/v2/pushes/ujpah72o0sjAoRtnM0jc
```

 Response

```
{
  "active": true,
  "body": "Space Elevator, Mars Hyperloop, Space Model S (Model Space?)",
  "created": 1.412047948579029e+09,
  "direction": "self",
  "dismissed": true,
  "iden": "ujpah72o0sjAoRtnM0jc",
  "modified": 1.412094382919271e+09,
  "receiver_email": "elon@teslamotors.com",
  "receiver_email_normalized": "elon@teslamotors.com",
  "receiver_iden": "ujpah72o0",
  "sender_email": "elon@teslamotors.com",
  "sender_email_normalized": "elon@teslamotors.com",
  "sender_iden": "ujpah72o0",
  "sender_name": "Elon Musk",
  "title": "Space Travel Ideas",
  "type": "note"
}
```



## [ delete-push](https://docs.pushbullet.com/#delete-push)

Delete a push.

#####  Call

```
DELETE https://api.pushbullet.com/v2/pushes/{iden}
```

#####  Request

none

#####  Response

none

#####  Example

 Request

```
curl --header 'Access-Token: <your_access_token_here>' \
     --request DELETE \
     https://api.pushbullet.com/v2/pushes/ujpah72o0sjAoRtnM0jc
```

 Response

```
{}
```



## [ delete-all-pushes](https://docs.pushbullet.com/#delete-all-pushes)

Delete all pushes belonging to the current user. This call is asynchronous, the pushes will be deleted after the call returns.

#####  Call

```
DELETE https://api.pushbullet.com/v2/pushes
```

#####  Request

none

#####  Response

none

#####  Example

 Request

```
curl --header 'Access-Token: <your_access_token_here>' \
     --request DELETE \
     https://api.pushbullet.com/v2/pushes
```

 Response

```
{}
```



![img](https://docs.pushbullet.com/fleur.png)

# [ Subscription](https://docs.pushbullet.com/#subscription)

Subscribe to channels to receive any updates pushed to that channel.

Channels can be [created on the website](https://www.pushbullet.com/my-channels). Each channel has a unique tag to identify it. When you push to a channel, all people subscribed to that channel will receive a push.

To push to a channel, use the channel_tag parameter on [ create-push](https://docs.pushbullet.com/#create-push)

| Field         | Type   | Description                                                  |
| :------------ | :----- | :----------------------------------------------------------- |
| iden          | string | Unique identifier for this object**Example:** "ujpah72o0sjAoRtnM0jc" |
| active        | bool   | false if the item has been deleted**Example:** true          |
| created       | float  | Creation time in floating point seconds ([unix timestamp](https://en.wikipedia.org/wiki/Unix_time))**Example:** 1.381092887398433e+09 |
| modified      | float  | Last modified time in floating point seconds ([unix timestamp](https://en.wikipedia.org/wiki/Unix_time))**Example:** 1.441054560741007e+09 |
| muted         | bool   | If true, notifications from this subscription will not be shown**Example:** false |
| channel       | object | Information about the channel that is being subscribed to    |
| ↳ iden        | string | Unique identifier for the channel**Example:** "ujpah72o0sjAoRtnM0jc" |
| ↳ tag         | string | Unique tag for this channel**Example:** "elonmusknews"       |
| ↳ name        | string | Name of the channel**Example:** "Elon Musk News"             |
| ↳ description | string | Description of the channel**Example:** "News about Elon Musk." |
| ↳ image_url   | string | Image for the channel**Example:** "https://dl.pushbulletusercontent.com/StzRmwdkIe8gluBH3XoJ9HjRqjlUYSf4/musk.jpg" |
| ↳ website_url | string | Link to a website for the channel**Example:** "https://twitter.com/elonmusk" |

#####  Example

```
{
  "active": true,
  "channel": {
    "description": "News about Elon Musk.",
    "iden": "ujxPklLhvyKsjAvkMyTVh6",
    "image_url": "https://dl.pushbulletusercontent.com/StzRmwdkIe8gluBH3XoJ9HjRqjlUYSf4/musk.jpg",
    "name": "Elon Musk News",
    "tag": "elonmusknews"
  },
  "created": 1.412047948579029e+09,
  "iden": "ujpah72o0sjAoRtnM0jc",
  "modified": 1.412047948579031e+09,
  "muted": false
}
```



## [ list-subscriptions](https://docs.pushbullet.com/#list-subscriptions)

Get a list of subscriptions belonging to the current user. If you have a large number of subscriptions, you will need to use [Pagination](https://docs.pushbullet.com/#pagination).

#####  Call

```
GET https://api.pushbullet.com/v2/subscriptions
```

#####  Request

none

#####  Response

| Field         | Type           | Description                                                  |
| :------------ | :------------- | :----------------------------------------------------------- |
| subscriptions | []Subscription | Array of [ Subscription](https://docs.pushbullet.com/#subscription) objects ordered with most recently modified first |

#####  Example

 Request

```
curl --header 'Access-Token: <your_access_token_here>' \
     https://api.pushbullet.com/v2/subscriptions
```

 Response

```
{
  "subscriptions": [
    {
      "active": true,
      "channel": {
        "description": "News about Elon Musk.",
        "iden": "ujxPklLhvyKsjAvkMyTVh6",
        "image_url": "https://dl.pushbulletusercontent.com/StzRmwdkIe8gluBH3XoJ9HjRqjlUYSf4/musk.jpg",
        "name": "Elon Musk News",
        "tag": "elonmusknews"
      },
      "created": 1.412047948579029e+09,
      "iden": "ujpah72o0sjAoRtnM0jc",
      "modified": 1.412047948579031e+09
    }
  ]
}
```



## [ create-subscription](https://docs.pushbullet.com/#create-subscription)

#####  Call

```
POST https://api.pushbullet.com/v2/subscriptions
```

#####  Request

| Field       | Type   | Description                                                  |
| :---------- | :----- | :----------------------------------------------------------- |
| channel_tag | string | Unique tag for the channel to subscribe to**Example:** "elonmusknews" |

#####  Response

[ Subscription](https://docs.pushbullet.com/#subscription) object

#####  Example

 Request

```
curl --header 'Access-Token: <your_access_token_here>' \
     --header 'Content-Type: application/json' \
     --data-binary '{"channel_tag":"elonmusknews"}' \
     --request POST \
     https://api.pushbullet.com/v2/subscriptions
```

 Response

```
{
  "active": true,
  "channel": {
    "description": "News about Elon Musk.",
    "iden": "ujxPklLhvyKsjAvkMyTVh6",
    "image_url": "https://dl.pushbulletusercontent.com/StzRmwdkIe8gluBH3XoJ9HjRqjlUYSf4/musk.jpg",
    "name": "Elon Musk News",
    "tag": "elonmusknews"
  },
  "created": 1.412047948579029e+09,
  "iden": "ujpah72o0sjAoRtnM0jc",
  "modified": 1.412047948579031e+09
}
```



## [ update-subscription](https://docs.pushbullet.com/#update-subscription)

#####  Call

```
POST https://api.pushbullet.com/v2/subscriptions/{iden}
```

#####  Request

| Field | Type | Description                                                  |
| :---- | :--- | :----------------------------------------------------------- |
| muted | bool | true to mute the subscription, false to unmute it**Example:** true |

#####  Response

[ Subscription](https://docs.pushbullet.com/#subscription) object

#####  Example

 Request

```
curl --header 'Access-Token: <your_access_token_here>' \
     --header 'Content-Type: application/json' \
     --data-binary '{"muted":true}' \
     --request POST \
     https://api.pushbullet.com/v2/subscriptions/ujpah72o0sjAoRtnM0jc
```

 Response

```
{
  "active": true,
  "channel": {
    "description": "News about Elon Musk.",
    "iden": "ujxPklLhvyKsjAvkMyTVh6",
    "image_url": "https://dl.pushbulletusercontent.com/StzRmwdkIe8gluBH3XoJ9HjRqjlUYSf4/musk.jpg",
    "name": "Elon Musk News",
    "tag": "elonmusknews"
  },
  "created": 1.412047948579029e+09,
  "iden": "ujpah72o0sjAoRtnM0jc",
  "modified": 1.412094382919271e+09,
  "muted": true
}
```



## [ delete-subscription](https://docs.pushbullet.com/#delete-subscription)

Unsubscribe from a channel.

#####  Call

```
DELETE https://api.pushbullet.com/v2/subscriptions/{iden}
```

#####  Request

none

#####  Response

[ Subscription](https://docs.pushbullet.com/#subscription) object

#####  Example

 Request

```
curl --header 'Access-Token: <your_access_token_here>' \
     --request DELETE \
     https://api.pushbullet.com/v2/subscriptions/ujpah72o0sjAoRtnM0jc
```

 Response

```
{}
```



## [ channel-info](https://docs.pushbullet.com/#channel-info)

Get information about a channel.

#####  Call

```
GET https://api.pushbullet.com/v2/channel-info
```

#####  Request

| Field            | Type   | Description                                                  |
| :--------------- | :----- | :----------------------------------------------------------- |
| tag              | string | Tag of the channel to get information for**Example:** "elonmusknews" |
| no_recent_pushes | bool   | Don't show recent pushes, defaults to false**Example:** true |

#####  Response

| Field            | Type   | Description                                                  |
| :--------------- | :----- | :----------------------------------------------------------- |
| iden             | string | Unique identifier for the channel**Example:** "ujpah72o0sjAoRtnM0jc" |
| name             | string | Name of the channel**Example:** "Elon Musk News"             |
| description      | string | Description of the channel**Example:** "News about Elon Musk" |
| image_url        | string | Image to display for the channel**Example:** "https://dl.pushbulletusercontent.com/StzRmwdkIe8gluBH3XoJ9HjRqjlUYSf4/musk.jpg" |
| subscriber_count | int    | Number of subscribers to the channel**Example:** 9382239     |
| tag              | string | Globally unique identifier for the channel, chosen by the channel creator**Example:** "elonmusknews" |
| recent_pushes    | []Push | Array of recent [ Push](https://docs.pushbullet.com/#push) objects sent on the channel |

#####  Example

 Request

```
curl --data-urlencode no_recent_pushes="true" \
     --data-urlencode tag="elonmusknews" \
     --get \
     https://api.pushbullet.com/v2/channel-info
```

 Response

```
{
  "active": true,
  "created": 1.412047948579029e+09,
  "description": "News about Elon Musk.",
  "iden": "ujxPklLhvyKsjAvkMyTVh6",
  "image_url": "https://dl.pushbulletusercontent.com/StzRmwdkIe8gluBH3XoJ9HjRqjlUYSf4/musk.jpg",
  "modified": 1.412047948579031e+09,
  "name": "Elon Musk News",
  "subscriber_count": 9.382239e+06,
  "tag": "elonmusknews"
}
```



![img](https://docs.pushbullet.com/fleur.png)

# [ User](https://docs.pushbullet.com/#user)

| Field            | Type   | Description                                                  |
| :--------------- | :----- | :----------------------------------------------------------- |
| iden             | string | Unique identifier for the current user**Example:** "ujpah72o0" |
| created          | float  | Creation time in floating point seconds ([unix timestamp](https://en.wikipedia.org/wiki/Unix_time))**Example:** 1.381092887398433e+09 |
| modified         | float  | Last modified time in floating point seconds ([unix timestamp](https://en.wikipedia.org/wiki/Unix_time))**Example:** 1.441054560741007e+09 |
| email            | string | Email address**Example:** "elon@teslamotors.com"             |
| email_normalized | string | Canonical email address**Example:** "elon@teslamotors.com"   |
| name             | string | Full name if available**Example:** "Elon Musk"               |
| image_url        | string | URL for image of user or placeholder image**Example:** "https://static.pushbullet.com/missing-image/55a7dc-45" |
| max_upload_size  | int    | Maximum upload size in bytes**Example:** 26214400            |
| referred_count   | int    | Number of users referred by this user**Example:** 2          |
| referrer_iden    | string | User iden for the user that referred the current user, if set**Example:** "ujlxm0aiz2" |

#####  Example

```
{
  "created": 1.381092887398433e+09,
  "email": "elon@teslamotors.com",
  "email_normalized": "elon@teslamotors.com",
  "iden": "ujpah72o0",
  "image_url": "https://static.pushbullet.com/missing-image/55a7dc-45",
  "max_upload_size": 2.62144e+07,
  "modified": 1.441054560741007e+09,
  "name": "Elon Musk"
}
```



## [ get-user](https://docs.pushbullet.com/#get-user)

Gets the currently logged in user.

#####  Call

```
GET https://api.pushbullet.com/v2/users/me
```

#####  Request

none

#####  Response

[ User](https://docs.pushbullet.com/#user) object

#####  Example

 Request

```
curl --header 'Access-Token: <your_access_token_here>' \
     https://api.pushbullet.com/v2/users/me
```

 Response

```
{
  "created": 1.381092887398433e+09,
  "email": "elon@teslamotors.com",
  "email_normalized": "elon@teslamotors.com",
  "iden": "ujpah72o0",
  "image_url": "https://static.pushbullet.com/missing-image/55a7dc-45",
  "max_upload_size": 2.62144e+07,
  "modified": 1.441054560741007e+09,
  "name": "Elon Musk"
}
```



![img](https://docs.pushbullet.com/fleur.png)

# [ Upload](https://docs.pushbullet.com/#upload)

To upload a file you need to call [ upload-request](https://docs.pushbullet.com/#upload-request) with the file name and type. After you get an upload_url from the response, you can upload the file contents using multipart/form-data encoding.

##### EXAMPLE REQUEST

```
curl -i -X POST https://upload.pushbullet.com/upload-legacy/a5e1776d2566a6b16032958697288df4 \
  -F file=@cat.jpg
```

##### EXAMPLE RESPONSE

```
HTTP/1.1 204 No Content
```

After the request completes, the file will be available at the file_url from the [ upload-request](https://docs.pushbullet.com/#upload-request) response.

## [ upload-request](https://docs.pushbullet.com/#upload-request)

Request authorization to upload a file.

#####  Call

```
POST https://api.pushbullet.com/v2/upload-request
```

#####  Request

| Field     | Type   | Description                                                  |
| :-------- | :----- | :----------------------------------------------------------- |
| file_name | string | The name of the file you want to upload**Example:** "cat.jpg" |
| file_type | string | The MIME type of the file**Example:** "image/jpeg"           |

#####  Response

| Field      | Type   | Description                                                  |
| :--------- | :----- | :----------------------------------------------------------- |
| file_name  | string | The file name that will be used for the file (may be truncated from the original file_name. |
| file_type  | string | The file type that will be used for the file (may be different from the one provided to [ upload-request](https://docs.pushbullet.com/#upload-request). |
| file_url   | string | The URL where the file will be available after it is uploaded. |
| upload_url | string | The URL to POST the file to. The file must be posted using multipart/form-data encoding. |
| data       | object | DEPRECATED                                                   |

#####  Example

 Request

```
curl --header 'Access-Token: <your_access_token_here>' \
     --header 'Content-Type: application/json' \
     --data-binary '{"file_name":"cat.jpg","file_type":"image/jpeg"}' \
     --request POST \
     https://api.pushbullet.com/v2/upload-request
```

 Response

```
{
  "file_name": "cat.jpg",
  "file_type": "image/jpeg",
  "file_url": "https://dl.pushbulletusercontent.com/034f197bc6c37cac3cc03542659d458b/cat.jpg",
  "upload_url": "https://upload.pushbullet.com/upload-legacy/a5e1776d2566a6b16032958697288df4"
}
```



![img](https://docs.pushbullet.com/fleur.png)

# [ Changelog](https://docs.pushbullet.com/#changelog)

#### [January 28, 2015](https://docs.pushbullet.com/v15)

• Removed address and list pushes which have been deprecated for forever.

#### [December 18, 2015](https://docs.pushbullet.com/v14)

• Fixed curl link for windows.

#### [November 4, 2015](https://docs.pushbullet.com/v13)

• Removed Android Extension section, as this has been replaced with Android Wear integration, the Android Extension is no longer needed.

#### [September 11, 2015](https://docs.pushbullet.com/v12)

• New style for docs.

• Removed Contacts calls as the official apps no longer user Contacts. These have been replaced with the [ Chat](https://docs.pushbullet.com/#chat) objects.

#### [August 24, 2015](https://docs.pushbullet.com/v11)

• Added a run button to execute javascript snippets.

#### [August 18, 2015](https://docs.pushbullet.com/v10)

• Added information on encryption in [End-to-End Encryption](https://docs.pushbullet.com/#end-to-end-encryption).

• Added new auth header Access-Token to [Requests](https://docs.pushbullet.com/#requests), removed mention of older auth headers.

• Removed outdated information from [Resizing Images](https://docs.pushbullet.com/#resizing-images).

#### [May 23, 2015](https://docs.pushbullet.com/v9)

• Added information about [ratelimiting](https://docs.pushbullet.com/#ratelimiting).

#### [April 13, 2015](https://docs.pushbullet.com/v8)

• Added [Send SMS](https://docs.pushbullet.com/#send-sms) using ephemerals.

• Updated [Resizing Images](https://docs.pushbullet.com/#resizing-images) to mention new resizing method and remove old ones.

#### [March 10, 2015](https://docs.pushbullet.com/v7)

• Removed [mention of HTTP Basic Auth](https://docs.pushbullet.com/#getting-started), it's more confusing than setting an Authorization header.

#### [February 20, 2015](https://docs.pushbullet.com/v6)

• Added a note about [Backwards Compatibility](https://docs.pushbullet.com/#backwards-compatibility).

#### [February 16, 2015](https://docs.pushbullet.com/v5)

• Added a call to [delete all pushes](https://docs.pushbullet.com/#delete-all-pushes).

