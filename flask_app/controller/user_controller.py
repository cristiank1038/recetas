
from flask import render_template, redirect, session, request, flash     #importaciones de módulos de flask
from flask_app import app

#Importando el Modelo de User
from flask_app.models.users import User

#Importamos el modelo de Recetas
from flask_app.models.recipes import Recipe

#Importando BCrypt (encriptar)
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app) #inicializando instancia de Bcrypt

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods = ['post'])
def register():
    if not User.valida_usuario(request.form):
        return redirect('/')

    pwd = bcrypt.generate_password_hash(request.form['password']) #Me encripta el password

    formulario = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pwd
    }

    id = User.save(formulario) #Guardando a mi usuario y recibo el ID del nuevo registro

    session['usuario_id'] = id

    return redirect('/dashboard')

@app.route('/login', methods=['post'])
def login():
    user = User.get_by_email(request.form)
    if not user:
        flash("E-mail no encontrado", 'login')
        return redirect('/')

    #Comparando la contraseña encriptada con la contraseña del LOGIN
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Password incorrect", 'login')
        return redirect('/')

    session['usuario_id'] = user.id

    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'usuario_id' not in session:
        return redirect('/')

    formulario = {
        "id": session['usuario_id']
    }
    user = User.get_by_id(formulario)  # esto es para obtener el nmbre de la persona
    
    recipes = Recipe.get_all() #Recibimos lista de recetas

    return render_template('dashboard.html', user=user, recipes=recipes)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


