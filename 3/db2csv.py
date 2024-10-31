import sqlite3
import pandas as pd

conn = sqlite3.connect('jeju2.db')

query = """
SELECT MCT_NAVER_NAME, UE_AMT_GRP, keywords 
FROM Information 
WHERE MCT_NAVER_NAME IS NOT NULL 
AND MCT_TYPE IS NOT NULL 
AND keywords IS NOT NULL
AND UE_AMT_GRP IS NOT NULL
"""

df = pd.read_sql_query(query, conn)

df.to_csv('matzip_info.csv', index=False, encoding='utf-8-sig')

conn.close()
