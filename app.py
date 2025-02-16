import streamlit as st
import cv2
import numpy as np
import requests
from ultralytics import YOLO
from openai import OpenAI

# AIMLAPI Credentials
API_KEY = st.secrets["AIMLAPI_KEY"]
USDA_API_KEY = st.secrets["USDA_API_KEY"]

client = OpenAI(
    base_url="https://api.aimlapi.com/v1",
    api_key=API_KEY,
)

# Load YOLOv10 model
model = YOLO("yolov8n.pt")  # Use correct model path

st.title("DietDeep: AI-Powered Meal Planner")

st.write("### Enter Your Dietary Goals")
goal = st.text_input("Example: 'I want a high-protein diet' or 'I need a low-carb diet'")

uploaded_file = st.file_uploader("Upload a Meal Image", type=["jpg", "jpeg", "png"])

def get_nutrition(food_name):
    """Fetch nutrition data from USDA API."""
    url = f"https://api.nal.usda.gov/fdc/v1/foods/search?query={food_name}&api_key={USDA_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data["foods"]:
            return data["foods"][0]["foodNutrients"]
    return None

if st.button("Generate Meal Plan"):
    if goal:
        st.write("Generating your personalized meal plan...")
        detected_foods = []

        if uploaded_file is not None:
            file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
            img = cv2.imdecode(file_bytes, 1)
            results = model(img)

            for r in results:
                for det in r.boxes.data.tolist():
                    x1, y1, x2, y2, conf, cls = det
                    detected_foods.append(model.names[int(cls)])
            
            st.image(img, caption="Detected Foods", use_container_width=True)
            st.write("### Detected Foods:")
            st.write(", ".join(set(detected_foods)))

        # Fetch nutrition data
        nutrition_data = {}
        for food in set(detected_foods):
            nutrition_data[food] = get_nutrition(food)

        # Generate meal plan using AI
        messages = [
            {"role": "system", "content": "You are a nutrition expert."},
            {"role": "user", "content": f"Based on {goal} and detected foods: {', '.join(set(detected_foods))}, generate a meal plan (Breakfast, Lunch, Dinner, Snacks) with portion sizes and nutritional values."}
        ]

        try:
            response = client.chat.completions.create(
                model="deepseek/deepseek-r1",
                messages=messages,
                max_tokens=1000
            )
            meal_plan = response.choices[0].message.content.strip()
            st.subheader("Your Personalized Meal Plan:")
            st.write(meal_plan)
        except Exception as e:
            st.error(f"Error fetching meal plan: {e}")
    else:
        st.error("Please enter your dietary goals.")
