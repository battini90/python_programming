import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = "tinku.is.koushik@gmail.com"
toaddr = "koushikbattini@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Test Email with python"

body = "Hello Battini, Merry christmas!!! Happy Holidays"
msg.attach(MIMEText(body, 'plain'))


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "9441124276")
text = msg.as_string()
server.sendmail(fromaddr,toaddr,text)
server.quit()

