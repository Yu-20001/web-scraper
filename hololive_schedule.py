import requests
from bs4 import BeautifulSoup


response = requests.get("https://schedule.hololive.tv/")
soup = BeautifulSoup(response.text,'html.parser')

#getting date
date_element= soup.find_all('div', class_="holodule navbar-text")
date_ls=[e.text for e in date_element]
for i in range(0,3):
    date_ls[i]=date_ls[i].replace(" ","")
    date_ls[i]=date_ls[i].replace("\r\n","")
#print(date_ls)

#getting name and time
tags = soup.find_all('a',class_="thumbnail")
time_compare_ls = []
time_num = 0
hour_str = ""
minute_str= ""
count = 0
time_ls=[]
for i in range(len(date_ls)):
    empty_ls=[]
    time_ls.append(empty_ls)
date = 0
for tag in tags:
    a = tag.get_text()
    a = a.replace(" ","")
    a = a.replace("\n","")
    a = a.replace("\r","")
    if(len(a)<5):
        continue
    else:
        #print(a)
        # hh:mm
        """
        for i in range(0, 5):
            print(a[i], end="")
        print(" ", end="")
        """
        # calc hh total
        for i in range(0, 2):
            hour_str += a[i]
        hour = int(hour_str)
        #print(hour, end=" ")
        # mm
        for i in range(3, 5):
            minute_str += a[i]
        minute = int(minute_str)
        #print(minute, end=" ")
        hour_str = ""
        minute_str = ""
        time_num += hour * 60 + minute
        time_compare_ls.append(time_num)
        time_num = 0
        #print(count, end=" ")
        #print(time_compare_ls[count])
        if(count == 0):
            time_ls[date].append(a)
        elif(time_compare_ls[count] >= time_compare_ls[count-1]):
            time_ls[date].append(a)
        else:
            #print("date=",date,end="")
            date+=1
            time_ls[date].append(a)
        count += 1
for i in range(3):
    print(date_ls[i])
    for e in time_ls[i]:
        for j in range(0,5):
            print(e[j],end="")
        print("",end=" ")
        for k in range(5,len(e)):
            print(e[k],end="")
        print("")
