from flask import Flask, request, jsonify
import subprocess
from scraper.utils import get_best_price

app = Flask(__name__)

@app.route('/optimize', methods=['POST'])
def optimize():
    data = request.json
    items = data['items']
    budget = data['budget']

    with open('../algorithm/input.txt', 'w') as f:
        f.write(f"{len(items)} {budget}\n")
        for item in items:
            name = item['name']
            value = item['value']
            price, link = get_best_price(name)
            f.write(f"{name}\n{price} {value}\n{link}\n")

    subprocess.call(['bash', '../algorithm/run_algorithm.sh'])

    with open('../algorithm/output.txt', 'r') as f:
        output = f.read()

    return jsonify({'result': output})

if __name__ == '__main__':
    app.run(debug=True)
