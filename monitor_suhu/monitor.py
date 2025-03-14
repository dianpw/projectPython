import random
from flask import Flask, render_template, jsonify

app = Flask(__name__)
# Simulasi data sensor
suhu = 25.0
kelembapan = 60.0
tekanan = 1010.0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    global suhu, kelembapan, tekanan

    suhu += random.uniform(-0.5, 0.5)
    kelembapan += random.uniform(-1, 1)
    tekanan += random.uniform(-2, 2)

    # Pastikan dalam rentang yang wajar
    suhu = max(20, min(35, suhu))
    kelembapan = max(40, min(80, kelembapan))
    tekanan = max(980, min(1050, tekanan))

    return jsonify({"suhu": round(suhu, 1), "kelembapan": round(kelembapan, 1), "tekanan": round(tekanan, 1)})


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')