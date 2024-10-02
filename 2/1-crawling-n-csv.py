import requests  # HTTP 요청을 보내기 위한 라이브러리
from bs4 import BeautifulSoup  # HTML 파싱을 위한 라이브러리
import matplotlib.pyplot as plt  # 그래프를 그리기 위한 라이브러리
import csv  # CSV 파일을 위한 라이브러리

# 1. 데이터 가져오기
url = "http://3.34.29.189:3000/n/5000"
response = requests.get(url)  # URL에 GET 요청을 보내고 응답을 받음

# 2. HTML 파싱
# 받은 HTML 응답을 BeautifulSoup으로 파싱. 그저 텍스트 데이터를 HTML 객체로 바꾸는 것.
soup = BeautifulSoup(response.text, 'html.parser')

# 3. 데이터 추출
data_pairs = []  # 소득과 집값을 저장할 리스트 초기화

house_price = None  # 집값을 저장할 변수를 초기화
for p in soup.find_all('p'):  # 모든 <p> 태그에 대해 반복
    text = p.get_text()  # <p> 태그의 텍스트 내용 추출
    if "House Price" in text:  # 텍스트에 House Price가 포함되어 있는지 확인
        # ": "로 나누고 첫 번째 부분에서 집값을 추출
        house_price = float(text.split(": ")[1].split(" ")[0])  # 숫자 부분만 -
    elif "Income" in text:  # 텍스트에 Income이 포함되어 있는지 확인
        # ": "로 나누고 첫 번째 부분에서 소득을 추출
        income = float(text.split(": ")[1].split(" ")[0])  # 천만 원 단위로 변환
        if house_price is not None:  # 이전에 집값이 설정되어 있으면 소득과 집값 piar를 리스트에 추가
            data_pairs.append((income, house_price))  # 튜플 형태로 저장


print(data_pairs)  # 전체 데이터 쌍

###########################################################################################

# csv: Comma-Separated Values

# writerow <<< 리스트 받아서 저장
# writerows <<< 2차원 리스트 받아서 저장

# CSV 파일로 저장
with open('income_house_price.csv', mode='w', newline='') as file:  # 파일을 write 모드로 열기
    writer = csv.writer(file)
    writer.writerow(['Income (천만 원)', 'House Price (억 원)'])  # 헤더 (첫 번째 행) 작성
    writer.writerows(data_pairs)
