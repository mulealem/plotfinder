from flask import Flask, jsonify, request
from tidb import query_db
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/search', methods=['POST'])
@cross_origin(supports_credentials=True)
def query():
    data = request.get_json()
    query = data.get('query')
    docs_with_score = query_db(query)
    return jsonify(docs_with_score), 200

if __name__ == '__main__':
    app.run(debug=False)
