from sklearn.datasets import fetch_california_housing

# 데이터 로드
data = fetch_california_housing()
X = data.data
y = data.target

# 중간 소득과 집 가격을 리스트로 변환
median_income_list = X[:, 0].tolist()  # 'MedInc'는 첫 번째 열
house_prices_list = y.tolist()

# 중간 소득 리스트를 txt 파일로 저장
with open('median_income.txt', 'w') as f:
    for value in median_income_list:
        f.write(f"{value}\n")

# 집 가격 리스트를 txt 파일로 저장
with open('house_prices.txt', 'w') as f:
    for value in house_prices_list:
        f.write(f"{value}\n")

print("파일 저장 완료!")
