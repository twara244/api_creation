from flask import Flask, jsonify, request
import os

app = Flask(__name__)

API_KEY = os.environ.get("API_KEY")

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/check',methods=['GET'])
def check_query():
      
    user_api_key = request.headers.get('X-API-Key')  # Check the API key from the request header
    if user_api_key is None or user_api_key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401

    n= request.args.get('n',type=int)
    word=request.args.get('word',type=str)

    if n is None or word is None:
        return jsonify({"error": "Invalid input"}), 400
    
    length = len(word)
    result = {
            'number': n,
            'number_check': "even" if n % 2 == 0 else "odd",
            'word': word,
            'length_of_word': length
            }
    return jsonify(result)


if __name__=="__main__":
    app.run(debug=True)
