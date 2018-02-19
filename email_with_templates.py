import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template


MY_ADDRESS = "tinku.is.koushik@gmail.com"
PASSWORD = ""

def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename

    """

    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for contact in contacts_file:
            names.append(contact.split()[0])
            emails.append(contact.split()[1])
    return names,emails

def read_template(filename):
    """
    Returns a Template object comprising the contents of the file specified by filename

    """
    with open(filename, mode='r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main():
    names, emails = get_contacts('mycontacts.txt')
    message_template = read_template('message.txt')

    #set up the smtp server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(MY_ADDRESS,PASSWORD)

    #for each contact send the email

    for name, email in zip(names, emails):
        msg =MIMEMultipart()  #create a message

        #add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title())

        #prints outs the message body for our sake
        print(message)

        #setup the parameters of the message
        msg['From'] = MY_ADDRESS
        msg['To'] = email
        msg['Subject'] = "Testing Email with Template object"

        #add in the message body
        msg.attach(MIMEText(message, 'plain'))

        text = msg.as_string()

        #send the message via the server setup earlier
        server.sendmail(MY_ADDRESS, email, text)
        del msg
    #Terminate the SMTP session and close the connection
    server.quit()

if __name__ == '__main__':
    main()
