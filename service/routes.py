from flask import Flask, jsonify, request, abort

app = Flask(__name__)

products = []

@app.route('/products', methods=['GET'])
def list_products():
    name = request.args.get('name')
    category = request.args.get('category')
    available = request.args.get('available')
    results = products
    if name:
        results = [p for p in results if p['name'] == name]
    if category:
        results = [p for p in results if p['category'] == category]
    if available:
        results = [p for p in results if str(p['available']).lower() == available.lower()]
    return jsonify(results)

@app.route('/products/<int:pid>', methods=['GET'])
def read_product(pid):
    for p in products:
        if p['id'] == pid:
            return jsonify(p)
    abort(404)

@app.route('/products', methods=['POST'])
def create_product():
    data = request.json
    data['id'] = len(products) + 1
    products.append(data)
    return jsonify(data), 201

@app.route('/products/<int:pid>', methods=['PUT'])
def update_product(pid):
    data = request.json
    for p in products:
        if p['id'] == pid:
            p.update(data)
            return jsonify(p)
    abort(404)

@app.route('/products/<int:pid>', methods=['DELETE'])
def delete_product(pid):
    global products
    products = [p for p in products if p['id'] != pid]
    return '', 204

if __name__ == "__main__":
    app.run(debug=True)
