# https://ai.google.dev/gemini-api/docs/api-key
# api-key 받기
# api는 ... 요청을 보내고 받는 모든 것을 뜻해요.
# api-key는 그렇다고 막무가내로 사용하면 구글 서버가 터져나감 -> api key 사용하도록
# pip3 install -U google-generativeai

import google.generativeai as genai
import os  # 수업 땐 직접 api key를 붙여넣기 하도록
from dotenv import load_dotenv  # ""

load_dotenv()


api_key = os.getenv("GEMINI_API_KEY")  # 수업 땐 직접 api key를 붙여넣기 하도록

genai.configure(api_key=api_key)

genai.GenerationConfig(
    max_output_tokens=1000,
    temperature=0.1,
)

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(
    "who are you?", stream=True)  # 스트림 없이 해서 바로 print(response.text) 먼저 한 후, stream = True

# print(response.text)


for chunk in response:
    print(chunk.text)
