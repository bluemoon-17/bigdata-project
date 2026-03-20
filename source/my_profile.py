import streamlit as st
import pandas as pd

st.title('자기소개')

st.write('## 기본정보')
st.write('**이름**: 이현승')
st.write('**학과**: 인공지능 소프트웨어학과')
st.write('**학년**: 3학년')

st.write('---')

st.write('## 이번 학기 시간표')
schedule = pd.DataFrame({
    '요일':['월', '화', '수', '목', '금'],
    '오전':['인공지능 라이브러리', '기초 일본어', '-', '-', '자연어 처리'],
    '오후':['취업 영어', '인공지능 캡스톤 디자인', '-', '인공지능 서비스 프로젝트', '빅데이터 분석 프로젝트']
})
st.write(schedule)

st.write('## 관심 분야')
st.write('- JAVA')
st.write('- 모바일 앱 개발')
st.write('- 백 엔드')

st.write('---')

st.write('## 이번 학기 목표')
goals = pd.DataFrame({
    '목표':['졸업 작품 완성', '졸업', '편입 합격'],
    '달성률':[0, 0, 0]
})
st.write(goals)
st.bar_chart(goals.set_index('목표'))