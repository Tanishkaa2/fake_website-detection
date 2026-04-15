
import pandas as pd
import kagglehub
import os
import re
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score
import streamlit as st

# ---------- Feature Extraction ----------
def extract_features(url):
    return [
        len(url),  # URL Length
        1 if re.search(r"\d+\.\d+\.\d+\.\d+", url) else 0,  # IP address
        1 if "https" in url else 0,  # HTTPS
        url.count('.'),  # dots
        url.count('-'),  # hyphens
        1 if "@" in url else 0,  # @ symbol
        1 if "login" in url.lower() else 0  # keyword
    ]

# ---------- Dataset ----------

# Download latest version
path = kagglehub.dataset_download("simaanjali/tes-upload")

files=os.listdir(path)
print("Files in dataset directory:", files)

csv_file=[f for f in files if f.endswith('.csv')][0]
df= pd.read_csv(os.path.join(path, csv_file))

print(df.head())
print(df.columns)

# Assuming URL is first column
urls = df.iloc[:, 0]
y = df.iloc[:, -1]

# Remove NaN in labels
mask = ~y.isna()
urls = urls[mask]
y = y[mask]

# Convert labels to numeric if needed
if y.dtype == 'object':
    y = y.str.lower()
    y = y.map({
        'fake': 1,
        'phishing': 1,
        'bad': 1,
        'malicious': 1,
        'real': 0,
        'legit': 0,
        'good': 0,
        'safe': 0
    })

# Drop any remaining NaN after mapping
mask = ~y.isna()
urls = urls[mask]
y = y[mask]

# Convert labels if needed
# y = y.map({'fake': 1, 'real': 0})

# Feature extraction
X = [extract_features(str(url)) for url in urls]

# ---------- Train Model ----------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression()
model.fit(X_train, y_train)

# ---------- Evaluation ----------
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))

# ---------- Streamlit UI ----------
st.title("🔍 Fake Website Detection System")

url_input = st.text_input("Enter Website URL")

if st.button("Check Website"):
    if url_input:
        features = extract_features(url_input)
        prediction = model.predict([features])[0]
        prob = model.predict_proba([features])[0][1]

        if prediction == 1:
            st.error(f"⚠️ Fake Website (Risk: {prob*100:.2f}%)")
        else:
            st.success(f"✅ Safe Website (Confidence: {(1-prob)*100:.2f}%)")

        st.subheader("Feature Analysis")
        st.write({
            "URL Length": len(url_input),
            "Uses HTTPS": "Yes" if "https" in url_input else "No",
            "Contains IP": "Yes" if re.search(r"\d+\.\d+\.\d+\.\d+", url_input) else "No",
            "Has @ symbol": "Yes" if "@" in url_input else "No",
            "Contains 'login'": "Yes" if "login" in url_input.lower() else "No"
        })

