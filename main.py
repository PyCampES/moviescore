from Telegram.Sender.Infrastructure.TelegramSender import TelegramSender

def main():
    my_sender = TelegramSender()
    response = my_sender.send_message("hola")
    assert response == 200

if __name__=="__main__":
    main()
