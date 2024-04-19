from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start-script', methods=['POST'])
def start_script():
    try:
        # Start the drive.py script as a subprocess
        subprocess.Popen(["python3", "drive.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return jsonify({'status': 'Script started successfully'})
    except Exception as e:
        return jsonify({'status': 'Failed to start the script', 'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
