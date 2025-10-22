import sqlite3
import pandas as pd

# SQLite DB 연결
conn = sqlite3.connect('./final.db')

# SQL 쿼리 실행하여 데이터 가져오기
query = "SELECT MCT_NAVER_NAME, MCT_TYPE, keywords FROM Information WHERE MCT_NAVER_NAME IS NOT NULL AND MCT_TYPE IS NOT NULL AND keywords IS NOT NULL"
df = pd.read_sql_query(query, conn)

# CSV 파일로 저장
df.to_csv('output.csv', index=False, encoding='utf-8-sig')

# 연결 종료
conn.close()

print("good!")
