<div align="center">

# 🔢 DigitAI

### AI-Powered Handwritten Digit Recognizer

A machine learning web application that recognizes handwritten digits **0–9** using an interactive Streamlit interface.

<br>

<a href="YOUR_STREAMLIT_LINK">
  <img src="https://img.shields.io/badge/🚀_Live_Demo-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
</a>
<a href="https://github.com/Anmolgoreja/DigitAI-Handwritten-Digit-Recognizer">
  <img src="https://img.shields.io/badge/💻_Source_Code-181717?style=for-the-badge&logo=github&logoColor=white">
</a>

<br><br>

<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
<img src="https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white">
<img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white">
<img src="https://img.shields.io/badge/Pillow-3776AB?style=for-the-badge&logo=python&logoColor=white">

<br><br>

<img src="https://img.shields.io/github/stars/Anmolgoreja/DigitAI-Handwritten-Digit-Recognizer?style=flat-square">
<img src="https://img.shields.io/github/forks/Anmolgoreja/DigitAI-Handwritten-Digit-Recognizer?style=flat-square">
<img src="https://img.shields.io/github/license/Anmolgoreja/DigitAI-Handwritten-Digit-Recognizer?style=flat-square">

</div>

---

## ✨ About The Project

**DigitAI** is an AI-powered handwritten digit recognition application built with **Python, Machine Learning, and Streamlit**.

The application allows users to either **draw a handwritten digit or upload an image**. The input is processed and passed to a trained machine learning model, which predicts the most likely digit and displays the **Top 3 predictions with confidence scores**.

The project combines machine learning with an interactive web interface to create a simple and practical AI application.

---

## 🎯 Key Features

<table>
<tr>
<td width="50%">

### ✏️ Draw Digit

Draw your handwritten digit directly inside the application.

</td>
<td width="50%">

### 🖼️ Upload Image

Upload an image containing a handwritten digit.

</td>
</tr>

<tr>
<td width="50%">

### 🤖 AI Prediction

Uses a trained machine learning model to recognize digits from 0–9.

</td>
<td width="50%">

### 🏆 Top 3 Results

Displays the three most likely predictions with confidence scores.

</td>
</tr>

<tr>
<td width="50%">

### 📊 Confidence Scores

See how confident the model is about each prediction.

</td>
<td width="50%">

### ⚡ Interactive Interface

A clean and responsive Streamlit interface designed for easy interaction.

</td>
</tr>
</table>

---

## 🖥️ Application Preview

<div align="center">

<img src="screenshot.png" alt="DigitAI Application Preview" width="900">

</div>

---

## 🧠 How It Works

<div align="center">

```text
        ✏️ User Input
              ↓
      Draw / Upload Digit
              ↓
     🖼️ Image Preprocessing
              ↓
       🔢 Pixel Features
              ↓
       🤖 ML Classifier
              ↓
     📊 Prediction Probabilities
              ↓
       🏆 Top 3 Results
```

</div>

The application converts the input image into numerical pixel data and processes it into the format expected by the trained model.

The model then generates prediction probabilities for the possible digits and the application displays the **three highest-probability predictions**.

---

## 🛠️ Tech Stack

<div align="center">

<img src="https://skillicons.dev/icons?i=python" height="60">
<img src="https://skillicons.dev/icons?i=numpy" height="60">

<br><br>

<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
<img src="https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white">
<img src="https://img.shields.io/badge/Pillow-3776AB?style=for-the-badge&logo=python&logoColor=white">

</div>

---

## 📂 Project Structure

```text
DigitAI-Handwritten-Digit-Recognizer/
│
├── 📄 app.py
├── 📄 train_model.py
├── 🤖 model.pkl
├── 📦 requirements.txt
├── 🖼️ screenshot.png
└── 📖 README.md
```

| File               | Description                     |
| ------------------ | ------------------------------- |
| `app.py`           | Main Streamlit application      |
| `train_model.py`   | Machine learning model training |
| `model.pkl`        | Saved trained model             |
| `requirements.txt` | Project dependencies            |
| `screenshot.png`   | Application preview             |
| `README.md`        | Project documentation           |

---

## 🚀 Getting Started

### Prerequisites

Make sure Python is installed on your system.

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/Anmolgoreja/DigitAI-Handwritten-Digit-Recognizer.git
```

**2. Navigate to the project**

```bash
cd DigitAI-Handwritten-Digit-Recognizer
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the application**

```bash
streamlit run app.py
```

---

## 🌐 Live Demo

<div align="center">

<a href="YOUR_STREAMLIT_LINK">
<img src="https://img.shields.io/badge/🚀_TRY_DIGITAI_NOW-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
</a>

<br><br>

<strong>Experience the handwritten digit recognizer directly in your browser.</strong>

</div>

---

## 📊 Prediction Output

DigitAI provides more than just one prediction.

For every input, the application displays:

<table align="center">
<tr>
<th>Rank</th>
<th>Prediction</th>
<th>Confidence</th>
</tr>
<tr>
<td>🥇 1st</td>
<td>Most likely digit</td>
<td>Highest probability</td>
</tr>
<tr>
<td>🥈 2nd</td>
<td>Second most likely digit</td>
<td>Second highest probability</td>
</tr>
<tr>
<td>🥉 3rd</td>
<td>Third most likely digit</td>
<td>Third highest probability</td>
</tr>
</table>

---

## 🎓 Learning Outcomes

This project provided practical experience with:

* 🐍 Python programming
* 🤖 Machine learning classification
* 🖼️ Image preprocessing
* 🔢 Pixel-based feature processing
* 📊 Prediction probabilities
* 💾 Saving and loading ML models
* 🎨 Streamlit interface development
* 🌐 ML application deployment

---

## 🔮 Future Improvements

* 🧠 Upgrade to a CNN/deep learning model
* ✍️ Improve drawing canvas functionality
* 🔤 Add handwritten letter recognition
* 📈 Add model performance visualizations
* 📱 Improve mobile responsiveness
* 🎨 Add additional UI themes and customization

---

## 👩‍💻 Author

<div align="center">

### Anmol Goreja

**Computer Science Student | Python | AI/ML | Web Development**

<br>

<a href="https://github.com/Anmolgoreja">
<img src="https://img.shields.io/badge/GitHub-Anmolgoreja-181717?style=for-the-badge&logo=github&logoColor=white">
</a>

<a href="YOUR_LINKEDIN_LINK">
<img src="https://img.shields.io/badge/LinkedIn-Anmol_Goreja-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white">
</a>

</div>

---

<div align="center">

### ⭐ If you like this project, consider giving it a star!

<br>

**Built with ❤️ using Python, Machine Learning & Streamlit**

</div>
