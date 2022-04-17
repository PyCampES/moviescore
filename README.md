# moviescore
Un server que habla con el bot de Telegram

# How to use?

Install virtualenv and dependecies.

```
python -m venv moviescore
source moviescore/bin/activate
pip install -r requirements.txt
```

Initial example usage can be found here:

```
python main.py
```

Bot responder usage:

You will need to export an environment variable with your Telegram bot
key:

```
export TELEGRAM_BOT_KEY={YOUR_KEY}
```

```
python my_bot.py
```