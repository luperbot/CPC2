from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash, jsonify

DEBUG = True
SECRET_KEY = 'super secret key'

app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/results", methods=['POST'])
def results():
    plant_counts = json.loads(request.form.get('plant_counts'))
    length = int(json.loads(request.form.get('plot_length')))
    width = int(json.loads(request.form.get('plot_width')))
    results = {
        'plot' : [
            [{'plant': 'Apple', 'benefit': 5}, {'plant': 'Basil', 'benefit': 3}],
            [{'plant': 'Apple', 'benefit': 5}, {'plant': 'Basil', 'benefit': 3}],
        ]
    }
    return jsonify(**results)

if __name__ == '__main__':
    app.run()

