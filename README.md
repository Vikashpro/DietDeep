🍽️ DeepDiet: AI-Powered Nutrition Guide

DeepDiet is an AI-driven meal planning and nutrition analysis tool that helps users generate personalized diet plans based on their dietary goals and uploaded meal images. It leverages state-of-the-art AI models for food recognition and meal planning.
🚀 Features

    🥗 AI-Powered Meal Planning – Generates personalized meal plans using DeepSeek-R1.
    📸 Food Recognition – Uses a YOLOv10 model to analyze uploaded meal images.
    🔬 Nutritional Analysis – Fetches nutrition facts from the USDA API.
    📝 Goal-Based Customization – Users can input dietary preferences (e.g., high-protein, low-carb).
    🏋️ Health Optimization – Suggests portion sizes and balanced meals.

🛠️ Tech Stack

    Frontend: Streamlit
    AI Models: DeepSeek-R1 (Meal Plan Generation), YOLOv10 (Food Recognition)
    APIs: USDA Food Data API
    Backend Processing: OpenAI API, NumPy, OpenCV, Requests

🚀 Installation & Setup
1️⃣ Clone the Repository

git clone https://github.com/your-username/DeepDiet.git
cd DeepDiet

2️⃣ Set Up Virtual Environment

pip install virtualenv
virtualenv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Set Up API Keys

Create a .streamlit folder and add a file secrets.toml with the following content:

AIMLAPI_KEY="YOUR_AIMLAPI_KEY"
USDA_API_KEY="YOUR_USDA_API_KEY"

Replace YOUR_AIMLAPI_KEY and YOUR_USDA_API_KEY with your actual API keys.
▶️ Running the App

streamlit run app.py

Open your browser and go to http://localhost:8501 to use the app.
🚀 Deployment on Streamlit Cloud

    Push this project to GitHub.
    Go to Streamlit Cloud and create a new app.
    Select your repository and deploy.
    Add API keys in Streamlit Secrets.

🤝 Contributing

Want to improve DeepDiet? Feel free to fork the repo and submit a pull request!
📜 License

This project is open-source and available under the MIT License.

Let me know if you'd like any changes! 🚀