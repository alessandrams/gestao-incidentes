from random import randint
from time import strftime
from flask import Flask, render_template, flash, request
from flask.helpers import url_for
from werkzeug.utils import redirect
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import api

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'SjdnUends821Jsdlkvxh391ksdODnejdDw'

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    email = TextField('Email:', validators=[validators.required()])
    cif = TextField('CIF:', validators=[validators.required()])
    descricao = TextField('Descrição geral:', validators=[validators.required()])
    descricao1 = TextField('Descrição geral:', validators=[validators.required()])

@app.route("/", methods=['GET', 'POST'])

def hello():
    form = ReusableForm(request.form)

    if request.method == 'POST':
        name=request.form.get("name")
        email=request.form.get("email")
        cif=request.form.get("cif")
        descricao=request.form.get("descricao")
        descricao1=request.form.get("descricao1")

        api.print_parameters(name, email,cif,descricao, descricao1)
        # print(name)
        # print(email)
        # print(cif)
        # print(descricao)

        if form.validate():
            flash('Formulário enviado com sucesso.')
        else:
            flash('Todos os campos devem ser preenchidos')   
            return render_template('teste1.html', form=form) 
            
    return render_template('teste1.html', form=form)    
           

if __name__ == "__main__":
    app.run()

