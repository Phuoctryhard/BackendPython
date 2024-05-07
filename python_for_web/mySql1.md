# Connect Flask Web Application With Mysql Database #6

# return json

@app.route('/home')
def trangchu():
return jsonify({
"data": {
"message": "thành công"
}
})
