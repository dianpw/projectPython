from flask import Flask
app = Flask(__name__)

@app.route('/age/<string:age>')
def hello_age(age):
    return 'I am {} years old'.format(age)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')