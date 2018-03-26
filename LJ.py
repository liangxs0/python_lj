import requests
import re
import pymysql
def get_info(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    add_add = r'<span class="region">(.*?)&nbsp;&nbsp;'
    stru_add = r'<span class="zone"><span>(.*?)&nbsp;&nbsp;'
    size_add = r'<span class="meters">(.*?)&nbsp;&nbsp;'

    floor_add = r'</a><span>/</span>(.*?)<span>/</span>.*?'
    source_add = r'<div class="con"><a href=".*?">(.*?)</a><'
    money_add = r'<div class="price"><span class="num">(.*?)</span>'
    add = re.findall(add_add,response.text)
    stru = re.findall(stru_add,response.text)

    floor = re.findall(floor_add,response.text)
    source = re.findall(source_add,response.text)
    size = re.findall(size_add,response.text)
    money = re.findall(money_add,response.text)
    #print(add[0],stru[0],source[0],floor[0],size[0],money[0])
    return add,stru,floor,source,size,money
def into_db(add,stru,floor,source,size,money):

if __name__ == '__main__':
    url = 'https://su.lianjia.com/zufang/'
    add, stru, floor, source, size, money = get_info(url)
    conn = pymysql.connect(host='127..0.0.1',port = 8080,user = 'root',password = '1230,charset = 'utf-8')
    cur = conn.cursor()
    cur.execute("create database if not EXISTS lj;")
    conn.select_db('lj')
    cur.execute("craete table info")
    into_db(add,stru,floor,source,size,money)

