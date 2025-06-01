from db import get_users_connection, hash_password
from flask import request, redirect, render_template, session
from server import app

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect('/companies')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_users_connection()
        user = conn.execute("SELECT * FROM users WHERE username = '"+ username +"' AND password = '"+hash_password(password)+"'").fetchone()
        conn.close()
        
        if user:
            app.config.update(
                SESSION_COOKIE_HTTPONLY=True, # Impide acceso desde JavaScript
                SESSION_COOKIE_SECURE=True, # Solo envía la cookie por HTTPS
                SESSION_COOKIE_SAMESITE='Lax' # Protege contra CSRF "cross-site request forgery"
            )
            app.config.update(
                SESSION_COOKIE_HTTPONLY=True, # Impide acceso desde JavaScript
                SESSION_COOKIE_SECURE=True, # Solo envía la cookie por HTTPS
                SESSION_COOKIE_SAMESITE='Lax' # Protege contra CSRF "cross-site"
            )
            app.config.update(
                SESSION_COOKIE_HTTPONLY=True, # Impide acceso desde JavaScript
                SESSION_COOKIE_SECURE=True, # Solo envía la cookie por HTTPS
                SESSION_COOKIE_SAMESITE='Lax' # Protege contra CSRF "cross-site"
            )

            return redirect('/companies')
        else:
            return render_template('auth/login.html', error="Invalid username or password")
    return render_template('auth/login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')
