# document:

# How to Upload and Store Images (In the DB) with Python (Flask)

- đã áp dụng thành công
  https://flask.palletsprojects.com/en/2.3.x/patterns/fileuploads/

* 3 bước : Ý tưởng cơ bản của việc tải tập tin lên thực ra khá đơn giản. Về cơ bản nó hoạt động như thế này:

- 1. Thẻ <form> được đánh dấu bằng enctype=multipart/form-data và <input type=file> được đặt trong biểu mẫu đó.

- 2. Ứng dụng truy cập tệp từ từ điển tệp trên đối tượng yêu cầu.

- 3. sử dụng phương thức save() của tệp để lưu tệp vĩnh viễn ở đâu đó trên hệ thống tệp.

* ví dụ : tải tệp lên thư mục tải lên cụ thể và hiển thị tệp cho người dùng.

# code server xử lí file :

- Bước 1 tạo đường dẫn chứa ảnh
  import os
  from flask import Flask, flash, request, redirect, url_for
  from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(**name**)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

- Giải thích : UPLOAD_FOLDER là nơi chúng tôi sẽ lưu trữ các tệp đã tải lên và
  ALLOWED_EXTENSIONS là tập hợp các phần mở rộng tệp được phép.
  Secure_filename : luôn sử dụng chức năng đó để bảo mật tên tệp trước khi lưu trữ trực tiếp trên hệ thống tệp.

* Bước 2 : upload file
  def allowed_file(filename):
  return '.' in filename and \
   filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
if request.method == 'POST': # check if the post request has the file part
if 'file' not in request.files:
flash('No file part')
return redirect(request.url)
file = request.files['file'] # If the user does not select a file, the browser submits an # empty file without a filename.
if file.filename == '':
flash('No selected file')
return redirect(request.url)
if file and allowed_file(file.filename):
filename = secure_filename(file.filename)
file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
return redirect(url_for('download_file', name=filename))
return '''

- upload img thông qua url
  vd: http://localhost:5000/uploads/424679559_699648792364951_7636736357083290069_n.jpg
  @app.route('/uploads/<filename>')
  def uploaded_file(filename):
  return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# xử lí form có file

import React, { useState } from 'react';

function UploadFile() {
const [file, setFile] = useState(null);

const handleChange = (event) => {
setFile(event.target.files[0]);
};

const handleSubmit = async (event) => {
event.preventDefault();
const formData = new FormData();
formData.append('file', file);
try {
const response = await fetch('http://localhost:5000/upload', {
method: 'POST',
body: formData,
});
// Xử lý phản hồi từ server nếu cần
console.log('File uploaded successfully');
} catch (error) {
console.error('Error uploading file:', error);
}

};

return (

<form onSubmit={handleSubmit} encType="multipart/form-data">
<input type="file" name="file" onChange={handleChange} />
<button type="submit">Upload a file</button>
</form>
);
}
export default UploadFile;
