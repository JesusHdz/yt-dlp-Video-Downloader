from flask import Flask, render_template, request, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        url = request.form["url"]  # Get the URL from the form input
        download_option = request.form.get("download_option")  # Get the download option (audio or video+audio)

        if url:
            try:
                if download_option == "audio":
                    # Call the Python script to download audio only
                    subprocess.run(["python", "downloader.py", url, "audio"], check=True)
                    message = "Audio downloaded successfully!"
                elif download_option == "video_audio":
                    # Call the Python script to download both video and audio
                    subprocess.run(["python", "downloader.py", url, "video_audio"], check=True)
                    message = "Video and audio downloaded successfully!"
                else:
                    message = "Please select a valid download option."
            except subprocess.CalledProcessError:
                message = "Error occurred during downloading."

            return render_template("index.html", message=message)

    return render_template("index.html", message="")

if __name__ == "__main__":
    app.run(debug=True)
