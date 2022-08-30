import pyautogui
import hashlib
from flask import Flask, render_template, redirect, url_for




USER_ID = "d27768db2cd058a3282ee47556342ccad977bbceb403888cd8a46dfce8d71c6f"
USER_PASS = "ede892dfa9a48c70cba04100da23ec4aadacd57c1b2807939d14d81cdb8bd27d"


app = Flask(__name__)

@app.route('/index/<user>')
def index():
    name = USER_ID
    return render_template('index.html', name = user)


if __name__ == "__main__":
    app.run(debug=True)

im1 = pyautogui.screenshot('abc.png')

