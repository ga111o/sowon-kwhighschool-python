import requests  # HTTP 요청을 보내기 위한 라이브러리
from bs4 import BeautifulSoup  # HTML 파싱을 위한 라이브러리
import matplotlib.pyplot as plt  # 그래프를 그리기 위한 라이브러리
import csv  # CSV 파일을 위한 라이브러리

# 1. 데이터 가져오기
url = "http://15.164.147.7:3000"
response = requests.get(url)  # URL에 GET 요청을 보내고 응답을 받음

# 2. HTML 파싱
# 받은 HTML 응답을 BeautifulSoup으로 파싱. 그저 텍스트 데이터를 HTML 객체로 바꾸는 것.
soup = BeautifulSoup(response.text, 'html.parser')

# 3. 데이터 추출
data_pairs = []  # 소득과 집값을 저장할 리스트 초기화

house_price = None  # 집값을 저장할 변수를 초기화
for p in soup.find_all('p'):  # 모든 <p> 태그에 대해 반복
    text = p.get_text()  # <p> 태그의 텍스트 내용 추출
    print(type(text))
    if "House Price" in text:  # 텍스트에 "House Price"가 포함되어 있는지 확인
        # ": "로 나누고 첫 번째 부분에서 집값을 추출
        house_price = float(text.split(": ")[1].split(" ")[0])  # 억 원 단위로 변환
    elif "Income" in text:  # 텍스트에 "Income"이 포함되어 있는지 확인
        # ": "로 나누고 첫 번째 부분에서 소득을 추출
        income = float(text.split(": ")[1].split(" ")[0])  # 천만 원 단위로 변환
        if house_price is not None:  # 이전에 집값이 설정되어 있으면
            # 소득과 집값의 쌍을 리스트에 추가
            data_pairs.append((income, house_price))


print(data_pairs)  # 전체 데이터 쌍을 출력


# 소득과 집값을 각각의 리스트로 분리
incomes = [pair[0] for pair in data_pairs]
house_prices = [pair[1] for pair in data_pairs]
# incomes, house_prices = zip(*data_pairs)  # 이러한 방법도 있음. unpacking을 통해 각각의 리스트로 변환


# 그래프 그리기
plt.figure(figsize=(10, 6))  # 그래프 크기 설정
plt.scatter(incomes, house_prices, color='blue', marker='o')  # 산점도 그래프
plt.title("House prices based on income")
plt.xlabel("Income")
plt.ylabel("House Price")
plt.grid(True)

# 각 점에 레이블 추가
for i in range(len(data_pairs)):  # 데이터 쌍 전체에 대해 반복
    plt.annotate(f"{house_prices[i]}", (incomes[i], house_prices[i]),  # 각 점에 집값 레이블 추가
                 textcoords="offset points", xytext=(0, 5), ha='center')  # 레이블 위치 조정

plt.show()  # 그래프 표시
