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
from json2html import *
from dateutil.relativedelta import *


channal1 = -1001164763046

#point users
client2user = pymongo.MongoClient("mongodb+srv://dd:dd@cluster0.2uqyz.mongodb.net/dd?retryWrites=true&w=majority")
mydb= client2user["dd"]

mycol = mydb["dd"]
mycol2 = mydb["saveurl"]
mycol3s = mydb["copon"]
allgive="1"
list = ["2120455416","421601117","1750254175","1205882498","421601117"]

listgrop = ["iijsjsjsiendbdbdnns"]

#your acouunt
d=["refreshToken=01a2693f1686bfd6f997506d12eaca72a024053d","refreshToken=3edb5104691bf67d2883d40fd3f902e21defe825","refreshToken=10ec31493bbb23ebc2e25bb32961f82004804845","refreshToken=cba3ab50dde807de1e5201d46937ff09261106a5","refreshToken=0ed9284140b46db33d1f40cb9c9000c541cf8422","refreshToken=d8b841275e832e1f1b5bf0fd696a824aa82ab9e2","refreshToken=924d2a11e5cd86f30418c15bcc572b92d40d538c","refreshToken=900e082b26ecff23a55e2542aacf94fe05628fe1","refreshToken=7a679442883f3f3089ed1df2108c0cfde27d6697","refreshToken=cd6d92f95e71260e4c45da9ca49775dd7b3c520e","refreshToken=cf2a9817b7218a9d01b350d302360e280fb61d86","refreshToken=de32306544ebdf0a79932bc385cca727d35bb724","refreshToken=b22fe5db18b4c44c94763c03213a2a91215b2a06","refreshToken=4b4c7b972a8ea8e55bd2ffb7fb7bcbc56c08c37b","refreshToken=39517c8b8da6a2eadbf90deb24d917404db0c882","refreshToken=e8059c4c871b71aca0fa18c6e3492beb967f32ec","refreshToken=8f5972fe1b4add69ae70e1d7373f94fb8de12f85","refreshToken=91ee3f657a287d42637a3d1417689ac38dadf7ea","refreshToken=b79c06fe7ac239a61e2d2e3130f6631e1e7042da","refreshToken=6b07f8ff9b3010502fd643b6a2b70717e704ff20","refreshToken=54456eab6a71959a8657c0afff7c7a808e30fe36","refreshToken=370ce4060c1a2abe4b7fe42434db227394170096","refreshToken=aaaa44c8c529d5a78f20dd995c2f926eaefa1286","refreshToken=9933d3b3c6ce447562dff1f7ebcab0c0804ab7a0","refreshToken=769dfbe8170978e4a93ae0a5fa51d15fb0ccf8fe","refreshToken=15d599886c2f49984e084fb8b80b44b6b63b339b","refreshToken=80c3c691bb3fe68f0316d69c99c48b11a0d15649","refreshToken=414ac14fcb8fb02aa50a84cc5b169cc3ce68b78c","refreshToken=23c4d55de28213a5c75d6b046bbfac2ede4789b7","refreshToken=a89c5bb1e5a0b1e75b419c8901d06b36f08c5e58","refreshToken=77dfe7c7c04cb72887c6104400679f8811c777ff","refreshToken=5934bfd1c498ca892600ed4efd9c74444e3ba476","refreshToken=56945f3a4d8e5033544ee6ffa8bf0cddf87c5a22","refreshToken=1365f01a8b107c92d70a6146e23063a29447c6cc","refreshToken=0c2af34a955c75b1d5a91044de8470c1daa4f8fe","refreshToken=ce56a8ed2673c242d00a878bf6c3eb49cca38343","refreshToken=4e824b26bbc1daab1c278e136acbafda43c42c60","refreshToken=6bd1a1167874a9cc094bc3ea08c9d3601b6f92c1","refreshToken=25944d5eb5a3a9343d08498ee94415c61f3a09a7","refreshToken=8f8f21d33d153a19b1a733acf93758b6f1e947cb","refreshToken=738f2ad67dff9620935196d4dc1c72c8c731f514","refreshToken=e0a85e0da759cbca8aa9aaf9b721083452a22cc4","refreshToken=568d1e79cd5c7eded232bfe3851cdc3d7780d305","refreshToken=027d4a763c81b1e519f2f28ecfdaaf31cd29d391","refreshToken=84850953ee7692a06d74c3a8ab8428fbc36b4738","refreshToken=32cec9a314f6562634b7b6e990c6d1bf5394ead4","refreshToken=6095cf32b5778788db24cf130cc0b3adb961386f","refreshToken=3e3b2f53d867a57c1be98037a2c0bc817dde0f29","refreshToken=719db62a3170f64bbd690d2de7a53588f1fcc800","refreshToken=3a7f02a417177bcdde0d75dc14ad9c6519e2cb93"]





