from urllib.request import urlopen
import re
import smtplib

from_address='dummymail@gmail.com'
to_address='rishabhjain7b@gmail.com'
subject='testing pi'

username='USERNAME'
password='PASSWORD'

url = 'http://checkip.dyndns.org'
#print ("ip address service is: ",url)

request=urlopen(url).read().decode('utf-8')

ourIP=re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",request)
ourIP= str(ourIP)

def send_email(ourIP):
    body_text= ourIP + 'is the IP'
    msg= '\r\n'.join(['To: %s' %to_address,
                      'From: %s' %from_address,
                      'Subject: %s' %subject,
                      '', body_text])
    server= smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(from_address, to_address, msg)
    server.quit()
    print ("Email sent")

send_email(ourIP)

