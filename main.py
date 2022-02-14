import telebot
import requests
import json
import random
import os
import re
from bs4 import BeautifulSoup as s
from telebot import types
import sys
import pymongo
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import time
import json
import urllib.parse
import random
import os
import re
from bs4 import BeautifulSoup
from telebot import types
from datetime import date, timedelta
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
channal1 = -1001529594535
channal2 = -1001238773838
#point users
client2user = pymongo.MongoClient("mongodb+srv://as:as@cluster0.kfjbc.mongodb.net/as?retryWrites=true&w=majority")
mydb= client2user["as"]

mycol = mydb["users"]
mycol2 = mydb["saveurlnew"]
mycol3 = mydb["saveurl1"]
mycola = mydb["user"]
mycol3s= mydb["copon"]
allgive="0"
#admin
list = ["1750254175","1205882498"]


listgrop = ["-1001238773838"]
#your acouunt
d=["refreshToken=21739380c8fd336388624c38b966775ac641d50e"]






payload={}
#urls need
url = "https://nk6xemh85d.execute-api.us-east-1.amazonaws.com/prod/user/qna-question"
url2limt="https://nk6xemh85d.execute-api.us-east-1.amazonaws.com/prod/user/qna-questions-limit"
emils = "https://nk6xemh85d.execute-api.us-east-1.amazonaws.com/prod/user/"
#token bot telegram
TELEGRAM_TOKEN = "1947290999:AAFhkMIlI9NrHJ6i0gRRpj_zWOqEj-YXm44"
bot = telebot.TeleBot(TELEGRAM_TOKEN, parse_mode=None  , threaded=False)





def sub7time(repy_id,add_time):
    try:
        print("oooo:"+repy_id)
        u=int(add_time)*1
        mydoc2 = mycola.find_one({ str(repy_id):str(repy_id)})
        print(str(mydoc2))

        print("id user time :"+str(repy_id))
        if str(repy_id) not  in str(mydoc2):
            print("user not in file time")
            date = datetime.now()
            print('time :'+str(date))
            date3 = date - relativedelta(days=u )
            mydict = {  str(repy_id):str(repy_id), "timeout": str(date3) }
            x = mycola.insert_one(mydict)
            mydoc2 = mycol.find_one({ str(repy_id):str(repy_id)})
            g=[mydoc2]
            falluser = str(g[0]['timeout'])
            e = '' + falluser + ''
            i = datetime.strptime(e, '%Y-%m-%d %H:%M:%S.%f')
            z = (i - datetime.now()).days
            print(z)

            # z = (date - datetime.now()).days
            return z
        else:
            print("user is old in file time :"+str(repy_id))
            g=[mydoc2]
            falluser = str(g[0]['timeout'])
            e = '' + falluser + ''
            i = datetime.strptime(e, '%Y-%m-%d %H:%M:%S.%f')
            print(i)
            date = i - relativedelta(days=u)
            print(str(date))
            mydict77 = {  str(repy_id):str(repy_id), "timeout": str(date) }
            mydict4 = { "$set":mydict77}
            mycola.update_one(mydoc2, mydict4)
            mydoc3 = mycol.find_one({ str(repy_id):str(repy_id)})
            g=[mydoc2]
            falluser = str(g[0]['timeout'])
            e = '' + falluser + ''
            i = datetime.strptime(e, '%Y-%m-%d %H:%M:%S.%f')
            z = (i - datetime.now()).days
            print(z)

           # z = (date - datetime.now()).days
            print(z)
            return z
    except:
        pass
def add7time(repy_id,add_time):
    try:
        print("oooo:"+repy_id)
        u=int(add_time)*1
        mydoc2 = mycola.find_one({ str(repy_id):str(repy_id)})
        print(str(mydoc2))

        print("id user time :"+str(repy_id))
        if str(repy_id) not  in str(mydoc2):
            print("user not in file time")
            date = datetime.now()
            print('time :'+str(date))
            date3 = date + relativedelta(days=u )
            mydict = {  str(repy_id):str(repy_id), "timeout": str(date3) }
            x = mycol.insert_one(mydict)
            mydoc2 = mycola.find_one({ str(repy_id):str(repy_id)})
            g=[mydoc2]
            falluser = str(g[0]['timeout'])
            e = '' + falluser + ''
            i = datetime.strptime(e, '%Y-%m-%d %H:%M:%S.%f')
            z = (i - datetime.now()).days
            print(z)

            # z = (date - datetime.now()).days
            return z
        else:
            print("user is old in file time :"+str(repy_id))
            g=[mydoc2]
            falluser = str(g[0]['timeout'])
            e = '' + falluser + ''
            i = datetime.strptime(e, '%Y-%m-%d %H:%M:%S.%f')
            print(i)
            date = i + relativedelta(days=u)
            print(str(date))
            mydict77 = {  str(repy_id):str(repy_id), "timeout": str(date) }
            mydict4 = { "$set":mydict77}
            mycola.update_one(mydoc2, mydict4)
            mydoc3 = mycola.find_one({ str(repy_id):str(repy_id)})
            g=[mydoc2]
            falluser = str(g[0]['timeout'])
            e = '' + falluser + ''
            i = datetime.strptime(e, '%Y-%m-%d %H:%M:%S.%f')
            z = (i - datetime.now()).days
            print(z)
            return z
    except:
        pass

    ### check time users
