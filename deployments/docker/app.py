from flask import Flask,  jsonify 
app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({
        'message': 'hello world',
        'environment': os.environment.get ('ENVIRONMENT')
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)