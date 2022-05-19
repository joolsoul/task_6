import os
from pymystem3 import Mystem

from flask import render_template, Flask, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def start():
    if request.method == 'GET':
        return render_template('start_page.html')

    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(os.path.join('static/input'))
    parse_text()
    return redirect(url_for('result'))


@app.route('/upload', methods=['GET', 'POST'])
def file_upload():
    if request.method == 'GET':
        return render_template("upload_file_page.html")


@app.route('/result', methods=['GET', 'POST'])
def result():
    return render_template("result_page.html")


def parse_text():
    input_text = read_from_file('input')
    m = Mystem()
    output_text = m.lemmatize(input_text)
    write_to_file("result", output_text)


def read_from_file(file_name):
    with open("static/" + file_name, encoding='utf-8') as file:
        text = file.read()
    return text


def write_to_file(file_name, text):
    with open("static/" + file_name, 'w', encoding='utf-8') as file:
        for element in text:
            file.write(element)


if __name__ == '__main__':
    app.run()
