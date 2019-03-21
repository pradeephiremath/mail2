import smtplib
import getpass
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

sender='pradeephiremath02@gmail.com'
receiver='imnagarjun4@gmail.com'

msg = MIMEMultipart()

body="hii"
msg.attach(MIMEText(body, 'plain'))

filename = "func.py"
attachment = open("/home/bl121/func.py", 'rb') 

p = MIMEBase('application', 'octet-stream') 
  
# To change the payload into encoded form 
p.set_payload((attachment).read()) 
  
# encode into base64 
encoders.encode_base64(p) 
   
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
  
# attach the instance 'p' to instance 'msg' 
msg.attach(p) 
text = msg.as_string()

s=smtplib.SMTP('smtp.gmail.com','587')
s.starttls()


p=getpass.getpass()
s.login(sender,p)
s.sendmail(sender,receiver,text)
print("msg sent")
s.quit()