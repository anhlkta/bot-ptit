# !pip install schedule
from requests.sessions import default_headers
import schedule
import time
import requests
from bs4 import BeautifulSoup
import json
import socket

socket.getaddrinfo('127.0.0.1', 8080)
baseUrl = "https://portal.ptit.edu.vn/category/tin-tuc"

historys = [["#"]] # Khởi tạo mảng
s = requests.Session() # Store sesstion lại
def Getdata():
    global historys 
    response = s.get(baseUrl, timeout=5) # Thực hiện Get request
    soup = BeautifulSoup(response.content, 'html.parser') # Lấy nội dung html
    titles = soup.findAll("div",class_="post-title") # Lấy tất cả các tiêu đề
    # print(titles) # In ra các tiêu đề
    historys_pre = [] # Lưu lại các tin mới
    ans = [] # Lưu lại kết quả
    for title in titles:
        x = title.find("a") # Lấy link và tiêu đề
        link = str(x['href']) # in link
        content = x.text # in nội dung tiêu đề
        historys_pre.append([link,content]) # Thêm tin vào mảng các tin mới
    if historys != historys_pre: # Nếu tin mới khác tin cũ
        for i in historys_pre: # Duyệt qua các tin mới
            if i != historys[0]: # Nếu tin mới khác tin cũ đầu tiên
                ans.append(i) # Thêm tin mới vào kết quả
            else:
                break # Nếu tin mới bằng tin cũ đầu tiên thì dừng
        if historys == [["#"]]: # Nếu tin cũ là mảng mới khởi tạo
            return [] # Trả về mảng rỗng
        historys = historys_pre # Gán lại tin cũ bằng tin mới
    return ans

def Sol():
    data = Getdata() # Lấy dữ liệu
    if data != []:
        print(data) # In ra các header
    return data
        
def Solve():
    schedule.every(10).seconds.do(Sol) # Thực hiện hàm Solve mỗi 10 giây
    while True:
        schedule.run_pending() 
        time.sleep(1) 