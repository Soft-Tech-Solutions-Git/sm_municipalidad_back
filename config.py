import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://usuario:contraseña@host/nombre_base_datos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
