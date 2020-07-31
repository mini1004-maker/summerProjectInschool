import pyautogui as pag
import time
from tkinter import Tk
from _tkinter import TclError
from coursePlanItem import CourseItem, PlanItem

#http://wing.chosun.ac.kr/toinb/ch_stu/sue1016wr.html

def get_clipBoard(x,y):
    global preData
    root= Tk()
    root.withdraw()
    result=None
    pag.moveTo(x,y)
    time.sleep(0.8)
    pag.doubleClick()
    pag.click()
    pag.hotkey('ctrl', 'c')
    time.sleep(0.1)
    try:
        result=root.clipboard_get()
        if(preData==result):
            result=""
        preData=result
    except TclError as e:
        print("클립보드 데이터가 비었습니다.")
    root.update() # now it stays on the clipboard after the window is closed
    root.destroy()
    return result
               
def get_courseItem():
    item=CourseItem()
    #3*4 table
    table_coloumn1 =501
    table_coloumn2 =884
    table_coloumn3 =1233
    y_start=308
    y_distance=27
    
    item['courseName']=get_clipBoard(table_coloumn1,y_start)  #교과목명657, 285 
    item['completionDivision']=get_clipBoard(table_coloumn1, y_start+y_distance*5)#지난학기 수업평가 686, 385 //이수구분-> 지난학기 평점
    item['courseId']=get_clipBoard(table_coloumn2,y_start)  #교과목번호 927,285
    item['classInfo']=get_clipBoard(table_coloumn3, y_start)#분반 1144, 285
    item['credit']=get_clipBoard(table_coloumn1, y_start+y_distance*1)#과목 학점 634, 305
    item['lectureType']=get_clipBoard(table_coloumn2, y_start+y_distance*1)#강좌유형 927, 305
    item['departmentManage']=get_clipBoard(table_coloumn1, y_start+y_distance*2)#주관학과 634, 325
    item['departmentTarget']=get_clipBoard(table_coloumn2, y_start+y_distance*2)#대상학과  927, 325
    item['grade']=get_clipBoard(table_coloumn3, y_start+y_distance*2)#대상학년 1144, 325
    item['timeAndLoc']=get_clipBoard(table_coloumn3, y_start+y_distance*1)#수업시간/강의실 1144, 305
    item['professor']=get_clipBoard(table_coloumn1, y_start+y_distance*3)#담당교수 634, 345
    item['contect']=get_clipBoard(table_coloumn2, y_start+y_distance*3)#연락처  927, 345
    item['timeAllocated']=get_clipBoard(table_coloumn3, y_start+y_distance*3)#상담가능시간 1144, 345
    item['mail']=get_clipBoard(table_coloumn1, y_start+y_distance*4)#이메일 #686 365
    item['manPowerOnWeeks']=get_clipBoard(table_coloumn3, y_start+y_distance*4)#수업외 주당 학습시간 1050, 365

    item['courseGoal']=get_clipBoard(table_coloumn1, 519)#학습 목표 713, 419
    item['teachingMethod']=get_clipBoard(table_coloumn1,608)+ get_clipBoard(table_coloumn1, 636 )#교수법 647,484 / 638, 502
    #중간 672,526 #기말 747,527 #과제 823, 525 #출석 899, 526 #실험실습 1003,527 #발표 1079, 527 #기타 1154, 527
    item['scoreRatio']="중간:%s 기말:%s 과제:%s 출석:%s 실험.실습:%s 발표:%s 기타:%s"%(get_clipBoard(524, 666),get_clipBoard(643, 670),get_clipBoard(757, 670),get_clipBoard(870, 672),get_clipBoard(1021, 671),get_clipBoard(1136, 672),get_clipBoard(1248, 671))
    item['bookInfo']=get_clipBoard(table_coloumn1,842)#교재 738,632
    item['coursePolicy']=get_clipBoard(table_coloumn1,917)#수업 정책 680,697
    yield item
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

def writeResult(fileName,totalOutput):
    f = open(fileName, 'w')
    for data in totalOutput:
        f.write(data+"\n")
    #for data in weekOutput:
    #    f.write(data+"\n")
    f.close()


pos = pag.position() 

#개설강좌 현황 창 (0,0)기준 (285,110)   (974,706)

#클릭 타겟 # (554, 133-144)  한페이지 38
#139 - 11단위
for i in range(2):
    for i in range(0,43):
        pag.moveTo(749,185+(17*i))
        pag.doubleClick() # 더블 클릭
        preData=""
        data1=outputText_total(get_courseItem())
        writeResult(data1[0].split(';')[1]+data1[3].split(';')[1]+'.txt',data1)
        pag.moveTo(1564, 178)
        pag.doubleClick() # 더블 클릭
    pag.scroll(700, x=1474, y=246) 
