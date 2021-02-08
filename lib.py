## import packages
import numpy as np

## import plotly packages
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot


## Engineer '-' and '\n' in zipcode
def extract_zip(raw_zip):
    try:
        int_zip = int(raw_zip)
    except:
        string = str(raw_zip)
        if '-' in string:
            start = string.index('-')
        elif '\n' in string:
            start = string.index('\n')
        
        int_zip = int(string[:start])
    return int_zip

## Function: check whether x is in ziplist
def helperInNYC(x,zipList):
    if x in zipList:
        return True
    else:
        return False

## Process price
def fix_price(x):
    if isinstance(x,str) and "$" in x:
        return np.float(x[1:-2].replace(',',''))
    else:
        return x

## function to calculate rent-to-price ratio
def cal_ratio(df, variable):
    df[variable + 'ratio'] = (df['Monthly_Rent']*0.75)/df[variable]

## plot histogram
def plot_hist(config):
    trace = [go.Histogram(
        x = config['x'],
        opacity=0.75
        )]

    layout = go.Layout(
        title=config['title'],
        xaxis=dict(title= config['xaxis']),
        yaxis = dict(title=config['yaxis'])
        )

    fig = go.Figure(data=trace, layout=layout)

    return iplot(fig)

## bar plot
def plot_bar(config):
    trace =[go.bar(
        x = config['x'],
        y = config['y']
        )]
    layout = go.Layout(
        title = config['title'],
        xaxis=dict(title= config['xaxis'], tickmode='linear'),
        yaxis = dict(title=config['yaxis'])
        )
    fig = go.Figure(data=trace,layout=layout)
    return iplot(fig)


## box plot
def plot_box(config):

    trace =[go.Box(
        y = config['y']
        )]

    layout = go.Layout(
        title = config['title'],
        xaxis = dict(title= config['xaxis']),
        yaxis = dict(title=config['yaxis'])
        )

    fig = go.Figure(data=trace, layout=layout)

    return iplot(fig)

## line plot
def plot_lines(config):
    
    legends = config['legends']
    legends = [str(legend) for legend in legends]

    x = config['x']
    y = config['y']
    traces = []
    for y_, legend in zip(y,legends):
        trace = go.Scatter(
            x=x,
            y=y_,
            mode = 'lines',
            name=legend)
        traces.append(trace)
    layout = go.Layout(
        title= config['title']
    )

    fig = go.Figure(data=traces,layout=layout)
    return iplot(fig)

## scatter plot
def plot_scatter(config):
   
    trace = [go.Scatter(
        x=config['x'],
        y=config['y'],
        mode = 'markers'
        )]
    layout = go.Layout(
        title = config['title'],
        xaxis = dict(title= config['xaxis'], tickmode='linear'),
        yaxis = dict(title=config['yaxis'])
    )

    fig = go.Figure(data=trace,layout=layout)
    return iplot(fig)
   
    