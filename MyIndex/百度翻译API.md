# 百度翻译API



目录：

[TOC]



## 1. 通用翻译 API 技术文档



### 1.1 接入方式

通用翻译 API 通过 HTTP 接口对外提供多语种互译服务。您只需要通过调用通用翻译 API，传入待翻译的内容，并指定要翻译的源语言（支持源语言语种自动检测）和目标语言种类，就可以得到相应的翻译结果。

+  通用翻译 API HTTP 地址：http://api.fanyi.baidu.com/api/trans/vip/translate

+  通用翻译 API HTTPS 地址：https://fanyi-api.baidu.com/api/trans/vip/translate

您需要向该地址通过 POST 或 GET 方法发送下列字段来访问服务

| 字段名 | 类型 | 必填参数 | 描述           | 备注                                                         |
| ------ | ---- | -------- | -------------- | ------------------------------------------------------------ |
| q      | TEXT | Y        | 请求翻译 query | UTF-8 编码                                                   |
| from   | TEXT | Y        | 翻译源语言     | [语言列表](https://api.fanyi.baidu.com/api/trans/product/apidoc#languageList) (可设置为 auto) |
| to     | TEXT | Y        | 译文语言       | [语言列表](https://api.fanyi.baidu.com/api/trans/product/apidoc#languageList) (不可设置为 auto) |
| appid  | TEXT | Y        | APP ID         | 可在[管理控制台](https://api.fanyi.baidu.com/api/trans/product/desktop?req=developer)查看 |
| salt   | TEXT | Y        | 随机数         |                                                              |
| sign   | TEXT | Y        | 签名           | appid+q+salt + 密钥 的 MD5 值                                |

+  签名是为了保证调用安全，使用 MD5 算法生成的一段字符串，生成的签名长度为 32 位，签名中的英文字符均为小写格式

+  为保证翻译质量，请将单次请求长度控制在 6000 bytes 以内。（汉字约为 2000 个）

+  签名生成方法如下：
   +  1、将请求参数中的 APPID (appid), 翻译 query (q, 注意为 UTF-8 编码), 随机数 (salt), 以及平台分配的密钥 (可在[管理控制台](https://api.fanyi.baidu.com/api/trans/product/desktop?req=developer)查看)
   +  按照 appid+q+salt + 密钥 的顺序拼接得到字符串 1。]
   +  对字符串 1 做 md5，得到 32 位小写的 sign。

+  注意:
   +  1、请先将需要翻译的文本转换为 UTF-8 编码
   +  2、在发送 HTTP 请求之前需要对各字段做 [URL encode](https://api.fanyi.baidu.com/api/trans/product/apidoc#appendix)。
   +  3、在生成签名拼接 appid+q+salt + 密钥 字符串时，q 不需要做 URL encode，在生成签名之后，发送 HTTP 请求之前才需要对要发送的待翻译文本字段 q 做 URL encode。



### 1.2 返回结果

+ 是 json 格式，包含以下字段：

| 字段名       | 类型       | 描述       |
| ------------ | ---------- | ---------- |
| from         | TEXT       | 翻译源语言 |
| to           | TEXT       | 译文语言   |
| trans_result | MIXED LIST | 翻译结果   |
| src          | TEXT       | 原文       |
| dst          | TEXT       | 译文       |

+  其中 trans_result 包含了 src 和 dst 字段。

   


### 1.3 实例
+ 例：将 apple 从英文翻译成中文：

+ 1. 请求参数：
   +  q=apple
  
   +  from=en
  
   +  to=zh
  
 +  appid=2015063000000001
  
   +  salt=1435660288
  
   +  平台分配的密钥: 12345678
  
      
  
+  2. 生成 sign：

   + 拼接字符串 1
      + 拼接 appid=2015063000000001+q=apple+salt=1435660288+ 密钥 = 12345678
      + 得到字符串 1 =2015063000000001apple143566028812345678
   + 计算签名 sign（对字符串 1 做 md5 加密，注意计算 md5 之前，串 1 必须为 UTF-8 编码）
      + sign=md5(2015063000000001apple143566028812345678)
      
      + sign=f89f9594663708c1605f3d736d01d2d4
      
         

+  完整请求为：<http://api.fanyi.baidu.com/api/trans/vip/translate?q=apple&from=en&to=zh&appid=2015063000000001&salt=1435660288&sign=f89f9594663708c1605f3d736d01d2d4>

+  也可以使用 POST 方法传送需要的参数。



### 1.4 语言列表

+  源语言语种不确定时可设置为 auto，目标语言语种不可设置为 auto。

| 语言简写 | 名称         |
| -------- | ------------ |
| auto     | 自动检测     |
| zh       | 中文         |
| en       | 英语         |
| yue      | 粤语         |
| wyw      | 文言文       |
| jp       | 日语         |
| kor      | 韩语         |
| fra      | 法语         |
| spa      | 西班牙语     |
| th       | 泰语         |
| ara      | 阿拉伯语     |
| ru       | 俄语         |
| pt       | 葡萄牙语     |
| de       | 德语         |
| it       | 意大利语     |
| el       | 希腊语       |
| nl       | 荷兰语       |
| pl       | 波兰语       |
| bul      | 保加利亚语   |
| est      | 爱沙尼亚语   |
| dan      | 丹麦语       |
| fin      | 芬兰语       |
| cs       | 捷克语       |
| rom      | 罗马尼亚语   |
| slo      | 斯洛文尼亚语 |
| swe      | 瑞典语       |
| hu       | 匈牙利语     |
| cht      | 繁体中文     |
| vie      | 越南语       |



#### 1.4.1 错误码列表

+  当翻译结果无法正常返回时，请参考下表处理：

| 错误码 | 含义               | 解决方法                                                     |
| ------ | ------------------ | ------------------------------------------------------------ |
| 52000  | 成功               |                                                              |
| 52001  | 请求超时           | 重试                                                         |
| 52002  | 系统错误           | 重试                                                         |
| 52003  | 未授权用户         | 检查您的 [appid](https://api.fanyi.baidu.com/api/trans/product/desktop?req=developer) 是否正确，或者服务是否开通 |
| 54000  | 必填参数为空       | 检查是否少传[参数](https://api.fanyi.baidu.com/api/trans/product/apidoc#joinFile) |
| 54001  | 签名错误           | 请检查您的签名生成方法                                       |
| 54003  | 访问频率受限       | 请降低您的调用频率                                           |
| 54004  | 账户余额不足       | 请前往[管理控制台](https://api.fanyi.baidu.com/api/trans/product/desktop)为账户充值 |
| 54005  | 长 query 请求频繁  | 请降低长 query 的发送频率，3s 后再试                         |
| 58000  | 客户端 IP 非法     | 检查个人资料里填写的 [IP 地址](https://api.fanyi.baidu.com/api/trans/product/desktop?req=developer) 是否正确 可前往管理控制平台修改 IP 限制，IP 可留空 |
| 58001  | 译文语言方向不支持 | 检查译文语言是否在语言列表里                                 |
| 58002  | 服务当前已关闭     | 请前往[管理控制台](https://api.fanyi.baidu.com/api/trans/product/desktop)开启服务 |
| 90107  | 认证未通过或未生效 | 请前往[我的认证](https://api.fanyi.baidu.com/api/trans/product/myIdentify)查看认证进度 |



#### 1.4.2 各语言 DEMO

+  PHP 版（[点击下载](https://fanyiapp.cdn.bcebos.com/api/demo/php.zip)）

+  JS 版（[点击下载](https://fanyiapp.cdn.bcebos.com/api/demo/js-sdk.zip)）

+  Python 版（[点击下载](https://fanyiapp.cdn.bcebos.com/api/demo/python.zip)）

+  C 版（[点击下载](https://fanyiapp.cdn.bcebos.com/api/demo/C.zip)）

+  Java 版（[点击下载](https://fanyiapp.cdn.bcebos.com/api/demo/java.zip)）

+  C# 版（[点击下载](https://fanyiapp.cdn.bcebos.com/api/demo/Baidu_Trans_C_Sharp.cs)）

   

```python
#/usr/bin/env python
#coding=utf8
 
import httplib
import md5
import urllib
import random

appid = '' #你的appid
secretKey = '' #你的密钥

 
httpClient = None
myurl = '/api/trans/vip/translate'
q = 'apple'
fromLang = 'en'
toLang = 'zh'
salt = random.randint(32768, 65536)

sign = appid+q+str(salt)+secretKey
m1 = md5.new()
m1.update(sign)
sign = m1.hexdigest()
myurl = myurl+'?appid='+appid+'&q='+urllib.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
 
try:
    httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
    httpClient.request('GET', myurl)
 
    #response是HTTPResponse对象
    response = httpClient.getresponse()
    print response.read()
except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()

```



### 1.5 常见问题

1. 如何在一次请求中翻译多个单词或者多段文本？

>  您可以在发送的字段 q 中用换行符（在多数编程语言中为转义符号 \n。其中 \n 是需要能被程序解析出来的换行符而不是字符串 \n，您可以将 \n 用双引号包围 ）或者回车换行来分隔要翻译的多个单词或者多段文本，这样您就能得到多段文本独立的翻译结果了。注意在发送请求之前需对 q 字段做 URL encode！

2. 什么是 URL encode？

>  网络标准 RFC 1738 规定了 URL 中只能使用英文字母、阿拉伯数字和某些标点符号，不能使用其他文字和符号。如果您需要翻译的文本里面出现了不在该规定范围内的字符（比如中文），需要通过 URL encode 将需要翻译的文本做 URL 编码才能发送 HTTP 请求。大部分编程语言都有现成的 URL encode 函数，具体使用方法可以针对您使用的编程语言自行搜索。

3. 为什么我的请求总是返回错误码 54001？

>  54001 表示签名错误，请检查您的签名生成方法是否正确。
>  应该对 appid+q+salt + 密钥 拼接成的字符串做 MD5 得到 32 位小写的 sign。确保要翻译的文本 q 为 UTF-8 编码。
>
>  注意在生成签名拼接 appid+q+salt + 密钥 字符串时，q 不需要做 URL encode，在生成签名之后，发送 HTTP 请求之前才需要对要发送的待翻译文本字段 q 做 URL encode。
>  如果您无法确认自己生成签名的结果是否正确，可以将您生成的签名结果和在 <https://md5jiami.51240.com/> 中生成的常规 md5 加密 - 32 位小写签名结果对比。





## 2. 垂直领域翻译 API 技术文档

### 2.1 接口地址

+  HTTP 地址：<http://api.fanyi.baidu.com/api/trans/vip/fieldtranslate>

+  HTTPS 地址：<https://fanyi-api.baidu.com/api/trans/vip/fieldtranslate>



### 2.2 参数说明

| 字段名 | 类型 | 必填参数 | 描述           | 备注                                                         |
| ------ | ---- | -------- | -------------- | ------------------------------------------------------------ |
| q      | TEXT | Y        | 请求翻译 query | UTF-8 编码                                                   |
| appid  | INT  | Y        | APP ID         | 可在[管理控制台](https://api.fanyi.baidu.com/api/trans/product/desktop?req=developer)查看 |
| salt   | INT  | Y        | 随机数         |                                                              |
| domain | TEXT | Y        | 翻译领域类型   | 具体查看描述                                                 |
| sign   | TEXT | Y        | 签名           | appid+q+salt+domain + 密钥 的 MD5 值                         |

+  domain 领域支持范围：

| 支持传入值  | 描述         | 支持语言方向                |
| ----------- | ------------ | --------------------------- |
| electronics | 电子科技领域 | 中文 --> 英语               |
| mechanics   | 水利机械领域 | 中文 --> 英语               |
| medicine    | 生物医药领域 | 中文 --> 英语 英语 --> 中文 |

+  签名是为了保证调用安全，使用 MD5 算法生成的一段字符串，生成的签名长度为 32 位，签名中的英文字符均为小写格式.。
+  为保证检测质量，请将单次请求长度控制在 2000 bytes 以内。

+  签名生成方法如下：
   +  1、将请求参数中的 APPID (appid), 检测 query (q, 注意为 UTF-8 编码), 随机数 (salt), 支持翻译领域 (domain), 以及平台分配的密钥 (可在[管理控制台](https://api.fanyi.baidu.com/api/trans/product/desktop?req=developer)查看)。
   +  按照 appid+q+salt+domain + 密钥 的顺序拼接得到字符串 1。
   +  2、对字符串 1 做 MD5，得到 32 位小写的 sign。

+  注意:

   +  1、请先将需要翻译的文本转换为 UTF-8 编码

   +  2、在发送 HTTP 请求之前需要对各字段做 [URL encode](https://api.fanyi.baidu.com/api/trans/product/apidoc#appendix)。

   +  3、在生成签名拼接 appid+q+salt+domain + 密钥 字符串时，q 不需要做 URL encode，在生成签名之后，发送 HTTP 请求之前才需要对要发送的待检测文本字段 q 做 URL encode。

   +  4、支持 post、get 方式传输，post 传输时 Content-Type 指定 application/x-www-form-urlencoded。

   +  5、科技电子、水利机械两个领域仅支持中到英，如设置语言方向为英到中，则默认输出通用翻译结果；生物医药领域可支持中到英和英到中两种语言方向。

      

### 2.3 返回结果

+  返回结果是 json 格式，包含以下字段：

| 字段名       | 类型       | 描述       |
| ------------ | ---------- | ---------- |
| from         | TEXT       | 翻译源语言 |
| to           | TEXT       | 译文语言   |
| trans_result | MIXED LIST | 翻译结果   |
| src          | TEXT       | 原文       |
| dst          | TEXT       | 译文       |



### 2.4 语种列表

+  源语言语种不确定时可设置为 auto，目标语言语种不可设置为 auto。

| 语言简写 | 名称     |
| -------- | -------- |
| auto     | 自动检测 |
| zh       | 中文     |
| en       | 英语     |



### 2.5 错误码列表

+  当翻译结果无法正常返回时，请参考下表处理：

| 错误码 | 含义               | 解决方法                                                     |
| ------ | ------------------ | ------------------------------------------------------------ |
| 52001  | 请求超时           | 重试                                                         |
| 52002  | 系统错误           | 重试                                                         |
| 52003  | 未授权用户         | 检查您的 [appid](https://api.fanyi.baidu.com/api/trans/product/desktop?req=developer) 是否正确，或者服务是否开通 |
| 54000  | 必填参数为空       | 检查是否少传[参数](https://api.fanyi.baidu.com/api/trans/product/apidoc#joinFile) |
| 54001  | 签名错误           | 请检查您的签名生成方法                                       |
| 54003  | 访问频率受限       | 请降低您的调用频率                                           |
| 54004  | 账户余额不足       | 请前往[管理控制台](https://api.fanyi.baidu.com/api/trans/product/desktop)为账户充值 |
| 54005  | 长 query 请求频繁  | 请降低长 query 的发送频率，3s 后再试                         |
| 58000  | 客户端 IP 非法     | 检查个人资料里填写的 [IP 地址](https://api.fanyi.baidu.com/api/trans/product/desktop?req=developer) 是否正确 可前往管理控制平台修改 IP 限制，IP 可留空 |
| 58001  | 译文语言方向不支持 | 检查译文语言是否在语言列表里                                 |
| 58002  | 服务当前已关闭     | 请前往[管理控制台](https://api.fanyi.baidu.com/api/trans/product/desktop)开启服务 |





## 3. 定制化翻译 API 技术文档



### 3.1 接入方式

+  定制化翻译 API 通过 HTTP 接口对外提供多语种互译服务。您只需要通过调用定制化翻译 API，传入待翻译的内容，并指定要翻译的源语言和目标语言种类，就可以得到相应的翻译结果。

+  定制化翻译 API HTTP 地址：http://api.fanyi.baidu.com/api/trans/private/translate

+  定制化翻译 API HTTPS 地址：https://fanyi-api.baidu.com/api/trans/private/translate

+  您需要向该地址通过 POST 或 GET 方法发送下列字段来访问服务

| 字段名 | 类型 | 必填参数 | 描述           | 备注                                                         |
| ------ | ---- | -------- | -------------- | ------------------------------------------------------------ |
| q      | TEXT | Y        | 请求翻译 query | UTF-8 编码                                                   |
| from   | TEXT | Y        | 翻译源语言     | [语言列表](https://api.fanyi.baidu.com/api/trans/product/apidoc#cuslanguageList) |
| to     | TEXT | Y        | 译文语言       | [语言列表](https://api.fanyi.baidu.com/api/trans/product/apidoc#cuslanguageList) |
| appid  | INT  | Y        | APP ID         | 可在[管理控制台](https://api.fanyi.baidu.com/api/trans/product/desktop?req=developer)查看 |
| salt   | INT  | Y        | 随机数         |                                                              |
| sign   | TEXT | Y        | 签名           | appid+q+salt + 密钥 的 MD5 值                                |

+  签名是为了保证调用安全，使用 MD5 算法生成的一段字符串，生成的签名长度为 32 位，签名中的英文字符均为小写格式

+  为保证翻译质量，请控制请求频次，并将单次请求长度控制在 6000 bytes 以内。（汉字约为 2000 个）

+  签名生成方法如下：
   +  1、将请求参数中的 APPID (appid), 翻译 query (q, 注意为 UTF-8 编码), 随机数 (salt), 以及平台分配的密钥 (可在[管理控制台](https://api.fanyi.baidu.com/api/trans/product/desktop?req=developer)查看)
   +  按照 appid+q+salt + 密钥 的顺序拼接得到字符串 1。
   +  2、对字符串 1 做 md5，得到 32 位小写的 sign。
+  注意:
   +  1、请先将需要翻译的文本转换为 UTF-8 编码
   +  2、在发送 HTTP 请求之前需要对各字段做 [URL encode](https://api.fanyi.baidu.com/api/trans/product/apidoc#cusappendix)。
   +  3、在生成签名拼接 appid+q+salt + 密钥 字符串时，q 不需要做 URL encode，在生成签名之后，发送 HTTP 请求之前才需要对要发送的待翻译文本字段 q 做 URL encode。



### 3.2 返回结果

+  json 格式，包含以下字段：

| 字段名       | 类型       | 描述       |
| ------------ | ---------- | ---------- |
| from         | TEXT       | 翻译源语言 |
| to           | TEXT       | 译文语言   |
| trans_result | MIXED LIST | 翻译结果   |
| src          | TEXT       | 原文       |
| dst          | TEXT       | 译文       |

+  其中 trans_result 包含了 src 和 dst 字段。



### 3.3 实例

+  例：将 apple 从英文翻译成中文：

+  1. 请求参数：

   +  q=apple

   +  from=en

   +  to=zh

   +  appid=2015063000000001

   +  salt=1435660288

   +  平台分配的密钥: 12345678

      

+  2. 生成 sign：

   +  拼接字符串 1

      +  拼接 appid=2015063000000001+q=apple+salt=1435660288+ 密钥 = 12345678
      +  得到字符串 1 =2015063000000001apple143566028812345678

   +  计算签名 sign（对字符串 1 做 md5 加密，注意计算 md5 之前，串 1 必须为 UTF-8 编码）

      +  sign=md5(2015063000000001apple143566028812345678)

      +  sign=f89f9594663708c1605f3d736d01d2d4

         

+  完整请求为：<http://api.fanyi.baidu.com/api/trans/private/translate?q=apple&from=en&to=zh&appid=2015063000000001&salt=1435660288&sign=f89f9594663708c1605f3d736d01d2d4>

+  也可以使用 POST 方法传送需要的参数。



### 3.3 语言列表

+  定制化翻译 API 语言方向目前只支持中文和英文。

| 语言简写 | 名称 |
| -------- | ---- |
| zh       | 中文 |
| en       | 英语 |

#### 3.3.1 错误码列表

+  当翻译结果无法正常返回时，请参考下表处理：

| 错误码 | 含义               | 解决方法                                                     |
| ------ | ------------------ | ------------------------------------------------------------ |
| 52000  | 成功               |                                                              |
| 52001  | 请求超时           | 重试                                                         |
| 52002  | 系统错误           | 重试                                                         |
| 52003  | 未授权用户         | 检查您的 [appid](https://api.fanyi.baidu.com/api/trans/product/desktop?req=developer) 是否正确，或者服务是否开通 |
| 54000  | 必填参数为空       | 检查是否少传[参数](https://api.fanyi.baidu.com/api/trans/product/apidoc#cusjoinFile) |
| 54001  | 签名错误           | 请检查您的签名生成方法                                       |
| 54003  | 访问频率受限       | 请降低您的调用频率                                           |
| 54004  | 账户余额不足       | 请前往[管理控制平台](https://api.fanyi.baidu.com/api/trans/product/desktop)为账户充值 |
| 54005  | 长 query 请求频繁  | 请降低长 query 的发送频率，3s 后再试                         |
| 58000  | 客户端 IP 非法     | 检查个人资料里填写的 [IP 地址](https://api.fanyi.baidu.com/api/trans/product/desktop?req=developer) 是否正确 可前往管理控制平台修改 IP 限制，IP 可留空 |
| 58001  | 译文语言方向不支持 | 检查译文语言是否在语言列表里                                 |



### 3.4 各语言 DEMO

PHP 版（[点击下载](https://fanyiapp.cdn.bcebos.com/api/demo/php.zip)）

JS 版（[点击下载](https://fanyiapp.cdn.bcebos.comm/api/demo/js-sdk.zip)）

Python 版（[点击下载](https://fanyiapp.cdn.bcebos.com/api/demo/python.zip)）

C 版（[点击下载](https://fanyiapp.cdn.bcebos.com/api/demo/C.zip)）

Java 版（[点击下载](https://fanyiapp.cdn.bcebos.com/api/demo/java.zip)）



```python
#/usr/bin/env python
#coding=utf8
 
import httplib
import md5
import urllib
import random

appid = '' #你的appid
secretKey = '' #你的密钥

 
httpClient = None
myurl = '/api/trans/vip/translate'
q = 'apple'
fromLang = 'en'
toLang = 'zh'
salt = random.randint(32768, 65536)

sign = appid+q+str(salt)+secretKey
m1 = md5.new()
m1.update(sign)
sign = m1.hexdigest()
myurl = myurl+'?appid='+appid+'&q='+urllib.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
 
try:
    httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
    httpClient.request('GET', myurl)
 
    #response是HTTPResponse对象
    response = httpClient.getresponse()
    print response.read()
except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()

```





### 3.5 常见问题

1. 如何在一次请求中翻译多个单词或者多段文本？

>  您可以在发送的字段 q 中用换行符（在多数编程语言中为转义符号 \n ）来分隔要翻译的多个单词或者多段文本，这样您就能得到多个单词或多段文本独立的翻译结果了。注意在发送请求之前对 q 字段做 URL encode！

2. 什么是 URL encode？

>  网络标准 RFC 1738 规定了 URL 中只能使用英文字母、阿拉伯数字和某些标点符号，不能使用其他文字和符号。如果您需要翻译的文本里面出现了不在该规定范围内的字符（比如中文），需要通过 URL encode 将需要翻译的文本做 URL 编码才能发送 HTTP 请求。大部分编程语言都有现成的 URL encode 函数，具体使用方法可以针对您使用的编程语言自行搜索。

3. 为什么我的请求总是返回错误码 54001？

>  54001 表示签名错误，请检查您的签名生成方法是否正确。
>  应该对 appid+q+salt + 密钥 拼接成的字符串做 MD5 得到 32 位小写的 sign。确保要翻译的文本 q 为 UTF-8 编码。
>  注意在生成签名拼接 appid+q+salt + 密钥 字符串时，q 不需要做 URL encode，在生成签名之后，发送 HTTP 请求之前才需要对要发送的待翻译文本字段 q 做 URL encode。
>  如果您无法确认自己生成签名的结果是否正确，可以将您生成的签名结果和在 <https://md5jiami.51240.com/> 中生成的常规 md5 加密 - 32 位小写签名结果对比。





## 4. 语种检测 API 技术文档



### 4.1 接口地址

+  HTTP 地址：<http://api.fanyi.baidu.com/api/trans/vip/language>

+  HTTPS 地址：<https://fanyi-api.baidu.com/api/trans/vip/language>

   

### 4.2 参数说明

| 字段名 | 类型 | 必填参数 | 描述           | 备注                                                         |
| ------ | ---- | -------- | -------------- | ------------------------------------------------------------ |
| q      | TEXT | Y        | 请求翻译 query | UTF-8 编码                                                   |
| appid  | INT  | Y        | APP ID         | 可在[管理控制台](https://api.fanyi.baidu.com/api/trans/product/desktop?req=developer)查看 |
| salt   | INT  | Y        | 随机数         |                                                              |
| sign   | TEXT | Y        | 签名           | appid+q+salt + 密钥 的 MD5 值                                |

+  签名是为了保证调用安全，使用 MD5 算法生成的一段字符串，生成的签名长度为 32 位，签名中的英文字符均为小写格式

+  为保证检测质量，请将单次请求长度控制在 2000 bytes 以内。

+  签名生成方法如下：
   +  1、将请求参数中的 APPID (appid), 翻译 query (q, 注意为 UTF-8 编码), 随机数 (salt), 以及平台分配的密钥 (可在[管理控制台](https://api.fanyi.baidu.com/api/trans/product/desktop?req=developer)查看)
   +  按照 appid+q+salt + 密钥 的顺序拼接得到字符串 1。
   +  2、对字符串 1 做 md5，得到 32 位小写的 sign。
+  注意:
   +  1、请先将需要翻译的文本转换为 UTF-8 编码
   +  2、在发送 HTTP 请求之前需要对各字段做 [URL encode](https://api.fanyi.baidu.com/api/trans/product/apidoc#appendix)。
   +  3、在生成签名拼接 appid+q+salt + 密钥 字符串时，q 不需要做 URL encode，在生成签名之后，发送
   +  HTTP 请求之前才需要对要发送的待翻译文本字段 q 做 URL encode。
   +  4、支持 post、get 方式传输，post 传输时 Content-Type 指定 application/x-www-form-urlencoded。



### 4.3 返回结果

+  返回结果是 json 格式，包含以下字段：

| 字段名     | 类型   | 描述         |
| ---------- | ------ | ------------ |
| error_code | STRING | 返回错误码   |
| error_msg  | STRING | 返回错误信息 |
| data       | OBJECT | 返回数据集   |
| data.src   | STRING | 检测语种结果 |



### 4.4 支持检测语种列表

| 语言简写 | 名称   |
| -------- | ------ |
| zh       | 中文   |
| en       | 英语   |
| jp       | 日语   |
| kor      | 韩语   |
| th       | 泰语   |
| vie      | 越南语 |



### 4.5 错误码列表

+  当翻译结果无法正常返回时，请参考下表处理：

| 错误码 | 含义           | 解决方法                                                     |
| ------ | -------------- | ------------------------------------------------------------ |
| 0      | 成功           |                                                              |
| 52001  | 请求超时       | 重试                                                         |
| 52002  | 系统错误       | 重试                                                         |
| 52003  | 未授权用户     | 检查您的 [appid](https://api.fanyi.baidu.com/api/trans/product/desktop?req=developer) 是否正确，或者服务是否开通 |
| 54000  | 必填参数为空   | 检查是否少传[参数](https://api.fanyi.baidu.com/api/trans/product/apidoc#joinFile) |
| 54001  | 签名错误       | 请检查您的签名生成方法                                       |
| 54003  | 访问频率受限   | 请降低您的调用频率                                           |
| 54004  | 账户余额不足   | 请前往[管理控制台](https://api.fanyi.baidu.com/api/trans/product/desktop)为账户充值 |
| 54009  | 语种检测失败   | 不在支持检测语种范围内                                       |
| 58000  | 客户端 IP 非法 | 检查个人资料里填写的 [IP 地址](https://api.fanyi.baidu.com/api/trans/product/desktop?req=developer) 是否正确 可前往管理控制平台修改 IP 限制，IP 可留空 |
| 58002  | 服务当前已关闭 | 请前往[管理控制台](https://api.fanyi.baidu.com/api/trans/product/desktop)开启服务 |