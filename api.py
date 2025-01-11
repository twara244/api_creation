from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/check',methods=['GET'])
def check_query():
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