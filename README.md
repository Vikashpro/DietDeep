# DeepDiet 🍏 AI-Powered Nutrition Guide

An AI-powered web app that provides personalized meal plans and nutrition insights using deep learning and food image recognition.

## 🚀 Features

- 🥗 AI-generated meal plans based on dietary goals.
- 📸 Image-based food recognition using YOLOv10.
- 🍽️ Fetches nutritional facts from the USDA API.
- 🧠 Uses DeepSeek-R1 for intelligent meal planning.

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **AI Models**: DeepSeek-R1, YOLOv10
- **Data Processing**: OpenAI API, USDA API
- **Backend**: Python, OpenAI SDK

## 📦 Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/DeepDiet.git
cd DeepDiet
```

### 2️⃣ Create a Virtual Environment

#### Windows:
```
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux:
```
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Set Up API Keys

Create a `.streamlit/secrets.toml` file and add:

```
AIMLAPI_KEY = "your_aimlapi_key"
USDA_API_KEY = "your_usda_api_key"
```

### 5️⃣ Run the Application

```
streamlit run app.py
```

Open your browser and go to [http://localhost:8501](http://localhost:8501).

## 🚀 Deployment on Streamlit Cloud

1. Push your project to GitHub.
2. Go to **Streamlit Cloud** and create a new app.
3. Select your repository and deploy.
4. Add API keys in **Streamlit Secrets**.

## 🤝 Contributing

Want to improve DeepDiet? Fork the repo and submit a PR! 💡
