from flask import Flask, render_template, request
from NumerologiaNome import NumNome
from NumerologiaAniversario import NumData
from tarot import Arcano
import smtplib

app = Flask(__name__)

def send_email(destinatario, msg):

    email = "qael12345@gmail.com"
    senha = "@Aa32496649"

    server = smtplib.SMTP('smtp.gmail.com', 587) # Connect to the server
    server.starttls() # Use TLS
    server.login(email, senha) # Login to the email server
    server.sendmail(email, destinatario , msg) # Send the email
    server.quit() # Logout of the email server

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/contato', methods=['POST', 'GET'])
def contato():

    if request.method == 'POST':

        nome = request.form.get('name')
        email = request.form.get('email')
        numero = request.form.get('numero')
        assunto = request.form.get('assunto')
        mensagem = request.form.get('mensagem')

        destinatario = 'qael12345@gmail.com' # Who you are sending the message to
        message = 'CONTATO SITE\nNome: {}\nEmail: {}\nNumero: {}\nAssunto: {}\nMensagem: {}\n\n\n'.format(nome,email,numero,assunto,mensagem) # The message in the email

        x = send_email(destinatario, message)

        return render_template("contact-usOK.html")

    return render_template("contact-us.html")

@app.route('/numerologia', methods=['POST', 'GET'])
def numerologia():

    if request.method == 'POST':

        resultNome = []
        resultData = []
        nome = ""
        data = ""

        try:
            nome = request.form.get('name')
            if nome:
                n = NumNome(nome)
                resultNome = n.runNome(nome)

            data = request.form.get('date')
            if data:
                d = NumData(data)
                resultData = d.runData(data)

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
        nome = request.form.get('name')
        if nome:
            try:
                n = Arcano(nome)
                result = n.runNome(nome)
                return render_template('resultTarot/tarot{}.html'.format(result))

            except Exception as e:
                pass

    return render_template("arcano.html")

@app.route('/temperamentos')
def temperamentos():
    return render_template('temperamentos.html')

@app.route('/tarot')
def tarot():
    return render_template('tarot.html')

@app.route('/wallpapers')
def wallpapers():
    return render_template('wallpapers.html')

@app.route('/wallpapers-cel')
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

@app.route('/totem_cordeiro', methods=['POST', 'GET'])
def totem_cordeiro():
    return render_template('totens/totem_cordeiro.html')

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



if __name__ == '__main__':

    app.run(debug = True, port = 3044)
