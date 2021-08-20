# 더닝크루거 곡선
# 외부 모듈(라이브러리)
# pip install 모듈
# pip install 모듈==1.0.0
# beautiful Soup. -> html parser.



# alias python=python3
# alias pip=pip3

from urllib import request
from bs4 import BeautifulSoup

content = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109")
soup = BeautifulSoup(content, 'html.parser')

# for data in soup.select("data"):
#     print("시간: ", data.select_one("tmef").string)
#     print("날씨: ", data.select_one("wf").string)
#     print("-" * 20)

'''
결과값
--------------------
시간:  2021-08-28 00:00
날씨:  흐림
--------------------
'''

for location in soup.select("location"):
    print("도시: ", location.select_one("city").string)
    print("날씨: ", location.select_one("wf").string)
    print("최저기온: ", location.select_one("tmn").string)
    print("최고기온: ", location.select_one("tmx").string)
    print()

