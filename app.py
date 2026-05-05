from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return f"bosh sahifa"



@app.route("/time")
def tim():
    return f"hozirgi vaqt 17:37"

@app.route("/day")
def day():
    return f"bugun sechanba"

@app.route("/weat")
def weather():
    return f"bugun quyoshli"

@app.route("/temp")
def temprature():
    return f"harorat 31°C"

@app.route("/contry")
def cont():
    return f"O\'zbekiston"

@app.route("/copital")
def copital():
    return f"poytaxt toshkeNT"

@app.route("/lang")
def language():
    return f"Davlat tili: Uzbek tili"

@app.route("/about")
def about():
    return f"bu sayt haqida"

@app.route("/contact")
def con():
    return f"bog\'lanish sahifasi"

@app.route("/help")
def get_help():
    return f"yordam sahifasi"



if __name__ == "__main__":
    app.run(debug=True)
