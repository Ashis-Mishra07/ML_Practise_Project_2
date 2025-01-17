from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    image_data = request.form['image_data']  # it is in the form of base 64 model

    response = jsonify(util.classify_image(image_data))  # the method will convert it into jasonify

    response.headers.add('Access-Control-Allow-Origin', '*')  

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()
    app.run(port=5000)