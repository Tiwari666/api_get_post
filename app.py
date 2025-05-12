from flask import Flask, request

# Initialize Flask app
app = Flask(__name__)

@app.route('/api', methods=['GET', 'POST'])
def api_handler():
    if request.method == 'POST':
        return {"Key": "Hello from POST API!"}
    else:
        return "<html><body><h2>Hello from GET API!</h2></body></html>"






