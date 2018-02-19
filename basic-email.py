import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("tinku.is.koushik@gmail.com", "")

msg = "Hello Koushik, its from your script"
server.sendmail("tinku.is.koushik@gmail.com", "koushikbattini@gmail.com", msg)
server.quit()
