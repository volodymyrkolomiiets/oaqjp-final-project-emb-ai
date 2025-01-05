import requests
import json

def extract_emotion(obj, emotion):
    return obj["emotionPredictions"][0]["emotion"][emotion]

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    my_object = { "raw_document": { "text": text_to_analyse } }
    res = requests.post(url, json=my_object, headers=headers).text

    d_obj = json.loads(res)

    dominant_emotion = max(d_obj["emotionPredictions"][0]["emotion"], key=d_obj["emotionPredictions"][0]["emotion"].get)

    res_obj = {
        "anger": extract_emotion(d_obj, "anger"),
        "disgust": extract_emotion(d_obj, "disgust"),
        "fear": extract_emotion(d_obj, "fear"),
        "joy": extract_emotion(d_obj, "joy"),
        "sadness": extract_emotion(d_obj, "sadness"),
        "dominant_emotion":dominant_emotion
    }


    return res_obj