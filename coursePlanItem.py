
import scrapy

class CourseItem(scrapy.Item):
    #//*[@id="content_text"]/table[1]/tbody/tr[2]/td[1]
    courseName = scrapy.Field() #과목
    #//*[@id="content_text"]/table[1]/tbody/tr[3]/td[1]
    courseId = scrapy.Field() #과목코드
    #//*[@id="content_text"]/table[1]/tbody/tr[2]/td[2]
    completionDivision = scrapy.Field() #이수 구분
    #//*[@id="content_text"]/table[1]/tbody/tr[4]/td[1]
    credit = scrapy.Field() #학점
    #//*[@id="content_text"]/table[1]/tbody/tr[3]/td[2]
    classInfo = scrapy.Field() #분반
    #//*[@id="content_text"]/table[1]/tbody/tr[4]/td[2]
    lectureType = scrapy.Field() #강의 유형
    #//*[@id="content_text"]/table[1]/tbody/tr[5]/td[1]
    departmentManage = scrapy.Field() #주관학과
    #//*[@id="content_text"]/table[1]/tbody/tr[5]/td[2]
    departmentTarget = scrapy.Field() #대상학과
    #//*[@id="content_text"]/table[1]/tbody/tr[6]/td[1]
    grade = scrapy.Field() #학년
    #//*[@id="content_text"]/table[1]/tbody/tr[6]/td[2]
    timeAndLoc = scrapy.Field()#수업시간/강의실
    #//*[@id="content_text"]/table[1]/tbody/tr[7]/td[1]
    professor = scrapy.Field()#교수
    #//*[@id="content_text"]/table[1]/tbody/tr[7]/td[2]
    contect = scrapy.Field()#연락처
    #//*[@id="content_text"]/table[1]/tbody/tr[8]/td[1]
    timeAllocated = scrapy.Field()#상담가능시간
    #//*[@id="content_text"]/table[1]/tbody/tr[8]/td[2]
    mail = scrapy.Field()#E-mail
    #//*[@id="content_text"]/table[1]/tbody/tr[9]/td
    manPowerOnWeeks = scrapy.Field()#수업 외 요구되는 주당 학습시간
    #//*[@id="content_text"]/table[2]/tbody/tr[1]/td
    courseGoal = scrapy.Field()#교과목 개요 및 학습 목표 
    #//*[@id="content_text"]/table[2]/tbody/tr[2]/td
    teachingMethod = scrapy.Field()#수업방법
    #//*[@id="content_text"]/table[2]/tbody/tr[3]/td
    scoreRatio = scrapy.Field()#성적평가 및 비율
    #//*[@id="content_text"]/table[2]/tbody/tr[4]/td
    bookInfo = scrapy.Field()#교재 및 참고문헌
    #//*[@id="content_text"]/table[2]/tbody/tr[5]/td
    coursePolicy = scrapy.Field()#수업운영정책


class PlanItem(scrapy.Item): #tr ->
    weekCount=scrapy.Field() #//*[@id="content_text"]/table[4]/tbody/tr[2]/th
    unitGoal=scrapy.Field() #//*[@id="content_text"]/table[4]/tbody/tr[2]/td[1]
    content=scrapy.Field()  #//*[@id="content_text"]/table[4]/tbody/tr[2]/td[2]
    teachinMethod=scrapy.Field() #//*[@id="content_text"]/table[4]/tbody/tr[2]/td[3]
    anotherContent=scrapy.Field() #//*[@id="content_text"]/table[4]/tbody/tr[2]/td[4]
