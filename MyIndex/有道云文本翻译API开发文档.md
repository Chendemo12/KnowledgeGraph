# 有道云文本翻译API开发文档



## 有道智云翻译 API 简介

Hi，您好，欢迎使用有道智云文本翻译 API 接口服务。如果您想快速体验服务，建议您前往[翻译体验中心](https://ai.youdao.com/product-fanyi.s)或者搜索小程序（有道智云体验中心）进行试用。

本文档主要针对需要集成 HTTP API 的技术开发工程师，详细描述文本翻译能力相关的技术内容。

如果您有与我们商务合作的需求，可以通过一下方式联系我们：

商务邮箱： `AIcloud_Business@corp.youdao.com`

如果您对文档内容有任何疑问，可以通过以下几种方式联系我们：

客服 QQ：1906538062

智云翻译技术交流 QQ 群: 652880659

智云 OCR 技术交流 QQ 群: 654064748

智云语音技术交流 QQ 群：861723255

联系邮箱： `zyservice@corp.youdao.com`

温馨提示：

- 本文档主要针对开发人员，接入测试前需要获取应用 ID（appKey）和应用密钥；如果您还没有，请按照[新手指南](https://ai.youdao.com/doc.s#guide)获取。
- 平台向每个账户赠送 100 元的体验金，供用户集成前测试所用，具体资费规则详见[文本翻译服务](http://aitest.youdao.com/docs/doc-trans-price.s#p07)报价。





## 接口能力

有道翻译 API 接口提供有道的翻译服务，包含了中英翻译和小语种翻译功能。您只需要通过调用有道翻译 API，传入待翻译的内容，并指定要翻译的源语言（支持源语言语种自动检测）和目标语言种类，就可以得到相应的翻译结果。

有道翻译 API HTTP 地址：

> ```
> http://openapi.youdao.com/api
> ```

有道翻译 API HTTPS 地址：

> ```
> https://openapi.youdao.com/api
> ```





## 协议须知

调用方在集成文本翻译 API 时，请遵循以下规则。

| 规则     | 描述                |
| :------- | :------------------ |
| 传输方式 | HTTP/HTTPS          |
| 请求方式 | GET/POST            |
| 字符编码 | 统一使用 UTF-8 编码 |
| 响应格式 | 统一采用 JSON 格式  |
| 传输方式 | HTTP/HTTPS          |





## 接口调用参数

调用 API 需要向接口发送以下字段来访问服务。



| 字段名   | 类型 | 含义                                                   | 必填  | 备注                                                         |
| :------- | :--: | :----------------------------------------------------- | :---- | :----------------------------------------------------------- |
| q        | text | 要翻译的文本                                           | True  | 必须是 UTF-8 编码                                            |
| from     | text | 源语言                                                 | True  | [语言列表](http://ai.youdao.com/docs/doc-trans-api.s#p05) (可设置为 auto) |
| to       | text | 目标语言                                               | True  | [语言列表](http://ai.youdao.com/docs/doc-trans-api.s#p05) (可设置为 auto) |
| appKey   | text | 应用标识（应用 ID）                                    | True  | 可在 [应用管理](http://ai.youdao.com/appmgr.s) 查看          |
| salt     | text | 随机字符串，最好是 UUID                                | True  |                                                              |
| sign     | text | 签名信息，sha256(appKey+<br>input+salt+curtime + 密钥) | True  | f9976efca9dd9e280d4c6637230da5d94<br>c2df6e520605db5a5a4d1d91ba45761 |
| ext      | text | 翻译结果音频格式，支持 mp3                             | false | mp3                                                          |
| voice    | text | 翻译结果发音选择，0 为女声，1 为男声，默认为女声       | false | 0                                                            |
| signType | text | 签名类型                                               | true  | v3                                                           |
| curtime  | text | 当前 UTC 时间戳                                        | true  | 1543199847                                                   |

解释：

> 1. `voice` 没有男声的，会输出女声。
> 2. 发音需要在控制台创建 tts 实例，并绑定应用才能使用，否则点击发音会报 `110` 错误。 
> 3.  接口 salt+curtime 来防重放（即一个请求不可以被请求 2 次），所以 salt 最好为 UUID

签名生成算法如下：

> + signType=v3，sha256 (应用 ID+input+salt+curtime + 密钥)，推荐使用
>
>   > sha256 签名计算方法为：sha256 (应用 ID+input+salt + 当前 UTC 时间戳 + 密钥)。
>   >
>   > 其中，input 的计算方式为：`input`=`q前10个字符` + `q长度` + `q后十个字符`（当 q 长度大于 20）或 `input`=`q字符串`（当 q 长度小于等于 20）。



不同语言获取时间戳，请参看此[此链接](http://tool.chinaz.com/Tools/unixtime.aspx)

如果对签名有疑问，可以参看各语言 demo。





## 输出结果

返回的结果是 json 格式，包含字段与 FROM 和 TO 的值有关，具体说明如下：

| 字段名       | 类型 | 含义             | 备注                                                         |
| :----------- | :--- | :--------------- | :----------------------------------------------------------- |
| errorCode    | text | 错误返回码       | 一定存在                                                     |
| query        | text | 源语言           | 查询正确时，一定存在                                         |
| translation  | text | 翻译结果         | 查询正确时，一定存在                                         |
| basic        | text | 词义             | 基本词典，查词时才有                                         |
| web          | text | 词义             | 网络释义，该结果不一定存在                                   |
| l            | text | 源语言和目标语言 | 一定存在                                                     |
| dict         | text | 词典 deeplink    | 查询语种为支持语言时，存在                                   |
| webdict      | text | webdeeplink      | 查询语种为支持语言时，存在                                   |
| tSpeakUrl    | text | 翻译结果发音地址 | 翻译成功一定存在，需要应用绑定语音合成实例才能正常播放，否则返回 110 错误码 |
| speakUrl     | text | 源语言发音地址   | 翻译成功一定存在，需要应用绑定语音合成实例才能正常播放，否则返回 110 错误码 |
| returnPhrase | text | 单词校验后的结果 | 主要校验字母大小写、单词前含符号、中文简繁体                 |

注：

a. 英文查词的 basic 字段中又包含以下字段，中文查词 basic 只包含 explains 字段。

| 字段        | 含义                                             |
| :---------- | :----------------------------------------------- |
| us-phonetic | 美式音标，英文查词成功，一定存在                 |
| phonetic    | 默认音标，默认是英式音标，英文查词成功，一定存在 |
| uk-phonetic | 英式音标，英文查词成功，一定存在                 |
| uk-speech   | 英式发音，英文查词成功，一定存在                 |
| us-speech   | 美式发音，英文查词成功，一定存在                 |
| explains    | 基本释义                                         |

b. 中文查词的 basic 字段只包含 explains 字段。





## 示例

使用 good 单词查询作为参考说明 json 返回结果：

| 字段名   | 参数数据                                                     | 描述                 |
| :------- | :----------------------------------------------------------- | :------------------- |
| q        | good                                                         | 要翻译的文本         |
| from     | en                                                           | 源语言               |
| to       | zh-CHS                                                       | 目标语言             |
| appKey   | ff889495                                                     | 您的应用 ID          |
| salt     | 1995882C5064805BC30A39829B779D7B                             | 实时计算，生成随机数 |
| sign     | f9976efca9dd9e280d4c6637230da5d94c<br>2df6e520605db5a5a4d1d91ba45761 | 实时计算             |
| signType | v2                                                           | 示例值               |

输出结果与 FROM 和 TO 的值有关：

1. 当 FROM 和 TO 的值都在 {zh-CHS, EN} 范围内时

```json
{
  "errorCode":"0",
  "query":"good", //查询正确时，一定存在
  "translation": [ //查询正确时一定存在
      "好"
  ],
  "basic":{ // 有道词典-基本词典,查词时才有
      "phonetic":"gʊd"
      "uk-phonetic":"gʊd" //英式音标
      "us-phonetic":"ɡʊd" //美式音标
      "uk-speech": "XXXX",//英式发音
      "us-speech": "XXXX",//美式发音
      "explains":[
          "好处",
          "好的"
          "好"
      ]
  },
  "web":[ // 有道词典-网络释义，该结果不一定存在
      {
          "key":"good",
          "value":["良好","善","美好"]
      },
      {...}
  ]
  ],
  "dict":{
      "url":"yddict://m.youdao.com/dict?le=eng&q=good"
  },
  "webdict":{
      "url":"http://m.youdao.com/dict?le=eng&q=good"
  },
  "l":"EN2zh-CHS",
  "tSpeakUrl":"XXX",//翻译后的发音地址
  "speakUrl": "XXX" //查询文本的发音地址
}
```

1. 当 FROM 和 TO 的值有在 {zh-CHS, EN} 范围外的时候

```json
{
   "errorCode": "0",
   "translation": ["大丈夫です"] //小语种翻译，一定存在
   "dict":{
       "url":"yddict://m.youdao.com/dict?le=jap&q=%E6%B2%A1%E5%85%B3%E7%B3%BB%E3%80%82"
   },
   "webdict":{
       "url":"http://m.youdao.com/dict?le=jap&q=%E6%B2%A1%E5%85%B3%E7%B3%BB%E3%80%82"
   },
   "l":"zh-CHS2ja",
   "tSpeakUrl":"XXX",//翻译后的发音地址
   "speakUrl": "XXX" //查询文本的发音地址
}
```





## 支持的语言表

| 源语言   | 支持目标语言                                                 |
| :------- | :----------------------------------------------------------- |
| 中文     | 英文、日文、韩文、法文、西班牙文、葡萄牙文、俄文、越南文、德文、阿拉伯文、印尼文、意大利文 |
| 英文     | 中文、日文                                                   |
| 日文     | 中文、英文                                                   |
| 韩文     | 中文                                                         |
| 法文     | 中文                                                         |
| 西班牙文 | 中文                                                         |
| 葡萄牙文 | 中文                                                         |
| 意大利文 | 中文                                                         |
| 俄文     | 中文                                                         |
| 越南文   | 中文                                                         |
| 德文     | 中文                                                         |
| 阿拉伯文 | 中文                                                         |
| 印尼文   | 中文                                                         |
| 自动识别 | 中文                                                         |

> 其中，自动识别支持以上所有语言的自动识别

> 下表为各语言对应代码：

| 语言     | 代码   |
| :------- | :----- |
| 中文     | zh-CHS |
| 英文     | en     |
| 日文     | ja     |
| 韩文     | ko     |
| 法文     | fr     |
| 西班牙文 | es     |
| 葡萄牙文 | pt     |
| 意大利文 | it     |
| 俄文     | ru     |
| 越南文   | vi     |
| 德文     | de     |
| 阿拉伯文 | ar     |
| 印尼文   | id     |
| 自动识别 | auto   |





## 错误代码列表

| 错误码 | 含义                                                         |
| :----- | :----------------------------------------------------------- |
| 101    | 缺少必填的参数，出现这个情况还可能是 et 的值和实际加密方式不对应 |
| 102    | 不支持的语言类型                                             |
| 103    | 翻译文本过长                                                 |
| 104    | 不支持的 API 类型                                            |
| 105    | 不支持的签名类型                                             |
| 106    | 不支持的响应类型                                             |
| 107    | 不支持的传输加密类型                                         |
| 108    | appKey 无效，注册账号， 登录后台创建应用和实例并完成绑定， 可获得应用 ID 和密钥等信息，其中应用 ID 就是 appKey（ 注意不是应用密钥） |
| 109    | batchLog 格式不正确                                          |
| 110    | 无相关服务的有效实例                                         |
| 111    | 开发者账号无效                                               |
| 113    | q 不能为空                                                   |
| 201    | 解密失败，可能为 DES,BASE64,URLDecode 的错误                 |
| 202    | 签名检验失败                                                 |
| 203    | 访问 IP 地址不在可访问 IP 列表                               |
| 205    | 请求的接口与应用的平台类型不一致，如有疑问请参考 [入门指南]() |
| 206    | 因为时间戳无效导致签名校验失败                               |
| 207    | 重放请求                                                     |
| 301    | 辞典查询失败                                                 |
| 302    | 翻译查询失败                                                 |
| 303    | 服务端的其它异常                                             |
| 401    | 账户已经欠费停                                               |
| 411    | 访问频率受限，请稍后访问                                     |
| 412    | 长请求过于频繁，请稍后访问                                   |







## 常见问题及注意事项

- 点击发音链接，返回 110

发音需要 tts 实例，需要在控制台创建语音合成实例绑定应用后方能使用。

- 返回 110

应用没有绑定服务实例，可以新建服务实例，绑定服务实例。

- 返回 108

appKey 无效，注册账号， 登录后台创建应用和实例并完成绑定， 可获得应用 ID 和密钥等信息，其中应用 ID 就是 appKey（ 注意不是应用密钥）

- 返回 101

首先确保必填参数齐全，然后，确认参数书写是否正确。

- 返回 202

如果确认 `appKey` 和 `appSecret` 的正确性，仍返回 202，一般是编码问题。请确保 `q` 为 UTF-8 编码.





## 常用语言 Demo

**Python 示例**

```python
# -*- coding: utf-8 -*-
import sys
import uuid
import requests
import hashlib
import time

reload(sys)
sys.setdefaultencoding('utf-8')

YOUDAO_URL = 'http://openapi.youdao.com/api'
APP_KEY = '您的应用ID'
APP_SECRET = '您的应用密钥'


def encrypt(signStr):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()


def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]


def do_request(data):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(YOUDAO_URL, data=data, headers=headers)


def connect():
    q = "test"

    data = {}
    data['from'] = 'EN'
    data['to'] = 'zh-CHS'
    data['signType'] = 'v3'
    curtime = str(int(time.time()))
    data['curtime'] = curtime
    salt = str(uuid.uuid1())
    signStr = APP_KEY + truncate(q) + salt + curtime + APP_SECRET
    sign = encrypt(signStr)
    data['appKey'] = APP_KEY
    data['q'] = q
    data['salt'] = salt
    data['sign'] = sign

    response = do_request(data)
    print response.content


if __name__ == '__main__':
    connect()

				
```