"""
Step-by-Step Instructions to Create and Run a Flask GET & POST API
===================================================================

1. Create the Virtual Environment
---------------------------------
Command:
    python -m venv venv

2. Activate the Virtual Environment (in Command Prompt)
-------------------------------------------------------
Command:
    venv\Scripts\activate.bat

3. Install Flask
----------------
Command:
    pip install flask

4. Create app.py
----------------

Content:
-------------------------
from flask import Flask, request

# Initialize the Flask app
app = Flask(__name__)

# POST route
@app.route("/api", methods=["POST"])
def api_post():
    return {"Key": "This is the post"}

# GET route
@app.route("/api", methods=["GET"])
def api_get():
    return "<html><body>Hello from GET API!</body></html>"
-------------------------

5. Create run.py
----------------

Content:
-------------------------
from app import app

if __name__ == "__main__":
    app.run(debug=True)
-------------------------

6. Restart Your Server (manually)
---------------------------------
Command:
    CTRL + C   # (to stop the server)

7. Run the App Again
--------------------
Command:
    python run.py

8. Test the GET API
-------------------
Open this URL in your browser:
    http://127.0.0.1:5000/api

9. Test the POST API
--------------------
Command:
    curl -X POST http://127.0.0.1:5000/api

Expected Output:
    {"Key": "This is the post"}
"""

##############################################Publish in GitHub
#Step 1: Make sure you're inside: C:\Users\naren\Desktop\New_DS\api_get_post
# Step 2: Create .gitignore : Create a file named .gitignore and add: 
#venv/
#__pycache__/
#*.pyc
# Go to https://github.com: Log in to your GitHub account and create a new repository callled "api_get_post".

