from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    print("hallo andre und dominik")
    return render_template("FlaskProject.html")
    

if __name__ == "__main__":
   app.run()