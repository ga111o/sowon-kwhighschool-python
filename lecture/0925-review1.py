# pip install requests beautifulsoup4


import requests
from bs4 import BeautifulSoup

# 웹 페이지 URL
url = 'https://example.com'

# 웹 페이지 요청
response = requests.get(url)

# 요청이 성공했는지 확인
if response.status_code == 200:
    # 페이지 내용을 파싱
    soup = BeautifulSoup(response.text, 'html.parser')

    # 필요한 데이터 추출 (예: 모든 링크)
    links = soup.find_all('a')

    # 링크를 저장할 리스트와 set
    link_list = []
    link_set = set()

    for link in links:
        href = link.get('href')
        if href:  # href가 None이 아닐 경우
            # 리스트에 추가
            link_list.append(href)
            # set에 추가 (중복 제거)
            link_set.add(href)

    # 결과 출력
    print("리스트에 저장된 링크:")
    print(link_list)

    print("\nset에 저장된 링크 (중복 제거):")
    print(link_set)

else:
    print(f"웹 페이지 요청 실패: {response.status_code}")
