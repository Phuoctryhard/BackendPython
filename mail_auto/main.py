from flask import Flask ,render_template,request
from flask_mail import Mail, Message
import json
import os # importing operating system module
app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Use 'smtp.gmail.com' instead of 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'nguyenhuynhan.dn@gmail.com'
app.config['MAIL_PASSWORD'] = 'rkif gdqq cdwk tqmj' 
app.config['MAIL_USE_TLS'] = True  # Uncomment this line to enable TLS
mail = Mail(app)
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

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)