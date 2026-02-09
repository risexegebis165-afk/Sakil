from flask import Flask, request, send_file
import yt_dlp
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "YouTube Downloader is Running!"

@app.route('/download')
def download():
    url = request.args.get('url')
    if not url:
        return "Please provide a URL", 400
    
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'video.mp4',
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    return send_file('video.mp4', as_attachment=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
  
