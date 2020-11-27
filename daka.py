from airtest.core.api import *
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
import time
import schedule
import datetime
import random
from chinese_calendar import is_workday

#定义你要的周期运行的函数
def job(useid,password):
    #nowTime = time.strftime('%Y%m%d', time.localtime())

    
    nowTime = datetime.date(datetime.datetime.now().year,datetime.datetime.now().month,datetime.datetime.now().day)
    print(is_workday(nowTime))

    if is_workday(nowTime):
        print('Its weekday')
        driver = WebChrome()
        driver.implicitly_wait(20)
        driver.get("http://sso.portal.unicom.local/eip_sso/aiportalLogin.html?appid=na186&success=http://service.aiportal.unicom.local/ssoclient/ssologin&error=http://sso.portal.unicom.local/eip_sso/aiportalLogin.html&return=http://sso.portal.unicom.local/eip_sso/aiportalLogin.html")
        #driver.find_element_by_id('login').send_keys('testguo')
        #driver.find_element_by_id('password').send_keys('testguo112')
        driver.find_element_by_id('login').send_keys(useid)
        driver.find_element_by_id('password').send_keys(password)
        driver.find_element_by_xpath("//button[@class='login_botton']").click()
        driver.find_element_by_xpath("//div[@class='pan' and @label='人力资源2.0']").click()
        driver.switch_to_new_tab()
        driver.find_element_by_xpath("//a[@class = 'gn_block gn_block1']").click()         
        driver.switch_to_new_tab()
        driver.find_element_by_xpath("button[@class='ant-btn sign-btn ant-btn-primary']").click()
        driver.quit()
    else:
        print('Its holiday')


#下班
def job1(useid,password):
    #通过python自带的模块判断是不是节假日    
    nowTime = datetime.date(datetime.datetime.now().year,datetime.datetime.now().month,datetime.datetime.now().day)
    print(is_workday(nowTime))

    if is_workday(nowTime):
        print('Its weekday')
        driver = WebChrome()
        driver.implicitly_wait(20)
        driver.get("http://sso.portal.unicom.local/eip_sso/aiportalLogin.html?appid=na186&success=http://service.aiportal.unicom.local/ssoclient/ssologin&error=http://sso.portal.unicom.local/eip_sso/aiportalLogin.html&return=http://sso.portal.unicom.local/eip_sso/aiportalLogin.html")
        driver.find_element_by_id('login').send_keys(useid)
        driver.find_element_by_id('password').send_keys(password)
        driver.find_element_by_xpath("//button[@class='login_botton']").click()
        driver.find_element_by_xpath("//div[@class='pan' and @label='人力资源2.0']").click()
        driver.switch_to_new_tab()
        driver.find_element_by_xpath("//a[@class = 'gn_block gn_block1']").click()        
        driver.switch_to_new_tab()
        driver.find_element_by_xpath("//button[@class='ant-btn sign-btn signout ant-btn-primary']").click()
        driver.quit()
    else:
        print('Its holiday')

def myRandomTime():
 
    mydelay = random.randint(10,600)
    print(mydelay)
    time.sleep(mydelay)
    job('testgao','testgao')
   #job('testguo','testguo112')
    #job()
    #job_gaosj()
    
def myRandomTime1():
    
    mydelay = random.randint(10,600)
    print(mydelay)
    time.sleep(mydelay)
    job1('testgao','testgao')
    #job1('testguo','testguo112')

schedule.every().day.at("07:28").do(myRandomTime)
schedule.every().day.at("17:30").do(myRandomTime1)
#schedule.every().minute.do(job1)
#job()
#myRandomTime1()
while True:
     schedule.run_pending()     #运行所有可以运行的任务
     time.sleep(1)


