from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    photos_file = open("photos.txt", "r", encoding = "UTF-8")
    photos_list = [i for i in photos_file]
    photos_file.close()
    return render_template('index.html', photos_list = photos_list)


@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/add-photos", methods = ["POST"])
def add_photos():
    photo = request.form["new-photos"]
    photos_file = open('photos.txt', 'a+', encoding = "UTF-8")
    photos_file.write(str(photo) + "\n")
    photos_file.close()
    return render_template("added.html")