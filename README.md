# 자연어처리기반 투자분석 및 예측시스템 개발

전 거래일의 기사 및 주가 data를 활용하여 다음 날의 주가 종가 상승하락을 예측하는 시스템 개발

한 종목의 주가를 예측하는 것이 아닌 한 주제의 종목들을 예측 (LG화학, SK이노베이션, 삼성SDI, 현대차)

감성 분류 모델 및 주가 상승 하락 모델 구축

전체적인 순서는 다음과 같다.


#### 1. 뉴스기사 수집
네이버 뉴스 검색창을 활용, 8개 경제지의 뉴스기사 1년치(191231 ~ 201231)를 크롤링하였다. (매일경제, 머니투데이, 서울경제, 아시아경제, 이데일리, 파이낸셜뉴스, 한국경제, 헤럴드경제)


https://github.com/brain4652/NLP_based_investment_forecasting_system


#### 2. 도메인 지식 학습
높은 정확성을 가진 데이터 구축을 위해 전기차 관련 도메인 지식을 학습했다.

https://github.com/brain4652/NLP_based_investment_forecasting_system


#### 3. 데이터 전처리
도메인 지식을 바탕으로 기사 문장의 긍부정 labeling 진행

https://github.com/brain4652/NLP_based_investment_forecasting_system

#### 4. 뉴스 감성분류를 위한 단어사전 구축
중복 어휘를 방지하기 위해 단어 통일 및 삭제 진행

https://github.com/brain4652/NLP_based_investment_forecasting_system
https://github.com/brain4652/NLP_based_investment_forecasting_system