def check_time(user_id):
    try:
        print("id user time :" + str(user_id))
        mydoc2 = mycola.find_one({str(user_id): str(user_id)})
        # print(str(mydoc2))
        # mydict = { str(user_id):str(user_id), "timeout": 44 }
        # x = mycol.insert_one(mydict)
        # point(x)

        if str(user_id) not in str(mydoc2):
            print("user not in  time")
            date = datetime.now()
            print('time :' + str(date))
            mydict = {str(user_id): str(user_id), "timeout": str(date)}
            x = mycola.insert_one(mydict)
            print(x)
           # falluser =str(date)
            #e = '' + falluser + ''
            #i = datetime.strptime(e, '%Y-%m-%d %H:%M:%S.%f')
            z = (datetime.now() - datetime.now()).days
            print(z)
            z1 = int(z)
            if z1 < 0 :
                print("oooo")
                add_time = str(z1 *(-1))
                print("add-nub:"+str(add_time))
                repy_id = str(user_id)
                uu = add7time(repy_id,add_time)
                print(uu)
                return str(0)
        else:
            g = [mydoc2]
            print("user is old in file time :" + str(g[0]['timeout']))
            falluser = g[0]['timeout']
            e = '' + falluser + ''
            i = datetime.strptime(e, '%Y-%m-%d %H:%M:%S.%f')
            z = (i - datetime.now()).days
            print(z)
            return str(z)
    except:
        pass
#del users

def zro(repy_id):
    try:
        mydoc2 = mycol.find_one({ str(repy_id):str(repy_id)})
        print(mydoc2)
        print("is sub grube")
        g=[mydoc2]
        oldadd=int(g[0]['point'])
        newadd=int(g[0]['point'])
        clc=oldadd-newadd
        print("is clc sub  :"+str(clc))
        mydict77 = {  str(repy_id):str(repy_id), "point": str(clc) }
        mydict4 = { "$set":mydict77}
        mycol.update_one(mydoc2, mydict4)
        return str(clc)
    except:
        pass

#sub grupe
def sub_point(user_id):
    try:
        mydoc2 = mycol.find_one({ str(user_id):str(user_id)})
        print(mydoc2)
        print("is sub ")
        g=[mydoc2]
        oldadd=int(g[0]['point'])
        newadd=int("1")
        clc=oldadd-newadd
        print("is clc sub  :"+str(clc))
        mydict77 = {  str(user_id):str(user_id), "point": str(clc) }
        mydict4 = { "$set":mydict77}
        mycol.update_one(mydoc2, mydict4)
        return str(clc)
    except:
        pass



#add points
def add_point(repy_id ,add):
    try:
        #print("id group points :"+str(chat_id)+"and add point :"+str(add_point))
        mydoc2 = mycol.find_one({ str(repy_id):str(repy_id)})
        print(mydoc2)
        if  str(repy_id)  not in str(mydoc2):
            mydict = {  str(repy_id):str(repy_id), "point": str(add) }
            x = mycol.insert_one(mydict)
            return str(add)
        else:
            print("is old grupe")
            g=[mydoc2]
            oldadd=int(g[0]['point'])
            newadd=int(add)
            clc=oldadd+newadd
            print("is clc :"+str(clc))
            mydict77 = {  str(repy_id):str(repy_id), "point": str(clc) }
            mydict4 = { "$set":mydict77}
            mycol.update_one(mydoc2, mydict4)
            return str(clc)
    except:
        pass



#chuck point
def get_point(user_id):
    try:
        print("id  points :"+str(user_id))
        mydoc2 = mycol.find_one({ str(user_id):str(user_id)})
        print(mydoc2)
        if  str(user_id)  not in str(mydoc2):
            mydict = {  str(user_id):str(user_id), "point": allgive }
            x = mycol.insert_one(mydict)
            return allgive
        else:
            g=[mydoc2]
            print("user is old in file time :"+str(g[0]['point']))
            return str(g[0]['point'])
    except:
        pass
def all4add(add):
    try:
        j=[]
        mydoc2 = mycol.find()
        for x in mydoc2:
            g=[x]
            j.append(g)
        for ch in j:
            print(ch[0])
            oldadd=int(ch[0]['point'])
            newadd=int(add)
            clc=oldadd+newadd
            print("is clc :"+str(clc))
            print(ch[0]['_id'])
            myy= {  "point": str(ch[0]['point']) }
            mydict77 = {  "point": str(clc) }
            mydict4 = { "$set":mydict77}
            mycol.update_one(ch[0], mydict4)
    except:
        pass

