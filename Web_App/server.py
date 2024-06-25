from flask import Flask, render_template, request 
from analysis import get_analysis
from waitress import serve
import json
import plotly
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
from plotly.subplots import make_subplots

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

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['date'], y=df['Goods_imports'],mode='lines+markers', name='Goods_imports'))
    fig.add_trace(go.Scatter(x=df['date'], y=df['Service_imports'], mode='lines+markers', name='Service_imports'))
    fig.add_trace(go.Scatter(x=df['date'], y=df['Goods_exports'], mode='lines+markers', name='Goods_exports'))
    fig.add_trace(go.Scatter(x=df['date'], y=df['Service_exports'], mode='lines+markers', name='Service_exports'))

    graphJSON2 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    df_2020_im = df[df['date'].dt.strftime('%Y') == '2022']
    labels = ['Agriculteral Raw Material Imports','Food imports','Fuel imports','Manufacturing Imports','Ores Metals Imports']
    values_im = [df_2020_im['Agri_raw_materials_imports'].iloc[0], df_2020_im['Food_imports'].iloc[0], df_2020_im['Fuel_imports'].iloc[0], df_2020_im['Manufacturing_imports'].iloc[0],df_2020_im['Ores_metal_imports'].iloc[0]]

    df_2020_ex = df[df['date'].dt.strftime('%Y') == '2022']
    values_ex = [df_2020_ex['Agri_raw_materials_exports'].iloc[0], df_2020_ex['Food_exports'].iloc[0], df_2020_ex['Fuel_exports'].iloc[0], df_2020_ex['Manufacturing_exports'].iloc[0],df_2020_ex['Ores_metal_exports'].iloc[0]]
    fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
    fig.add_trace(go.Pie(labels=labels, values=values_im, name="Imports"),1, 1)
    fig.add_trace(go.Pie(labels=labels, values=values_ex, name="Exports"), 1, 2)

    # Use `hole` to create a donut-like pie chart
    fig.update_traces(hole=.4, hoverinfo="label+percent+name")

    fig.update_layout(
        # Add annotations in the center of the donut pies.
        annotations=[dict(text='Imports', x=0.16, y=0.5, font_size=20, showarrow=False),
                    dict(text='Exports', x=0.84, y=0.5, font_size=20, showarrow=False)])
    
    graphJSON3 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=df['date'], y=df['Military_expenditure'], fill='tonexty',
                        mode='none',name='Military Expendiure' # override default markers+lines
                        ))
    fig.add_trace(go.Scatter(x=df['date'], y=df['Education_expenditure'], fill='tonexty',
                        mode= 'none',name='Education Expendiure'))

    fig.add_trace(go.Scatter(x=df['date'], y=df['Tourism_expenditure'], fill='tonexty',
                        mode= 'none',name='Tourism Expendiure'))

    fig.add_trace(go.Scatter(x=df['date'], y=df['Household_expenditure'], fill='tonexty',
                        mode= 'none',name='Household Expendiure',fillcolor = 'lightblue'))
    
    graphJSON4 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    check = 'Works'
    return render_template(
        'analysis.html', 
        title=country,
        graphJSON = graphJSON,
        graphJSON2 = graphJSON2, 
        graphJSON3 = graphJSON3,
        graphJSON4 = graphJSON4
    )

if __name__ == "__main__": 
    serve(app,host = '0.0.0.0', port=8000)
