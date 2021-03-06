from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Discord: xyz#7777\nvk.com: vk.com/haqker'

if __name__ == "__main__":
    app.run()