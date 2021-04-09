from selenium import webdriver
import time
import sys
import json
import re
import random
import warnings
import threading
warnings.filterwarnings("ignore")
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
import cv2 as cv
import numpy as np
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
import cv2
# 创建浏览器对象,发请求
#System.setProperty("webdriver.chrome.driver", );



class WeiBoSpider:
    def __init__(self):
        self.baseurl="https://accounts.binancezh.co/zh-CN/register"
        self.ip=0

        self.timestart = [0,0]
        self.timeend = 0
        self.timeuse = 0

        self.Kai = 0
        self.num =0
        self.mailadress = 0
        self.driverlist= []
        self.PROIP = 1
    def pasepage(self):
        while True:

            desired_capabilities = DesiredCapabilities.CHROME  # 修改页面加载策略
            desired_capabilities["pageLoadStrategy"] = "eager"  # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出
            chromeOptions = webdriver.ChromeOptions()

            chromeOptions.add_experimental_option('excludeSwitches', ['enable-automation'])
            chromeOptions.add_argument("--disable-blink-features=AutomationControlled")
            if self.PROIP == 1:

                chromeOptions.add_argument("--proxy-server=http://"+self.ip)

            self.timestart.append(time.time())

            self.driverlist.append(webdriver.Chrome(chrome_options = chromeOptions))
            print("当前已经使用",len(self.driverlist),"个")
            #driver.set_window_size(640,550) #改变窗口大小。这个网站做了响应式布局，分别看到三栏、两栏、一栏
            #driver.set_window_position(1400,100)
            #time.sleep(2)
            #driver.set_window_size(480,size['height'])
            self.driverlist[len(self.driverlist)-1].execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined
            })
            """
            })
            self.num=random.randint(10000000,999999999)
            self.mailadress = str(self.num)+"@yopmail.com"
            print("邮件地址：",self.mailadress)



            ######申请账号
            try:
                #driver.get("http://httpbin.org/get")
                #time.sleep(1)
                self.driverlist[len(self.driverlist)-1].get(self.baseurl)



            except:
                self.driverlist[len(self.driverlist)-1].quit()
                self.driverlist[len(self.driverlist)-1] .pop(len(self.driverlist)-1)
                print("IP不行")
                return
            while True:
                try:

                    uname = WebDriverWait(self.driverlist[len(self.driverlist)-1], 10).until(EC .element_to_be_clickable((By.XPATH,'//div[@class="css-1eewrf"]')))
                    uname.click()

                    #unaself.driverlist[len(driverlist)-1].find_element_by_xpath('//div[@class="css-1eewrf"]')
                    #print(uname)

                    time.sleep(1)
                    uname1 = self.driverlist[len(self.driverlist)-1].find_element_by_xpath('//div[@class=" css-azvb1b"]//input')
                    uname1.send_keys(self.mailadress)

                    uname1 = self.driverlist[len(self.driverlist)-1].find_element_by_xpath('//div[@class=" css-azvb1b"]//input[@name]')
                    print("输入密码为","Zzzz"+self.mailadress[0:4])
                    uname1.send_keys("Zzzz"+self.mailadress[0:4])

                    uname1 = self.driverlist[len(self.driverlist)-1].find_element_by_xpath('//div[@class="css-xrxl27"]')
                    uname1.click()

                    uname1 = self.driverlist[len(self.driverlist)-1].find_element_by_xpath('//div[@class=" css-azvb1b"]//input[@name="agentId"]')
                    uname1.send_keys(48441240)#54299024

                    uname1 = self.driverlist[len(self.driverlist)-1].find_element_by_xpath('//button[@id]')
                    uname1.click()

                    break

                except Exception as  e:

                    print(e)
                    continue
                #print(imgg)


            while True:

                try :
                    #time.sleep(2)
                    WebDriverWait(self.driverlist[len(self.driverlist)-1],2).until(EC.presence_of_element_located((By.XPATH,"//input[@inputmode]")))
                    #sss = self.driverlist[len(driverlist)-1].find_element_by_xpath('//input[@inputmode]')
                    self.Kai = 1
                    break

                except:
                    pass
            while self.Kai == 1:

               time.sleep(1)
        #self.mailcodeget(ip)
    def mailcodeget(self):
        #####邮箱获取验证码
        print("开始获取验证码")
        chromeOptions = webdriver.ChromeOptions()


        opt = webdriver.ChromeOptions()            # 创建Chrome参数对象
        opt.headless = True              # 把Chrome设置成可视化无界面模式，windows/Linux 皆可
        #driver = Chrome(options=opt)     # 创建Chrome无界面对象
        #chromeOptions.add_argument("--proxy-server=http://"+"113.120.142.254:13456")
        desired_capabilities = DesiredCapabilities.CHROME  # 修改页面加载策略
        desired_capabilities["pageLoadStrategy"] = "eager"  # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出
        if self.PROIP == 1:
            chromeOptions.add_argument("--proxy-server=http://"+self.ip)
        driver2 = webdriver.Chrome(chrome_options = chromeOptions)
        #driver2.set_window_size(680,550)
        #driver2.set_window_position(300,100)

        driver2.get("http://www.yopmail.com/zh/")
       # desired_capabilities["pageLoadStrategy"] = "eager"
        useflag = 0;
        while True:
            print("useflag",useflag,"self.Kai",self.Kai)

            while self.Kai == 0 :
                time.sleep(1)


            if useflag == 0:

                print('开始找输入框')

                drivername=WebDriverWait(driver2,30,0.5,True).until(EC.visibility_of(driver2.find_element(By.XPATH,'//td[@class="nw"]//input[@onclick]')))
                #drivername = driver2.find_element_by_xpath('//td[@class="nw"]//input[@onclick]')
                drivername.send_keys(str(self.num))
                print('开始找查看邮箱')
                drivername = WebDriverWait(driver2, 20).until(
                            EC.presence_of_element_located(
                                (By.CSS_SELECTOR, 'input')))
                print('开始找按钮')


                drivername = driver2.find_element_by_xpath('//input[@type="submit"]')
                #drivername=WebDriverWait(driver2,2).until(EC.visibility_of(driver2.find_element(By.XPATH,'//input[@class="sbut"]')))


                try:
                    print('按下去')
                    drivername.click()
                    #time.sleep(1)

                except:
                    print('超时继续执行下一步')
            else:
                print('开始找输入框')
                driver2.switch_to.default_content()
                drivername=WebDriverWait(driver2,30,0.5,True).until(EC.visibility_of(driver2.find_element(By.XPATH,'//td[@class="nw"]//input[@onclick]')))
                #drivername = driver2.find_element_by_xpath('//td[@class="nw"]//input[@onclick]')
                drivername.clear()
                drivername.send_keys(str(self.num))
                print('开始找查看邮箱')
                drivername = WebDriverWait(driver2, 20).until(
                            EC.presence_of_element_located(
                                (By.CSS_SELECTOR, 'input')))
                print('开始找按钮')


                drivername = driver2.find_element_by_xpath('//span[@class="mgif irefresh b"]')
                #drivername=WebDriverWait(driver2,2).until(EC.visibility_of(driver2.find_element(By.XPATH,'//input[@class="sbut"]')))


                try:
                    print('按下去')
                    drivername.click()
                    time.sleep(1)

                except:
                    print('超时继续执行下一步')
            """try:

                driver2.set_page_load_timeout(20)
                driver2.set_script_timeout(20)#这两种设置都进行才有效
                iframe = WebDriverWait(driver2, 20).until(
                        EC.presence_of_element_located(
                            (By.CSS_SELECTOR, 'iframe')))
            except:
                print("s")"""
            self.Kai = 0
            while True:


                print('开始找邮箱内容')
                #driver2.implicitly_wait(30)
                for i in range(20):

                    try:

                        iframe = driver2.find_element_by_xpath('//div//iframe[@id="ifmail"]')

                    except:
                        time.sleep(2)
                        print('加载没完')
                #iframe = WebDriverWait(driver2,10).until(EC.visibility_of(driver2.find_element(By.XPATH,'//div//iframe[@id="ifmail"]')))
                #iframe = driver2.find_element_by_xpath('//div//iframe[@id="ifmail"]')
                print('开始转换')
                driver2.switch_to_frame(iframe)

                print('开始寻找')
                drivername=driver2.find_element_by_xpath('//*')
                #drivername1=drivername.get_attribute('textContent')

                #print(drivername.text)
                yan=re.findall("激活验证码为：\n\n(.*?)\n",drivername.text)
                if yan:
                    break
                else:
                    try:
                        drivername = driver2.find_element_by_xpath('//span[@class="mgif irefresh b"]')
                        drivername.click()
                    except:

                        driver2.refresh()


            useflag = 1
            ##########输入验证码

            uname1 = self.driverlist[0].find_element_by_xpath('//div[@class="css-vurnku"]//input[@inputmode]')
            uname1.send_keys(yan[0])
            self.timeend = time.time()
            self.timeuse = self.timeend - self.timestart[0]

            time.sleep(8)



            print("总耗时为：%s" % self.timeuse)


            self.driverlist[0].quit()
            self.driverlist.pop(0)
            self.timestart.pop(0)

            with open('注册.txt','a+') as f:
                f.write(self.mailadress+ "  用时 " +str(self.timeuse)+" IP:  "+self.ip)
            print("完成第 ",len(open(r"注册.txt",'rU').readlines()),"个")

    def readcookies(self):
        print('开始')

        ipda="http://proxy.httpdaili.com/apinew.asp?sl=20&noinfo=true&ddbh=1702724112122637424"
        res = requests.get(url=ipda,timeout=8)
        assdf=res.text
        iplist=assdf.split()
        #print(iplist)
        with open("IP.txt","w",encoding="UTF-8") as f:
            for i in iplist:
                f.write(i+'\n')
        for i  in  open("IP.txt","r",encoding="UTF-8"):
            if "#" in i:
                self.ip = re.findall("(.*?)#",i)[0]
            else:
                self.ip=i

            ipadress = "https://"+self.ip
            print("代理IP为:",ipadress)



            '''head 信息'''
            head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
                   'Connection': 'keep-alive'}
            '''http://icanhazip.com会返回当前的IP地址'''



            try:

                res = requests.get(url="http://icanhazip.com/",timeout=8,proxies={"https":self.ip})
                print('代理有效：',res.text)
            except Exception as  e:
                print("代理无效")
                print(e)
                continue






            threads = []
            threads.append(threading.Thread(target=self.pasepage,args=( )))
            threads.append(threading.Thread(target=self.mailcodeget,args=( )))




            for n in threads:
                print("xiancheng",threads)
                n.start()   #准备就绪,等待cpu执行
            for n in threads:
                n.join()   #准备就绪,等待cpu执行
            #self.pasepage(driver,ip)
    def workon(self):

            self.readcookies()
#pinglun=driver.find_elements_by_xpath('//h3')
#for i in pinglun:

#   print(i.text)
"""
# 获取截图(验证码)
#driver.save_screenshot("验证码.png")
# 找 用户名、密码、验证、登陆豆瓣按钮
#uname = driver.find_element_by_name("form_email")
#uname.send_keys("309435365@qq.com")
# 密码
pwd = driver.find_element_by_name("form_password")
pwd.send_keys("zhanshen001")
# 验证码
key = input("请输入验证码：")
yzm = driver.find_element_by_id("captcha_field")
yzm.send_keys(key)
driver.save_screenshot("完成.png")
# 点击登陆按钮
login = driver.find_element_by_class_name("bn-submit")
login.click()
time.sleep(1)
driver.save_screenshot("登陆成功.png")
"""

if __name__ == "__main__":
    spider = WeiBoSpider()
    spider.workon()
