from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash, jsonify

import parse_plants

DEBUG = True
SECRET_KEY = 'super secret key'

app = Flask(__name__)
app.config.from_object(__name__)

# Load inital values for plants.
PLANTS = parse_plants.parse_file('cpc/plantdata.txt')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/plants.json")
def plants():
    return jsonify(**PLANTS)

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

