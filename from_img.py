from PIL import Image, ImageDraw, ImageFont
import face_recognition
from openpyxl import Workbook
from datetime import datetime

# Dictionary of known faces with their corresponding images
known_faces = {
    "Amisha": "amisha.jpeg",
    "Sahiti": "sahiti.jpeg",
    "Sampreety": "sam.jpeg",
    "Atul": "atul.jpeg",
    "Vansh": "vansh.jpeg",
    "Khushi": "khushi.jpeg",  
    "Jasmine": "jasmine.jpeg",
    "Harsh": "loomba.jpeg",
}

# Load known face images
known_face_encodings = {}
for name, image_path in known_faces.items():
    known_image = face_recognition.load_image_file(image_path)
    known_face_encodings[name] = face_recognition.face_encodings(known_image)[0]

# Image file path
image_path = "group.jpg"

# Load the image
image = face_recognition.load_image_file(image_path)

# Find all face locations in the image
face_locations = face_recognition.face_locations(image)
face_encodings = face_recognition.face_encodings(image, face_locations)

# Initialize variables for accuracy calculation
total_faces = len(face_locations)
correctly_identified_faces = 0

# Create a new Excel workbook and select the active sheet
wb = Workbook()
ws = wb.active

# Set up headers for the Excel sheet
ws.append(["Name"])

# Convert image to PIL format for drawing
pil_image = Image.fromarray(image)
draw = ImageDraw.Draw(pil_image)
font = ImageFont.truetype("arial.ttf", 66)  # Font for text display

# Iterate through each face found in the image
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    # Check if the face matches any known faces
    matches = face_recognition.compare_faces(list(known_face_encodings.values()), face_encoding)
    name = "Unknown"

    # Find the name of the known face with the smallest distance to the new face
    if True in matches:
        matched_index = matches.index(True)
        name = list(known_face_encodings.keys())[matched_index]
        correctly_identified_faces += 1

    # Draw a bounding box and label around the face
    draw.rectangle(((left, top), (right, bottom)), outline=(255, 0, 0), width=5)
    draw.text((left, top - 70), name, fill=(255, 0, 0, 0), font=font)

    # Add the name to the Excel sheet
    ws.append([name])

# Calculate accuracy
accuracy = (correctly_identified_faces-3 / total_faces) * 100

# Display or save the image with bounding boxes and labels
pil_image.show()  # or pil_image.save("output.jpg")

# Save the Excel file
current_datetime = datetime.now().strftime("%Y-%m-%d")
excel_filename = f"course_name_img{current_datetime}.xlsx"
wb.save(excel_filename)
# Print the accuracy
print("Accuracy: {:.2f}%".format(accuracy))
