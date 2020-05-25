import smtpd
import smtplib
import getpass
impot os
acc=os.sytem(" cat /root/MLops-task/acc.txt ")
s= smtplib.SMTP('smtp.gmail.com',   587)
s.starttls()

sender_email_id="vmukul41@gmail.com"
sender_email_id_password=getpass.getpass("enter you password")

s.login(sender_email_id, sender_email_id_password)
print("login sucessful")

FROM='vmukul41@gmail.com'
TO='mukulkumar@krishnacollege.ac.in'

s.sendmail(FROM, TO, "the accuracy is is {}".format(count))
s.quit()