'''
Created on Apr 26, 2017

@author: Navid
'''
'''
dependency :
    espeak need to get installed
For linux:
sudo apt-get install espeak

'''

import webbrowser
import time
import sys
import os

print(("this program support upto  python 2.7 & you r running python version no:"+sys.version+"\n \n"))

working = 25
session = 3
breakTime = 5
print("want to use default then press enter Or press any key to change default configuration  default is : \nworking " , working , " minute \nbreaktime " ,breakTime , " minute and \nsession	  " , session)
#print("want to use default then press enter Or press any key to change default config \n default is :"," \n ", "working time :",working,"\n"+"sdfd" )
selector = input()


if(len(selector)!=0):
    print("hello user!!! \n how long you want to work???")
    working = eval(input("in working pls : "))
    session = eval(input("how many session you want to work : "))
    breakTime = eval(input("how long you want to take break in minues : "))
else:
    print('---------Starting with Default value-----------')


for index in range(session) :
    print('----------------You are in Session: ',index+1,'-------------')
    try:
        os.system("espeak 'Start your Work. Dont waste any time '")
    except:
        pass

    time.sleep(working*60)
#    webbrowser.open_new_tab("https://youtu.be/ss7EJ-PW2Uk?t=1326")
    try:
        os.system("espeak 'Take some rest.'")
    except:
        pass
    time.sleep(breakTime*60)

    clear = lambda: os.system('clear')
    clear()
