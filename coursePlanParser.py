from selenium import webdriver
from scrapy.selector import Selector
import re
from coursePlanItem import CourseItem, PlanItem
import time

def parseTotalInfo(browser,url):
    browser.get(url)
    browser.implicitly_wait(5)
    html=browser.find_element_by_xpath('//*').get_attribute('outerHTML')
    selector =Selector(text=html)
    item=CourseItem()
    firstTable='//*[@id="content_text"]/table[1]/tbody/'
    item['courseName']=re.sub('<.+?>', '',selector.xpath(firstTable+'tr[2]/td[1]').extract()[0], 0).strip()
    item['completionDivision']=re.sub('<.+?>', '',selector.xpath(firstTable+'tr[2]/td[2]').extract()[0], 0).strip()
    item['courseId']=re.sub('<.+?>', '',selector.xpath(firstTable+'tr[3]/td[1]').extract()[0], 0).strip()
    item['classInfo']=re.sub('<.+?>', '',selector.xpath(firstTable+'tr[3]/td[2]').extract()[0], 0).strip()
    item['credit']=re.sub('<.+?>', '',selector.xpath(firstTable+'tr[4]/td[1]').extract()[0], 0).strip()
    item['lectureType']=re.sub('<.+?>', '',selector.xpath(firstTable+'tr[4]/td[2]').extract()[0], 0).strip()
    item['departmentManage']=re.sub('<.+?>', '',selector.xpath(firstTable+'tr[5]/td[1]').extract()[0], 0).strip()
    item['departmentTarget']=re.sub('<.+?>', '',selector.xpath(firstTable+'tr[5]/td[2]').extract()[0], 0).strip()
    item['grade']=re.sub('<.+?>', '',selector.xpath(firstTable+'tr[6]/td[1]').extract()[0], 0).strip()
    item['timeAndLoc']=re.sub('<.+?>', '',selector.xpath(firstTable+'tr[6]/td[2]').extract()[0], 0).strip()
    item['professor']=re.sub('<.+?>', '',selector.xpath(firstTable+'tr[7]/td[1]').extract()[0], 0).strip()
    item['contect']=re.sub('<.+?>', '',selector.xpath(firstTable+'tr[7]/td[2]').extract()[0], 0).strip()
    item['timeAllocated']=re.sub('<.+?>', '',selector.xpath(firstTable+'tr[8]/td[1]').extract()[0], 0).strip()
    item['mail']=re.sub('<.+?>', '',selector.xpath(firstTable+'tr[8]/td[2]').extract()[0], 0).strip()
    item['manPowerOnWeeks']=re.sub('<.+?>', '',selector.xpath(firstTable+'tr[9]/td').extract()[0], 0).strip()

    secondTable='//*[@id="content_text"]/table[2]/tbody/'
    item['courseGoal']=re.sub('<.+?>', '',selector.xpath(secondTable+'tr[1]/td').extract()[0], 0).strip()
    item['teachingMethod']=re.sub('<.+?>', '',selector.xpath(secondTable+'tr[2]/td').extract()[0], 0).strip()
    item['scoreRatio']=re.sub('<.+?>', '',selector.xpath(secondTable+'tr[3]/td').extract()[0], 0).strip()
    item['bookInfo']=re.sub('<.+?>', '',selector.xpath(secondTable+'tr[4]/td').extract()[0], 0).strip()
    item['coursePolicy']=re.sub('<.+?>', '',selector.xpath(secondTable+'tr[5]/td').extract()[0], 0).strip()
    yield item

def parseWeekInfo(browser, url):
    browser.get(url)
    browser.implicitly_wait(5)
    html=browser.find_element_by_xpath('//*').get_attribute('outerHTML')
    selector =Selector(text=html)
    weekList=[]
    weekItem=PlanItem()
    frontPath='//*[@id="content_text"]/table[4]/tbody/tr['
    for i in range(2,17):
        weekItem['weekCount']=re.sub('<.+?>', '',selector.xpath(frontPath+str(i)+']/th').extract()[0], 0).strip()
        weekItem['unitGoal']=re.sub('<.+?>', '',selector.xpath(frontPath+str(i)+']/td[1]').extract()[0], 0).strip()
        weekItem['content']=re.sub('<.+?>', '',selector.xpath(frontPath+str(i)+']/td[2]').extract()[0], 0).strip()
        weekItem['teachinMethod']=re.sub('<.+?>', '',selector.xpath(frontPath+str(i)+']/td[3]').extract()[0], 0).strip()
        weekItem['anotherContent']=re.sub('<.+?>', '',selector.xpath(frontPath+str(i)+']/td[4]').extract()[0], 0).strip()
        yield weekItem

def login(browser,my_id,my_pw):
    print("check 1")
    browser.get('http://clc.chosun.ac.kr/ilos/main/member/login_form.acl')
    print("check 2")
    time.sleep(4)
    print("check 3")
    browser.find_element_by_id('usr_id').send_keys(my_id,)
    print("check 4")
    browser.implicitly_wait(0.3)
    print("check 5")
    browser.find_element_by_id('usr_pwd').send_keys(my_pw)
    print("check 6")
    browser.implicitly_wait(0.2)
    print("check 7")
    browser.find_element_by_xpath('//*[@id="myform"]/div/div/div/fieldset/div[2]/input[3]').click()
    print("check 8")
    browser.get('http://clc.chosun.ac.kr/ilos/st/main/course_ing_list_form.acl')
    return browser

def outputText_total(CourseItem):
    output=[]
    for courseItem in CourseItem:
        output.append("과목명;"+courseItem['courseName']+";")
        output.append("이수구분;"+courseItem['completionDivision']+";")
        output.append("과목코드;"+courseItem['courseId']+";")
        output.append("분반;"+courseItem['classInfo']+";")
        output.append("학점;"+courseItem['credit']+";")
        output.append("강의유형;"+courseItem['lectureType']+";")
        output.append("주관학과;"+courseItem['departmentManage']+";")
        output.append("대상학과;"+courseItem['departmentTarget']+";")
        output.append("학년;"+courseItem['grade']+";")
        output.append("시간/강의실;"+courseItem['timeAndLoc']+";")
        output.append("교수;"+courseItem['professor']+";")
        output.append("연락처;"+courseItem['contect']+";")
        output.append("상담시간;"+courseItem['timeAllocated']+";")
        output.append("이메일;"+courseItem['mail']+";")
        output.append("목표;"+courseItem['courseGoal']+";")
        output.append("강의법;"+courseItem['teachingMethod']+";")
        output.append("성적비중;"+courseItem['scoreRatio']+";")
        output.append("과목정책;"+courseItem['coursePolicy']+";")
    return output
    
def outputText_week(PlanItem):
    output=[]
    for planItem in PlanItem:
        output.append("주차;"+planItem['weekCount']+";")
        output.append("단원목표;"+planItem['unitGoal']+";")
        output.append("내용;"+planItem['content']+";")
        output.append("교수법;"+planItem['teachinMethod']+";")
        output.append("기타;"+planItem['anotherContent']+";")
    return output
def writeResult(fileName,totalOutput,weekOutput):
    f = open(fileName, 'w')
    for data in totalOutput:
        f.write(data+"\n")
    for data in weekOutput:
        f.write(data+"\n")
    f.close()

def parsingWithURL(browser,url):
    data1=outputText_total(parseTotalInfo(browser,url))
    data2=outputText_week(parseWeekInfo(browser,url))
    writeResult(data1[0].split(';')[1]+data1[3].split(';')[1]+'.txt',data1,data2)
    

    























    



















    
