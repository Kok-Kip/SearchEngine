from app.app import create_app
from flask import jsonify

app = create_app()

# DO NOT move this line unless you know what you are doing
from app.biz.doc_rank import get_one


@app.route('/search', methods=['POST'])
def search():
    # req = request.get_json()
    x = get_one()
    print('get one:', x)
    # get_pertinent_doc_by_key(req['key'])

    return jsonify(message='ok')
