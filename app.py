from flask import Flask, render_template_string, request, send_file
import yt_dlp
import os

app = Flask(__name__)

# সুন্দর ইন্টারফেসের জন্য HTML
HTML_CODE = """
<!DOCTYPE html>
<html>
<head>
    <title>Sakil Downloader</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: sans-serif; text-align: center; padding: 50px; background: #f0f2f5; }
        .box { background: white; padding: 30px; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); max-width: 400px; margin: auto; }
        input { width: 90%; padding: 12px; margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; }
        button { background: #ff0000; color: white; border: none; padding: 12px 20px; border-radius: 5px; cursor: pointer; width: 95%; }
    </style>
</head>
<body>
    <div class="box">
        <h2 style="color: #ff0000;">YouTube Downloader</h2>
        <form action="/download" method="get">
            <input type="text" name="url" placeholder="ভিডিও লিঙ্ক দিন..." required>
            <button type="submit">ডাউনলোড শুরু করুন</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_CODE)

@app.route('/download')
def download():
    url = request.args.get('url')
    if not url: return "No URL provided"
    
    output = "video.mp4"
    if os.path.exists(output): os.remove(output)
    
    ydl_opts = {'format': 'best', 'outtmpl': output}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    return send_file(output, as_attachment=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    
