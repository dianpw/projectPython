import random

from flask import Flask, render_template

app = Flask (__name__)

@app.route('/')
def about():
    a = round(random.uniform(20,40),2)
    print(a)
    return render_template('hello.html', marks=a)


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
