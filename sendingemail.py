import smtplib

EMAIL_ADDRESS = '19520218@gm.uit.edu.vn'
EMAIL_PASSWORD = input("nhap pass:")
EMAIL_REC = 'ichigo.bleach.006@gmail.com'

msg = 'Testing python'
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
server.sendmail(EMAIL_ADDRESS,EMAIL_REC,msg)