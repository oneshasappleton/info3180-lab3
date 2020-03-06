from flask import Flask
from flask_mail import Mail 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is Sparta!'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAILPORT'] = '25' # 465 or 2525
app.config['MAIL_USERNAME'] = 'redacted'
app.config['MAIL_PASSWORD'] = 'redacted'

mail = Mail(app)
from app import views 
