from google.cloud import translate_v2 as translate
import os
import six

class Translator():
    def __init__(self):
        self.translate_client = translate.Client()
        self.recent_source = None
    
    def translate_to_english(self, text):

        if isinstance(text, six.binary_type):
          text = text.decode("utf-8")

        result = self.translate_client.translate(text, target_language="en", format_='text')
        self.recent_source = result["detectedSourceLanguage"]
        if "pt" in self.recent_source:
            self.recent_source == "pt-BR"
        return result["translatedText"]
    
    def translate_back(self, text):
        if isinstance(text, six.binary_type):
          text = text.decode("utf-8")

        result = self.translate_client.translate(text, target_language=self.recent_source, format_='text')
        return result["translatedText"]

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./paraphraseia-translate-key.json"