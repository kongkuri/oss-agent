작성 : Claude Code / 확인: (이름)

# week09/tools.py 함수 정리💚

## 파일 개요💚

- 영화진흥위원회(KOBIS) 박스오피스 API로 영화 정보를 가져오는 도구 모음임💚
- `requests` 라이브러리로 API를 호출함💚
- API 키는 `secret.py`의 `API_KEY`에서 불러옴💚
- 요청 주소(`BASE_URL`)는 일별 박스오피스 조회 API(`searchDailyBoxOfficeList.json`)임💚

## 함수 목록💚

### `get_boxoffice_rank_1(date)`💚

- 역할 : 입력한 날짜의 박스오피스 1위 영화 제목을 알려줌💚
- 입력 : `date` (str), `YYYYMMDD` 형식의 날짜임 (예: `"20260824"`)💚
- 출력 : str, 1위 영화 제목임 (예: `"오디세이"`)💚
- 동작 순서💚
  1. `key`(API 키)와 `targetDt`(날짜)를 요청 파라미터로 만듦💚
  2. `requests.get`으로 API를 호출함 (제한 시간 10초)💚
  3. 응답을 JSON으로 바꿈💚
  4. `boxOfficeResult` → `dailyBoxOfficeList`에서 영화 목록을 꺼냄💚
  5. 목록의 첫 번째 영화(`movies[0]`)의 `movieNm`(영화 제목)을 돌려줌💚

## 참고 사항💚

- 함수는 현재 1개뿐임💚
- 오류 처리가 없음💚
  - 날짜 형식이 틀리거나 결과가 없으면 `KeyError` 또는 `IndexError`가 날 수 있음💚
  - 네트워크 오류나 시간 초과 시 `requests` 예외가 그대로 발생함💚
