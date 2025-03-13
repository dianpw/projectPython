from flask import Flask, render_template

app = Flask (__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about/<name>')
def about(name):
    #return "Hello {}!".format(name)
    return render_template('about.html', name=name)


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