payload={}
#urls need
url = "https://nk6xemh85d.execute-api.us-east-1.amazonaws.com/prod/user/qna-question"
url2limt="https://nk6xemh85d.execute-api.us-east-1.amazonaws.com/prod/user/qna-questions-limit"
emils = "https://nk6xemh85d.execute-api.us-east-1.amazonaws.com/prod/user/"
#token bot telegram
TELEGRAM_TOKEN = "5103052340:AAFyGEn8XnIOgZdGDRaN8OOQX4diJY15hlc"
bot = telebot.TeleBot(TELEGRAM_TOKEN, parse_mode=None  , threaded=False)






#del users
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
        mydict77 = {   "point": str(clc) }
        mydict4 = { "$set":mydict77}
        mycol.update_one(mydoc2, mydict4)
        return str(clc)
    except:
        pass


def get_point(user_id):
    try:
        print("id  points :"+str(user_id))
        mydoc2 = mycol.find_one({ str(user_id):str(user_id)})
        print(mydoc2)
        if  str(user_id)  not in str(mydoc2):
            return [0 , 0]
        else:
            g=[mydoc2]
            print("user is old in file time :"+str(g[0]['point']))
            falluser = str(g[0]['timeout'])
            e = '' + falluser + ''
            i = datetime.strptime(e, '%Y-%m-%d %H:%M:%S.%f')
            z = (i - datetime.now()).days
            zz=z+1
            pii= int( g[0]['point']   )
            if zz <= 0:
                print("time out member")
                mycol.delete_one(mydoc2)
                return [0 , 0]
            elif pii <= 0 :
                mycol.delete_one(mydoc2)
                return [0 , 0]
            else :
                return [g[0]['point'] , z+1]
    except:
        pass
#add points
def add_point(repy_id ,add  ,timeout):
    try:
        #print("id group points :"+str(chat_id)+"and add point :"+str(add_point))
        mydoc2 = mycol.find_one({ str(repy_id):str(repy_id)})
        print(mydoc2)
        u=int(timeout)*1
        date = datetime.now()
        print('time days:'+str(u))
        date3 = date + relativedelta(days=u+1 )
        print(date3)
        if  str(repy_id)  not in str(mydoc2):
            mydict = {  str(repy_id):str(repy_id),  "userid":str(repy_id)  ,"point":str(add)  ,"timeout": str(date3)  }
            x = mycol.insert_one(mydict)
            return [add ,timeout]
        else:
            print("is old grupe")
            g=[mydoc2]
            oldadd=int(g[0]['point'])
            newadd=int(add)
            clc=oldadd+newadd
            falluser = str(g[0]['timeout'])
            e = '' + falluser + ''
            i = datetime.strptime(e, '%Y-%m-%d %H:%M:%S.%f')
            date3 = i + relativedelta(days=u)
            ####
            print("is clc :"+str(clc))
            mydict77 = {  "point": str(clc)  ,"timeout": str(date3) }
            mydict4 = { "$set":mydict77}
            mycol.update_one(mydoc2, mydict4)
            #######
            falluser = str(g[0]['timeout'])
            e = '' + falluser + ''
            i = datetime.strptime(e, '%Y-%m-%d %H:%M:%S.%f')
            z = (i - datetime.now()).days
            return [clc ,z+1]
    except:
        pass

