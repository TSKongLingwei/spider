#!/usr/bin/python
#-*-coding:utf-8 -*-
import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# driver = webdriver.Chrome(chrome_options=chrome_options)

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='/home/kong/Downloads/SLIC/chromedriver')  #写好自己电脑的chromedriver的地址
plus=9 #评论页数，以6增长，抓取的第plus—plus+6页
pages=0 #汽车页数，IP被拦截后在此设置页数继续

def get_id(pages): #获得所有汽车id
    url_lis=[]
    url='http://car.autohome.com.cn/price/list-0-0-0-0-0-0-2-0-0-0-0-0-0-0-0-'+str(pages+1)+'.html'
    driver.get(url)
    title_elements = driver.find_elements_by_class_name("main-title")
    for element in title_elements:
        url = element.find_element_by_tag_name("a").get_attribute("href")
        p=r'https://car.autohome.com.cn/price/series-(.*?).html#pvareaid='
        url_l=re.findall(p,url)
        url_lis.append(url_l[0])
    return url_lis

def parser(plus, pages):
    link_and_date=[]
    url_lll=get_id(pages)
    comments=[]
    type1=[]
    type2=[]
    score=[]
    date=[]
    evaluation=[]
    price=[]
    connect=[0]
    connect1=[0]
    connect2=[0]
    connect3=[0]
    print(url_lll)

    logfile = open("testfile.txt", 'a')
    for i in url_lll: #汽车id
        flag=0
        for j in range(6):
            # url_each='https://k.autohome.com.cn/detail/view_019qtvft176rtk6c9n64000000.html?st=1&piap=0|67|0|0|1|0|0|0|0|0|3#pvareaid=2112108'#修改这里，直到抓取完所有页数
            url_each ='http://k.autohome.com.cn/'+i+'/index_'+str(j + 1 + plus) +'.html#dataList' #修改这里，直到抓取完所有页数
            print(url_each,file=logfile)
            driver.get(url_each)
            mouthcon_elements = driver.find_elements_by_class_name("mouthcon-cont")
            for mouthcon_element in mouthcon_elements:
                element = mouthcon_element.find_element_by_class_name("mouth-main")
                element_ = element.find_element_by_class_name("mouth-item").find_element_by_class_name("title-name").find_element_by_tag_name('b').find_element_by_tag_name('a')
                link = element_.get_attribute('href')
                time = element_.text
                print("link:", link,file=logfile)
                print("time:", time,file=logfile)
                    
                comment_element = element.find_element_by_class_name("text-cont")
                comment = comment_element.text
                print("comment:", comment,file=logfile)
                    
                
                left_element = driver.find_element_by_class_name("mouthcon-cont-left")
                
                element_lis = left_element.find_elements_by_class_name("choose-dl")


                for element in element_lis:
                    name = element.find_element_by_tag_name("dt").text
                    value = element.find_element_by_tag_name("dd").text
                    print("name:", name,file=logfile)
                    print("value:", value,file=logfile)

                print('-----------------------------------------------------')
    logfile.close()
    return  score,type1

if __name__ == '__main__':
    parser(plus, pages)
    print("finish!!!")
    pass

