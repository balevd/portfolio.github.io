from flask import Flask, render_template, redirect, url_for, flash, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def enter():
    return render_template('index.html')


@app.route('/morse', methods=['GET'])
def morse_code():
    return render_template('morse.html')


if __name__ == "__main__":
    app.run(debug=True)