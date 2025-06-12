from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the MYSTK creators portal"})

@app.route('/learn')
def learn():
    return jsonify({"section": "learn", "content": "Learning resources placeholder"})

@app.route('/metrics')
def metrics():
    return jsonify({"section": "metrics", "content": "Monthly metrics placeholder"})

@app.route('/support')
def support():
    return jsonify({"section": "support", "content": "Support information placeholder"})

if __name__ == '__main__':
    app.run(debug=True)
