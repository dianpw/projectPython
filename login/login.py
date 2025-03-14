from flask import Flask, request, flash, render_template, redirect, url_for

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'  # Tambahkan SECRET_KEY

@app.route("/success/<name>")
def success(name):
    return render_template("read.html", name=name)
    #return "Welcome {}".format(name)

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        flash('Login Berhasil!', 'success')
        return redirect(url_for("success", name=user))
    else:
        flash('Login Gagal', 'error')
        return render_template("login.html")
    
if __name__ == "__main__":
    app.run(debug=True)