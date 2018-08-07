from flask import Flask, jsonify
import requests
import json
import time
from lxml import etree
app = Flask(__name__)

@app.route('/get_wanxi_message')
def wanxi_message():
    url = "http://www.wxc.edu.cn/4/list.htm"
    headers = {
        'User_Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Host': 'www.wxc.edu.cn'

    }
    response = requests.get(url, headers=headers)
    after_lxml_object = etree.HTML(response.text)
    board = after_lxml_object.xpath('//span[@class="column-news-title"]/text()')
    # for i in range(14):
    #     print("board", board[i].text)
    return_dict = {
        'result': board
    }
    print('123')
    time.sleep(1000)
    return jsonify(return_dict)   # 跟下面结果二选一
    # return json.dumps(return_dict)


@app.route('/')
def weather():
    return 'sun day'
#
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, threaded=True)