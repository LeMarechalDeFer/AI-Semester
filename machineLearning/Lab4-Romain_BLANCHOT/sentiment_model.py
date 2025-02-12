from label_studio_ml.model import LabelStudioMLBase
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class SentimentModel(LabelStudioMLBase):
    def __init__(self, **kwargs):
        super(SentimentModel, self).__init__(**kwargs)
        self.analyzer = SentimentIntensityAnalyzer()
    
    def predict(self, tasks, **kwargs):
        predictions = []
        for task in tasks:
            text = task['data']['OriginalTweet']
            score = self.analyzer.polarity_scores(text)['compound']

            if score >= 0.05:
                label = "Positive"
            elif score <= -0.05:
                label = "Negative"
            else:
                label = "Neutral"

            predictions.append({
                "result": [{
                    "value": {"choices": [label]},
                    "from_name": "sentiment",
                    "to_name": "text",
                    "type": "choices"
                }]
            })
        return predictions