def infocode():
    try:
        how=0
        j=[]
        anf={}
        
        t=''
        mydoc2 = mycol3s.find()

        for x in mydoc2:
            g=[x]
            j.append(g)
        for ch in j :
            x={ "code-":ch[0]['code']  ,"point": ch[0]['points'] ,"days":ch[0]['number'] }

            d=json2html.convert(json = x)
            t+=d
            how+=1
        print(how)

        f=open('code.html','w')
        f.write(f'{str(datetime.now())}\n\nVIP Number :{str(how)}\n\n'+t)
        f.close()
        url = "https://siasky.net/skynet/skyfile"
        payload={}

        files = [
            ('file', ("information.html", open("code.html", 'rb'), 'text/html'))
        ]
        headers7 = {
            'referrer': 'https://siasky.net/'
        }
        response = requests.request("POST", url, headers=headers7, data=payload, files=files)
        print(response.text)
        return  "https://siasky.net/" + response.json()["skylink"]
    except:
        pass


def insp2pass(code ,numberdays ,points):
    try:
        codes=str(code)
        mydict = {  str(codes):str(codes), "code": str(codes) ,"number":str(numberdays) ,"points":str(points) }
        x = mycol3s.insert_one(mydict)
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
    markup.add(InlineKeyboardButton("🔰More chances🔰", url="https://t.me/abo0odf16"))
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
    markup.add(InlineKeyboardButton("🔰اضغط للتحدث مع الادمن 🔰", url="https://t.me/abo0odf16"))
    return markup
def gen_markupz():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("🔰chegg 🔰", url="https://t.me/Eng_abdallah_bots/25/386"),InlineKeyboardButton("🔰admin🔰", url="https://t.me/abo0odf16"),InlineKeyboardButton("🔰Bartleby 🔰", url="https://t.me/Eng_abdallah_bots/24"))
    return markup
def gen_markup7():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("🔰 Channel  🔰", url="https://t.me/Eng_abdallah_bots"))
    return markup
