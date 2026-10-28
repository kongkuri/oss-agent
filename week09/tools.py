"""tools.py - 박스오피스 API를 이용하여 영화 정보를 가져오는 도구 모음"""

import requests
from secret import API_KEY
BASE_URL = ("https://www.kobis.or.kr/kobisopenapi/webservice/"
            "rest/boxoffice/searchDailyBoxOfficeList.json")
def get_boxoffice_rank_1(date):
    """
    그 날짜의 박스오피스 1위 영화 제목을 알려준다
    받는 것 : date (str) : YYYYMMDD 형식의 날짜 예:(20260824)
    돌려주는 것 : str : 1위 영화 제목 예 : "오디세이"
    """

    params = {"key": API_KEY, "targetDt": date}
    response = requests.get(BASE_URL, params=params, timeout=10)
    data = response.json()
    movies = data["boxOfficeResult"]["dailyBoxOfficeList"]
    return movies[0]['movieNm']