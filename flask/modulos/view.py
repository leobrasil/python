from flask import Blueprint, jsonify, render_template

view = Blueprint('view', __name__, url_prefix='/view')

@view.route('/')
def modelo_view():
    return render_template('index.html')

@view.login('/login')
def render_login():
    render_template('login.html')

