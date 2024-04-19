import subprocess
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start-driving', methods=['POST'])
def start_driving():
    try:
        # Start drive.py as a subprocess
        subprocess.Popen(["python3", "drive.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return jsonify({'status': 'Drive script started successfully'})
    except Exception as e:
        return jsonify({'status': 'Failed to start the script', 'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
