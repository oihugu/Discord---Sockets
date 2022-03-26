from email import message
from APP import model, control
import flask
from flask import Flask
import threading
import os



if __name__ == '__main__':
    message_list = []
    threading.Thread(target=control.chat_sockets.server.run).start()
    threading.Thread(target=control.discord_bot.run, args=(message_list,)).start()

    app = Flask(__name__)

    id_list = []

    os.environ['FLASK_APP'] = 'main.py'
    os.environ['FLASK_ENV'] = 'development'
    os.environ['APP_URL'] = 'http://localhost:5000'

    @app.route("/")
    def hello_world():
        messages = model.message.get_message_list()
        return flask.render_template('main.html', messages=messages)

    @app.route("/generate_id")
    def generate_id():
        return control.generate_id(id_list)


    app.run()