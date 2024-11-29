# 제가 csv를 드릴게요. 이건 주변 음식점과 음식점 리뷰가 담긴 csv예요.

# name, type, review가 들어있죠.

# 유저가 "달달한 디저트"를 검색하면, 달달한 디저트를 파는 곳을 알려주는 서비스를 만들어 볼게요.

# 이러한 서비스를 만들기 위해선 우선...

# 1. csv의 데이터들 임베딩을 해야겠죠?

import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

# Load model and data
model = SentenceTransformer("upskyy/bge-m3-korean")
df = pd.read_csv('./jeju.csv')

sentences = []
embeddings = []
for _, row in df.iterrows():
    sentence = f"{row['type']} - {row['review']}"
    sentences.append(sentence)

    embedding = model.encode(sentence)
    embeddings.append(embedding)
    print(_)

df['embeddings'] = embeddings

# 유저 입력의 임베딩 생성
user_input = "바다가 보이는 디저트 카페"
user_embedding = model.encode(user_input)

# 각 임베딩과 유저 입력 임베딩 간의 유사도 계산
similarities = []
for embedding in df['embeddings']:
    similarity = model.similarity(user_embedding, embedding)

    similarity_value = similarity.item()  # similarity.item()을 사용하여 텐서에서 실제 숫자 값을 추출

    similarities.append(similarity_value)

    print(similarity_value)


# 유사도가 가장 높은 상위 5개 가게 추출
# similarities 리스트를 numpy 배열로 변환
similarities = np.array(similarities)

# argsort()로 similarities 배열을 정렬했을 때의 인덱스를 반환
# [-5:]로 가장 큰 5개의 값의 인덱스를 선택
# [::-1]로 내림차순 정렬 (가장 큰 값이 먼저 오도록)
top5 = similarities.argsort()[-5:][::-1]

# df.loc를 사용해 top5_indices에 해당하는 행들을 선택
# ['name', 'type', 'review'] 컬럼만 선택해서 새로운 데이터프레임 생성
top5_restaurants = df.loc[top5, ['name', 'type', 'review']]

print(top5_restaurants)

# 좋아요. 여러분은 "바다가 보이는 디저트 카페"라는 인간만이 알아들을 수 있는 말을 컴퓨터가 알아들을 수 있도록 하고,
# 이랑 비슷한 값들을 찾아내게 되었습니다.

# 그럼 오늘 수업은 여기까지 할게요. 수고하셨습니다.
