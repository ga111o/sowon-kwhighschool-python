import pandas as pd
import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")  # 수업 땐 직접 api key를 붙여넣기 하도록

genai.configure(api_key=api_key)

genai.GenerationConfig(
    max_output_tokens=1000,
    temperature=0.1,
)

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(
    f"""tell me a joke""")

print(response.text)
