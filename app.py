from flask import Flask, request, jsonify
from cassandra.cluster import Cluster

cluster = Cluster(['cassandra'])
session = cluster.connect()
app = Flask(__name__)

# Welcome the user
@app.route('/')
def hello_world():
    return ('<h1>hello</h1>')

# list all the users from zzplus
@app.route('/zzplus', methods=['GET'])
def zzplus():
    rows = session.execute("""Select * From zzplus.user""")
    for user in rows:
        return ('<h2>This is all users : {} </h2>'.format(rows.current_rows))
    return ('<h1>That data does not exist!</h1>')

# add new user
@app.route('/add_user', methods=['POST'])
def create_a_record():
    if not request.json or not 'name' in request.json or not 'id' in request.json or not 'subject' in request.json:
        return jsonify({'error': 'Incomplete data'}), 400
    new_record = {
        'id': request.json['id'],
        'subject': request.json['subject'],
        'name': request.json['name'],
        'password': request.json['password']
     }
    session.execute("""insert into zzplus.user(id, name, subject, password) values ({}, '{}',{},'{}')""".format(new_record['id'],new_record['name'],new_record['subject'],new_record['password']))
    return jsonify({'message': 'Record has created: {}'.format(new_record['name'])}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
