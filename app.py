from flask import Flask, render_template, request, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        url = request.form["url"]  # Get the URL from the form input
        if url:
            # Pass the URL as an argument to the Python script
            try:
                subprocess.run(["python", "universal-downloader.py", url], check=True)
                message = "Audio downloaded successfully!"
            except subprocess.CalledProcessError:
                message = "Error occurred during downloading the audio."
            return render_template("index.html", message=message)
    return render_template("index.html", message="")

if __name__ == "__main__":
    app.run(debug=True)
