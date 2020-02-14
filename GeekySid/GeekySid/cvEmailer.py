from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from . import settings
import emoji
import smtplib


# information fetcheed from settings.py
email_signature = settings.EMAIL_SIGNATURE
self_email = settings.EMAIL_SELF

# function that attaches resume to the mail body
def cv_attachment():

    # path to the RESUME
    cv_file = settings.CV_PATH

    with open(cv_file, 'rb') as attachment:
        try:
            attached_file = MIMEBase('application', 'octat-stream')
            attached_file.set_payload(attachment.read())
            encoders.encode_base64(attached_file)
            attached_file.add_header('Content-Disposition', 'attachment; filename= ' + cv_file[-23:])
        except Exception as e:
            pass
    return attached_file


# function that connects to smtp and send mail
def sendMail(from_email, to_email, msg):
    
    # information fetcheed from settings.py to connect to smtp
    smtp_user = settings.EMAIL_USER
    smtp_pass = settings.EMAIL_PASS
    smtp_address = settings.EMAIL_HOST
    smtp_port = settings.EMAIL_PORT

    with smtplib.SMTP_SSL(smtp_address, smtp_port) as smtp:
        smtp.login(smtp_user, smtp_pass)
        try:
            smtp.sendmail(from_email, to_email, msg)
        except Exception as e:
            print(str(e))


# function that executes whne user fills form from contact page
def contactPage_mail(user_name, user_email, user_msg):

    # message setting for self mail
    msg = MIMEMultipart()
    msg['To'] = self_email
    msg['From'] = user_email
    msg['Subject'] = user_name + ' : Sent you Message from GeekySid. ' + emoji.emojize(":sign_of_the_horns:")

    body = user_name + ' made an enquiry through website.<p> His message is: <br />' + user_msg + '<p>His email address is: <br />' + user_email + '<p><br />--<br />'+ email_signature
    msg.attach(MIMEText(body, 'html'))

    # send mail to self about 
    sendMail(user_email, self_email, msg.as_string())

    # seding resume to the user
    resume_mail(user_email, user_name)


# function that sends resume to the user
def resume_mail(*args):

    user_email = args[0]

    if len(args) == 2:
        user_name = args[1]
    else:
        user_name = 'Sid/Madam'

    # message setting for user mail
    msg = MIMEMultipart()
    msg['To'] = user_email
    msg['From'] = self_email
    msg['Subject'] = 'Resume - Siddhant Shah - Python and Django Developer' + emoji.emojize(":sign_of_the_horns:")

    body = 'Dear ' + user_name + ',<p>Thankyou for contacting me through my website http://www.geekysid.com. I really appreciate that you took time to go through my website.'\
            '<p>Just to remind you again, I am a Python and Django Developer with good understanding of python modules like Requests, BeautifulSoup, Pandas, numPy and few more.'\
            '<p>Also PFA my resume for your reference.'\
            '<p>Let\'s talk on my below number and see how can we work together in near future.'\
            '<p><br />--<br />'+ email_signature

    msg.attach(MIMEText(body, 'html'))

    msg.attach(cv_attachment())

    # send mail to user with my resume
    sendMail(self_email, user_email, msg.as_string())


# function that bookstore order confirmation
def bookStore_checkout_mail(user_email, order_msg):

    # message setting for user mail
    msg = MIMEMultipart()
    msg['To'] = user_email
    msg['From'] = self_email
    msg['Subject'] = 'BookStore: Your order is placed.' + emoji.emojize(":sign_of_the_horns:")

    body = 'Dear Sir/Madam,<p>Thankyou for visiting my website http://www.geekysid.com/bookstore. I really appreciate that you took time to go through my website.'\
            '<p>Just to remind you again, I am a Python and Django Developer with good understanding of python modules like Requests, BeautifulSoup, Pandas, numPy and few more.<p>Also if you like my work and would like to refer me somewhere or offer so me a job, I have attached my <strong>resume</strong> for your reference.'\
            '<p>Let\'s talk on my below number and see how can we work together in near future.'\
            '<p>' + order_msg + ''\
            '<p><span style="color:red">I am sure you are smart enough to understand that this is just a dummy order and no book(s) will be delivered to you.</span>' + emoji.emojize(":grinning_face_with_smiling_eyes:") + ''\
            '<p><br />--<br />'+ email_signature

    msg.attach(MIMEText(body, 'html'))

    msg.attach(cv_attachment())

    # send mail to user with my resume
    sendMail(self_email, user_email, msg.as_string())
    
    # sending information to myself about this purchase
    bookstore_self_mail(user_email, order_msg)



# function that executes whne user fills form from contact page
def bookstore_self_mail(user_email, user_msg):

    # message setting for self mail
    msg = MIMEMultipart()
    msg['To'] = self_email
    msg['From'] = user_email
    msg['Subject'] = 'Someone made a purchase on Bookstore App' + emoji.emojize(":sign_of_the_horns:")

    body = user_email + ' made an purchase through Bookstore app.<p> His order is: <br />' + user_msg + '<p><br />--<br />'+ email_signature
    msg.attach(MIMEText(body, 'html'))

    # send mail to self about 
    sendMail(user_email, self_email, msg.as_string())