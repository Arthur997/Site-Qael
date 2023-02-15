from flask import Flask, render_template, request, redirect, url_for
from NumerologiaNome import NumNomeComum, NumNomeBatismo
from NumerologiaAniversario import NumData
from tarot import Arcano
import os
# from flask_sqlalchemy import SQLAlchemy
# import bcrypt

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template("index.html")

# # URL format for PostgreSQL: 'postgresql://username:password@host:port/database'
# # This should be updated with the appropriate values for your PostgreSQL server
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@host:port/database'

# db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     password_hash = db.Column(db.String(120), nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     phone_number = db.Column(db.String(20), unique=True, nullable=False)
#     full_name = db.Column(db.String(120), nullable=False)
#     birth_date = db.Column(db.Date, nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.username

# @app.route('/', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']

#         # Check if the user exists
#         user = User.query.filter_by(username=username).first()
#         if user is None:
#             return 'Invalid username'

#         # Check if the password is correct
#         if bcrypt.checkpw(password.encode('utf-8'), user.password_hash.encode('utf-8')):
#             # Login successful
#             return 'Login successful'
#         else:
#             return 'Invalid password'
#     else:
#         return '''
#             <form method="post">
#                 <input type="text" name="username" placeholder="Username">
#                 <input type="password" name="password" placeholder="Password">
#                 <input type="submit" value="Login">
#             </form>
#             <form method="post" action="register">
#                 <input type="text" name="username" placeholder="Username">
#                 <input type="password" name="password" placeholder="Password">
#                 <input type="email" name="email" placeholder="Email">
#                 <input type="text" name="phone_number" placeholder="Phone number">
#                 <input type="text" name="full_name" placeholder="Full name">
#                 <input type="date" name="birth_date" placeholder="Birth date">
#                 <input type="submit" value="Create">
#             </form>
#         '''

# @app.route('/register', methods=['POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         email = request.form['email']
#         phone_number = request.form['phone_number']
#         full_name = request.form['full_name']
#         birth_date = request.form['birth_date']

#         # Hash the password
#         password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
#         # Create a new user
#         user = User(username=username, password_hash=password, email=email, phone_number=phone_number, full_name=full_name, birth_date=birth_date)
#         db.session.add(user)
#         db.session.commit()
        
#         return 'User created'
#     else:
#         return '''
#             <form method="post">
#                 <input type="text" name="username" placeholder="Username">
#                 <input type="password" name="password" placeholder="Password">
#                 <input type="email" name="email" placeholder="Email">
#                 <input type="text" name="phone_number" placeholder="Phone number">
#                 <input type="text" name="full_name" placeholder="Full name">
#                 <input type="date" name="birth_date" placeholder="Birth date">
#                 <input type="submit" value="Create">
#             </form>
#         '''

@app.route('/numerologia', methods=['POST', 'GET'])
def numerologia():

    if request.method == 'POST':

        resultNome = []
        resultData = []
        nome = ""
        data = ""

        try:
            #check_box determina se o nome é comum ou de batismo
            check_box = request.form.get('formCheck-1')
            nome = request.form.get('name')
            
            if nome and check_box:
                n = NumNomeBatismo(nome)
                resultNome = n.runNomeBatismo()
            
            elif nome:
                n = NumNomeComum(nome)
                resultNome = n.runNomeComum()

            data = request.form.get('date')
            if data:
                d = NumData(data)
                resultData = d.runData()

            return render_template('resultNumerologia.html',resultNome=resultNome,
                                                            resultData=resultData,
                                                            nome=nome,
                                                            data=data)

        except Exception as e:
            pass



    return render_template("numerologia.html")

@app.route('/arcano', methods=['POST', 'GET'])
def arcanoNome():

    if request.method == 'POST':
        #check_box determina se o nome é comum ou de batismo
        check_box = request.form.get('formCheck-1')
        nome = request.form.get('name')
        data = request.form.get('date') 
        
        try:              
            if nome and check_box and data:
                d = NumData(data)
                data = d.runData()
                destino = data['TOTAL']
                n = Arcano(nome, destino)
                result = n.runArcano()
                return render_template('resultTarot/tarot{}.html'.format(result))
            
            elif nome:
                n = Arcano(nome)
                result = n.runArcano()
                return render_template('resultTarot/tarot{}.html'.format(result))

        except Exception as e:
            pass

    return render_template("arcano.html")

def get_links_artigos():
    caminho =   {"Deus": "/artigos/deus", 
                "Yahoa": "/artigos/yashoa",
                "Famulus": "/artigos/famulus",
                "Os Filhos de Qæl": "/sobre_nos"}
    
    nome_pag = ["Deus",
                "Yahoa",
                "Famulus",
                "Os Filhos de Qæl"] 
    
    return caminho

