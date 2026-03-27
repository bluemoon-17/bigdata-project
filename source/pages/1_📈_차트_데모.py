import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="차트 분석", layout="wide")
st.title("📈 시계열 및 항목별 차트 분석")

# 가상 데이터 생성
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['매출', '비용', '이익']
)

col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 선 그래프 (추이)")
    st.line_chart(chart_data)

with col2:
    st.subheader("🟦 막대 그래프 (비교)")
    st.bar_chart(chart_data)

st.info("💡 위 차트는 실시간으로 생성된 가상 데이터이며, 마우스를 올리면 수치를 확인할 수 있습니다.")