from flask import Flask
#conexion con la base de datos
from flask_sqlalchemy from SQLAlchemy

app=Flask(__name__)
app.config['SECRET_KEY']='Esto es un secreto'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database/video.db'

db=SQLAlchemy(app)