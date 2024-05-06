# Connect Flask Web Application With Mysql Database #6

- Install: pip install mysql-connector-python
  pip install flask-mysqldb

-Step 1: Connecting a Flask Application to a MySQL Database
-Step 2: Configuring the MySQL Connection Cursor
-Step 3: Programming a Flask Application
-Step 4: Putting the Code into Action

# return json

@app.route('/home')
def trangchu():
return jsonify({
"data": {
"message": "thành công"
}
})

# Select Mysql

import mysql.connector

mydb = mysql.connector.connect(
host="localhost",
user="yourusername",
password="yourpassword",
database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT \* FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
print(x)

# link tài liệu học: connect flask to mysql

https://hevodata.com/learn/flask-mysql/
https://planetscale.com/learn/courses/mysql-for-python-developers/building-a-flask-app-with-mysql/updates-for-a-single-booking

- Link video Connect Flask Web Application With Mysql Database #6
  https://www.youtube.com/watch?v=qfYzCdkVwig

# w3School có Mongodb và mysql

# Ví dụ :

from flask import Flask, render_template, request, url_for, flash
from werkzeug.utils import redirect
from flask_mysqldb import MySQL

app = Flask(**name**)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'M@tech@pp1234'
app.config['MYSQL_DB'] = 'crud'

mysql = MySQL(app)

@app.route('/')
def Index():
cur = mysql.connection.cursor()
cur.execute("SELECT \* FROM students")
data = cur.fetchall()
cur.close()

    return render_template('index.html', students=data)

@app.route('/insert', methods=['POST'])
def insert():
if request.method == "POST":
flash("Data Inserted Successfully")
name = request.form['name']
email = request.form['email']
phone = request.form['phone']
cur = mysql.connection.cursor()
cur.execute("INSERT INTO students (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
mysql.connection.commit()
return redirect(url_for('Index'))

@app.route('/delete/<string:id_data>', methods=['GET'])

<!--  Trong trường hợp này, id_data là tên biến và <string> chỉ ra rằng biến này sẽ chứa một chuỗi.
 xử lý các yêu cầu GET được gửi đến địa chỉ '/delete/<id_data>', trong đó id_data là một giá trị động có thể là bất kỳ chuỗi nà
 -->

def delete(id_data):
flash("Record Has Been Deleted Successfully")
cur = mysql.connection.cursor()
cur.execute("DELETE FROM students WHERE id=%s", (id_data,))

<!-- viết tắt :
sql = "DELETE FROM user WHERE name = %s"
cursor.execute(sql, (name_data,))

 -->

mysql.connection.commit()
return redirect(url_for('Index'))

@app.route('/update', methods=['POST', 'GET'])
def update():
if request.method == 'POST':
id_data = request.form['id']
name = request.form['name']
email = request.form['email']
phone = request.form['phone']

        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE students SET name=%s, email=%s, phone=%s
        WHERE id=%s
        """, (name, email, phone, id_data))
        flash("Data Updated Successfully")
        return redirect(url_for('Index'))

if **name** == "**main**":
app.run(debug=True)

#### Update

from flask import request

@app.route('/update', methods=['PUT'])
def update():
data = request.json
name = data.get('name')
email = data.get('email')
id = data.get('id')
    if not name or not email or id is None:
        return jsonify({"error": "Thiếu thông tin cần thiết"}), 400

    cur = mysql.connection.cursor()
    cur.execute("""
    UPDATE user SET name=%s, email=%s
    WHERE id=%s
    """, (name, email, id))
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "Data Updated Successfully"})

# delete
@app.route('/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
try:
cursor = mysql.cursor()
sql = "DELETE FROM user WHERE id = %s"
cursor.execute(sql, (user_id,))
mysql.commit()
cursor.close()
return jsonify({"message": "Xóa người dùng thành công!"})
except mysql.connector.Error as err:
return jsonify({"error": "Xóa người dùng không thành công: {}".format(err)}), 500

if **name** == '**main**':
app.run(debug=True)
