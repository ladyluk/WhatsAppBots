#!"C:\Python33\python.exe"
import pywhatkit as pwk
import datetime
from datetime import datetime as dt

tddt = dt.today().strftime('%m-%d')

marlinNeighborsAnniversaryList ={
    #February
    "02-25" : ["Anupama & Raghu"],
    "03-01": ["Yogeshwari & Baps"],
    "04-30" : ["Sheetal & Rahul"],
    "05-11" : ["Kshitija & Ganesh"],
    "06-26" : ["Neera & Yash"],
    "06-29" : ["Jessie & Victor"],
    "08-29" : ["Halona & Tony"],
    "11-19" : ["Sumathi & Ramesh"],
    "11-22" : ["Laura & Abhinav"],
    "11-27" : ["Ritu & Ram"],
    "12-07" : ["Sindhu & Chaitanya"]
}

marlinNeighborsBirthdayList = {
    #January
    "01-12": ["Jessie"],
    "01-14": ["Aaran", "Kirath"], 
    #February
    #March
    "03-02": ["Tyler"],
    "03-09": ["Ashrit"],
    "03-13": ["Yuvan"],
    "03-17": ["Nilima"],
    "03-19": ["Victor"],
    "03-22": ["Abhinav"],
    "03-24": ["Raya"],
    #April
    "04-11": ["Sumathi"],
    "04-17": ["Agastya"],
    #May
    "05-12": ["Yogeshwari"],
    "05-12": ["Tanishq"],
    #June
    "06-12": ["Laura"],
    "06-15": ["Halona", "Mango 🐶", "Bruno 🐶"],
    "06-22": ["Rupinder"],
    "06-25": ["Yash"],
    #July
    "07-09" : ["Rijul"],
    "07-12": ["Ram", "Harshul"],
    "07-20": ["Mason"],
    "07-21": ["Sindhu"],
    "07-26": ["Isha"],
    "07-28": ["Skittles 🐶"],
    #August
    "08-03":["Ganesh"],
    "08-06": ["Arish"],
    "08-16" : ["Baps"],
    "08-18" : ["Reyansh"],
    "08-22": ["Kshitija"],
    "08-29": ["Punit"],
    "08-30":["Tony"],
    #September
    "09-27" : ["Anupama"],
    "09-28" : ["George P. Burdell"],
    #October
    "10-05":["Sheetal"],
    "10-06" : ["Ritu"],
    "10-15" : ["Ramesh"],
    "10-20" : ["Chaitanya"],
    "10-29" : ["Vai"],
    #November
    "11-04" : ["Neera"],
    "11-07" : ["Cotton 🐶"],
    "11-13" : ["Kolm 🐶"],
    #December
    "12-02": ["Tanay"],
    "12-03" : ["Makarand"],
    "12-05" : ["Rahul"],
    "12-12" : ["Raghu"],
    "12-20" : ["Marley 🐶"],
    "12-22" : ["Shlok"],
    "12-27" : ["Samar"],
    "12-30" : ["Aditya"],
    "12-30" : ["Riya"]
}

for d, l in marlinNeighborsAnniversaryList.items():
    if d == tddt:
        for p in l:
            pwk.sendwhatmsg_to_group("EKTjU1Q83VQEOHivz0PjIC", "Happy Anniversary" + p, 7, 0)

for d, l in marlinNeighborsBirthdayList.items():
    if d == tddt:
        for p in l:
            pwk.sendwhatmsg_to_group("EKTjU1Q83VQEOHivz0PjIC", "Happy Birthday" + p, 7, 0)
