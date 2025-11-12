from colaciones import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    rut = db.Column(db.String(20), unique = True, nullable = False)

    def __init__(self, username, rut):
        self.username = username
        self.rut = rut

    def __repr__(self):
        return f"<User: {self.username} >"    
    

#Relacionar tablas
class Colaciones(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    dia = db.Column(db.String(100), nullable = False)
    fruta = db.Column(db.text)
    postre = db.Column(db.text)
    opcion1 = db.Column(db.text)
    opcion2 = db.Column(db.text)
    hipocalorico = db.Column(db.text)
    ensalada = db.Column(db.text)
    sopa = db.Column(db.text)
    state = db.Column(db.Boolean, default = False)

    def __init__(self, dia, fruta, postre, opcion1, opcion2, hipocalorico, ensalada, state = False):
        self.dia = dia
        self.fruta = fruta
        self.postre = postre
        self.opcion1 = opcion1
        self.opcion2 = opcion2
        self.hipocalorico = hipocalorico
        self.ensalada = ensalada
        self.state = state
        
    def __repr__(self):
        return f"<colaciones: {self.dia} >"