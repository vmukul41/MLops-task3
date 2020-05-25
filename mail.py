f= open("/root/MLops-task/acc.txt" ,"r")
a=f.read()
import getpass
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
host_address = "vmukul41@gmail.com"
host_pass = getpass.getpass("enter your password:")
guest_address = "mukulkumar@krishnacollege.ac.in"
subject = "Regarding Success of your model "
content = "congratulations your model trained successfully with"+ str(a)+ "accuracy";
message = MIMEMultipart()
message['From'] = host_address
message['To'] = guest_address
message['Subject'] = subject
message.attach(MIMEText(content, 'plain'))
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(host_address, host_pass)
text = message.as_string()
session.sendmail(host_address, guest_address  , text)
session.quit()
print('Successfully sent your mail')