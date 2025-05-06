import cv2
import dlib
import numpy as np
import matplotlib
matplotlib.use('Agg')  
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, jsonify
import os
import base64
from io import BytesIO
app = Flask(__name__)
cascade_path = os.path.join(os.path.dirname(__file__), 'LBP_face_default.xml')
face_cascade = cv2.CascadeClassifier(cascade_path)

@app.route('/')
def home():
    return render_template('my.html')

@app.route('/detect', methods=['POST'])
def detect():
    try:
        file = request.files['image.png']
        npimg = np.frombuffer(file.read(), np.uint8)
        img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        response = {'faces_detected': len(faces)}
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
