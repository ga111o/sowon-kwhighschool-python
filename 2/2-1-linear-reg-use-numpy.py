import numpy as np
import matplotlib.pyplot as plt
import csv

# CSV 파일 읽기
income = []
house_price = []

with open('income_house_price.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # 헤더 건너뛰기
    for row in reader:
        income.append(float(row[0]))  # 첫 번째 열: Income
        house_price.append(float(row[1]))  # 두 번째 열: House Price

# 데이터 포인트 개수
n = len(income)

# 기울기(b1)와 절편(b0) 계산
x_mean = np.mean(income)
y_mean = np.mean(house_price)

# 기울기 계산
numerator = np.sum((income - x_mean) * (house_price - y_mean))
denominator = np.sum((income - x_mean) ** 2)
b1 = numerator / denominator

# 절편 계산
b0 = y_mean - b1 * x_mean

print(f"기울기 (b1): {b1}")
print(f"절편 (b0): {b0}")

# 회귀선 값 계산
predicted_price = b0 + b1 * income

# 결과 시각화
plt.scatter(income, house_price, color='blue', label='실제 데이터')
plt.plot(income, predicted_price, color='red', label='회귀선')
plt.xlabel('Income (천만 원)')
plt.ylabel('House Price (억 원)')
plt.title('선형 회귀')
plt.legend()
plt.show()