@app.route('/artigos/deus', methods=['POST', 'GET'])
def artigos_deus():
    caminho = get_links_artigos()
    return render_template('artigos-deus.html', caminho = caminho)

@app.route('/artigos/famulus', methods=['POST', 'GET'])
def artigos_famulus():
    caminho = get_links_artigos()    
    return render_template('artigos-famulus.html', caminho = caminho)

@app.route('/artigos/yashoa', methods=['POST', 'GET'])
def artigos_yashoa():
    caminho = get_links_artigos() 
    return render_template('artigos-yashoa.html', caminho = caminho)

@app.route('/sobre_nos', methods=['POST', 'GET'])
def sobre_nos():
    caminho = get_links_artigos() 
    return render_template('sobre_nos.html', caminho = caminho)

@app.route('/temperamentos', methods=['POST', 'GET'])
def temperamentos():
    return render_template('temperamentos.html')

@app.route('/tarot', methods=['POST', 'GET'])
def tarot():
    return render_template('tarot.html')

@app.route('/wallpapers', methods=['POST', 'GET'])
def wallpapers():
    return render_template('wallpapers.html')

@app.route('/wallpapers-cel', methods=['POST', 'GET'])
def wallpapers_cel():
    return render_template('wallpaper-cel.html')

@app.route('/totem', methods=['POST', 'GET'])
def totem():
    return render_template('totem.html')

@app.route('/totem_abelha', methods=['POST', 'GET'])
def totem_abelha():
    return render_template('totens/totem_abelha.html')

@app.route('/totem_aguia', methods=['POST', 'GET'])
def totem_aguia():
    return render_template('totens/totem_aguia.html')

@app.route('/totem_beijaflor', methods=['POST', 'GET'])
def totem_beijaflor():
    return render_template('totens/totem_beijaflor.html')

@app.route('/totem_borboleta', methods=['POST', 'GET'])
def totem_borboleta():
    return render_template('totens/totem_borboleta.html')

@app.route('/totem_cachorro', methods=['POST', 'GET'])
def totem_cachorro():
    return render_template('totens/totem_cachorro.html')

@app.route('/totem_cavalo', methods=['POST', 'GET'])
def totem_cavalo():
    return render_template('totens/totem_cavalo.html')

@app.route('/totem_cervo', methods=['POST', 'GET'])
def totem_cervo():
    return render_template('totens/totem_cervo.html')

@app.route('/totem_chimpanze', methods=['POST', 'GET'])
def totem_chimpanze():
    return render_template('totens/totem_chimpanze.html')

@app.route('/totem_cordeiro', methods=['POST', 'GET'])
def totem_cordeiro():
    return render_template('totens/totem_cordeiro.html')

@app.route('/totem_coelho', methods=['POST', 'GET'])
def totem_coelho():
    return render_template('totens/totem_coelho.html')

@app.route('/totem_coruja', methods=['POST', 'GET'])
def totem_coruja():
    return render_template('totens/totem_coruja.html')

@app.route('/totem_elefante', methods=['POST', 'GET'])
def totem_elefante():
    return render_template('totens/totem_elefante.html')

@app.route('/totem_gato', methods=['POST', 'GET'])
def totem_gato():
    return render_template('totens/totem_gato.html')

@app.route('/totem_golfinho', methods=['POST', 'GET'])
def totem_golfinho():
    return render_template('totens/totem_golfinho.html')

@app.route('/totem_jaguar', methods=['POST', 'GET'])
def totem_jaguar():
    return render_template('totens/totem_jaguar.html')

@app.route('/totem_libelula', methods=['POST', 'GET'])
def totem_libelula():
    return render_template('totens/totem_libelula.html')

@app.route('/totem_lobo', methods=['POST', 'GET'])
def totem_lobo():
    return render_template('totens/totem_lobo.html')

@app.route('/totem_mandril', methods=['POST', 'GET'])
def totem_mandril():
    return render_template('totens/totem_mandril.html')

@app.route('/totem_qrub', methods=['POST', 'GET'])
def totem_qrub():
    return render_template('totens/totem_qrub.html')

@app.route('/totem_serpente', methods=['POST', 'GET'])
def totem_serpente():
    return render_template('totens/totem_serpente.html')

@app.route('/totem_tigre', methods=['POST', 'GET'])
def totem_tigre():
    return render_template('totens/totem_tigre.html')

@app.route('/totem_urso', methods=['POST', 'GET'])
def totem_urso():
    return render_template('totens/totem_urso.html')

@app.route('/downloads', methods=['POST', 'GET'])
def downloads():
    return render_template('downloads.html')


if __name__ == '__main__':

    app.run(debug = True, port = 3044)
