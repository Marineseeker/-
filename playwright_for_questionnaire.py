from playwright.sync_api import Playwright, sync_playwright, expect
import re
import random
from time import sleep
import requests

index_2 = random.randint(1, 2)
index_4 = random.randint(1, 4)
index_5 = random.randint(1, 5)
index_6 = random.randint(1, 6)

randomUA = random.choice(['Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13'
, 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.48 Safari/525.19', 'Mozilla/5.0 (X11; U; Linux i686; rv:1.7.3) Gecko/20040913 Firefox/0.10', 
'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.33 Safari/530.5', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.38 Safari/532.0', 
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.55 Safari/533.4', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; ja; rv:1.9.0.6) Gecko/2009011913 Firefox/3.0.6', 
'Mozilla/5.0 (Windows; U; Windows NT 6.0; ja; rv:1.9.0.6) Gecko/2009011913 Firefox/3.0.6 (.NET CLR 3.5.30729)', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:9.0.1) Gecko/20100101 Firefox/9.0.1'
, 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:9.0.1) Gecko/20100101 Firefox/9.0.1'])

api_url = 'http://v2.api.juliangip.com/dynamic/getips?auto_white=1&num=1&pt=1&result_type=text&split=1&trade_no=1846081008406246&sign=5621bb03d5a7a53543773ef25caf51fc'
proxy_ip = requests.get(api_url).text
username = "19130603472"
password = "e5a7Rq60"
proxies = {
"http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip},
"https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip},
}


def run(playwright: Playwright) -> None:
    
    page.locator(f'//*[@id="div1"]/div[2]/div[{index_2}]/div').click()
    page.locator(f'//*[@id="div2"]/div[2]/div[{index_5}]/div').click()
    page.locator(f'//*[@id="div3"]/div[2]/div[{index_5}]/div').click()
    understand_xpath = ['//*[@id="div4"]/div[2]/div[1]/div', 
                        '//*[@id="div4"]/div[2]/div[2]/div', 
                        '//*[@id="div4"]/div[2]/div[3]/div',
                        '//*[@id="div4"]/div[2]/div[4]/div',]
    for xpath in random.sample(understand_xpath, int(index_4)):
        page.locator(xpath).click()
    relative_xpath = ['//*[@id="div5"]/div[2]/div[1]/div',
                      '//*[@id="div5"]/div[2]/div[2]/div',
                      '//*[@id="div5"]/div[2]/div[3]/div',
                      '//*[@id="div5"]/div[2]/div[4]/div',
                      '//*[@id="div5"]/div[2]/div[5]/div',]                   
    for xpath in random.sample(relative_xpath, int(index_5)):
        page.locator(xpath).click()
    page.locator(f'//*[@id="div6"]/div[2]/div[{index_4}]/div').click()
    page.locator(f'//*[@id="div7"]/div[2]/div[{index_5}]/div').click()
    page.locator(f'//*[@id="div8"]/div[2]/div[{index_6}]/div').click()
    page.locator(f'//*[@id="div9"]/div[2]/div[{index_4}]/div').click()
    page.locator(f'//*[@id="div10"]/div[2]/div[{index_4}]/div').click()
    page.locator(f'//*[@id="div11"]/div[2]/div[{index_4}]/div').click()
    page.locator(f'//*[@id="div12"]/div[2]/div[{index_2}]/div').click()
    Sichuan_industrial_heritage = ['西南应用磁学研究所旧址', '卓筒井和蓬基井', 
                                   '中国核动力九〇九基地', '六合丝厂',
                                   '国营锦江机器厂', '威远煤矿工业遗产群', 
                                   '桑都记忆1958']
    
    selected_heritage = random.sample(Sichuan_industrial_heritage, random.randint(1, 3))
    # 使用空格连接列表中的所有元素
    heri_str = ' '.join(selected_heritage)
    page.locator("input[name=\"q13\"]").fill(heri_str)
    page.locator('//*[@id="q14"]').fill('无')
    page.get_by_text("提交").click()
    
    try:
        page.wait_for_selector("//div[@id='captcha']", timeout=2000)
        page.locator("//div[@id='captcha']").click()
        sleep(4)
    except:
        print("没有智能验证")
    # ---------------------

with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless = True, proxy={"server": proxy_ip, "username": '19130603472', "password": 'e5a7Rq60'})
    # browser = playwright.firefox.launch(headless = True)
    context = browser.new_context(user_agent=randomUA)
    # context.route('**/*.{png,jpg,jpeg,svg,gif}', lambda route, _: route.abort())
    n = 0
    for _ in range(50):
        
        page = context.new_page()

        page.goto("https://www.wjx.cn/vm/OfWWQ1Y.aspx")
        
        try:
            page.wait_for_selector('//*[@id="layui-layer1"]/div[3]/a[2]', timeout=2000)
            page.locator("//div[@id='captcha']").click()
            sleep(2)
        except:
            pass
        run(playwright)
        n += 1
        print(f"第{n}次提交")