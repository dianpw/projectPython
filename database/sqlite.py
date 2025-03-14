from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)
# Fungsi untuk membuat database jika belum ada
def init_db():
    with sql.connect('database.db') as con:
        print("Database opened successfully")  # Debugging: memastikan database dibuka
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS students (
                        name TEXT, 
                        addr TEXT, 
                        city TEXT, 
                        pin TEXT)''')  # Membuat tabel jika belum ada
        con.commit()  # Simpan perubahan
        print("Table created successfully")  # Debugging: memastikan tabel dibuat

init_db()  # Pastikan tabel dibuat saat aplikasi dimulai

@app.route('/')
def home():
   return render_template('indexsql.html')

@app.route('/enternew')
def new_student():
   return render_template('student.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
    msg = ""  # Variabel pesan untuk menampilkan hasil
    con = None  # Inisialisasi koneksi database
    
    if request.method == 'POST':  # Jika metode POST digunakan
        try:
            # Ambil data dari form
            name = request.form['name']
            addr = request.form['addr']
            city = request.form['city']
            pin = request.form['pin']
            
            # Simpan ke database
            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students (name, addr, city, pin) VALUES (?,?,?,?)",
                            (name, addr, city, pin))  # Query untuk memasukkan data
                con.commit()  # Simpan perubahan
                msg = "Record successfully added"  # Pesan sukses
        except Exception as e:
            msg = f"Error in insert operation: {str(e)}"  # Tangani kesalahan
        finally:
            return render_template("result.html", msg=msg)  # Tampilkan hasil operasi
            
@app.route('/list')
def list():
    con = sql.connect("database.db")  # Koneksi ke database
    con.row_factory = sql.Row  # Memungkinkan akses kolom dengan nama (bukan indeks)
    
    cur = con.cursor()
    cur.execute("SELECT * FROM students")  # Ambil semua data siswa
    
    rows = cur.fetchall()  # Simpan hasil query ke dalam variabel
    return render_template("list.html", rows=rows)  # Kirim data ke template `list.html`

if __name__ == '__main__':
    app.run(debug = True)
