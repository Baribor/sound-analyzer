# import needed dependencies
from flask import Flask, render_template, request, redirect
import speech_recognition as sr
# initiate flask
app = Flask(__name__)
# render homepage as get and post from html and css files
@app.route("/", methods=["GET", "POST"])
def index():
    transcript = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")
        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key=None)
    return render_template('index.html', transcript=transcript)
if __name__ == "__main__":
    app.run(debug=True, threaded=True)

