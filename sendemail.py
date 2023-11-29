import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText

# Informações da conta de email de envio
email_from = "vitormcamargo60@gmail.com"
password = "kvjb dzto msrs tghj"

# Informações do servidor SMTP (Gmail neste exemplo)
smtp_servidor = "smtp.gmail.com"
smtp_porta = 587

# Recebe os dados do formulário HTML
def sendemail(emailTo, code):
    body = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                color: #000000;
                background-color: #FFFFFF;
            }}
            h1 {{
                color: #000000;
            }}
        </style>
    </head>
    <body>
        <h1 style="font-size: 20px; color:green;" >PyStudy - Verify Code</h1>
        <p style="font-size: 20px; color:black;" >{code}</p>
    </body>
    </html>
    """
# Configura o email a ser enviado
    msg = EmailMessage()
    msg.set_content(body, subtype='html')

# Configura as informações do email (Remetente, Destinatário, Assunto)
    msg["From"] = email_from
    msg["To"] = emailTo
    msg["Subject"] = "PyStudy - Verify Code"

# Conecta-se ao servidor SMTP e envia o email
    try:
        servidor = smtplib.SMTP(smtp_servidor, smtp_porta)
        servidor.starttls()
        servidor.login(email_from, password)
        servidor.send_message(msg)
        servidor.quit()
    except Exception as e:
        print(f"Error {e}")