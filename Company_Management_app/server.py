import os
from flask import Flask
from flask_wtf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)

# Lee la clave de entorno; si no existe, falla al arrancar o genera una aleatoria
secret = os.getenv('FLASK_SECRET_KEY')
if not secret:
    raise RuntimeError("FLASK_SECRET_KEY no definida en el entorno")
app.secret_key = secret

app.permanent_session_lifetime = 99999999

app.config.update(
    SESSION_COOKIE_HTTPONLY=True,  # Impide acceso desde JavaScript
    SESSION_COOKIE_SECURE=True,    # Solo envía la cookie por HTTPS
    SESSION_COOKIE_SAMESITE='Lax'  # Protege contra CSRF "cross-site"
)
