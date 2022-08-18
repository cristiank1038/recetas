from flask_app import app

#Importando Controlador
from flask_app.controller import user_controller, recipes_controller

#Pasos a seguir:
#pipenv install flask pymysql
#pipenv shell
#python server.py -> python3, py o python

if __name__=="__main__":
    app.run(debug=True)

