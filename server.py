from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detection():

    text_to_analyze = request.args.get("textToAnalyze", "")

    emotion_scores = emotion_detector(text_to_analyze)

    formatted_response = (
        f"For the given statement, the system response is 'anger': {emotion_scores['anger']}, "
        f"'disgust': {emotion_scores['disgust']}, 'fear': {emotion_scores['fear']}, "
        f"'joy': {emotion_scores['joy']} and 'sadness': {emotion_scores['sadness']}. "
        f"The dominant emotion is {emotion_scores['dominant_emotion']}."
    )
    if emotion_scores["dominant_emotion"] is None:
        return "Invalid input! Try again."

    return formatted_response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
