from flask import Flask, request, render_template, abort, redirect, url_for
import requests

app = Flask(__name__, template_folder="templates")

main_index = 'Discord: xyz#7777<br>vk: vk.com/haqker'

some_text = ""

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
