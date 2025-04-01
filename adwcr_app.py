from flask import Flask, request

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET'])
def prediction_model():
    a = request.args.get("a", default = 0.0, type = float)
    b = request.args.get("b", default = 0.0, type = float)
    
    if a + b > 5.8:
        prediction = 1
    else:
        prediction = 0

    resp = {
        'prediction': prediction,
        'features': {
            'message': f'The prediction equals {prediction}',
            'a': a,
            'b': b
        }
    }
    
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
