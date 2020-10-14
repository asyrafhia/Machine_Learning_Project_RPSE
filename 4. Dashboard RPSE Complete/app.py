from flask import Flask, render_template, url_for, request, redirect
import plotly
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import json
import joblib
import sqlalchemy as db
import mysql.connector
from function.function import OnlineshopFunction

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

def category_plot(cat_plot='histplot', cat_x='month', cat_y='administrative', estimator='count', hue='revenue'):

    # dfol = pd.read_csv('./static/online_shop.csv')

    con = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'Welldone1+',
        database = 'olshop'
    )
    c = con.cursor(buffered=True)
    query = 'select * from online_shop'
    c.execute(query)
    res = c.fetchall()
    dfol = pd.DataFrame(data=res, columns=c.column_names)
    # dfol = pd.read_sql('select * from online_shop', con)   

    if cat_plot == 'histplot':

        data = []

        for val in dfol[hue].unique(): #['True', 'False']
            hist = go.Histogram(
                x=dfol[dfol[hue] == val][cat_x],
                y=dfol[dfol[hue] == val][cat_y],
                histfunc= estimator,
                name = str(val)
            )

            data.append(hist)

            title = 'Histogram'
    
    elif cat_plot == 'boxplot':
        data = []

        for val in dfol[hue].unique(): #['Yes', 'No']
            box = go.Box(
                x=dfol[dfol[hue] == val][cat_x],
                y=dfol[dfol[hue] == val][cat_y],
                name = str(val)
            )

            data.append(box)

            title = 'Box'
    
    if cat_plot == 'histplot' and estimator =='count':
        layout = go.Layout(
            title=title,
            xaxis=dict(title=cat_x),
            yaxis=dict(title='count of person'),
            boxmode='group'
        )
    elif cat_plot == 'histplot' and estimator !='count':
        layout = go.Layout(
            title=title,
            xaxis=dict(title=cat_x),
            yaxis=dict(title=cat_y),
            boxmode='group'
        )
    elif cat_plot == 'boxplot':
        layout = go.Layout(
            title=title,
            xaxis=dict(title=cat_x),
            yaxis=dict(title=cat_y),
            boxmode='group'
        )

    res = {"data": data, "layout": layout}

    graphJSON = json.dumps(res, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

@app.route('/index')
def index():

    plot = category_plot() 

    #Dropdown menu
    #            drop[0],       drop[1]
    list_plot = [('histplot', 'Histogram'), ('boxplot', 'Box')]
    list_x = [('specialday', 'SpecialDay'), ('month', 'Month'), ('operatingsystems', 'OperatingSystems'), ('browser', 'Browser'), ('region', 'Region'), ('traffictype', 'TrafficType'), ('visitortype', 'VisitorType'), ('weekend', 'Weekend'), ('revenue', 'Revenue')]
    list_y = [('administrative', 'Administrative'), ('administrative_duration', 'Administrative_Duration'), ('informational', 'Informational'), ('informational_duration', 'Informational_Duration'), ('productRelated', 'ProductRelated'), ('productRelated_duration', 'ProductRelated_Duration'), ('bouncerates', 'BounceRates'), ('exitrates', 'ExitRates'), ('pagevalues', 'PageValues')]
    list_estimator = [('count', 'Count'), ('avg', 'Average'), ('max', 'Max'), ('min', 'Min')]
    list_hue = [('revenue', 'Revenue')]

    return render_template(
        'category.html',
        plot=plot,
        focus_plot='histplot',
        # awalnya focux_x
        focus_x='month',
        # awalnya focus_extimator
        focus_estimator='count',
        focus_hue='revenue',
        drop_plot=list_plot,
        drop_x=list_x,
        drop_y=list_y,
        drop_estimator=list_estimator,
        drop_hue=list_hue
    )

@app.route('/cat_fn/<nav>')
def cat_fn(nav):
    
    if nav == 'True': # Saat klik menu navigasi
        cat_plot='histplot'
        cat_x='month'
        cat_y='administrative'
        estimator='count'
        hue='revenue'

    else: # Saat memilih value dari form
        cat_plot = request.args.get('cat_plot') # boxplot
        cat_x = request.args.get('cat_x') # sex
        cat_y = request.args.get('cat_y') # None
        estimator = request.args.get('estimator') # count
        hue = request.args.get('hue') # smoker

    # Dari boxplot ke histogram
    if estimator == None:
        estimator = 'count'

    # saat estimator count, dropdown menu sumbu Y di disabled dan memberikan nilai None
    if cat_y == None:
        cat_y = 'administrative'

    #Dropdown menu
    list_plot = [('histplot', 'Histogram'), ('boxplot', 'Box')]
    list_x = [('specialday', 'SpecialDay'), ('month', 'Month'), ('operatingsystems', 'OperatingSystems'), ('browser', 'Browser'), ('region', 'Region'), ('traffictype', 'TrafficType'), ('visitortype', 'VisitorType'), ('weekend', 'Weekend'), ('revenue', 'Revenue')]
    list_y = [('administrative', 'Administrative'), ('administrative_duration', 'Administrative_Duration'), ('informational', 'Informational'), ('informational_duration', 'Informational_Duration'), ('productRelated', 'ProductRelated'), ('productRelated_duration', 'ProductRelated_Duration'), ('bouncerates', 'BounceRates'), ('exitrates', 'ExitRates'), ('pagevalues', 'PageValues')]
    list_estimator = [('count', 'Count'), ('avg', 'Average'), ('max', 'Max'), ('min', 'Min')]
    list_hue = [('revenue', 'Revenue')]

    plot = category_plot(cat_plot, cat_x, cat_y, estimator, hue)

    return render_template(
        'category.html',
        plot=plot,
        focus_plot=cat_plot,
        # awalnya focux_x
        focus_x=cat_x,
        focus_y=cat_y,
        # awalnya focus_extimator
        focus_estimator=estimator,
        focus_hue=hue,
        drop_plot=list_plot,
        drop_x=list_x,
        drop_y=list_y,
        drop_estimator=list_estimator,
        drop_hue=list_hue
    )

def scatter_plot(cat_x, cat_y, hue):
    # dfol = pd.read_csv('./static/online_shop.csv')

    con = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'Welldone1+',
        database = 'olshop'
    )
    dfol = pd.read_sql('select * from online_shop', con)

    data = []

    for val in dfol[hue].unique():
        scatt = go.Scatter(
            x=dfol[dfol[hue] == val][cat_x],
            y=dfol[dfol[hue] == val][cat_y],
            mode= 'markers',
            name=str(val)
        )

        data.append(scatt)    

    layout = go.Layout(
        title='Scatter',
        title_x=0.5,
        xaxis=dict(title=cat_x),
        yaxis=dict(title=cat_y)
    )

    res = {'data': data, 'layout': layout}

    graphJSON = json.dumps(res, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

@app.route('/scatt_fn')
def scatt_fn():
    cat_x = request.args.get('cat_x')
    cat_y = request.args.get('cat_y')
    hue = request.args.get('hue')

    # WAJIB! default value ketika scatter pertama kali dipanggil
    if cat_x == None and cat_y == None and hue == None:
        cat_x = 'administrative'
        cat_y = 'informational'
        hue = 'revenue'

    # Dropdown menu
    list_x = [('administrative', 'Administrative'), ('administrative_duration', 'Administrative_Duration'), ('informational', 'Informational'), ('informational_duration', 'Informational_Duration'), ('productRelated', 'ProductRelated'), ('productRelated_duration', 'ProductRelated_Duration'), ('bouncerates', 'BounceRates'), ('exitrates', 'ExitRates'), ('pagevalues', 'PageValues')]
    list_y = [('administrative', 'Administrative'), ('administrative_duration', 'Administrative_Duration'), ('informational', 'Informational'), ('informational_duration', 'Informational_Duration'), ('productRelated', 'ProductRelated'), ('productRelated_duration', 'ProductRelated_Duration'), ('bouncerates', 'BounceRates'), ('exitrates', 'ExitRates'), ('pagevalues', 'PageValues')]
    list_hue = [('revenue', 'Revenue')]

    plot = scatter_plot(cat_x, cat_y, hue)

    return render_template(
        'scatter.html',
        plot=plot,
        focus_x=cat_x,
        focus_y=cat_y,
        focus_hue=hue,
        drop_x=list_x,
        drop_y=list_y,
        drop_hue=list_hue
    )

def pie_plot(hue = "revenue"):

    # dfol = pd.read_csv('./static/online_shop.csv')

    con = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'Welldone1+',
        database = 'olshop'
    )
    dfol = pd.read_sql('select * from online_shop', con)

    vcounts = dfol[hue].value_counts()

    labels = []
    values = []

    for item in vcounts.iteritems():
        labels.append(item[0])
        values.append(item[1])

    data = [go.Pie(labels=labels, values=values)]

    layout = go.Layout(title='Pie')

    res = {'data': data, 'layout': layout}

    graphJSON = json.dumps(res, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

@app.route('/pie_fn')
def pie_fn():
    hue = request.args.get('hue')
    #requests

    if hue == None:
        hue = 'revenue'
    
    list_hue = [('revenue', 'Revenue'), ('specialday', 'SpecialDay'), ('month', 'Month'), ('operatingsystems', 'OperatingSystems'), ('browser', 'Browser'), ('region', 'Region'), ('traffictype', 'TrafficType'), ('visitortype', 'VisitorType'), ('weekend', 'Weekend')]

    plot = pie_plot(hue)
    return render_template('pie.html', plot=plot, focus_hue=hue, drop_hue=list_hue)


@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        input = request.form
        
        SpecialDay = float(input['specialday'])
        if SpecialDay == 0.0:
            SpecialDayRes = '0.0'
        elif SpecialDay == 0.2:
            SpecialDayRes = '0.2'
        elif SpecialDay == 0.4:
            SpecialDayRes = '0.4'
        elif SpecialDay == 0.6:
            SpecialDayRes = '0.6'
        elif SpecialDay == 0.8:
            SpecialDayRes = '0.8'
        else:
            SpecialDayRes = '1'

        Month = float(input['month'])
        if Month == 2:
            MonthRes = 'February'
        elif Month == 5:
            MonthRes = 'March'
        elif Month == 6:
            MonthRes = 'May'
        elif Month == 4:
            MonthRes = 'June'
        elif Month == 3:
            MonthRes = 'July'
        elif Month == 0:
            MonthRes = 'August'
        elif Month == 9:
            MonthRes = 'September'
        elif Month == 8:
            MonthRes = 'October'
        elif Month == 7:
            MonthRes = 'November'
        elif Month == 1:
            MonthRes = 'December'

        Region = float(input['region'])
        if Region == 0:
            RegionRes = '1'
        elif Region == 1:
            RegionRes = '2'
        elif Region == 2:
            RegionRes = '3'
        elif Region == 3:
            RegionRes = '4'
        elif Region == 4:
            RegionRes = '5'
        elif Region == 5:
            RegionRes = '6'
        elif Region == 6:
            RegionRes = '7'
        elif Region == 7:
            RegionRes = '8'
        elif Region == 8:
            RegionRes = '9'

        TrafficType = float(input['traffictype'])
        if TrafficType == 0:
            TrafficTypeRes = '1'
        elif TrafficType == 1:
            TrafficTypeRes = '2'
        elif TrafficType == 2:
            TrafficTypeRes = '3'
        elif TrafficType == 3:
            TrafficTypeRes = '4'
        elif TrafficType == 4:
            TrafficTypeRes = '5'
        elif TrafficType == 5:
            TrafficTypeRes = '6'
        elif TrafficType == 6:
            TrafficTypeRes = '7'
        elif TrafficType == 7:
            TrafficTypeRes = '8'
        elif TrafficType == 8:
            TrafficTypeRes = '9'
        elif TrafficType == 9:
            TrafficTypeRes = '10'
        elif TrafficType == 10:
            TrafficTypeRes = '11'
        elif TrafficType == 11:
            TrafficTypeRes = '12'
        elif TrafficType == 12:
            TrafficTypeRes = '13'
        elif TrafficType == 13:
            TrafficTypeRes = '14'
        elif TrafficType == 14:
            TrafficTypeRes = '15'
        elif TrafficType == 15:
            TrafficTypeRes = '16'
        elif TrafficType == 16:
            TrafficTypeRes = '17'
        elif TrafficType == 17:
            TrafficTypeRes = '18'
        elif TrafficType == 18:
            TrafficTypeRes = '19'
        elif TrafficType == 19:
            TrafficTypeRes = '20'

        VisitorType = float(input['visitortype'])
        if VisitorType == 2:
            VisitorTypeRes = 'Returning_Visitor'
        elif VisitorType == 0:
            VisitorTypeRes = 'New_Visitor'
        elif VisitorType == 1:
            VisitorTypeRes = 'Other'

        Weekend = float(input['weekend'])
        if Weekend == 0:
            WeekendRes = 'False'
        elif Weekend == 1:
            WeekendRes = 'True'

        feature = [
            float(input['administrative']),
            float(input['informational']),
            float(input['productrelated']),
            float(input['exitrates']),
            float(input['pagevalues']),
            float(input['specialday']),
            float(input['month']),
            float(input['region']),
            float(input['traffictype']),
            float(input['visitortype']),
            float(input['weekend'])
        ]

    pred_proba = rfc.predict_proba([feature])
    rfc_pred_thres_custom = 0 if pred_proba[0][1] < 0.62 else 1
    pred = 'REVENUE' if rfc_pred_thres_custom == 1 else 'NO REVENUE'
    proba = pred_proba[0][0] if pred == 'NO REVENUE' else pred_proba[0][1]
    endresult = f"{round(proba*100,2)}% {pred}"

    # return render_template('result.html', data=input, prediction=endresult)
    return render_template('result.html', prediction=endresult, Administrative=input['administrative'], 
    Informational=input['informational'], ProductRelated=input['productrelated'], ExitRates=input['exitrates'],
    PageValues=input['pagevalues'], SpecialDay=SpecialDayRes, Month=MonthRes, Region=RegionRes, TrafficType=TrafficTypeRes,
    VisitorType=VisitorTypeRes, Weekend=WeekendRes)


@app.route("/data_main", methods=['GET'])
def data_main():
    con = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'Welldone1+',
        database = 'olshop'
    )
    c = con.cursor(buffered=True)
    query = 'select * from online_shop order by id desc limit 20'
    c.execute(query)
    res_data = c.fetchall()
    return render_template('data_index.html', onlineshop=res_data)


@app.route("/data_create", methods=['GET'])
def data_create():
    return render_template('data_create.html')


@app.route("/data_store", methods=['POST'])
def data_store():
    data = request.form
    con = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'Welldone1+',
        database = 'olshop'
    )
    c = con.cursor(buffered=True)
    value = OnlineshopFunction(data)
    x = 'insert into online_shop (administrative, administrative_duration, informational, informational_duration, productrelated, productrelated_duration, bouncerates, exitrates, pagevalues, specialday, month, operatingsystems, browser, region, traffictype, visitortype, weekend, revenue) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    y = (value.administrative, value.administrative_duration, value.informational, value.informational_duration, value.productrelated, value.productrelated_duration, value.bouncesrates, value.exitrates, value.pagevalues, value.specialday, value.month, value.operatingsystems, value.browser, value.region, value.traffictype, value.visitortype, value.weekend, value.revenue)
    c.execute(x,y)
    con.commit() # menjalankan sql nya agar data insertnya masuk
    return redirect(url_for('data_main'))


if __name__ == '__main__':
    rfc = joblib.load('rfc')
    app.run(debug=True, port=3838)