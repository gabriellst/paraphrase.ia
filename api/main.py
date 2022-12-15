from flask import Flask, request
from flask_cors import CORS
from paraphraser import Paraphraser 
import json

paraphraser = Paraphraser()
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def check_request_body():
    if request.data:
        body = dict(json.loads(request.data))
        text = body['text']
        
        print("Request body: ", body)
        print("Text: ", text)

        paraphrases = paraphraser.paraphraseia(text)
        return json.dumps({"data": paraphrases})
    else:
        return "Request body does not exist."

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
