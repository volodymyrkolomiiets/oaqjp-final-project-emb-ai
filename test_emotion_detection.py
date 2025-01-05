from EmotionDetection.emotion_detection import emotion_detector
import unittest



class TestEmotionDetector(unittest.TestCase):

    def test_emotion_detector(self):

        emotion = emotion_detector("I am glad this happened")["dominant_emotion"]
        self.assertEqual(emotion, "joy")

        emotion = emotion_detector("I am really mad about this")["dominant_emotion"]
        self.assertEqual(emotion, "anger")

        emotion = emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"]
        self.assertEqual(emotion, "disgust")

        emotion = emotion_detector("I am so sad about this")["dominant_emotion"]
        self.assertEqual(emotion, "sadness")

        emotion = emotion_detector("I am really afraid that this will happen")["dominant_emotion"]
        self.assertEqual(emotion, "fear")

if __name__ == "__main__":
    unittest.main()


