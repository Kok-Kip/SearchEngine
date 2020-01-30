# -*- coding: utf8 -*-
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from app.redis.redis_handler import get, set

import http.client
import json
import time

def get_token():
    # find in redis
    token = get('token')
    if token is not None:
        token = json.loads(str(token, encoding='utf-8'))
        print(token)
        expire_time = token['ExpireTime']
        present_time = time.time()
        if expire_time > int(present_time):
            return token['Id']

    token = get_token_remote()
    token_str = json.dumps(token)
    token_bytes = bytes(token_str, encoding="utf-8")
    set('token', token_bytes)
    return token['Id']

def get_token_remote():
    # Create AcsClient
    client = AcsClient(
        "LTAI4FvbUkbyYDQ6PZY13Hin",
        "AGSS25KHDLyyDe5QIoiZqLgUqGRENi",
        "cn-shanghai"
    );
    # Create request and set Params
    request = CommonRequest()
    request.set_method('POST')
    request.set_domain('nls-meta.cn-shanghai.aliyuncs.com')
    request.set_version('2019-02-28')
    request.set_action_name('CreateToken')
    response = client.do_action_with_exception(request)

    # bytes to json
    res_str = str(response, 'utf-8')
    res = json.loads(res_str)
    print(res['Token'])
    return res['Token']


def get_text(audioFile):
    appKey = 'oIO7nqiFIunoSK4F'
    # API address
    url = 'http://nls-gateway.cn-shanghai.aliyuncs.com/stream/v1/asr'
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
    # set HTTP header
    httpHeaders = {
        'X-NLS-Token': token,
        'Content-type': 'application/octet-stream',
        'Content-Length': len(audioFile)
    }

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
