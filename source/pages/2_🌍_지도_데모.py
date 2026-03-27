import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="지도 데모", layout="wide")
st.title("🌍 위치 기반 데이터 분석")

# 서울 시청 인근 가상 좌표 생성
df_map = pd.DataFrame(
    np.random.randn(100, 2) / [80, 80] + [37.5665, 126.9780],
    columns=['lat', 'lon']
)

st.write("📍 서울 중심부의 주요 지점 분포도")
st.map(df_map)

st.success(f"현재 지도에 표시된 지점 개수: {len(df_map)}개")