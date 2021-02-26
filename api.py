import markdown
from flask import Flask, request, jsonify
import os
import utils
import numpy as np

# Create an instance of Flask
app = Flask(__name__)

@app.route("/")
def index():
    """present some documentation"""

    # open the README file
    with open(os.path.dirname(app.root_path) + '/ML-model-API/README.md', 'r') as markdown_file:
        content = markdown_file.read()

        # convert to HTML
        return markdown.markdown(content)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['body']
    print(data)
    result = utils.predict(np.array(data).reshape(1,-1))

    return jsonify({"prediction": utils.get_label_name(result[0])})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
