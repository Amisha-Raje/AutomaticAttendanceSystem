from flask import Flask, request, render_template, jsonify
import subprocess
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('homepage.html')



@app.route('/fac-menu')
def fac_menu():
    # Generate the URL for the redirection page
    # fac_menu_url = url_for('fac_menu.html')
    # Render the template and pass the URL as a variable
    return render_template('Fac_menu.html')

@app.route('/fac-login')
def fac_login():
    # Pass the URL to the template
    return render_template('Fac_login.html')

@app.route('/fac-addcourse')
def fac_takeaddcourse():
    # Pass the URL to the template
    return render_template('Fac_addCourse.html')

@app.route('/stud-uploadimage')
def fac_uploadimage():
    # Pass the URL to the template
    return render_template('Stud_uploadImage.html')


def generate_excel_filename():
    current_date = datetime.now().strftime("%Y-%m-%d")
    return f"course_name_cam_{current_date}.xlsx"

# Route to handle downloading of the Excel file
@app.route('/open_excel')
def open_excel():
    excel_filename = "course_name_cam_2024-03-26.xlsx"  # Update with the actual filename
    print("File path:", excel_filename)  # Print the file path
    return send_file(excel_filename, as_attachment=True)

@app.route('/upload', methods=['POST'])
def upload():
    try:
        if 'image' not in request.files:
            return jsonify(message="No file part"), 400
        
        image = request.files['image']

        if image.filename == '':
            return jsonify(message="No selected file"), 400

        if image:
            # Save the uploaded image
            image_path = 'uploads/' + image.filename
            image.save(image_path)

            # Now process the image using face recognition script
            result = subprocess.check_output(['python', 'from_img.py', image_path])
            # Example: result = subprocess.check_output(['python', 'face_recognition_script.py', image_path])

            # Handle the result as needed
            result = result.decode('utf-8').strip()  # Decode bytes to string
            return jsonify(message="Image uploaded and processed successfully", result=result), 200
    except Exception as e:
        return jsonify(message=str(e)), 500

    return jsonify(message="An error occurred"), 500

@app.route('/fac-takeatt')
def fac_takeatt():
    # Pass the URL to the template
    return render_template('Fac_takeAtt.html')

@app.route('/stud-login')
def stud_login():
    return render_template('Stud_login.html')


@app.route('/stud-register')
def stud_register():
    return render_template('Stud_register.html')

@app.route('/fac-register')
def fac_register():
    return render_template('Fac_register.html')

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

# @app.route('/run_homepage')
# def run_homepage():
#     try:
#         subprocess.run(['python', 'homepage.html'])
#         return 'Another Python script executed successfully', 200
#     except Exception as e:
#         return f'Error executing another Python script: {e}', 500    

if __name__ == '__main__':
    app.run(debug=True)
