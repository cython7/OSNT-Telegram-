
# - @HAHAHA_DECOD
#2025-05-26
#ZAXOTEL MADE

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
print("   '01' Отправка анонимного письма.\n   '00' Выход.") 


def send_email(sender_email, sender_password, receiver_email, message):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = 'AnonTool Sender'
        msg.attach(MIMEText(message, 'plain'))
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print(f"Письмо успешно отправлено от {sender_email} на {receiver_email}!")
    except Exception as e:
        print(f"Ошибка при отправке письма от {sender_email} на {receiver_email}: {e}")

senders = {
    'anonymous854785@gmail.com': 'wmth dinz jiek nhfy'
}

def main():
    while True:
        command = input("   Введите команду: ")
        
        if command == "01":
            gmail = input('   Куда: ')
            receivers = [f'{gmail}']
            message = input('   Текст: ')
            
            for sender_email, sender_password in senders.items():
                for receiver_email in receivers:
                    send_email(sender_email, sender_password, receiver_email, message)
                    
        if command == "1":
            gmail = input('   Куда: ')
            receivers = [f'{gmail}']
            message = input('   Текст: ')
            
            for sender_email, sender_password in senders.items():
                for receiver_email in receivers:
                    send_email(sender_email, sender_password, receiver_email, message)
        
        elif command == "00":
            print("   Выход из программы...")
            os.system("python main.py")
            break
        
        else:
            print("   Некорректный ввод. Пожалуйста, введите '01' для начала или '00' для выхода.")

if __name__ == "__main__":
    main()