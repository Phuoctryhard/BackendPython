
from flask import Flask, render_template, jsonify,request
import os  # importing operating system module
# database
from flask_mysqldb import MySQL

app = Flask(__name__)
# config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask_db'
mysql = MySQL(app)


@app.route('/')  # this decorator create the home route
def home():
    return jsonify({"message": "anh yêu em"})


@app.route('/about')
def about():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM user")
    columns = [col[0] for col in cursor.description]  # Lấy tên cột
    results = cursor.fetchall()
    cursor.close()
    # Chuyển đổi kết quả thành danh sách các từ điển
    data = []
    for row in results:
        data.append(dict(zip(columns, row)))

    return jsonify(data)


@app.route('/insert', methods=['POST'])
def insert():
    try:
        cursor = mysql.connection.cursor()
        sql = "INSERT INTO user (name, email) VALUES (%s, %s)"
        val = ("John", "Highway 21")
        cursor.execute(sql, val)
        mysql.connection.commit()
        cursor.close()
        return jsonify({"message": "Thêm dữ liệu thành công!"})
    except mysql.connector.Error as err:
        return jsonify({"message": "Thêm dữ liệu không thành công: {}".format(err)})


@app.route('/delete/<string:name_data>', methods=['DELETE'])
def delete(name_data):
    try:
        cursor = mysql.connection.cursor()
        sql = "DELETE FROM user WHERE name = %s"
        cursor.execute(sql, (name_data,))
        mysql.connection.commit()
        cursor.close()
        return jsonify({"message": "Xóa dữ liệu thành công!"})
    except mysql.connector.Error as err:
        return jsonify({"message": "Xóa dữ liệu không thành công: {}".format(err)})


@app.route('/home')
def trangchu():
    return jsonify({
        {
            "id": 1,
            "slug": "lorem-ipsum",
            "url": "https://jsonplaceholder.org/posts/lorem-ipsum",
            "title": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "content": "Ante taciti nulla sit libero orci sed nam. Sagittis suspendisse gravida ornare iaculis cras nullam varius ac ullamcorper. Nunc euismod hendrerit netus ligula aptent potenti. Aliquam volutpat nibh scelerisque at. Ipsum molestie phasellus euismod sagittis mauris, erat ut. Gravida morbi, sagittis blandit quis ipsum mi mus semper dictum amet himenaeos. Accumsan non congue praesent interdum habitasse turpis orci. Ante curabitur porttitor ullamcorper sagittis sem donec, inceptos cubilia venenatis ac. Augue fringilla sodales in ullamcorper enim curae; rutrum hac in sociis! Scelerisque integer varius et euismod aenean nulla. Quam habitasse risus nullam enim. Ultrices etiam viverra mattis aliquam? Consectetur velit vel volutpat eget curae;. Volutpat class mus elementum pulvinar! Nisi tincidunt volutpat consectetur. Primis morbi pulvinar est montes diam himenaeos duis elit est orci. Taciti sociis aptent venenatis dui malesuada dui justo faucibus primis consequat volutpat. Rhoncus ante purus eros nibh, id et hendrerit pellentesque scelerisque vehicula sollicitudin quam. Hac class vitae natoque tortor dolor dui praesent suspendisse. Vehicula euismod tincidunt odio platea aenean habitasse neque ad proin. Bibendum phasellus enim fames risus eget felis et sem fringilla etiam. Integer.",
            "image": "https://dummyimage.com/800x430/FFFFFF/lorem-ipsum.png&text=jsonplaceholder.org",
            "thumbnail": "https://dummyimage.com/200x200/FFFFFF/lorem-ipsum.png&text=jsonplaceholder.org",
            "status": "published",
            "category": "lorem",
            "publishedAt": "04/02/2023 13:25:21",
            "updatedAt": "14/03/2023 17:22:20",
            "userId": 1
        }
    })


@app.route('/update', methods=['PUT'])
def update():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    id = data.get('id')
    cur = mysql.connection.cursor()
    cur.execute("""
    UPDATE user SET name=%s, email=%s
    WHERE id=%s
    """, (name, email, id))
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "Data Updated Successfully"})

@app.route('/join')
def join():
    cur = mysql.connection.cursor()
    sql = "SELECT \
    user.name AS users, \
    products.name AS favorites \
    FROM user \
    INNER JOIN products ON user.product = products.id"
    cur.execute(sql)
    myresult = cur.fetchall()
    return jsonify(myresult)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
