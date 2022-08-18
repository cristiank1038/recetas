from flask import Flask

app= Flask(__name__)

#vamos a generar la secret key
app.secret_key = "Esta es mi llave super secreta"
