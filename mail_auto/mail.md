- pip install flask flask-mail
  https://www.youtube.com/watch?v=nOkpTwPvDTg
  https://www.youtube.com/watch?v=L7Cslucyyyo
- Tài liệu
  https://pythonhosted.org/Flask-Mail/

* how to make send email

# import

from flask import Flask ,render_template,request
from flask_mail import Mail, Message
import json
import os # importing operating system module

# config

app = Flask(**name**)
app.config['MAIL_SERVER'] = 'smtp.gmail.com' # Use 'smtp.gmail.com' instead of 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'nguyenhuynhan.dn@gmail.com'
app.config['MAIL_PASSWORD'] = 'rkif gdqq cdwk tqmj'
app.config['MAIL_USE_TLS'] = True # Uncomment this line to enable TLS
mail = Mail(app)

# route

@app.route('/',methods = ['GET','POST']) # this decorator create the home route
def home ():
if request.method=='POST':
username = "ngo dinh phuoc dep trai"
password = "0865446276"

        msg = Message("Hey ",sender='nguyenhuynhan.dn@gmail.com',recipients=['ngodinhphuoc100@gmail.com','nguyenvanhuy20053012@gmail.com'])
        msg.body = f"Username: {username}\nPassword: {password}"

        mail.send(msg)
        return "Send Email"
    return render_template('index.html')

# Note : Với f-string, bạn có thể chèn giá trị của biến hoặc biểu thức Python trực tiếp vào chuỗi. Trong ví dụ của chúng ta:

- msg.body = f"Username: {username}\nPassword: {password}"
