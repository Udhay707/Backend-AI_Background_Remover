from flask import Flask, request, jsonify
from rembg import remove
from PIL import Image
import io
import base64

app = Flask(__name__)

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    try:
        file = request.files['image']
        input_image = Image.open(file)
        output_image = remove(input_image)
        buffered = io.BytesIO()
        output_image.save(buffered, format='PNG')
        encoded_image = base64.b64encode(buffered.getvalue()).decode('utf-8')
        return jsonify({'image': encoded_image})
    except Exception as e:
        return jsonify({'error': str(e)}),500

if __name__ == '__main__':
    app.run()
