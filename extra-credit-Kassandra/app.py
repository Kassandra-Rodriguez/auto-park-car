from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/start-drive')
def start_drive():
    """Route to start the drive.py script."""
    try:
        # Starting the drive.py script as a subprocess
        subprocess.Popen(['python3', '/home/kassandrarodriguez/auto-park-car/extra-credit-Kassandra/drive.py'])
        return "Drive script initiated successfully.", 200
    except Exception as e:
        return f"Failed to start the script: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
    
    
    
