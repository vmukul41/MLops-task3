import smtpd
import smtplib
import getpass
s= smtplib.SMTP('smtp.gmail.com',   587)
s.starttls()

sender_email_id="vmukul41@gmail.com"
sender_email_id_password=getpass.getpass("enter you password")

s.login(sender_email_id, sender_email_id_password)
print("login sucessful")

FROM='vmukul41@gmail.com'
TO='vineet96.vk@gmail.com'

s.sendmail(FROM, TO, "the attendence is is {}".format(count))
s.quit()