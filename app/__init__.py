from app.app import create_app
from flask import jsonify

app = create_app()


@app.route('/search', methods=['POST'])
def search():
    # req = request.get_json()
    # get_pertinent_doc_by_key(req['key'])

    return jsonify(message='ok')
