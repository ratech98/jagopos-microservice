import cv2
from PIL import Image, ImageDraw, ImageFont
import pytesseract
import os
from flask import Flask, send_file, jsonify
import config

# Initialize the Flask app
app = Flask(__name__)

# Set the path to Tesseract (ensure it's correctly configured for your environment)
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

# File paths
background_path = './images/2.jpg'
blueprint_path = './images/3.jpg'
output_path = 'updated_menu.jpg'

# JSON Data for item and category mappings
JSON = {
    "item": {'cat01-item01': ['Idly', False], 'cat01-item02': ['banana', True], 'cat01-item03': ['cherry', True],
             'cat01-item04': ['date', True], 'cat01-item05': ['elderberry', True], 'cat01-item06': ['fig', True],
             'cat01-item07': ['grape', True], 'cat01-item08': ['honeydew', True], 'cat01-item09': ['kiwi', True],
             'cat01-item10': ['lemon', True], 'c1-p1': ['$6.99', False], 'c1-p2': ['$6.00', True],
             'c1-p3': ['$7.00', True], 'c1-p4': ['$8.00', True], 'c1-p5': ['$5.00', True], 'c1-p7': ['$6.00', True],
             'c1-p6': ['$6.00', True], 'c1-p8': ['$7.00', True], 'c1-p9': ['$8.00', True], 'cat02-item01': ['mango', True],
             'cat02-item02': ['nectarine', True], 'cat02-item03': ['orange', True], 'cat02-item04': ['papaya', True],
             'cat02-item05': ['quince', True], 'cat03-item01': ['raspberry', True], 'cat03-item02': ['strawberry', True],
             'cat03-item03': ['tangerine', True], 'cat03-item04': ['ugli fruit', True], 'cat03-item05': ['watermelon', True],
             'c3-p1': ['$10.01', True], 'c3-p2': ['$10.02', True], 'c3-p3': ['$10.03', True], 'c3-p4': ['$10.04', True],
             'c3-p5': ['$10.07', True], 'c2-p1': ['$5.00', True], 'c2-p2': ['$6.00', True], 'c2-p3': ['$7.00', True],
             'c2-p4': ['$8.00', True], 'c2-p5': ['$5.00', True]},
    "category": {"cat01": "Coffee", "cat02": "Tea", "cat03": "Snacks"}
}

PRODUCT_MAPPING = JSON['item']
CATEGORY_MAPPING = JSON['category']

# Load images
background_img = Image.open(background_path)
blueprint_img = Image.open(blueprint_path)

# Preprocess the blueprint image
blueprint_cv_img = cv2.imread(blueprint_path)

# Convert to grayscale
gray = cv2.cvtColor(blueprint_cv_img, cv2.COLOR_BGR2GRAY)

# Apply thresholding
_, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

# Extract text using Pytesseract with processed image
data = pytesseract.image_to_data(thresh, output_type=pytesseract.Output.DICT)

# Create drawing object for the background image
draw = ImageDraw.Draw(background_img)

# Loop through detected text blocks and replace text
for i in range(len(data['text'])):
    text = data['text'][i].lower()
    print(text)
    # Replace product names
    if text in PRODUCT_MAPPING:
        # Get position
        x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
        new_text = PRODUCT_MAPPING.get(text)

        # Get font and calculate text size using getbbox
        font = ImageFont.truetype(config.PRODUCT_FONT_FAMILY, config.PRODUCT_FONT_SIZE)

        # Write new text onto the background image
        draw.text((x, y), new_text[0], fill=config.PRODUCT_FONT_COLOR, font=font)
        if not new_text[1]:
            text_bbox = font.getbbox(new_text[0])  # Returns (left, top, right, bottom)
            text_width, text_height = text_bbox[2], text_bbox[3]

            # Add a strike-through line
            strike_y = y + text_height // 2  # Middle of the text vertically
            draw.line((x, strike_y, x + text_width, strike_y), fill=config.STRIKE_OUT_COLOR, width=config.STRIKE_OUT_SIZE)

    # Replace category names
    elif text in CATEGORY_MAPPING:
        # Get position
        x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
        new_text = CATEGORY_MAPPING.get(text, "Add")
        # Write new text onto the background image
        draw.text((x, y), new_text, fill=config.CATEGORY_FONT_COLOR,
                  font=ImageFont.truetype(config.CATEGORY_FONT_FAMILY, config.CATEGORY_FONT_SIZE))

# Save the updated image
background_img.save(output_path)

print(f"Updated menu saved at: {output_path}")

# Serve the image via Flask
@app.route('/', methods=['GET'])
def serve_image():
    return send_file(output_path, mimetype='image/jpeg')

if __name__ == "__main__":
    # Run the app on port 8080
    app.run(host='0.0.0.0', port=8080)

