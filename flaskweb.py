from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Fac_takeAtt.html')

@app.route('/run_script')
def run_script():
    try:
        subprocess.run(['python', 'face.py'])
        return 'Python script executed successfully', 200
    except Exception as e:
        return f'Error executing Python script: {e}', 500 

@app.route('/run_another_script')
def run_another_script():
    try:
        subprocess.run(['python', 'from_img.py'])
        return 'Another Python script executed successfully', 200
    except Exception as e:
        return f'Error executing another Python script: {e}', 500 

if __name__ == '__main__':
    app.run(debug=True)
