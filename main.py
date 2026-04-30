from flask import Flask, request, send_file, render_template
import yt_dlp
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")

        ydl_opts = {
            'format': 'best[ext=mp4]',
            'outtmpl': 'video.%(ext)s',
            'noplaylist': True,
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            file_path = "video.mp4"

            if not os.path.exists(file_path):
                return "Fehler: Datei nicht gefunden"

            return send_file(file_path, as_attachment=True)

        except Exception as e:
            return f"Fehler: {str(e)}"

    return render_template("index.html")


app.run(host="0.0.0.0", port=81)
