import csv
import matplotlib.pyplot as plt

income = []
house_price = []

with open('income_house_price.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # 헤더 건너뛰기
    for row in reader:
        income.append(float(row[0]))  # 첫 번짹 칼럼
        house_price.append(float(row[1]))  # 두 번째 칼럼

# x변량 수
n = len(income)

# 평균
x_mean = sum(income) / n
y_mean = sum(house_price) / n

numerator = 0
denominator = 0

# b_1
for i in range(n):
    numerator += (income[i] - x_mean) * (house_price[i] - y_mean)
    denominator += (income[i] - x_mean) ** 2

b1 = numerator / denominator

# b_0
b0 = y_mean - b1 * x_mean

print(f"y = {b1}x + {b0}")

predicted_price = [b0 + b1 * x for x in income]

# 결과 시각화
plt.scatter(income, house_price, color='blue', label='real value', s=1)
plt.plot(income, predicted_price, color='red', label='linear regression line')
plt.xlabel('Income')
plt.ylabel('House Price')
plt.legend()
plt.show()