#sub all points

def all4sub(add):
    try:
        j=[]
        mydoc2 = mycol.find()
        for x in mydoc2:
            g=[x]
            j.append(g)
        for ch in j:
            print(ch[0])
            oldadd=int(ch[0]['point'])
            newadd=int("0")
            clc=oldadd*newadd
            print("is clc :"+str(clc))
            print(ch[0]['_id'])
            myy= {  "point": str(ch[0]['point']) }
            mydict77 = {  "point": str(clc) }
            mydict4 = { "$set":mydict77}
            mycol.update_one(ch[0], mydict4)
    except:
        pass    
###########
def Business():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Accounting']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Management']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Economics']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Marketing']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Finance']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Operations-Management']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Back']])
    return keyboard
##########
def Engineering():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Chemical-Engineering']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Computer-Science']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Civil-Engineering']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Electrical-Engineering']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Computer-Engineering']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Mechanical-Engineering']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Back']])
    return keyboard
############
def Math():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Algebra']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Probability']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Advanced-Math']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Calculus']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Statistics']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Geometry']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Trigonometry']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Back']])
    return keyboard


#############
def Science():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Nursing']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Physics']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Biology']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Biochemistry']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Chemistry']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Advanced-Physics']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Back']])
    return keyboard


#############
def Social_Science():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Psychology']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Sociology']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Back']])
    return keyboard
###################
def New_Subjects():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Anatomy-and-Physiology']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['History']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Earth-Science']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Geography']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Political-Science']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Back']])
    return keyboard
##############
def back():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Engineering']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Business']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Math']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Science']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Social Science']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['New Subjects']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Exit']])
    return keyboard

##########
def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("🔰More chances🔰", url="https://t.me/chegglock/55"))
    return markup

def gen_markup4():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("🔘اضغط هنا للاشتراك (subscribe)🔘", url="https://t.me/chegglock/65"),InlineKeyboardButton("🔘Click here to subscribe🔘", url="https://t.me/chegglock/67"),InlineKeyboardButton("🔘Admin🔘", url="https://t.me/lock140"))
    return markup
#############   
def gen_markup2filed():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    return keyboard 
#dif all subjuct
def all_subj():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Engineering']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Business']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Math']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Science']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Social Science']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['New Subjects']])
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name in ['Exit']])
    return keyboard
def gen_markup9():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("chegg solution", url="https://t.me/chegg_So"))
    return markup

def gen_markup7():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("🔘Channel🔘", url="https://t.me/chegglock"))
    return markup

def gen_markup7s():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("🔘Bartleby Group🔘", url="https://t.me/Bartleby_vipp"))
    return markup

def key():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("🛑chegg solution🛑", url="https://t.me/chegg_So"),InlineKeyboardButton("🔵Bartleby solution🔵", url="https://t.me/chegg_So"),InlineKeyboardButton("🔘Admin🔘", url="https://t.me/lock140"))
    return markup


