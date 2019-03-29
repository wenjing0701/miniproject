from flask import Flask, request, jsonify, json
from cassandra.cluster import Cluster

with open('records.json') as f:
    all_records = json.load(f)

cluster = Cluster(['cassandra'])
session = cluster.connect()

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name","World")
    return('<h1>Hello, {}!</h1>'.format(name))

@app.route('/pokemon/<name>')
def profile(name):
    rows = session.execute( """Select * From pokemon.stats where name = '{}'""".format(name))
    for pokemon in rows:
        return('<h1>{} has {} defense!</h1>'.format(name,pokemon.defense))
    return('<h1>That Pokemon does not exist!</h1>')

@app.route('/pokemon/<name>/special defensive strength', methods=['POST'])
def create_a_record():
    if not request.json or not 'name' in request.json:
        return jsonify({'error':'The new record needs to have a pokemon name'}), 400
    new_record={
        'name':request.json['name'],
        'special defensive strength':request.json.get['special defensive strength','']
    }
    all_records.append(new_record)
    return jsonify({'message': 'created: /records/{}'.format(new_record['name'])}), 201 


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

