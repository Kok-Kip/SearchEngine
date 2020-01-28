# -*- coding: utf8 -*-
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
import http.client
import json

def get_token():
   # 创建AcsClient实例
   client = AcsClient(
      "LTAI4FvbUkbyYDQ6PZY13Hin",
      "AGSS25KHDLyyDe5QIoiZqLgUqGRENi",
      "cn-shanghai"
   );
   # 创建request，并设置参数
   request = CommonRequest()
   request.set_method('POST')
   request.set_domain('nls-meta.cn-shanghai.aliyuncs.com')
   request.set_version('2019-02-28')
   request.set_action_name('CreateToken')
   response = client.do_action_with_exception(request)
   print(response)
   # bytes to json
   res_str = str(response, 'utf-8')
   res = json.loads(res_str)
   print(res['Token'])
   return res['Token']


def get_text(audioFile):
   appKey = 'oIO7nqiFIunoSK4F'
   # API address
   url = 'http://nls-gateway.cn-shanghai.aliyuncs.com/stream/v1/asr'
   # audioFile = './nls-sample-16k.wav'
   format = 'pcm'
   sampleRate = 16000
   enablePunctuationPrediction = True
   enableInverseTextNormalization = True
   enableVoiceDetection = False

   # set RESTful Request Parameters
   request = url + '?appkey=' + appKey
   request = request + '&format=' + format
   request = request + '&sample_rate=' + str(sampleRate)
   if enablePunctuationPrediction:
      request = request + '&enable_punctuation_prediction=' + 'true'
   if enableInverseTextNormalization:
      request = request + '&enable_inverse_text_normalization=' + 'true'
   if enableVoiceDetection:
      request = request + '&enable_voice_detection=' + 'true'
   print('Request: ' + request)

   token = get_token()
   result = process(request, token['Id'], audioFile)
   return result

def process(request, token, audioFile):
   host = 'nls-gateway.cn-shanghai.aliyuncs.com'
   # # 读取音频文件
   # with open(audioFile, mode='rb') as f:
   #    audioContent = f.read()
   # 设置HTTP请求头部
   httpHeaders = {
      'X-NLS-Token': token,
      'Content-type': 'application/octet-stream',
      'Content-Length': len(audioFile)
   }
   # Python 3.x 请使用http.client
   conn = http.client.HTTPConnection(host)
   conn.request(method='POST', url=request, body=audioFile, headers=httpHeaders)
   response = conn.getresponse()
   print('Response status and response reason:')
   print(response.status, response.reason)
   body = response.read()
   try:
      print('Recognize response is:')
      body = json.loads(body)
      print(body)
      status = body['status']
      if status == 20000000:
         result = body['result']
         print('Recognize result: ' + result)
         return result
      else:
         print('Recognizer failed!')
         return ""
   except ValueError:
      print('The response is not json format string')
   conn.close()
