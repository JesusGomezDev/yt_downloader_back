from flask import Flask
from flask import request
from pytube import YouTube

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/download", methods=['POST'])
def download():
    url = request.json['url']
    type = request.json['type']

    yt = YouTube(url)

    if type == 'video':
        file = yt.streams.get_highest_resolution()
        file.download('./downloads')
    elif type == 'audio':
        file = yt.streams.get_audio_only()
        file.download('./downloads')

    return 'Downloaded!'