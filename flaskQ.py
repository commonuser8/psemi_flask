from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    lis = []
    for i in range(10):
        lis.append(i)
    dic = {"name": "KC", "age": 21, "address": "Okinawa"}

    return render_template('flaskQ.html', lis=lis, dic=dic)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)