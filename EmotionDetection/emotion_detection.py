"""
This module provides a utility to detect emotions in text using Watson NLP.
It includes functions to extract individual emotion scores and determine the dominant emotion.
"""
import json
import requests


def extract_emotion(obj, emotion):
    """
    Extracts the specified emotion score from the Watson NLP response.

    Args:
        obj (dict): The response object from the Watson NLP API.
        emotion (str): The emotion to extract (e.g., 'anger', 'joy').

    Returns:
        float: The score of the specified emotion.
    """
    return obj["emotionPredictions"][0]["emotion"][emotion]

def emotion_detector(text_to_analyse):
    """
    Analyzes text to detect emotions using Watson NLP.

    Args:
        text_to_analyse (str): The text to be analyzed for emotions.

    Returns:
        dict: A dictionary containing scores for each emotion (anger, disgust, fear, joy, sadness)
              and the dominant emotion. If the API call fails, all values are set to None.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson."\
    + "runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    my_object = { "raw_document": { "text": text_to_analyse } }
    res = requests.post(url, json=my_object, headers=headers)

    d_obj = json.loads(res.text)

    if res.status_code == 200:
        dominant_emotion = max(d_obj["emotionPredictions"][0]["emotion"],
                                key=d_obj["emotionPredictions"][0]["emotion"].get)
        res_obj = {
            "anger": extract_emotion(d_obj, "anger"),
            "disgust": extract_emotion(d_obj, "disgust"),
            "fear": extract_emotion(d_obj, "fear"),
            "joy": extract_emotion(d_obj, "joy"),
            "sadness": extract_emotion(d_obj, "sadness"),
            "dominant_emotion": dominant_emotion
        }

    elif res.status_code == 400:
        res_obj = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    return res_obj
