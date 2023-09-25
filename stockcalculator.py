from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET', 'POST'])
def add_numbers():
    if request.method == 'GET':
        # Get input from URL parameters
        num1 = float(request.args.get('num1', 0))
        num2 = float(request.args.get('num2', 0))
    elif request.method == 'POST':
        # Get input from JSON in POST data
        data = request.get_json()
        num1 = float(data.get('num1', 0))
        num2 = float(data.get('num2', 0))

    # Perform addition operation
    result = num1 + num2

    # Create a JSON response
    response = {'result': result}

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
