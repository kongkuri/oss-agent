# week09/tools.py 분석 노트

## 개요

`tools.py`는 영화진흥위원회(KOBIS) 오픈 API로 박스오피스 정보를 가져오는 도구 모음입니다.

- 사용하는 라이브러리: `requests`
- API 키: `secret.py`의 `API_KEY`를 불러와 사용
- 요청 주소(`BASE_URL`): KOBIS 일별 박스오피스 조회 API (`searchDailyBoxOfficeList.json`)

## 함수 목록

### `get_boxoffice_rank_1(date)`

지정한 날짜에 박스오피스 1위를 한 영화의 제목을 돌려줍니다.

| 항목 | 내용 |
|------|------|
| 입력 | `date` (str): `YYYYMMDD` 형식의 날짜 (예: `"20260824"`) |
| 출력 | str: 1위 영화 제목 (예: `"오디세이"`) |

**동작 순서**

1. `key`(API 키)와 `targetDt`(날짜)를 요청 파라미터로 만든다.
2. `requests.get`으로 API를 호출한다 (타임아웃 10초).
3. 응답 JSON에서 `boxOfficeResult` → `dailyBoxOfficeList` 목록을 꺼낸다.
4. 목록의 첫 번째 항목(1위)의 `movieNm`(영화 제목)을 돌려준다.

## 참고 사항

- 파일에 있는 함수는 `get_boxoffice_rank_1` 하나입니다.
- 오류 처리가 없습니다. 날짜 형식이 틀렸거나, API 키가 잘못됐거나, 결과 목록이 비어 있으면 `KeyError`나 `IndexError`가 날 수 있습니다.
- HTTP 상태 코드를 확인하지 않습니다(`response.raise_for_status()` 호출 없음).
