import requests

URL = 'https://api.telegram.org/'
TOKEN = 'bot5322008217:AAFJKos4mWaZ6ozlkMSu2ebyo9rZ_8SpUK8'
CHANNEL_ID = '-1001605748380'

class TelegramSender:

    def __init__(self):
        pass

    def send_message(self, message):
        request = URL + TOKEN + '/sendMessage'
        data = {
            'chat_id': CHANNEL_ID,
            'text': message
        }
        response = requests.post(request, data=data)
        return response.status_code
    
    def send_photo(self, photo_path, caption):
        request = URL + TOKEN + '/sendPhoto'
        data = {
            'chat_id': CHANNEL_ID,
            'caption': caption
        }
        files = {
            'photo': (open(photo_path, 'rb'))
        }
        response = requests.post(request, data=data, files=files)
        return response.status_code

    def caption_builder(self, comic):
        text = None
        text = '📔 | {0}\n\n📆 | {1}\n💬 | 🇺🇸'.format(
            comic.issue, 
            comic.year)
        return text