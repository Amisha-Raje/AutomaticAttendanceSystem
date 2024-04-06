from flask import Flask, request, render_template, jsonify, send_file
import subprocess
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/fac-menu')
def fac_menu():
    return render_template('Fac_menu.html')

@app.route('/stud-menu')
def stud_menu():
    return render_template('Stud_menu.html')

@app.route('/fac-login')
def fac_login():
    return render_template('Fac_login.html')

@app.route('/fac-addcourse')
def fac_takeaddcourse():
    return render_template('Fac_addCourse.html')

@app.route('/fac-uploadimage')
def fac_uploadimage():
    return render_template('fac_uploadImage.html')

@app.route('/stud-uploadimage')
def stud_uploadimage():
    return render_template('Stud_uploadImage.html')

@app.route('/stud-viewimage')
def stud_viewimage():
    return render_template('Stud_viewImage.html')

@app.route('/stud-regcourse')
def stud_regcourse():
    return render_template('Stud_regCourse.html')

def generate_excel_filename():
    current_date = datetime.now().strftime("%Y-%m-%d")
    return f"course_name_cam_{current_date}.xlsx"

# Route to handle downloading of the Excel file
@app.route('/open_excel')
def open_excel():
    excel_filename = "course_name_cam_2024-03-26.xlsx"  # Update with the actual filename
    print("File path:", excel_filename)  # Print the file path
    return send_file(excel_filename, as_attachment=True)

@app.route('/fac-takeatt')
def fac_takeatt():
    return render_template('Fac_takeAtt.html')

# @app.route('/upload')
# def fupload():
#     # Pass the URL to the template
#     return render_template('from_img.py')

@app.route('/stud-login')
def stud_login():
    return render_template('Stud_login.html')

@app.route('/excel')
def excel():
     excel_file_path = 'C:\XAMPP\htdocs\capstone_face_recognition\course_name_cam_2024-03-26.xlsx'
     return send_file(excel_file_path, as_attachment=True)

@app.route('/stud-register')
def stud_register():
    return render_template('Stud_register.html')

@app.route('/fac-register')
def fac_register():
    return render_template('Fac_register.html')

@app.route('/home')
def home():
    return render_template('homepage.html')

@app.route('/run_script')
def run_script():
    try:
        subprocess.run(['python', 'face.py'])
        return 'Python script executed successfully', 200
    except Exception as e:
        return f'Error executing Python script: {e}', 500 

@app.route('/upload')
def upload():
    try:
        subprocess.run(['python', 'from_img.py'])
        return 'Another Python script executed successfully', 200
    except Exception as e:
        return f'Error executing another Python script: {e}', 500 

# @app.route('/run_homepage')
# def run_homepage():
#     try:
#         subprocess.run(['python', 'homepage.html'])
#         return 'Another Python script executed successfully', 200
#     except Exception as e:
#         return f'Error executing another Python script: {e}', 500    

if __name__ == '__main__':
    app.run(debug=True)