# 프로젝트 계획: Gemini API 기반 블로그 콘텐츠 자동 생성기

## 목적
- Google Gemini API를 활용하여 블로그 제목에 맞는 콘텐츠 자동 생성
- 생성된 콘텐츠를 네이버 블로그에 자동으로 업로드하는 시스템 구축

## 참고 자료
 - Gemini API 문서: https://ai.google.dev/gemini-api/docs/get-started/tutorial?hl=ko&lang=python

## 파일 구조
- `/data/sample_data.py`: 테스트용 블로그 제목 샘플 데이터 생성
- `/docs/data.xlsx`: 블로그 제목(A열)과 생성된 콘텐츠(B열) 저장
- `/naver/gemini_test.py`: Gemini API 연동 테스트
- `/naver/create_contents.py`: Gemini API로 블로그 콘텐츠 자동 생성
- `/naver/auto_write.py`: Selenium으로 네이버 블로그 자동 글쓰기

## 구현 단계

### 1. 샘플 데이터 생성 (`sample_data.py`)
- 목적: 후킹성 블로그 제목 샘플 10개가 포함된 data.xlsx 자동 생성
- 사용 라이브러리: openpyxl
- 주요 기능:
  - data.xlsx 파일 생성
  - A1: '제목', B1: '내용' 헤더 입력
  - A2~A11: 후킹성 블로그 제목 10개 입력
  - B열은 내용 입력을 위한 빈칸으로 유지

### 2. Gemini API 연동 (`gemini_test.py`)
- 목적: Google Gemini API 연동 테스트
- 주요 설정:
  - 모델: gemini-2.0-flash
  - API 키 사용
- 기능: API 연동 테스트 및 응답 확인

### 3. 콘텐츠 자동 생성 (`create_contents.py`)
- 목적: Gemini API를 활용하여 블로그 제목에 맞는 콘텐츠 자동 생성
- 주요 기능:
  - /docs/data.xlsx 파일에서 A열의 블로그 제목 읽기
  - 각 제목마다 서론/본론/결론 구조의 블로그 콘텐츠 생성
  - 생성된 콘텐츠를 엑셀 B열에 저장
  - 진행상황 출력 및 결과 저장

### 4. 네이버 블로그 자동 업로드 (`auto_write.py`)
- 목적: Selenium을 활용한 네이버 블로그 자동 글쓰기
- 주요 기능:
  1. 네이버 로그인 자동화:
     - 네이버 로그인 페이지 접속
     - 아이디/비밀번호 입력 (봇 탐지 우회 기법 적용)
     - 로그인 버튼 클릭

  2. 블로그 글쓰기 자동화:
     - 블로그 글쓰기 페이지 접속
     - iframe 전환 및 팝업 처리
     - 제목 및 내용 입력 (ActionChains 사용, 랜덤 타이핑 지연 적용)
     - 저장 버튼 클릭
     
  3. 데이터 처리:
     - /docs/data.xlsx 파일의 2행부터 마지막 행까지 순차적으로 처리
     - 각 행의 제목(A열)과 내용(B열)을 블로그에 게시

## 실행 방법
1. 샘플 데이터 생성: `python data/sample_data.py`
2. 콘텐츠 생성: `python naver/create_contents.py`
3. 블로그 자동 업로드: `python naver/auto_write.py`

## 주의사항
- 네이버 로그인 시 자동화 봇 탐지를 피하기 위한 특수 기법 적용 필요
- API 키 및 로그인 정보는 보안에 유의
- 자동화 스크립트 실행 시 충분한 대기 시간 설정 필요 