import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


fromaddr = 'arkardy@gmail.com'
toaddr = 'titkov@nxt.ru'
mypass = 'kdkl vqop yrni vwqn'
reportname = 'log.txt'

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'Привет от питона'

with open(reportname, 'rb') as f:
    part =MIMEApplication(f.read(), Name=basename(reportname))
    part['Content-Disposition'] = 'attachment; filename = "%s"' %basename(reportname)
    msg.attach(part)

body = 'This is test messages'
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.postmarkapp.com', 587)
server.set_debuglevel(True)
server.ehlo()
server.starttls()
server.ehlo()
server.login(fromaddr, mypass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.close()
