from coursePlanParser import *
from selenium import webdriver
from scrapy.selector import Selector
from bs4 import BeautifulSoup as bs
import time
 

 
#my_id=
#my_pw=
 

browser = webdriver.Chrome('chromedriver')

browser=login(browser,my_id,my_pw)

browser.implicitly_wait(5)


url_list=[]

 

for i in range(1,8):
    try:
        browser.get('http://clc.chosun.ac.kr/ilos/st/main/course_ing_list_form.acl')
        browser.implicitly_wait(5)
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="content_text"]/div/a['+str(i)+']').click()
        print(i,end=' ')
        time.sleep(5)
        browser.implicitly_wait(5)
    except:
        print("-1")

    html=browser.find_element_by_xpath('//*[@id="content_text"]/table/tbody').get_attribute('outerHTML')
    soup=bs(html, 'html.parser')
    class_list= []
 

    for tag in soup.select('.site-link'):
        class_list.append(re.findall('\d+', tag['href'])[0])
        #print(i,re.findall('\d+', tag['href'])[0] ,end = ' ' )

    

    for j in range(len(class_list)):
        try:
            browser.get('http://clc.chosun.ac.kr/ilos/st/main/course_ing_list_form.acl')
            browser.implicitly_wait(100)
            time.sleep(5)
            browser.find_element_by_xpath('//*[@id="content_text"]/div/a['+str(i)+']').click()
            time.sleep(5)
            print("\n"+i,end=' ' )
            browser.implicitly_wait(5)

        except:
            print("-1",end =' ')
            print(i)
            pass

                

        browser.find_element_by_xpath('//*[@id="'+class_list[j]+'"]/td[3]/a').click()

        browser.implicitly_wait(0.2)

        parsingWithURL(browser,browser.current_url)

 

 
