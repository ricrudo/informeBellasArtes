from flask_mail import Mail, Message

def sendTemporalPass(email, tempPass, app):
    mensaje = f'''
    Gracias por acceder al informe semestral de la Facultad de Bellas Artes de la Universidad del Atlántico

    Por favor, utilice esta contraseña para ingresar. 

    {tempPass}

    La contraseña es válida por 15 minutos.
    '''
    mail = Mail(app)
    try:
        msg = Message(
            subject="Constraseña temporal - Informe Bellas Artes",
            sender=app.config['MAIL_USERNAME'],
            recipients=[email],  # Lista de destinatarios
            body=mensaje
        )
        mail.send(msg)
        return "Correo enviado exitosamente."
    except Exception as e:
        return f"Error al enviar el correo: {e}"


def testEmail(app):
    return sendTemporalPass('ricardood@gmail.com', 'tempPass', app)

