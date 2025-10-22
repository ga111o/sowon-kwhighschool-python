import pandas as pd

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
