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
                #data esta no formato yyyy-mm-dd, isso inverte a strig    
                data = data[8:]+data[4:8]+data[0:4] 
            
                d = NumData(data)
                resultData = d.runData(data) 
 
            return render_template('resultNumerologia.html',resultNome=resultNome,
                                                            resultData=resultData,
                                                            nome=nome,
                                                            data=data)
        
        except Exception as e:
            pass

        
     
    return render_template("numerologia.html")

@app.route('/temperamentos')
def temperamentos():
    return render_template('temperamentos.html')


@app.route('/tarot')
def tarot():
    return render_template('tarot.html')


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


    return render_template('arcano.html')
 

@app.route('/wallpapers')
def wallpapers():
    return render_template('wallpapers.html')


if __name__ == '__main__':

    app.run(debug = True, port = 3044)
 