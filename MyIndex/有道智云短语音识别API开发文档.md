# 有道智云短语音识别 API开发文档



## 有道智云短语音识别 API 简介

有道短语音识别API接口提供有道的短语音识别服务，包含了中文和英文的识别功能。您只需要通过调用有道语音识别API，传入待识别的音频文件，并指定要识别的源语言种类，以POST方式请求就可以得到相应的识别结果。

上传的文件时长不能超过15s，文件大小不能超过2M。

有道语音识别API HTTP地址：

> ```
> http://openapi.youdao.com/asrapi
> ```

有道语音识别API HTTPS地址：

> ```
> https://openapi.youdao.com/asrapi
> ```





## 接口调用参数

调用API需要向接口发送以下字段来访问服务。

| 字段名   | 类型 | 含义                                         | 必填 | 备注                                                     |
| :------- | :--- | :------------------------------------------- | :--- | :------------------------------------------------------- |
| q        | text | 要识别的音频文件的base64编码字符串           | True | 必须是Base64编码                                         |
| langType | text | 源语言                                       | True | [语言列表](https://ai.youdao.com/docs/doc-asr-api.s#p05) |
| appKey   | text | 应用 ID                                      | True | 可在 [应用管理](https://ai.youdao.com/appmgr.s) 查看     |
| salt     | text | 随机数                                       | True |                                                          |
| sign     | text | 签名，通过md5(appKey+q+salt+密钥)生成        | True | appKey+q+salt+密钥的MD5值                                |
| format   | text | 语音文件的格式，wav                          | true | wav                                                      |
| rate     | text | 采样率， 8000 或者 16000， 推荐 16000 采用率 | true | 8000                                                     |
| channel  | text | 声道数， 仅支持单声道，请填写固定值1         | true | 1                                                        |
| type     | text | 上传类型， 仅支持base64上传，请填写固定值1   | true | 1                                                        |

签名生成方法如下：

1. 将请求参数中的 `appKey`，识别文本 `q` (注意为UTF-8编码)，随机数 `salt` 和`密钥` （可在 [应用管理](https://ai.youdao.com/appmgr.s) 查看）， 按照 `appKey+q+salt+密钥` 的顺序拼接得到字符串 `str`。
2. 对字符串 `str` 做md5，得到32位大写的 `sign` [(参考Java生成MD5示例)](https://ai.youdao.com/docs/doc-asr-api.s#p08)

**注意:**

1. 请先将需要识别的音频文件转换为 Base64 编码
2. 在发送 HTTP 请求之前需要对各字段做 URL encode。
3. 在生成签名拼接 `appKey+q+salt+密钥` 字符串时，`q` 不需要做 URL encode，在生成签名之后，发送 HTTP 请求之前才需要对要发送的待识别文本字段 `q` 做 URL encode。



## 输出结果

响应结果是以json形式输出，包含字段如下表所示：

| 字段      | 含义                       |
| :-------- | :------------------------- |
| errorCode | 识别结果错误码，一定存在   |
| result    | 识别结果，识别成功一定存在 |



## 示例

```json
{
    "result": [
        "今天天气不错"
    ],    //识别结果
    "errorCode": "0",    //错误码。一定存在
}
```





## 支持的语言表

支持中文和英文音频的识别。

| 语言 | 代码   |
| :--- | :----- |
| 中文 | zh-CHS |
| 英文 | en     |
| 日文 | ja     |
| 韩文 | ko     |



## 语音支持

格式支持：wav（不压缩、pcm编码）

采样率：8k或者16k。推荐16k。

编码：16bit位深的单声道

| 格式 | 代码 |
| :--- | :--- |
| wav  | wav  |



## 错误代码列表

| 错误码 | 含义                                                         |
| :----- | :----------------------------------------------------------- |
| 101    | 缺少必填的参数                                               |
| 102    | 不支持的语言类型                                             |
| 103    | 请求文本过长                                                 |
| 104    | 不支持的API类型                                              |
| 105    | 不支持的签名类型                                             |
| 106    | 不支持的响应类型                                             |
| 107    | 不支持的传输加密类型                                         |
| 108    | appKey无效                                                   |
| 109    | batchLog格式不正确                                           |
| 110    | 无相关服务的有效实例                                         |
| 111    | 用户无效                                                     |
| 112    | 请求服务无效                                                 |
| 113    | 请求文本不能为空                                             |
| 201    | 解密失败                                                     |
| 202    | 签名检验失败                                                 |
| 203    | 访问IP地址不在可访问IP列表                                   |
| 205    | 使用的接入方式（Android SDK、iOS SDK、API）与创建的应用平台类型不一致 |
| 301    | 词典查询失败                                                 |
| 302    | 小语种识别失败                                               |
| 303    | 服务的异常                                                   |
| 401    | 账户已经欠费停止                                             |
| 402    | offlinesdk不可用                                             |
| 411    | 访问频率受限,请稍后访问                                      |
| 412    | 超过最大请求字符数                                           |
| 4001   | 不支持的语音识别格式                                         |
| 4002   | 不支持的语音识别采样率                                       |
| 4003   | 不支持的语音识别声道                                         |
| 4004   | 不支持的语音上传类型                                         |
| 4005   | 不支持的语言类型                                             |
| 4006   | 识别音频文件过大                                             |
| 4007   | 识别音频时长过长                                             |
| 4201   | 解密失败                                                     |
| 4301   | 语音识别失败                                                 |
| 4303   | 服务的异常                                                   |
| 4411   | 访问频率受限,请稍后访问                                      |
| 4412   | 超过最大请求时长                                             |





## 常见问题及注意事项

- 返回110

应用没有绑定服务实例，可以新建服务实例，绑定服务实例。

- 返回108

appKey无效，注册账号， 登录后台创建应用和实例并完成绑定， 可获得应用ID和密钥等信息，其中应用ID就是appKey（ 注意不是应用密钥）

- 返回101

首先确保必填参数齐全，然后，确认参数书写是否正确。

- 返回202

如果确认 `appKey` 和 `appSecret` 的正确性，仍返回202，一般是编码问题。请确保 `q` 为UTF-8编码.

- 返回205

确保接入方式（Android SDK、IOS SDK、API）与创建的应用平台类型一致。



## 音频转换

本部分描述如何把其他格式的音频转成符合语音识别输入要求的格式文件。

语音识别底层使用的是pcm格式，因此推荐使用pcm格式音频。音频格式转换推荐使用ffmpeg



## PCM文件音频介绍

pcm保存的是未压缩的音频信息,没有头文件

16bits编码是指每次采样信息用2个字节保存。

16000采样率，是指1秒采样16000次，常见的音频是44100HZ，即一秒采样44100次。

单声道： 只有一个声道。

根据这些信息，可以得出：

1ms的16采样率音频文件大小是 2*16 = 32字节 。

1ms的8采样率音频文件大小是 2*8 = 16字节，由此即可得到音频的长度。





## 常用语言 Demo



Python 示例



```python
# -*- coding: utf-8 -*-
import requests
import md5
import random
import wave
import base64
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
asrUrl = "http://openapi.youdao.com/asrapi"
appKey = "您的应用ID"
appSecret = "您的应用密钥"

def asr(app_key, q ,app_secret ,lang,channel,rate,format):
    data = {}
    salt = random.randint(1, 65536)

    sign = app_key + q + str(salt) + app_secret
    m1 = md5.new()
    m1.update(sign)
    sign = m1.hexdigest()

    data['appKey'] = app_key
    data['q'] = q
    data['salt'] = salt
    data['sign'] = sign
    data['langType'] = lang
    data['channel'] = channel
    data['rate'] = rate
    data['format'] = format
    data['type'] = 1
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(asrUrl,data=data,headers = headers)
    return response


filename = 'd:/en.wav'
extension = filename[filename.rindex('.')+1:]
if extension == "wav" :
    # load wav
    file_to_play = wave.open(filename, 'rb')
    file_wav = open(r'd:\en.wav', 'rb')
    q = base64.b64encode(file_wav.read())
    file_wav.close()
    sample_width = file_to_play.getsampwidth()
    sample_rate = file_to_play.getframerate()
    nchannels = file_to_play.getnchannels()
    bit_rate = 16

    # request
    response = asr(appKey,q,appSecret,"en",nchannels,sample_rate,'wav')
    print response.content
else:
    print '不支持的音频类型'

```