#get text
@bot.message_handler(content_types=['text'])
def send_text(message):
    mention = "[" + str(message.from_user.first_name) + "](tg://user?id=" + (str(message.from_user.id)) + ")"

    result = bot.get_chat_member(channal1, message.from_user.id)
    result1 = bot.get_chat_member(channal2, message.from_user.id)
    

    if "'status': 'left'" in str(result1):
        print("nooooooo me")
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, '{s} \n مرحبا.. \nعليك الاشتراك في القناة لتستطيع استخدام البوت مجانا \nYou must subscribe to the channel to be able to use the bot for free🌚'.format(s=str(mention)) , disable_notification=True ,reply_markup=gen_markup7s() ,parse_mode='Markdown')
    elif "'status': 'left'" in str(result) :
        print("nooooooo me")
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, '{s} \n مرحبا.. \nعليك الاشتراك في القناة لتستطيع استخدام البوت مجانا \nYou must subscribe to the channel to be able to use the bot for free🌚'.format(s=str(mention)) , disable_notification=True ,reply_markup=gen_markup7() ,parse_mode='Markdown')
    else:
        if message.text=="/get":

          datenow = datetime.today().strftime('%Y-%m-%d')
          user_id=message.from_user.id

          pi=get_point(user_id)
          print(pi)
          r = check_time(user_id)
          print(str(r))
          ee=int(r)
          ff=int(pi)

          if  ee>0:
            bot.send_message(message.chat.id,'🛑Remaining  chances : free post'+"\n\n❇️Type : Free post for  "+str(r)+ " days\n\n🕛Date : " + datenow ,reply_to_message_id=message.message_id)
          else :
            if ff==0 :
             bot.send_message(message.chat.id,'❎Remaining  Point : '+str(pi)+"\n\n🔘Type : Not activated ❌"+ "\n\n🕛Date : " + datenow ,reply_to_message_id=message.message_id)
            else : 
             bot.send_message(message.chat.id,'🅿️Remaining  point : '+str(pi)+"\n\n🔘Type : ✅ Activated ✅"+ "\n\n🕛Date : " + datenow ,reply_to_message_id=message.message_id)

        elif ("/free-") in message.text  and str(message.from_user.id) in str(list) and message.reply_to_message.from_user.id :

          print(message.text)
          strin = str(message.text)
          pattern = '\d+'
          resultsub = re.findall(pattern, strin)
          print(resultsub)
          add_time = resultsub[0]
          repy_id = str(message.reply_to_message.from_user.id)
          user_id = repy_id
          print(check_time(user_id))
          tt = add7time(repy_id, add_time)
          r = check_time(user_id)
          yy=int(r)
          bot.send_message(message.chat.id, f'✅Added time : {resultsub[0]} days' +"\n\n🔘Total free : "+str(yy)+"days" ,reply_to_message_id=message.reply_to_message.message_id)     
        elif ("www.chegg.com") in message.text:
            bot.delete_message(message.chat.id, message.message_id)
            bot.send_message(message.chat.id, '{s}\n مرحباً ...\n❌ It is not allowed to send jake links here.. Send the link of your question in the group below\n❌غير مسموح ارسال روابط جيك هنا..قم بأرسال رابط سؤالك في المجموعة ادناه'.format(s=str(mention)) , disable_notification=True ,reply_markup=gen_markup9() ,parse_mode='Markdown')
        elif ("www.coursehero.com") in message.text:
            bot.delete_message(message.chat.id, message.message_id)
        elif ("t.me/") in message.text and str(message.from_user.id) not in str(list):
            bot.delete_message(message.chat.id, message.message_id)
        elif message.text.startswith('/add-') and message.reply_to_message and str(message.from_user.id) in str(list):
            datenow = datetime.today().strftime('%Y-%m-%d')
            repy_id=message.reply_to_message.from_user.id
            string = str(message.text)
            pattern = '\d+'
            result = re.findall(pattern, string)
            print(result)
            add=str(result[0])
            asd=add_point(repy_id ,add)
            bot.send_message(message.chat.id,"✅point add is : " + str(add)+'\n\n🔘Total point : '+str(asd) + "\n\n🕛Date : " + datenow,reply_to_message_id=message.reply_to_message.message_id)
        elif message.text.startswith('/all-')  and str(message.from_user.id) in str(list):
            string = str(message.text)
            pattern = '\d+'
            result = re.findall(pattern, string)
            print(result)
            add=str(result[0])
            all4add(add)
            bot.send_message(message.chat.id,'✅Chances are increased for everyone : '+str(add) ,reply_to_message_id=message.message_id)
        elif message.text.startswith("/sub-") and str(message.from_user.id) in str(list) and message.reply_to_message.from_user.id :
            print(message.text)

            strin = str(message.text)
            pattern = '\d+'
            resultsub = re.findall(pattern, strin)
            print(resultsub)
            add_time = resultsub[0]
            repy_id = str(message.reply_to_message.from_user.id)
            tt = sub7time(repy_id, add_time)
            bot.send_message(message.chat.id, f'Sub time for the member: {resultsub[0]} days',reply_to_message_id=message.reply_to_message.message_id)    
            
        elif message.text.startswith('/allzero') and str(message.from_user.id) in str(list):  
            add="0"
            all4sub(add)
            bot.send_message(message.chat.id,'Total points have been deleted all' ,reply_to_message_id=message.message_id)    
        elif message.text=="/zero" and message.reply_to_message and str(message.from_user.id) in str(list):
            repy_id=message.reply_to_message.from_user.id
            zz=zro(repy_id)
            bot.send_message(message.chat.id,'Total points have been deleted' ,reply_to_message_id=message.message_id)
        elif message.text.startswith("/info"):
            num = mycol3.count()
            bot.send_message(message.chat.id,f"❇️ Number of Links Saved : {num}\n\n ❇️ عدد الاسئلة المرفوعة : {num} ",reply_to_message_id=message.message_id)

        elif message.text.startswith("/saver"):
            num = mycol2.count()
            bot.send_message(message.chat.id,f"🟡 Number of questions waiting : {num}\n\n🟡 عدد الاسئلة في الانتظار : {num}",reply_to_message_id=message.message_id)     
        elif message.text.startswith("https://www.bartleby.com/questions-and-answers"):
          if message.chat.type == 'private' and str(message.from_user.id)  not in str(list) :
            bot.send_message(message.chat.id,'❌البوت يعمل في المجموعات فقط❌\n\nThe bot works only in groups',reply_markup=gen_markup7s(),reply_to_message_id=message.message_id)
          
          else: 
          
            datenow = datetime.today().strftime('%Y-%m-%d')
            url = message.text
            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
  'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
  'Cookie': "_gcl_au=1.1.1121526104.1634843983; _ga=GA1.2.1222430549.1634843987; _fbp=fb.1.1634843992366.448561356; _hjid=92625c32-3023-4af1-8849-636b31e86451; G_ENABLED_IDPS=google; _hjSessionUser_1400488=eyJpZCI6IjU0NTc5Yzc3LWJjNWQtNTkyYi04NWIyLWIwNmU5OWQxYTE3YSIsImNyZWF0ZWQiOjE2Mzc1OTkyMjc1OTgsImV4aXN0aW5nIjp0cnVlfQ==; ki_r=; _gaexp=GAX1.2.X-uOdja7RPmf-CPQrv8FPQ.19036.x272; optimizelyEndUserId=oeu1638895397140r0.3740585328332844; cookieconsent_status=dismiss; sailthru_visitor=52e2faea-fccc-4a46-a04e-54c5c204078d; _fssid=3ee56717-d615-4d8e-9aa5-d5b54dabcd5e; __qca=P0-555405187-1638895793329; _gid=GA1.2.606343047.1639640607; _uetsid=dc07d7305e4311ecaecb0d0f1a2f03b7; _uetvid=ed23459032a311eca0d79738a7076d00; _gat_UA-20169249-1=1; accessToken=9617b5e4259c99c2cbaaf34a9edbd562c22d4dc4; refreshToken=dc2e07bc6c90c9c5780e047be85f3111af37024c; userId=0f2dcb64-1540-4756-96dd-426a2dd96aa1; bartlebyRefreshTokenExpiresAt=2022-01-15T09:27:15.497Z; promotionId=; userStatus=A1; sku=bb999_firstmonth; _hjCachedUserAttributes=eyJhdHRyaWJ1dGVzIjp7ImNvdW50cnkiOiJJUSIsImdlb2dyYXBoeSI6IkludGVybmF0aW9uYWwiLCJzdWJzY3JpcHRpb25fbW9udGgiOiIiLCJ1c2VyX3NvdXJjZSI6IkNPTVBBU1MiLCJ1c2VyX3N0YXR1cyI6IkExIn0sInVzZXJJZCI6IjBmMmRjYjY0LTE1NDAtNDc1Ni05NmRkLTQyNmEyZGQ5NmFhMSJ9; _gat_UA-93748-2=1; _hjAbsoluteSessionInProgress=0; isNoQuestionAskedModalClosed=true; btbLiveChatFabTriggerDate=2021-12-16T09:57:29.592Z; ABTasty=uid=m2mzpgn34r161m44&fst=1634843987659&pst=1639643301659&cst=1639646839760&ns=27&pvt=246&pvis=4&th=720581.895278.1.1.1.1.1637600262683.1637600262683.1; ABTastySession=mrasn=&sen=3&lp=https%253A%252F%252Fwww.bartleby.com%252Fdashboard%252Fmy-questions; ki_t=1636491439129%3B1639640618846%3B1639646875561%3B9%3B41; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Dec+16+2021+12%3A27%3A56+GMT%2B0300+(Arabian+Standard+Time)&version=6.23.0&isIABGlobal=false&hosts=&consentId=26193cab-828e-4028-b23d-87b7e6f51dd0&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CBG1%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false&landingPath=NotLandingPage&groups=C0001%3A1%2CBG1%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false"
}

            response = requests.request("GET", url, headers=headers)
            b = BeautifulSoup(response.text, "html.parser")
            uid = re.findall("\w{8}-\w{4}-\w{4}-\w{4}-\w{12}", str(message.text))[0]
            print(uid)
            url = f"https://prod-api.bnedcompass.com/qna/answer/{uid}"
            headers = {
                'User-Agent': 'Bartleby/196 CFNetwork/1240.0.4 Darwin/20.5.0',
                'Authorization': 'Bearer 4f6064e00735f1c47e32ad8b60047630c796b099',
            }
            response = requests.request("GET", url, headers=headers)
            print(response.text)
            stats = json.loads(response.text)['data']['question']['status']
            if ("Rejected") in str(stats):
                bot.send_message(message.chat.id,
                                 "❌ *تم حذف سوالك من قبل الموقع ...Your question has been deleted * ❌",
                                 parse_mode='Markdown', reply_to_message_id=message.message_id)
            elif ('Pending') in str(stats):
                bot.send_message(message.chat.id, "⚠️ *لم يتم حل السؤال ...تحقق من الرابط\n Your question has not been solved yet ..... * ⚠️",
                                 parse_mode='Markdown', reply_to_message_id=message.message_id)
            else:
                uid = re.findall("\w{8}-\w{4}-\w{4}-\w{4}-\w{12}", str(message.text))[0]
                print(uid)
                url = f"https://prod-api.bnedcompass.com/qna/answer/{uid}"
                headers = {
                    'User-Agent': 'Bartleby/196 CFNetwork/1240.0.4 Darwin/20.5.0',
                    'Authorization': 'Bearer 4f6064e00735f1c47e32ad8b60047630c796b099',
                }
                response = requests.request("GET", url, headers=headers)
                questionPhoto = json.loads(response.text)['data']['question']
                print(questionPhoto)
                print(questionPhoto['images'])
                if questionPhoto['images'] == []:
                    img = questionPhoto['text']
                elif questionPhoto['images']:
                    qq = questionPhoto['images']
                    img = f"<img src='{qq[0]['imageUrl']}'>"
                x0 = b.find('div', '</div>', class_="styles__MyQuestionContainer-sc-1xvt7re-1 dhCoVb")
                x1 = b.find('div', '</div>', class_="styles__MyAnswerContainer-sc-1xvt7re-12 dbSTOD")
                x1.find('div', '</div>', class_="styles__MyAnswerHeader-sc-1xvt7re-13 jFcvrg").decompose()
                images = x1.findAll('img')
                f = open("answer.html", "w", encoding='UTF-8')
                print("reach")
                messagee = str(
                    """
                    

                    <html><head>
                
                 <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
                
                
                <style>
                                            
                                            .a {
                                                background-color: #33FF00;
                                                border: 7px solid #33FF00;
                                            }
                                            
                                            .nn {
                                                background-color: red;
                                                border: 7px solid red;
                                            }
                                            
                                           <meta charset="UTF-8"><html><head><link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css"><link rel="preconnect" href="https://fonts.gstatic.com"><link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet"><link rel = "stylesheet" type = "text/css" href = "https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.9.0/katex.min.css" /><link href="https://fonts.googleapis.com/css2?family=Baloo+Bhaina+2:wght@600&display=swap" rel="stylesheet"></head><body><style>.x {background-color: white;border:solid red 5px; }.y {background-color: white;border:solid green 5px;}.x img{max-width: 100%;max-height: 100%;margin: auto;display: block;}.y img{ max-width: 100%; max-height: 100%; margin: auto; display: block; }  .highlighted-text {background-image: url('data:');  </style> <link rel="preconnect" href="https://fonts.gstatic.com"> <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet"> <link rel = "stylesheet" type = "text/css" href = "https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.9.0/katex.min.css" /> <link href="https://fonts.googleapis.com/css2?family=Baloo+Bhaina+2:wght@600&display=swap" rel="stylesheet"> <h1> <div class="tele"> <div class="center"> <center><strong><div><p>Solution obtained by STUDENT SERVICES</p> </div> <div class="center" ><center><strong> <img src="https://blogger.googleusercontent.com/img/a/AVvXsEg9LnL_z1-JsSaZPeLeHPnLY8P4XSAHt7vaSOuGsuFpFJOVznOr4cj-0zi5hc5yqUPiGH2CuBsgTd2GKjRNS2GssNy6Mkk_sdkrbpzS8YW0HcY3YACznWdzG47me34UNhfcUDeU0iMmDGPY9d1EYu4JHiDrDUxndUchHDqdae9F3e5OBwiNKKtJFo6RuQ=s228"> 
<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">×</span></button>
                                            <center><strong> <p><a href="https://t.me/Bartleby_vipp">For All Answers bartleby Join group : @Bartleby_vipp</a></p></strong>
                                            </div> <span class="group_title"></span> <div class="tgme_page_extra"></div><p><span class="highlighted-text"></span> </p></div> <center><strong> <p><a href="https://t.me/chegg_So">For All Answers chegg Join group : chegg_So</a></p></strong>
                                            </div> <div> </div> </div> </h1> <h1> <p> <div class="center">            
                                                     
                                                </div>
                                            </div>
                                            </h1>
                                              <h1>
                                                <p>
                                                    
                                                    <div class="nn"
                                                     align="center">Your Question
                                                    </div>
                                                </p>
                                            </h1>
                                        <div class="x" align="center"> """+ str(
                        img) +"""</div>
                                            </div>
                                              <h1>
                                                <p>
                                                    <div class="a"
                                                     align="center">Your Answer
                                                    </div>
                                                </p>
                                            </h1>
                                            <div class="y">
                                        </div>"""+ str(
                        x1) +
                                       
                        """
                                                
                                                          </html> """  )
                f.write(messagee)
                f.close()
                i = open('./answer.html', 'rb')
                bot.send_document(message.chat.id, i,
                                  caption=
                                  f"*Name *: {mention}\n\n"
                                  f"*✅This is your answer* \n"
                                  f"\n🕛Date : {datenow} \n",reply_markup=key(),
                                  parse_mode='Markdown', reply_to_message_id=message.message_id)     
    
