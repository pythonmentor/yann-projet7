from flask import Flask, render_template

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.

# To get one variable, tape app.config['MY_VARIABLE']


@app.route('/')
@app.route('/homepage/')
def index():
    return render_template("homepage.html")



if __name__ == "__main__":
    app.run()