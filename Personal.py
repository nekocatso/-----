import json
import requests
import time
import random


def process_json(uid, end):
def get_headers():
    headers = {
        "Host": "virtualcourse.zhihuishu.com",
        "Connection": "keep-alive",
        "Content-Length": "23341",
        "sec-ch-ua": """" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100" """,
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
        "sec-ch-ua-platform": "Windows",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Origin": "https://ar.zhihuishu.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https//ar.zhihuishu.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9 ",
    }
    return headers


def first(uid):
    url = (
    )
    headers = {
        "Host": "virtualcourse.zhihuishu.com",
        "Connection": "keep-alive",
        "sec-ch-ua": """" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100" """,
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
        "sec-ch-ua-platform": "Windows",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Origin": "https://ar.zhihuishu.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https//ar.zhihuishu.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9 ",
    }
    res = requests.get(url, headers=headers)
    print(res.text)


def second():
    url = "https://studyservice.zhihuishu.com/api/stuExperiment/systemTime"
    headers = {
        "Host": "studyservice.zhihuishu.com",
        "Connection": "keep-alive",
        "sec-ch-ua": """" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100" """,
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
        "sec-ch-ua-platform": "Windows",
        "Accept": "*/*",
        "Origin": "https://ar.zhihuishu.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https//ar.zhihuishu.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9 ",
    }
    resp = requests.get(url, headers=headers)
    data = resp.text
    print(data)
    data = json.loads(data)
    return data["data"]


def third(uid, end):
    url = "https://virtualcourse.zhihuishu.com/report/saveReport"
    data = process_json(uid, end)
    data = {"jsonStr": data, "ticket": None}
    headers = get_headers()
    response = requests.post(url, data=data, headers=headers)
    print(response.status_code)
    print(response.text)


if __name__ == "__main__":
    uid = "         "  # 输入你的uuid运行即可
    # 打开恰同学少年网页F12输入 getUUID()获得UUid替换上面再执行文件即可
    # 如需帮助,请联系微信: NULL0001000
    end = second()
    third(uid, end)
