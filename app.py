from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/index", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nama = request.form.get("username")
        return f"Halo, {nama}"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)



