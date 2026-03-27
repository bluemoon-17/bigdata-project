import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="통계 분석", layout="wide")
st.title("📊 누적 통계 및 데이터 요약")

# 데이터 생성
data = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['A팀', 'B팀', 'C팀']
)

st.subheader("🌊 누적 영역 차트 (비중 변화)")
st.area_chart(data)

st.divider()

st.subheader("📋 데이터 요약 정보")
col1, col2 = st.columns([1, 2])

with col1:
    st.write("**기초 통계량**")
    st.dataframe(data.describe())

with col2:
    st.write("**전체 데이터셋**")
    st.dataframe(data, use_container_width=True)