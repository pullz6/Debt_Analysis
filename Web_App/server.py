from flask import Flask, render_template, request 
from analysis import get_analysis
from waitress import serve
import json
import plotly
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/analysis')

def get_country(): 
    country = request.args.get('country')
    df = get_analysis(country)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['date'], y=df['External_Debts'],mode='lines+markers', name='External Debts'))
    fig.add_trace(go.Scatter(x=df['date'], y=df['IMF_Credit'], mode='lines+markers', name='IMF Credit'))
    fig.add_trace(go.Scatter(x=df['date'], y=df['Short_term_debt'], mode='lines+markers', name='Short Term Debt'))
    fig.add_trace(go.Scatter(x=df['date'], y=df['Gross_income'], mode='lines+markers', name='Income'))
    fig.add_trace(go.Scatter(x=df['date'], y=df['Exports'], mode='lines+markers', name='Exports'))
    fig.add_trace(go.Scatter(x=df['date'], y=df['Imports'], mode='lines+markers', name='Imports'))
    fig.add_trace(go.Scatter(x=df['date'], y=df['National_Expenditure'], mode='lines+markers', name='National_Expenditure'))
    # Create graphJSON
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    check = 'Works'
    return render_template(
        'analysis.html', 
        title=country,
        graphJSON=graphJSON
    )

if __name__ == "__main__": 
    serve(app,host = '0.0.0.0', port=8000)
