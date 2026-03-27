import streamlit as st
import pandas as pd
import numpy as np

# ---- 1. 페이지 설정 ----
st.set_page_config(page_title='기초 EDA 대시보드 Pro', layout='wide')
st.title('📊 기초 EDA 대시보드')

# ---- 2. 데이터 생성 (가상 데이터) ----
@st.cache_data # 데이터를 캐싱하여 페이지 조작 시 속도를 높임
def load_data():
    np.random.seed(42)
    data = pd.DataFrame({
        '날짜': pd.date_range('2026-01-01', periods=100),
        '카테고리': np.random.choice(['전자제품', '의류', '식품'], 100),
        '매출': np.random.randint(100, 1000, 100),
        '고객수': np.random.randint(10, 200, 100),
        '전환율': np.random.uniform(0.01, 0.20, 100).round(4)
    })
    return data

df=load_data()

# ---- 3. 사이드바: 필터 ----
st.sidebar.header('🔍 데이터 필터')

# 카테고리 필터
selected_category=st.sidebar.selectbox(
    '카테고리 선택',
    ['전체'] + list(df['카테고리'].unique())
)

# 데이터 개수 필터 (슬라이더)
data_range=st.sidebar.slider('데이터 표시 범위 (행)', 10, 100, 100)

# ---- 4. 데이터 필터링 로직 ----
filtered_df=df.head(data_range)

if selected_category != '전체':
    filtered_df=filtered_df[filtered_df['카테고리'] == selected_category]

st.sidebar.write('---')
st.sidebar.write(f'✅ 필터링된 데이터: **{len(filtered_df)}행**')

# ---- 5. 메인 레이아웃: 탭 구성 ----
tab1, tab2 = st.tabs(['📈 요약 대시보드', '📄 원본 데이터'])

with tab1:
    # KPI 지표 (3열 구성)
    st.subheader('📌 핵심성과지표 (KPI)')
    kpi1, kpi2, kpi3=st.columns(3)
    
    with kpi1:
        total_sales=filtered_df['매출'].sum()
        avg_sales=filtered_df['매출'].mean()
        st.metric('총 매출', f"₩{total_sales:,}만", f"평균 {avg_sales:.0f}")
        
    with kpi2:
        total_cust=filtered_df['고객수'].sum()
        avg_cust=filtered_df['고객수'].mean()
        st.metric('총 고객수', f"{total_cust:,}명", f"평균 {avg_cust:.0f}")
        
    with kpi3:
        avg_conv=filtered_df['전환율'].mean()
        std_conv=filtered_df['전환율'].std()
        st.metric('평균 전환율', f"{avg_conv:.2%}", f"표준편차 {std_conv:.2%}")

    st.write('---')

    # 차트 섹션 (2열 구성)
    col1, col2=st.columns(2)
    
    with col1:
        st.subheader('📅 일별 매출 추이')
        chart_data=filtered_df.groupby('날짜')['매출'].sum()
        st.line_chart(chart_data)
        
    with col2:
        st.subheader('🛍️ 카테고리별 매출 비중')
        category_data=filtered_df.groupby('카테고리')['매출'].sum()
        st.bar_chart(category_data)

with tab2:
    st.subheader('📑 상세 데이터 보기')
    
    # CSV 다운로드 버튼 추가
    csv=filtered_df.to_csv(index=False).encode('utf-8-sig') # 한글 깨짐 방지 sig
    st.download_button(
        label="📥 필터링된 데이터 다운로드 (CSV)",
        data=csv,
        file_name='eda_filtered_data.csv',
        mime='text/csv',
    )
    
    st.dataframe(filtered_df, use_container_width=True, height=400)
    
    # 기술통계 Expander
    with st.expander('📊 데이터 기술통계 요약 보기'):
        st.dataframe(filtered_df.describe().T) # 행/열 전치하여 보기 편하게 제공