#get photo from users
@bot.message_handler(content_types=['photo'])
def get_phot(message):
    mention = "[" + str(message.from_user.first_name) + "](tg://user?id=" + (str(message.from_user.id)) + ")"

    result = bot.get_chat_member(channal1, message.from_user.id)
    result1 = bot.get_chat_member(channal2, message.from_user.id)
    

    if "'status': 'left'" in str(result1) and str(result):
        print("nooooooo me")
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, '{s} \n مرحبا.. \nعليك الاشتراك في القناة لتستطيع استخدام البوت مجانا \nYou must subscribe to the channel to be able to use the bot for free🌚'.format(s=str(mention)) , disable_notification=True ,reply_markup=gen_markup7s() ,parse_mode='Markdown')
    elif "'status': 'left'" in str(result) and str(result1):
        print("nooooooo me")
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, '{s} \n مرحبا.. \nعليك الاشتراك في القناة لتستطيع استخدام البوت مجانا \nYou must subscribe to the channel to be able to use the bot for free🌚'.format(s=str(mention)) , disable_notification=True ,reply_markup=gen_markup7() ,parse_mode='Markdown')
    else :  

      user_id=message.from_user.id
      pi=get_point(user_id)
      print(pi)
      ress=int(pi)
      r = check_time(user_id)
      print(str(r))
      reaa=int(r)
      if (ress==0 or ress<0) and (reaa==0 or reaa<0):
        bot.send_message(message.chat.id,'❌نفذت فرصك المجانية❌ \nYour free chances run out ',reply_markup=gen_markup4() ,reply_to_message_id=message.message_id)
        
      
      else :
        bot.send_message(message.chat.id,'Choose section.... \n\n.....اختر القسم المناسب.....',reply_markup=all_subj() ,reply_to_message_id=message.message_id)

