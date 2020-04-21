import requests as rq
import datetime as dt
import json
from flask import render_template,redirect,request
from app import app
from app.models import Data

@app.route('/',methods=['GET','POST'])
def index():
    if request.method =='GET':
        recomandari={
        'Piatra Neamt' : 670889,
        'Iasi' : 675810,
        "Bucuresti" : 683506,
        'Atena' : 264371,
        'Londra': 2643741
        }
        return render_template('home.html',rec=recomandari)
    else:
        cod=request.form['cod']
        key='df38acd7030338d18ceb272c83e62dcc'
        r=rq.get('https://api.openweathermap.org/data/2.5/forecast?id='+cod+'&APPID='+key)

        if r.status_code == 200:

            fisier=r.json()

            rasarit= dt.datetime.fromtimestamp(fisier['city']['sunrise'])
            rasarit=rasarit.strftime('%H:%M:%S')
            apus= dt.datetime.fromtimestamp(fisier['city']['sunset'])
            apus=apus.strftime('%H:%M:%S')

            date={
            'Oras' : fisier['city']['name'],
            'Temperatura':round(fisier['list'][0]['main']['temp']-273.15,2),
            'Temp. Resimtita' : round(fisier['list'][0]['main']['feels_like']-273.15,2),
            'Temperatura minima' : round(fisier['list'][0]['main']['temp_min']-273.15,2),
            'Temperatura maxima' : round(fisier['list'][0]['main']['temp_max']-273.15,2),
            'Rasarit' : rasarit,
            'Apus' : apus,
            'Situatie' : fisier['list'][0]['weather'][0]['main'],
            'Descriere situatie' : fisier['list'][0]['weather'][0]['description'],
            }
            return render_template('cautat.html',date=date)
        else:
             return """Ceva a mers prost,incearca din nou.
             <a href='/'>Pagina de start</a>
             """

@app.route('/coduri',methods=['GET','POST'])
def coduri():
    if request.method == 'GET':
        return render_template('cautarecod.html')

    else:
        city=request.form['oras']
        search='%{}%'.format(city)
        date = Data.query.filter(Data.nume.like(search)).all()
        if date:
            return render_template('orasgasit.html',date=date)
        else:
            return render_template('orasgresit.html')
    return file