#get text
@bot.message_handler(content_types=['text'])
def send_text(message):
  result = bot.get_chat_member(channal1, message.from_user.id)
  mention = "[" + str(message.from_user.first_name) + "](tg://user?id=" + (str(message.from_user.id)) + ")"

  if "'status': 'left'" in str(result):
        print("nooooooo me")
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, '{s} \n🚸 | عذرا عزيزي\n🔰 | يجب عليك الانضمام بالقناة حتى تستطيع استخدام البوت مجانا \n🔰 | You must subscribe to the channel to be able to use the bot for free '.format(s=str(mention)) , disable_notification=True ,reply_markup=gen_markup7() ,parse_mode='Markdown')
 
  else :
        if message.text=="/get":
            user_id=message.from_user.id
            pi=get_point(user_id)
            print(pi)
            bot.send_message(message.chat.id, 'Remaining  chances :'+str(pi[0])+'\n\n Your points expire after :'+str(pi[1])+'days' , reply_to_message_id=message.message_id)
        
        elif ("t.me/") in message.text and str(message.from_user.id) not in str(list):
            bot.delete_message(message.chat.id, message.message_id)
        elif message.text.startswith('/all-')  and str(message.from_user.id) in str(list):
            string = str(message.text)
            pattern = '\d+'
            result = re.findall(pattern, string)
            print(result)
            add=str(result[0])
            all4add(add)
            bot.send_message(message.chat.id,'Chances are increased for everyone: '+str(add) ,reply_to_message_id=message.message_id)
            
        elif message.text.startswith('/allzero') and str(message.from_user.id) in str(list):  
            add="0"
            all4sub(add)
            bot.send_message(message.chat.id,'Total points have been deleted all' ,reply_to_message_id=message.message_id)    
        elif message.text.startswith('/add-') and message.reply_to_message and str(message.from_user.id) in str(list):
            repy_id=message.reply_to_message.from_user.id
            string = str(message.text)
            pattern = '\d+'
            result = re.findall(pattern, string)
            print(result)
            add = str(result[0])
            timeout=result[1]
            asd=add_point(repy_id ,add   ,timeout)
            bot.send_message(message.chat.id,'chances increased:'+str(asd[0])+'\n\ndays increased:'+str(asd[1]),
                             reply_to_message_id=message.reply_to_message.message_id)

        elif message.text.startswith("/copon-") and str(message.from_user.id) in str(list) :
            string = str(message.text)
            pattern = '\d+'
            result = re.findall(pattern, string)
            for e in range(int(result[0])):
                name = ''.join(random.choice("mohyfcfkjd") for e in range(4))
                email = ''.join(random.choice("ytfhjkmabcdefghijklmnopqrstwxyz1234567890") for x in range(9)) + 'om'
                password = ''.join(random.choice("ugtfgfhujabcdefghijklmnopqrsjgftwxyz1234567890") for y in range(9)) + 'm1$mohammed'
                print(f'/buy-{name}-{email}-{password}')
                code=f'/buy-{name}-{email}-{password}'
                numberdays=result[2]
                points=result[1]
                d=insp2pass(code ,numberdays ,points)
            bot.send_message(message.chat.id,f'Done\n\ndays-{result[1]}\n\nnumber codes-{result[0]}' ,reply_to_message_id=message.message_id)
            bot.send_message(message.chat.id,f'\n{code}' ,reply_to_message_id=message.message_id)
        elif  message.text=="نشر اذاعه"  and message.from_user.id in list and message.reply_to_message:

          j=[]
          clc=0
          mydoc2 = mycol.find()
          for x in mydoc2:
            g=[x]
            j.append(g)
          for ch in j:
            clc+=1
            print(ch[0])
            try:
                bot.forward_message(ch[0]["userid"], message.chat.id, message.reply_to_message.message_id)
            except:
                pass
          bot.send_message(message.chat.id,"تم نشر اذاعه\nعدد اشخاص التي وصل لهم اذاعه\n\n"+str(clc) ,reply_to_message_id=message.message_id)
        elif message.text.startswith("/buy-") :
            mydoc2 = mycol3s.find_one({ str(message.text):str(message.text)})
            print(str(mydoc2))
            if "/buy" in str(mydoc2):
                g=[mydoc2]
                repy_id=message.from_user.id
                add=str(g[0]['points'])
                timeout=str(g[0]['number'])
                asd=add_point(repy_id ,add   ,timeout)
                mycol3s.delete_one(mydoc2)
                bot.send_message(message.chat.id,"Your points have been increased-"+str(add)+"\nYour days have been increased-"+str(timeout)+"\n\nTo find out your remaining days and points , write\n/get" ,reply_to_message_id=message.message_id)
            else:
                bot.send_message(message.chat.id,"The code was not found or has been used before....\n\nتحقق من كوبون" ,reply_to_message_id=message.message_id)
        elif message.text=="/mycode" and str(message.from_user.id) in str(list):
            d =infocode()
            bot.send_message(message.chat.id,d ,reply_to_message_id=message.message_id)  
        elif message.text=="/zero" and message.reply_to_message and str(message.from_user.id) in str(list):
            repy_id=message.reply_to_message.from_user.id
            zz=zro(repy_id)
            bot.send_message(message.chat.id,'Total points have been deleted' ,reply_to_message_id=message.message_id)
        elif message.text.startswith("https://www.bartleby.com/questions-and-answers") :


          
            
            url = message.text
            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
  'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
  'Cookie': "_ga=GA1.2.1222430549.1634843987; _fbp=fb.1.1634843992366.448561356; _hjid=92625c32-3023-4af1-8849-636b31e86451; G_ENABLED_IDPS=google; _hjSessionUser_1400488=eyJpZCI6IjU0NTc5Yzc3LWJjNWQtNTkyYi04NWIyLWIwNmU5OWQxYTE3YSIsImNyZWF0ZWQiOjE2Mzc1OTkyMjc1OTgsImV4aXN0aW5nIjp0cnVlfQ==; ki_r=; _gaexp=GAX1.2.X-uOdja7RPmf-CPQrv8FPQ.19036.x272; optimizelyEndUserId=oeu1638895397140r0.3740585328332844; cookieconsent_status=dismiss; _fssid=3ee56717-d615-4d8e-9aa5-d5b54dabcd5e; __qca=P0-555405187-1638895793329; isNoQuestionAskedModalClosed=true; sailthru_visitor=52e2faea-fccc-4a46-a04e-54c5c204078d; splat_user=%7B%22userId%22%3A%22386037130%22%2C%22isPremium%22%3Afalse%7D; FPID=FPID1.2.FXQXHVoIMmjlox1iWQ9zFNYp2EdAzuCj%2BKHBXZsaFyY%3D.1634843987; _gcl_au=1.1.39061517.1642772877; _uetvid=ed23459032a311eca0d79738a7076d00; ki_t=1636491439129%3B1642772919188%3B1642772943000%3B17%3B64; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Jan+21+2022+17%3A01%3A56+GMT%2B0300+(Arabian+Standard+Time)&version=6.23.0&isIABGlobal=false&hosts=&consentId=26193cab-828e-4028-b23d-87b7e6f51dd0&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CBG1%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false; sailthru_hid=f91f0ce1521413b59972bbcc4fce59ae61f06d43c2f6de6f6a7c01fe762757c596829040f0aa4f2a02e8b4ad; _hjSession_1400488=eyJpZCI6ImVkY2M2NDk4LTQ5MzEtNDdhNy1hYzk3LWU0N2ExZjYyMTM0MSIsImNyZWF0ZWQiOjE2NDM0MzcyNjc5NjMsImluU2FtcGxlIjp0cnVlfQ==; _hjAbsoluteSessionInProgress=0; accessToken=8ed7301eb7a2a526da5bee12a0feb4de40237bcf; refreshToken=dff211601c98f240296afd772793a23dd878372b; bartlebyRefreshTokenExpiresAt=2022-02-28T06:23:51.115Z; userId=f860a248-b7e2-4fa7-b3c3-ce464c3805b0; userStatus=A1; promotionId=; sku=bb1499_plus; _hjCachedUserAttributes=eyJhdHRyaWJ1dGVzIjp7ImNvdW50cnkiOiJJUSIsImdlb2dyYXBoeSI6IkludGVybmF0aW9uYWwiLCJzdWJzY3JpcHRpb25fbW9udGgiOiIiLCJ1c2VyX3NvdXJjZSI6IkNPTVBBU1MiLCJ1c2VyX3N0YXR1cyI6IkExIn0sInVzZXJJZCI6ImY4NjBhMjQ4LWI3ZTItNGZhNy1iM2MzLWNlNDY0YzM4MDViMCJ9; ABTasty=uid=m2mzpgn34r161m44&fst=1634843987659&pst=1642772942861&cst=1643437148952&ns=39&pvt=277&pvis=3&th=; ABTastySession=mrasn=&sen=2&referrer=&lp=https%253A%252F%252Fwww.bartleby.com%252F; btbLiveChatFabTriggerDate=2022-01-29T06:54:45.442Z"
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
                mention = "[" + str(message.from_user.first_name) + "](tg://user?id=" + (str(message.from_user.id)) + ")"
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
                                            
                                           <meta charset="UTF-8"><html><head><link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css"><link rel="preconnect" href="https://fonts.gstatic.com"><link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet"><link rel = "stylesheet" type = "text/css" href = "https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.9.0/katex.min.css" /><link href="https://fonts.googleapis.com/css2?family=Baloo+Bhaina+2:wght@600&display=swap" rel="stylesheet"></head><body><style>.x {background-color: white;border:solid red 5px; }.y {background-color: white;border:solid green 5px;}.x img{max-width: 100%;max-height: 100%;margin: auto;display: block;}.y img{ max-width: 100%; max-height: 100%; margin: auto; display: block; }  .highlighted-text {background-image: url('data:');  </style> <link rel="preconnect" href="https://fonts.gstatic.com"> <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet"> <link rel = "stylesheet" type = "text/css" href = "https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.9.0/katex.min.css" /> 
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
                                                
                                                          </html> """ )
                f.write(messagee)
                f.close()
                i = open('./answer.html', 'rb')
                bot.send_document(message.chat.id, i,
                                  caption=
                                  f"*Name *: {mention}\n\n"
                                  f"*✅This is your answer* \n"
                                  ,reply_markup=gen_markupz(),
                                  parse_mode='Markdown', reply_to_message_id=message.message_id)    
    
#get photo from users
@bot.message_handler(content_types=['photo'])
def get_phot(message):
  result = bot.get_chat_member(channal1, message.from_user.id)
  mention = "[" + str(message.from_user.first_name) + "](tg://user?id=" + (str(message.from_user.id)) + ")"

  if "'status': 'left'" in str(result):
        print("nooooooo me")
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, '{s} \n🚸 | عذرا عزيزي\n🔰 | يجب عليك الانضمام بالقناة حتى تستطيع استخدام البوت مجانا \n🔰 | You must subscribe to the channel to be able to use the bot for free '.format(s=str(mention)) , disable_notification=True ,reply_markup=gen_markup7() ,parse_mode='Markdown')

  else :      
    user_id=message.from_user.id
    pi=get_point(user_id)
    ress = int(pi[0])
    timemm=int(pi[1])
    if ress <= 0  or timemm <=0 :
        bot.send_message(message.chat.id,'نفذت فرصك ⚠️ يمكنك شراء المزيد 💵💰               =\npoints expired\n للاشتراك مراسلة الادمن 🔰:https://t.me/abo0odf16' ,reply_to_message_id=message.message_id)

    else :
        bot.send_message(message.chat.id,'------اختر القسم------',reply_markup=all_subj() ,reply_to_message_id=message.message_id)

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
      point =int(pi[0])
          
          
          
          
      if point <= 0 or point == -1 :
            bot.edit_message_text(chat_id=c.message.chat.id,text=" ❌You do not have points❌", message_id=c.message.message_id)

      else :
        
        print("ok")
        if c.message.reply_to_message and c.message.reply_to_message.from_user.id == c.from_user.id:
            call_message = c.message
            call_data = c.data
            print(1)
            cappsh = ''
            if c.message.reply_to_message.caption == None:
                cappsh = ""
            else:
                cappsh = c.message.reply_to_message.caption
            urlref = "https://nk6xemh85d.execute-api.us-east-1.amazonaws.com/prod/user/refresh-token"
            payloadref = json.dumps({
                "refreshToken": "a253ff38ca450e765d393473e75405edb968ec91"
            })
            headersref = {'authority': 'nk6xemh85d.execute-api.us-east-1.amazonaws.com',
                          'sec-ch-ua': '"Opera";v="81", " Not;A Brand";v="99", "Chromium";v="95"',
                          'sec-ch-ua-mobile': '?0',
                          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 OPR/81.0.4196.60',
                          'sec-ch-ua-platform': '"Windows"', 'content-type': 'application/json', 'accept': '*/*',
                          'origin': 'https://www.bartleby.com', 'sec-fetch-site': 'cross-site',
                          'sec-fetch-mode': 'cors',
                          'sec-fetch-dest': 'empty', 'referer': 'https://www.bartleby.com/',
                          'accept-language': 'en-US,en;q=0.9'
                          }
            responseref = requests.request("POST", urlref, headers=headersref, data=payloadref).json()['data'][
                'accessToken']
            c = "https://prod-api.bnedcompass.com/user/register"
            n = {"Host": "prod-api.bnedcompass.com", "accept": "application/json",
                 "authorization": f"Bearer {responseref}", "content-type": "application/json;charset\u003dutf-8",
                 "x-mobile-device": "ios", "x-mobile-os": "ios",
                 "user-agent": "Bartleby/207 CFNetwork/1240.0.4 Darwin/20.5.0"
                 }
            name = ''.join(random.choice("zahraaatrflogdcssdv") for x in range(4))
            domain = random.choice(['gmail.com', 'hotmil.com', 'outlook.com', 'yahoo.com'])
            email = 'v'.join(
                        random.choice("reyskslwoldsldodkdcl") for x in range(10)) + f'@{domain}'
            password = 'v'.join(random.choice("sde4567yuhdre46fd") for k in range(9)) + 'Zp@'
            d = json.dumps(
                {"firstName": f"{name}", "lastName": f"{name}", "emailAddress": f"{email}", "password": f"{password}",
                 "sku": "bb499firstweek_999month", "source": "MOBILE_IOS", "planCode": "qna_trial",
                 "noEmailVerification": True})
            rt = requests.post(c, headers=n, data=d)
            if rt.status_code==502:
                bot.send_message(str(call_message.reply_to_message.chat.id),
                                 "Failed To Post Resend it again\nفشل النشر ارسله مرة اخرى",
                                 disable_web_page_preview=True,
                                 reply_to_message_id=call_message.reply_to_message.message_id, parse_mode='Markdown')
            print(rt.text)
            access_token = rt.json()['data']['accessToken']
            print(access_token)
            print("gooooooooood")
            headers9 = {'authorization': f'Bearer {access_token}'}
            print(headers9)
            o0 = '''{"questionText":"''' + str(cappsh) + '''"'''
            o1 = ''',"subjectShortName":"''' + str(call_data) + '''"}'''
            payload9 = {'data': str(o0 + o1)}
            raw = call_message.reply_to_message.photo[-1].file_id
            path = raw + ".jpg"
            file_info = bot.get_file(raw)
            downloaded_file = bot.download_file(file_info.file_path)
            with open("img.jpg", 'wb') as new_file:
                new_file.write(downloaded_file)
                files = [('uploads', (path, open("img.jpg", 'rb'), 'image/png'))]
            response = requests.request("POST", url, headers=headers9, data=payload9, files=files)
            print(response.json())
            response4 = requests.request("GET", url2limt, headers=headers9, data=payload)
            print(response4.text)
            ll = "https://www.bartleby.com/questions-and-answers/finance-question/"
            if "Question successfully posted." in str(response.text):
                
                idqna = json.loads(response.text)['data']['questionId']
                user_id = call_message.reply_to_message.from_user.id
                sub_point(user_id)
                pi=get_point(user_id)
                bot.edit_message_text(chat_id=call_message.chat.id, message_id=call_message.message_id,
                                      text=f"*Successfully Posted in {call_data}\n\nRemaining point : {pi[0]}\n\nLink : {ll + idqna}\n\n\n✅  تم رفع السوال بنجاح انتظر إجابة الخبير بعد قليل\n✅Question successfully raised Wait for an expert to answer shortly\n\n🔰 Bartleby bot➡️ *", parse_mode='Markdown',disable_web_page_preview=True)
          
                  

                mydict = {str(call_message.reply_to_message.from_user.id): str(
                    call_message.reply_to_message.from_user.id),
                    "name": str(call_message.reply_to_message.from_user.first_name),
                    "id": str(call_message.reply_to_message.from_user.id),
                    'url': str(json.loads(response.text)['data']['questionId']),"chatidusr":str(call_message.reply_to_message.chat.id)}
                x = mycol2.insert_one(mydict)

            else :
              cappsh = ''
              if c.message.reply_to_message.caption == None:
                cappsh = ""
              else:
                cappsh = c.message.reply_to_message.caption
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
              o5 = '''{"questionText":"''' + str(cappsh) + '''"'''

              o = ''',"subjectShortName":"''' + str(c.data) + '''"}'''
              payload9={'data': str(o5 + o)}
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
                user_id=c.message.reply_to_message.from_user.id
                sub_point(user_id)
                pi=get_point(user_id)
                bot.edit_message_reply_markup(chat_id=c.message.chat.id, message_id=c.message.message_id, reply_markup=gen_markup2filed())
                bot.send_message(str(c.message.reply_to_message.chat.id), "Successfully Posted in "+c.data+'\nRemaining : 🔓'+str(pi)+'🔓\nLink : ➡️ '+str(ll+response.json()['data']['questionId'])+'\n✅  تم رفع السوال بنجاح انتظر إجابة الخبير بعد قليل\n✅Question successfully raised Wait for an expert to answer shortly\n\n🔰 Bartleby ➡️ ', disable_web_page_preview=True,reply_to_message_id=c.message.reply_to_message.message_id)
                mydict = { str(c.message.reply_to_message.from_user.id):str(c.message.reply_to_message.from_user.id),"name": str(c.message.reply_to_message.from_user.first_name), "id": str(c.message.reply_to_message.from_user.id) ,'url':str(response.json()['data']['questionId']) ,"chatidusr":str(c.message.reply_to_message.chat.id)}

                x = mycol2.insert_one(mydict)
                bot.send_message(str(65504980), "emailAddress:\n\n"+str(response2emal.json()['data']['emailAddress'])+"\nThe rest of the number of chances in an account: "+str(response4.json()['data']['count'])+"\nA total of questions have been posted to an account :"+str(response4.json()['data']['allTimeQuestionsAsked']))
              else:
                bot.send_message(str(65504980), "Cookie: "+str(cut_text9)+"\nemailAddress:"+str(response2emal.json()['data']['emailAddress'])+"\nThe rest of the number of chances in an account: "+str(response4.json()['data']['count'])+"\nA total of questions have been posted to an account :"+str(response4.json()['data']['allTimeQuestionsAsked']))
                bot.send_message(str(c.message.reply_to_message.chat.id), "اعد محاوله في وقت اخر",reply_to_message_id=c.message.reply_to_message.message_id)    



def principal():
    while True:
        try:
            bot.infinity_polling(True)
            bot.polling(none_stop=True)
        except:
            time.sleep(10)


principal()

#bot.polling()
