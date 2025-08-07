# 🎣 Phishing URL Analyzer

A simple but effective web tool to detect suspicious or potentially phishing URLs.

## 🔍 Features

- ✅ Detect punycode in domains (`xn--` format)
- ✅ Compare domains to known brand names using similarity score
- ✅ Display potential phishing warnings
- ✅ Clean UI with Bootstrap 5 and Font Awesome
- ✅ Deployable to Render (no Docker required)

## 💡 Technologies

- Python 3.x
- Django 5.x
- Bootstrap 5
- Font Awesome
- tldextract, difflib

## 🚀 Live Demo

👉 [Visit the app](https://phishing-url-analyzer.onrender.com)  
> Paste any URL and test if it could be phishing.

## 📦 Setup

```bash

git clone https://github.com/CyberB0x/phishing-url-analyzer.git
cd phishing-url-analyzer
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
