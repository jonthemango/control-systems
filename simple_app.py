from flask import Flask,render_template,flash, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FloatField
from wtforms.validators import DataRequired
from control import *
from control.matlab import * 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io
import base64
from scratch_pad import percent_overshoot, is_stable, get_poles, get_zeroes, plot_root_locus

app = Flask(__name__)
import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

class LoginForm(FlaskForm):
    kd = FloatField('kd', validators=[DataRequired()])
    kp = FloatField('kp', validators=[DataRequired()])
    submit = SubmitField('Run Results')

s = tf('s')
G = tf(1,[240,0,1400])

@app.route('/', methods=['GET', 'POST'])
def main():
    try:
        kp = float(request.args.get('kp'))
        kd = float(request.args.get('kd'))
    except:
        kp = kd = 1
    form = LoginForm()
    if form.validate_on_submit():
        kd = form.kd.data
        kp = form.kp.data
        return redirect(url_for('main', kp=kp, kd=kd))
    
    form.kd.data = kd
    form.kp.data = kp
    C = kp + kd*s 
    closed_loop = feedback(series(C,G),1)
    sys_step_info = step_info(closed_loop)
    sys_stability = is_stable(closed_loop)
    poles = get_poles(closed_loop)
    #sys_damp = damp(closed_loop)
    x,y = step_response(closed_loop)

    
    fig = Figure()
    ax = fig.subplots()
    ax.plot(x,y)
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    buf.close()

    

    return render_template('ui.html', title='Sign In', kd=kd, kp=kp, form=form, G=G, C=C, sys_stability=sys_stability, poles=poles, sys_step_info=sys_step_info, closed_loop=closed_loop, img=data)

if __name__ == '__main__':
    app.run()