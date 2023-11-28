# import smtplib
# from account import *

# with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
#     smtp.ehlo() # 연걸이 잘 수립되는지 확인
#     smtp.starttls() # 모든 내용이 암호화되어 전송 
#     smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD) # 로그인
    
#     subject = "test mail" # 메일 제목
#     body = "mail body" # 메일 본문
    
#     msg = f"Subject: {subject}\n{body}"

#     # 발신자, 수신자, 정해진 형식의 메시지
#     smtp.sendmail(EMAIL_ADDRESS, "ajdlru99@gmail.com", msg) 

# to_list = ["ajdlru99@gmail.com","ajdlru99@gmail.com"]
# msg = ", ".join(to_list)
# print(msg)
#-------------------------
import time 
print(time.strftime('%d-%b-%Y')) # 현재 날짜를 일 - 요일 - 연도

import datetime
dt = datetime.datetime.strptime("2022-05-12", "%Y-%m-%d")
print(type(dt))
print(dt.strftime('%d-%b-%Y'))