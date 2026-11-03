# week09 - 박스오피스 1위 영화 조회

## 무엇을 하는 코드인가
영화진흥위원회(KOBIS) 오픈 API를 이용해 특정 날짜(`YYYYMMDD`)의 박스오피스 1위 영화 제목을 출력합니다.

## 설치
```bash
pip install -r requirements.txt
```
그리고 같은 폴더에 `secret.py`를 만들어 KOBIS API 키를 넣습니다. (이 파일은 공유하지 마세요.)
```python
API_KEY = "발급받은_API_키"
```

## 실행
```bash
python main.py
```
조회할 날짜를 바꾸려면 `main.py`에 있는 날짜 문자열을 수정하세요.
