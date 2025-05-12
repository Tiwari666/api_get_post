#  Flask API Project — GET & POST

This is a simple Flask application demonstrating GET and POST APIs.

---

## 📁 Project Structure

![image](https://github.com/user-attachments/assets/cc4a2a57-1a2a-4cb4-b7fe-93db48257b20)


#  Add api_config.yaml

api:

  name: Flask GET & POST API
  
  version: 1.0
  
  routes:
  
    - path: /api
    
      method: GET
      
      response: HTML message
      
    - path: /api
    
      method: POST
      
      response: JSON {"Key": "This is the post"}
      
setup:

  venv: true
  
  dependencies:
  
    - flask


# Then upload it manually to GitHub (like before), or push it via VS Code using:

git add api_config.yaml
git commit -m "Add API config YAML"
git push

# Create requirements.txt:

pip freeze > requirements.txt

pip install -r requirements.txt

# write the following code inside the requirements.txt:

flask==3.1.0
