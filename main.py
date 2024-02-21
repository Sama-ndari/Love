from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/popup')
def show_popup():
    return render_template('popup.html')


@app.route('/move_button', methods=['POST'])
def move_button():
    x = random.randint(0, 350)
    y = random.randint(0, 350)
    return {'x': x, 'y': y}


if __name__ == '__main__':
    app.run(debug=True)
