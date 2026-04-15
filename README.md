# fake_website-detection
Developed a machine learning-based phishing detection system using Logistic Regression to classify URLs as safe or malicious. Implemented feature engineering on URL patterns and built an interactive web app using Streamlit for real-time prediction and analysis.
# 🔍 Fake Website Detection System (ML + Streamlit)

A machine learning-based web application that detects whether a website URL is **legitimate or phishing** using URL feature analysis and Logistic Regression.

---

## 🚀 Overview

This project analyzes URLs and classifies them as **safe or malicious** based on patterns commonly found in phishing websites. It uses a trained machine learning model and provides a simple web interface for real-time predictions.

---

## 🎯 Features

- 🔐 Detects phishing/fake websites in real-time  
- ⚡ Fast prediction using Logistic Regression model  
- 🌐 Interactive web app built with Streamlit  
- 📊 Displays prediction confidence score  
- 🧠 Shows URL feature breakdown for transparency  

---

## 🧠 How It Works

The system extracts important features from a URL such as:

- URL length  
- Presence of HTTPS  
- IP address in URL  
- Number of dots (.)  
- Number of hyphens (-)  
- Presence of special characters (@)  
- Suspicious keywords like "login"  

These features are fed into a Logistic Regression model trained on labeled data.

---

## 🛠️ Tech Stack

- Python 🐍  
- Pandas  
- Scikit-learn  
- Regex  
- Streamlit  
- Kaggle dataset  

---

## 📁 Project Structure
