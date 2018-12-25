#!/usr/bin/env python3
#####################################################
#                   Ali Alohali                     #
#                    alioh.com                      #
#                    Building8                      #
#           Simple Property Management System       #
#####################################################


from flask import Flask, g, redirect, url_for, render_template,\
             flash, request, abort
from flask_oidc import OpenIDConnect
from okta import UsersClient
from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Resident, Bill, Property
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import InputRequired
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

#   Database
engine = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
environ["SECRET_KEY"] = 'emptyfornow'

#   Routes
@app.route('/')
def index():
    properties = session.query(Property).all()
    return render_template('index.html', properties=properties)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)