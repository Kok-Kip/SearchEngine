from app.app import create_app
from flask import jsonify, request
from app.remote.aliyun_caller import get_token, get_text
import time
import logging

# set logging level
logging.getLogger().setLevel(logging.INFO)

app = create_app()


@app.route('/search', methods=['GET'])
def search():
    start_time = time.time()
    key = request.args.get("key")
    if key is None:
        return jsonify(message='ok', data=None)

    from app.biz.doc_rank import get_pertinent_doc_by_key
    res = get_pertinent_doc_by_key(key)
    during_time = time.time() - start_time
    logging.info(f'the query {key} has spent {during_time}s')
    return jsonify(message='ok', data=res)


@app.route('/test', methods=['GET'])
def test():
    return jsonify(message='ok')

@app.route('/test_api', methods=['POST'])
def test_api():
    file = request.files.get('file')
    print(file)
    data = file.read()
    print(type(data))
    if len(data) == 0:
        return jsonify(message='error', data='')

    audioFile = data
    result = get_text(audioFile)

    # result = "hhh"
    return jsonify(message='ok', data=result)

@app.route('/test_redis', methods=['GET'])
def test_redis():
    token = get_token()
    return jsonify(message='ok', data=token)

def make_test_data():
    # 制造假数据
    res = list()

    r = dict()
    r['title'] = '育成大佬'
    r['description'] = '这一天，我们终于发现育成大佬的恐怖'
    r['url'] = 'https://github.com/leungyukshing'
    res.append(r)

    r2 = dict()
    r2['title'] = '梁育诚是不是好人?_百度知道'
    r2['description'] = '最佳答案: 嗯,确实'
    r2['url'] = 'https://zhidao.baidu.com/question/405800210.html'
    res.append(r2)

    r3 = dict()
    r3['title'] = '梁育诚 engineer Bytedance'
    r3['description'] = '梁育诚 Senior Student in SYSU'
    r3['url'] = 'https://cn.linkedin.com/in/%E8%82%B2%E8%AF%9A-%E6%A2%81-359909190?trk=people-guest_' \
                'profile-result-card_result-card_full-click'
    res.append(r3)

    r4 = dict()
    r4['title'] = 'Personal Resume'
    r4['description'] = '梁育诚 Student 基本信息 个人信息 梁育诚 / 男 / 21岁 英语水平 CET-6 ...曾获2016、' \
                        '2017中山大学“康乐杯”东校区冠军、四校总决赛季军 工作经历...'
    r4['url'] = 'https://leungyukshing.gitee.io/resume/'
    res.append(r4)
    return res
