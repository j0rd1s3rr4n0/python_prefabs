#-------------------------------------------------------------------------------
# Name:        StatusChecker
# Purpose:     Checks the status of Contabo server issues on your servers and 
#              sends you an email to notify you (cron job required).
#
# Author:      J0rd1S3rr4n0
#
# Created:     14/11/2022
# Copyright:   (c) J0rd1S3rr4n0 2022
# Licence:     Apache License 2.0 
#-------------------------------------------------------------------------------
import os
import requests
from bs4 import BeautifulSoup
import smtplib
# pip install <package>
# pip install smtplib, BeautifulSoup
#-------------------------------------------------------------------------------
# URL Website
URL = 'https://contabo-status.com'
# Sender Credentials
my_email = "youremail@gmail.com"
password = "password"
# User Params
EMAIL_SEND_TO = "youremail@gmail.com"
ID_SERVER = ['12215',16733]
# Show More Information
verbose = False
#-------------------------------------------------------------------------------

def sendEmail(text):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    # Transport Layer Security (TLS) secures our sensitive information and data from hackers.
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="anotheremail@yahoo.com",
                            msg="Subject:New Incidence Contabo\n"+text)
def getStatus(status):
    if status == 200:
            print('SERVER OK!') 
    elif status < 400: #30X
        print('REDIRECT? ',status)
    elif status < 500: # 40X
        print('CLIENT ERROR ',status)
    elif status > 400: # 50X
        print ('SERVER ERROR ',status)

def replaceTextSubject(text):
    text = str(text).replace("</td>","").replace('<td class="maintenence_subject">',"")
    return text

def replaceTextContent(text):
    text = str(text).replace("</td>","").replace('<td class="maintenence_content">',"")
    return text

def main():
    try:
        r = requests.get(URL)
        if r.ok:
            soup = BeautifulSoup(r.text, "html.parser")
            #title = str(soup.find("title"))
            #title = soup.find(id="tab_area_running")
            title = soup.findAll("td",class_='maintenence_subject')
            context = soup.findAll("td",class_='maintenence_content')
            i = 0
            while i<(len(context)):
                head___one = replaceTextSubject(title[i])
                head___two = replaceTextSubject(title[i+1])
                head_three = replaceTextSubject(title[i+2])
                head__four = replaceTextSubject(title[i+3])
        
                context___one = replaceTextContent(context[i])
                context___two = replaceTextContent(context[i+1])
                context_three = replaceTextContent(context[i+2])
                context__four = replaceTextContent(context[i+3])
                if verbose == True:
                    print(head___one,' : ',context___one)
                    print(head___two,' : ',context___two)
                    print(head_three,' : ',context_three)
                    print(head__four,' : ',context__four)
                i+=4
                for id in ID_SERVER:
                    if(str(id) in context_three):
                        if verbose == True:
                            text = 'AFECTADO: ',str(id),' DURANTE APROX.',context___two, ' AVISO DE ',context___one,' SISTEMAS AFECTADOS: ',context___two,' DESCRIPCION ',context__four
                        else:
                            text = 'AFECTADO: ',str(id),' DURANTE APROX.',context___two, ' AVISO DE ',context___one
                        print(text)
                        #sendEmail(text)
    except:
      print("ERROR - URL DOESN'T EXIST OR NOT RUNNING YET!")

if __name__ == '__main__':
    main()

