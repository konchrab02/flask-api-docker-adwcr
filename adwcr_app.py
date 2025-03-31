from flask import Flask, request

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET'])
def prediction_model():
    a = request.args.get("a", "")
    b = request.args.get("b", "")
    
    if a and b:
        a = float(a)
        b = float(b)
        if a + b > 5.8:
            prediction = 1
        else:
            prediction = 0
    elif a and not b:
        a = float(a)
        if a > 5.8:
            prediction = 1
            b = 0
        else:
            prediction = 0
            b = 0
    elif not a and b:
        b = float(b)
        if b > 5.8:
            prediction = 1
            a = 0
        else:
            prediction = 0
            a = 0
    else:
        prediction = 0
        a = 0
        b = 0

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
