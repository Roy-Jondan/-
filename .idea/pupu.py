import requests
import datetime
import time



# 获取数据
def getData():
    url = 'https://j1.pupuapi.com/client/product/storeproduct/detail/deef1dd8-65ee-46bc-9e18-8cf1478a67e9/f8aed0cf-06b9-4247-9e08-13c450401964'
    # 浏览器标识
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat'
    }
    # 发送请求给url
    productData = requests.get(url, headers=headers).json()
    return productData


def getProduct():
    # 获取相应的值
    response = getData()
    name = response['data']['name']
    spec = response['data']['spec']
    price = str(response['data']['price'] / 100)
    guide = str(response['data']['market_price'] / 100)
    title = response['data']['sub_title']
    text = response['data']['custom_tag_text']
    # 输出商品信息
    print('---------------' + '商品: ' + name + '---------------')
    print('规格:' + spec)
    print('价格: ' + price)
    print('原价/折扣价: ' + guide + '/' + price)
    print('详细内容: ' + spec + '; ' + title + text)
    print('---------------' + '商品: ' + name + '的价格波动---------------')


def monitor():
    # 监控价格
    while 1:
        # 获取相应的值
        response = getData()
        price = str(response['data']['price'] / 100)
        # 获取当前时间
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('当前时间为' + now_time + ', ' + '价格为' + price)
        time.sleep(1)


# 调用函数
def run():
    getProduct()
    monitor()


# 运行
run()