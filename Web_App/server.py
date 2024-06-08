from flask import Flask, render_template, request 
from analysis import get_analysis
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/analysis')

def get_country(): 
    country = request.args.get('country')
    debt_data = get_analysis(country)
    return render_template(
        'analysis.html', 
        title=country,
        temp = debt_data
    )

if __name__ == "__main__": 
    serve(app,host = '0.0.0.0', port=8000)
