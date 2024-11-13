from flask import Blueprint, render_template, request, session, redirect, url_for

bp = Blueprint('auth', __name__, url_prefix='/')

@bp.route("/", methods=['GET', 'POST'])
def login():
    '''
    Punto de entrada de la app
    '''
    if request.method == 'GET':
        #if 'email' in session:
        #    if users_credential.check_user(DB_engine, name_db, session['email'], session['passwd']):
        #        return render_template('initial_menu.html')
        return render_template('login.html')
    elif request.method == 'POST':
        return render_template('initial_menu.html')
        email = request.form['email']
        passwd = request.form['passwd']
        #if users_credential.check_user(DB_engine, name_db, email, passwd):
        #    session['email'] = email
        #    session['passwd'] = passwd
        #    return render_template('initial_menu.html')
        return render_template('login.html')


@bp.route("/logout")
def logout():
    session.pop('email', None)
    session.pop('passwd', None)
    return redirect(url_for('auth.login'))

@bp.get("/recovery_password")
def recovery_psswd_post():
    return "Eyyy! cule güeva que perdiste la contraseña. desde el bp"
