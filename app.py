from flask import Flask

app = Flask(__name__)
app.config.from_object('settings')

@app.route('/search', methods=['POST'])
def search():
    req = request.get_json()

    # get_pertinent_doc_by_key(req['key'])

    return jsonify(message='ok')