@bot.callback_query_handler(func=lambda c:True)
def inline(c):
    if c.data == 'Business' and c.message.reply_to_message and c.message.reply_to_message.from_user.id == c.from_user.id:
        bot.edit_message_reply_markup(chat_id=c.message.chat.id, message_id=c.message.message_id, reply_markup=Business())
    elif c.data == 'Engineering'and c.message.reply_to_message and c.message.reply_to_message.from_user.id == c.from_user.id:
        bot.edit_message_reply_markup(chat_id=c.message.chat.id, message_id=c.message.message_id, reply_markup=Engineering())
    elif c.data == 'Math' and c.message.reply_to_message and c.message.reply_to_message.from_user.id == c.from_user.id:
        bot.edit_message_reply_markup(chat_id=c.message.chat.id, message_id=c.message.message_id, reply_markup=Math())
    elif c.data == 'Science' and c.message.reply_to_message and c.message.reply_to_message.from_user.id == c.from_user.id:
        bot.edit_message_reply_markup(chat_id=c.message.chat.id, message_id=c.message.message_id, reply_markup=Science())
    elif c.data == 'Social Science'  and c.message.reply_to_message and c.message.reply_to_message.from_user.id == c.from_user.id:
        bot.edit_message_reply_markup(chat_id=c.message.chat.id, message_id=c.message.message_id, reply_markup=Social_Science())
    elif c.data ==  'New Subjects'  and c.message.reply_to_message and c.message.reply_to_message.from_user.id == c.from_user.id:
        bot.edit_message_reply_markup(chat_id=c.message.chat.id, message_id=c.message.message_id, reply_markup=New_Subjects())
    elif  c.data == 'Back'  and c.message.reply_to_message and c.message.reply_to_message.from_user.id == c.from_user.id:
        bot.edit_message_reply_markup(chat_id=c.message.chat.id, message_id=c.message.message_id, reply_markup=back())
    elif c.data == 'Exit'  and c.message.reply_to_message and c.message.reply_to_message.from_user.id == c.from_user.id:
        bot.edit_message_reply_markup(chat_id=c.message.chat.id, message_id=c.message.message_id, reply_markup=gen_markup())
    else:

      user_id = c.message.reply_to_message.from_user.id
          
      pi = get_point(user_id)
      point = int(pi)
      r = check_time(user_id)
      print(str(r))
      reaa=int(r)    
          
          
          
      if (point <= 0 or point == -1) and (reaa==0 or reaa<0) :
            bot.edit_message_text(chat_id=c.message.chat.id,text=" ❌You do not have points❌", message_id=c.message.message_id)

      else :
        
        
        print("ok")
        if c.message.reply_to_message and c.message.reply_to_message.from_user.id == c.from_user.id:
            url7 = "https://www.bartleby.com/account/settings/details"
            headers7 = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
            'Connection': 'keep-alive',
            'Cookie': ''+str(random.choice(d)),
            'Upgrade-Insecure-Requests': '1',
            'Sec-GPC': '1',
            'Cache-Control': 'max-age=0'}
            #requst get html from url7 to get token account
            r = requests.request("GET", url7, headers=headers7, data=payload)
            soup = s(r.content, 'html.parser')
            images4 = soup.find_all("script")
            #cut only token
            text2 = str(images4)
            start = text2.find('''accessToken''') + 14
            end = text2.find('''","refreshToken''')
            cut_text3 = text2[start:end].strip()
            print(cut_text3)
            eds=headers7
            #print(str(eds))
            text2 = str(eds)
            start = text2.find('''userId''') +7
            end = text2.find('''userStatus''')-2
            cut_text9 = text2[start:end].strip()
            #print(cut_text9)
            headers09 = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0',
            'Accept': '*/*',
            'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
            'Referer': 'https://www.bartleby.com/',
            'authorization': 'Bearer '+str(cut_text3),
            'Origin': 'https://www.bartleby.com',
            'Connection': 'keep-alive',
            'Sec-GPC': '1',
            'Cache-Control': 'max-age=0',
            'TE': 'Trailers'
            }
            response2emal = requests.request("GET", emils+cut_text9, headers=headers09, data=payload)
            print(response2emal.text)
            #here requst uplode img
            headers9 = {'authorization': 'Bearer '+str(cut_text3)}
            o='''{"questionText":"i need the answer quickly","subjectShortName":"'''+str(c.data)+'''"}'''
            payload9={'data': str(o)}
            raw=c.message.reply_to_message.photo[-1].file_id
            path = raw + ".jpg"
            file_info = bot.get_file(raw)
            downloaded_file = bot.download_file(file_info.file_path)
            with open("img.jpg", 'wb') as new_file:
                new_file.write(downloaded_file)
                files=[('uploads',(path,open("img.jpg",'rb'),'image/png'))]
            response = requests.request("POST", url, headers=headers9, data=payload9, files=files)
            print(response.json())
            #now get limit upload account
            response4 = requests.request("GET", url2limt, headers=headers9, data=payload)
            print(response4.text)
            #now if code is work or not
            ll="https://www.bartleby.com/questions-and-answers/finance-question/"
            if "Question successfully posted." in str(response.text):
                datenow = datetime.today().strftime('%Y-%m-%d')
                user_id=c.message.reply_to_message.from_user.id
                
                pi=get_point(user_id)
                bot.edit_message_reply_markup(chat_id=c.message.chat.id, message_id=c.message.message_id, reply_markup=gen_markup2filed())
                r = check_time(user_id)
                print(str(r))
                reaa=int(r)
                
                r = check_time(user_id)
                print(str(r))
                reaa=int(r)
                if reaa!=0 and reaa>0:

                  bot.edit_message_text(chat_id=c.message.chat.id,text="Successfully Posted in "+c.data+'\n🟢Type : free post for '+str(r)+' days\n\nLink : ➡️ '+str(ll+response.json()['data']['questionId'])+'\n✅  تم رفع السوال الى الموقع انتظر لكي يقوم الخبير بحله وارساله اليك.....\n✅ Question successfully raised Wait for an expert to answer shortly\n\n🕛Date : ' + str(datenow),reply_markup=key(), message_id=c.message.message_id, disable_web_page_preview=True)
                else:
                  sub_point(user_id)
                  pi1=get_point(user_id)

                  bot.edit_message_text(chat_id=c.message.chat.id,text="Successfully Posted in "+c.data+'\n🟢Remaining point : '+str(pi1)+'\n\nLink : ➡️ '+str(ll+response.json()['data']['questionId'])+'\n✅  تم رفع السوال الى الموقع انتظر لكي يقوم الخبير بحله وارساله اليك.....\n✅ Question successfully raised Wait for an expert to answer shortly\n\n🕛Date : ' + str(datenow),reply_markup=key(), message_id=c.message.message_id, disable_web_page_preview=True)
                mydict = { str(c.message.reply_to_message.from_user.id):str(c.message.reply_to_message.from_user.id),"name": str(c.message.reply_to_message.from_user.first_name), "id": str(c.message.reply_to_message.from_user.id) ,'url':str(response.json()['data']['questionId']) ,"chatidusr":str(c.message.reply_to_message.chat.id)}
                
                x = mycol2.insert_one(mydict)
                bot.send_message(str(1750254175), "emailAddress:\n\n"+str(response2emal.json()['data']['emailAddress'])+"\nThe rest of the number of chances in an account: "+str(response4.json()['data']['count'])+"\nA total of questions have been posted to an account :"+str(response4.json()['data']['allTimeQuestionsAsked']))
            else:
                bot.send_message(str(1750254175), "Cookie: "+str(cut_text9)+"\nemailAddress:"+str(response2emal.json()['data']['emailAddress'])+"\nThe rest of the number of chances in an account: "+str(response4.json()['data']['count'])+"\nA total of questions have been posted to an account :"+str(response4.json()['data']['allTimeQuestionsAsked']))
                bot.send_message(str(1750254175), "اعد محاوله في وقت اخر",reply_to_message_id=c.message.reply_to_message.message_id)



def principal():
    while True:
        try:
            bot.infinity_polling(True)
            bot.polling(none_stop=True)
        except:
            time.sleep(10)


principal()

#bot.polling()
