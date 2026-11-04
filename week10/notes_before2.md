# week09/tools.py 함수 설명

## 파일 개요

`tools.py`는 영화진흥위원회(KOBIS) 오픈 API를 호출해 박스오피스 정보를 가져오는 도구 모음입니다.

- 외부 라이브러리: `requests` (HTTP 요청)
- API 키: `secret.py`에서 `API_KEY`를 import
- `BASE_URL`: KOBIS 일별 박스오피스 조회 API 주소 (`searchDailyBoxOfficeList.json`)

## 함수 목록

| 함수 | 설명 |
|------|------|
| `get_boxoffice_rank_1(date)` | 지정한 날짜의 박스오피스 1위 영화 제목을 돌려준다 |

## `get_boxoffice_rank_1(date)`

- **매개변수**: `date` (str) — `YYYYMMDD` 형식의 날짜 (예: `"20260824"`)
- **반환값**: str — 그 날짜 1위 영화 제목 (예: `"오디세이"`)

**동작 과정**

1. API 키(`key`)와 조회 날짜(`targetDt`)로 요청 파라미터를 만든다.
2. `requests.get(BASE_URL, params=params, timeout=10)`으로 API를 호출한다.
3. 응답을 JSON으로 바꾼 뒤 `data["boxOfficeResult"]["dailyBoxOfficeList"]`에서 영화 목록을 꺼낸다.
4. 첫 번째 영화(`movies[0]`)의 `movieNm` 값을 반환한다.

**사용 예**

```python
from tools import get_boxoffice_rank_1

print(get_boxoffice_rank_1("20260824"))  # 예: 오디세이
```

## 주의할 점

- 예외 처리가 없어서 API 키 오류, 잘못된 날짜, 빈 결과 목록일 때 `KeyError` 또는 `IndexError`가 발생할 수 있다.
- HTTP 응답 상태 코드를 확인하지 않는다.
- `secret.py` 파일과 그 안의 `API_KEY`가 있어야 실행된다.
