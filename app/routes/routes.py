from gettext import find
from flask import Blueprint, render_template,request
import time
import json,urllib.request
import os
from operator import itemgetter
from datetime import datetime
import csv

import pandas as pd








global_scope = Blueprint("views", __name__)


@global_scope.route("/", methods=['GET'])
def home():
    """Landing page route."""

    parameters = {"title": "Diana's Project",
                  "description": "This is a simple page for diana"
                  }

    return render_template("home.html", **parameters)

@global_scope.route("/ranking", methods=['GET'])
def ranking():
    "Page for the ranking"
    titulo="Ranking 50M"
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'data', 'data.json')
    data = json.load(open(json_url))
    data["columnas"]=data["data"][0][:]
    data["data"]=data["data"][1:]
    competencias=[]
    for datos in data["data"]:
        for fmt in ('%M:%S:%f', '%M:%S'):
            try:
                if type(datos[3]==datetime.time):
                    datos[3]=datos[3]
                else:
                    datos[3]=datetime.strptime(datos[3], fmt).time()
            except ValueError:
                pass    
        competencias.append(datos[8])
    
    data["data"] = sorted(data["data"], key=itemgetter(8))
    competencias=list(dict.fromkeys(competencias))
    print(competencias)    
    
    
    parameters = {"title": "Ranking 50M",
                "description": "Here is the ranking",
                "titulo":titulo,
                "data":data,
                "competencias":competencias
                }
    return render_template("ranking.html", **parameters)

@global_scope.route("/ranking25", methods=['GET'])
def ranking25():
    "Page for the ranking of 25M"
    titulo="Ranking 25M"
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    csv_url = os.path.join(SITE_ROOT, 'data', 'Ranking50M.csv')
    with open(csv_url) as f:
        reader = csv.reader(f)
        data = list(reader)
    xlsx_file = os.path.join(SITE_ROOT, 'data', 'Ranking25M.xlsx')
    df=pd.read_excel(xlsx_file)
    df = df[["Event","Rk","Team","Date","Time","FinaPoints","Birth","Name","Gender"]]
    df['Date']= pd.to_datetime(df['Date']).dt.date
    df['Birth']= pd.to_datetime(df['Birth']).dt.date
    myList=df.values.tolist()
    print(myList)
    columnas=list(df.columns.values)
    
    parameters = {"title": "Ranking 25M",
                "description": "Here is the ranking",
                "titulo":titulo,
                "data":myList,
                "columnas":columnas
                }

    return render_template("ranking25.html", **parameters)

@global_scope.route("/ranking4",methods=["GET"])
def ranking4():
    url="http://localhost:7001/api/ranking"
    response=urllib.request.urlopen(url)
    data=response.read()
    dict=json.loads(data)
    print(type(dict["data"]))
    print(dict["data"])
    return render_template("ranking4.html",datos2=dict["data"])

@global_scope.route("/rankingGeneral",methods=["GET","POST"])
def rankingGeneral():
    if request.method=="GET":
        return render_template("rankingGeneral.html")