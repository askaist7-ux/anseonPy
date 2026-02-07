# Flask 템플릿 프로젝트

간단한 Flask 웹 애플리케이션입니다.

## 설치 및 실행

### 1. 가상환경 생성
```bash
python -m venv venv
```

### 2. 가상환경 활성화
**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 3. 의존성 설치
```bash
pip install -r requirements.txt
```

### 4. 애플리케이션 실행
```bash
python app.py
```

브라우저에서 `http://localhost:5000` 접속

## 배포

Railway에 배포하기:

1. [Railway.app](https://railway.app) 회원가입
2. GitHub 저장소 선택
3. Railway가 자동으로 배포

## 구조

```
anseonPy/
├── app.py              # Flask 애플리케이션
├── test_app.py         # 테스트 코드
├── requirements.txt    # Python 의존성
├── Procfile           # 배포 설정
├── runtime.txt        # Python 버전
├── .gitignore         # Git 무시 파일
└── templates/
    └── index.html     # 웹페이지
```

## 기능

- 🏠 메인 페이지 (index.html)
- 🔗 네이버 이동 링크
- 🔵 API 테스트 엔드포인트
- 🎨 반응형 디자인

## 라이선스

MIT
