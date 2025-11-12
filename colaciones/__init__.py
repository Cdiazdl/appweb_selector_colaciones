from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)

    #Aca van las configuraciones
    app.config.from_mapping(
        DEBUG = True,
        SECRETE_KEY = "contrasena",
        SQLALCHEMY_DATABASE_URI = "sqlite:///selector_colaciones.db"
    )

    db.init_app(app)
    
    #Blueprint ayuda en las vistas, separandolas 
    from . import colaciones
    app.register_blueprint(colaciones.bp)
    from . import auth
    app.register_blueprint(auth.bp)

    @app.route("/")
    def index():
        return render_template("index.html")
    
    with app.app_context():
        db.create_all()
    

    return app