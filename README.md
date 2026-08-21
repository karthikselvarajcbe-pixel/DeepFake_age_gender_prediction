# DeepFake_age_gender_prediction
DeepFake Age & Gender Prediction
📌 Project Overview

This project is an AI-based facial image analysis system designed to perform DeepFake detection, age-group prediction, and gender prediction from uploaded facial images.

The system follows a sequential analysis pipeline:

Upload Image → DeepFake Detection → Real/Fake Classification → Age & Gender Prediction

The primary objective of this project is to combine computer vision and deep learning techniques to analyze facial images and determine whether an image is REAL or FAKE. For images classified as REAL, the system can further perform age-group and gender prediction.

🚀 Key Features
🖼️ Upload and analyze multiple facial images
🔍 DeepFake Detection using a trained ResNet50 model
✅ Classifies images as REAL or FAKE
👤 Gender Prediction for REAL images
🎂 Age Group Prediction for REAL images
📊 Displays prediction results for each uploaded image
⚡ Supports batch image analysis
🧠 Uses deep learning-based computer vision models
🌐 Designed to be integrated with a Streamlit web application
🧠 Models Used
1. DeepFake Detection — ResNet50

A customized ResNet50-based image classification model is trained to distinguish between REAL and FAKE facial images.

Output:

REAL
FAKE

The DeepFake model acts as the first stage of the pipeline.

2. Age & Gender Prediction — InsightFace

For images classified as REAL, the system can perform additional facial analysis using InsightFace.

The system provides:

##Gender: Male / Female
##Age Group:
18–25
26–35
36–50
50+


#📦 Large Model Files

The trained .pth and .pkl files are larger than the recommended GitHub file size limit.

Therefore, the trained models and supporting files have been stored separately in Google Drive.

Google Drive — Trained Models & Files
https://drive.google.com/drive/folders/1Llyo3igolD1KFVKgHWuX9WNznJm4qYQE
