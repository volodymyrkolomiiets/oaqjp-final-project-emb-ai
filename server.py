"""
server.py

This module contains a Flask application to detect emotions from
text input using the EmotionDetection package. It provides endpoints
to render a user interface and analyze emotions in user-provided text.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """
    The `index()` function returns the rendered template
    for the "index.html" file.
    :return: The function `index()` is returning the
    result of rendering the template "index.html".
    """
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detection():
    """
    The `emotion_detection` function analyzes text input
    for emotions and returns a formatted response
    with emotion scores and dominant emotion.
    :return: The function `emotion_detection()` returns 
    a formatted response containing emotion scores
    for the given text to analyze. If the dominant 
    emotion is not detected (i.e., `None`), it returns a
    message saying "Invalid text! Please try again!".
    """

    text_to_analyze = request.args.get("textToAnalyze", "")

    emotion_scores = emotion_detector(text_to_analyze)

    formatted_response = (
        f"For the given statement, the system response is 'anger': {emotion_scores['anger']}, "
        f"'disgust': {emotion_scores['disgust']}, 'fear': {emotion_scores['fear']}, "
        f"'joy': {emotion_scores['joy']} and 'sadness': {emotion_scores['sadness']}. "
        f"The dominant emotion is {emotion_scores['dominant_emotion']}."
    )
    if emotion_scores["dominant_emotion"] is None:
        return "Invalid text! Please try again!."

    return formatted_response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
