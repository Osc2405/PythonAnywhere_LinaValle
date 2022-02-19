from gettext import find
from webbrowser import Chrome
from flask import Blueprint, render_template
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

##driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path='C:/Users/orose/Desktop/Diana_Proyecto/Intento1/app/routes/drivers/chromedriver.exe')



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
    driver.get("https://www.colombiaacuatica.com/backtun/torneos/fecna/sw/rankingfecna01.php")
    titulo=driver.title
    rows=len(driver.find_elements_by_class_name("row"))
    time.sleep(5)
    columns=len(driver.find_elements_by_xpath("(//div[contains(@class, 'row')])"))
    time.sleep(5)
    fila=[]
    for i in range (2,columns-2):
        for j in range (1,5):
            dato= driver.find_element_by_xpath("/html/body/div["+str(i)+"]/div["+str(j)+"]").text
            fila.append(dato)
    contenido=fila
    size=len(contenido)
    driver.quit()

    chunked_list = list()
    chunk_size = 4
    for i in range(0, len(contenido), chunk_size):
        chunked_list.append(contenido[i:i+chunk_size])
    print(chunked_list)
    parameters = {"title": "Ranking",
                "description": "Here is the ranking",
                "titulo":titulo,
                "columnas":columns,
                "filas":rows,
                "contenido":chunked_list,
                "size":size
                }
    return render_template("ranking.html", **parameters)