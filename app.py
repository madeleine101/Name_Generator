from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-script', methods=['POST'])
def run_script():
    # Execute your Python script
    subprocess.run(["python3", "script.py"])
    return "Script executed successfully!"

if __name__ == '__main__':
    app.run(debug=True)
