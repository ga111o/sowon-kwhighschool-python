import pandas as pd
import google.generativeai as genai
import os  # 수업 땐 직접 api key를 붙여넣기 하도록
from dotenv import load_dotenv  # ""

load_dotenv()


######################################################################################

file_path = './matzip_info.csv'
data = pd.read_csv(file_path)

top_10_restaurants = data[data['매출_비율'] == '상위_10']

restaurants = []

for index, row in top_10_restaurants.iterrows():  # .iterrows <<< 판다스에서, 각 행을 하나씩 순회해서 튜플로 반환
    print(f"음식점 이름: {row['음식점_이름']}, 키워드: {row['키워드']}")
    restaurants.append({
        'name': row['음식점_이름'],
        'keyword': row['키워드']
    })

print(restaurants)

######################################################################################


api_key = os.getenv("GEMINI_API_KEY")  # 수업 땐 직접 api key를 붙여넣기 하도록

genai.configure(api_key=api_key)

genai.GenerationConfig(
    max_output_tokens=1000,
    temperature=0.1,
)

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(
    f"""
    아래 제공한 건 맛집 리스트야. 바다가 보이는 횟집 추천해줘.
    
    {restaurants}""", stream=True)

# print(response.text)


for chunk in response:
    print(chunk.text)
