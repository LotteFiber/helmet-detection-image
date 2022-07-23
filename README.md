# HelmetSys

Web application, Mobile application, OCR program for scanning student cards and motorcycle license plates For students who do not wear helmets or violate the traffic rules of Naresuan University

## Technology 

- [Web application: React]
- [Mobile application: Flutter]
- [Backend API: Express]
- [Database: MongoDB]
- [MQTT connection: Paho MQTT]
- [OCR program: Python]
- [OCR extraction: YOLO and EasyOCR]
- [OCR model: NU vision lab]

## Getting Started
Each folder must be installed as follows.

### HelmetDetection_V2ByImage
Copy folder "model" to this folder
Library to install
- `pip paho-mqtt`
- `conda numpy`
- `conda opencv`
- `conda dlib`
- `pip easyocr`

Runs the app in the development mode.<br>
-  `python runDetection.py`

