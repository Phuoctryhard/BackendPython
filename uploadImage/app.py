
# from flask import Flask, jsonify, request, render_template, Response, send_file
# import os  # importing operating system module
# import io

# # database
# from flask_mysqldb import MySQL
# from werkzeug.utils import secure_filename
# app = Flask(__name__)
# # config
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'flask_db'
# mysql = MySQL(app)


# @app.route('/')  # this decorator create the home route
# def home():
#     return render_template('index.html')


# # @app.route('/about')
# # def about():
# #     cursor = mysql.connection.cursor()
# #     cursor.execute("SELECT * FROM user")
# #     columns = [col[0] for col in cursor.description]  # Lấy tên cột
# #     results = cursor.fetchall()
# #     cursor.close()
# #     # Chuyển đổi kết quả thành danh sách các từ điển
# #     data = []
# #     for row in results:
# #         data.append(dict(zip(columns, row)))

# #     return jsonify(data)

# @app.route('/upload', methods=["POST"])
# def upload():
#     pic = request.files['pic']
#     if not pic:
#         return "no pic uploaded ", 400
#     filename = secure_filename(pic.filename)
#     mimetype = pic.mimetype
#     # Đọc dữ liệu hình ảnh dưới dạng bytes
#     img_data = pic.read()
#     # Chèn dữ liệu vào cơ sở dữ liệu
#     cursor = mysql.connection.cursor()
#     cursor.execute("INSERT INTO img (img, name, mimetype) VALUES (%s, %s, %s)",
#                    (img_data, filename, mimetype,))
#     mysql.connection.commit()
#     return "Thành công thêm ", 200


# @app.route('/image/<name>')
# def get_image_by_name(name):
#     try:
#         # Kết nối đến cơ sở dữ liệu
#         cursor = mysql.connection.cursor()

#         # Truy vấn để lấy dữ liệu hình ảnh từ cơ sở dữ liệu dựa trên tên
#         cursor.execute("SELECT img FROM img WHERE name = %s", (name,))
#         img_data = cursor.fetchone()

#         if img_data:
#             # Trả về dữ liệu hình ảnh trực tiếp, không giải mã
#             return send_file(io.BytesIO(img_data[0]), mimetype='image/jpeg'), 200
#         else:
#             # Trả về lỗi nếu không tìm thấy ảnh
#             return "Không tìm thấy ảnh", 404
#     except Exception as e:
#         return str(e), 500


# if __name__ == '__main__':
#     # for deployment we use the environ
#     # to make it work for both production and development
#     port = int(os.environ.get("PORT", 5000))
#     app.run(debug=True, host='0.0.0.0', port=port)

import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './static/img'  # Thư mục để lưu trữ tệp tải lên
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')  # this decorator create the home route
def home():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    print(request.files)
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file'))  # Đổi 'uploaded_file' thành 'upload_file'
    return ''
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
if __name__ == '__main__':
    app.run(debug=True)
