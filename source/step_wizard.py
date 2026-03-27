import streamlit as st

st.set_page_config(page_title="단계별 입력", page_icon="📝")
st.title('📝 단계별 정보 입력')

# ---- 1. 상태 초기화 ----
# 필요한 모든 변수들을 미리 session_state에 만들어둡니다.
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'name' not in st.session_state:
    st.session_state.name = ""
if 'age' not in st.session_state:
    st.session_state.age = 20
if 'interests' not in st.session_state:
    st.session_state.interests = []

# ---- 2. 진행률 표시 ----
progress = st.session_state.step / 3
st.progress(progress, text=f'현재 단계: Step {st.session_state.step} / 3')

# ---- Step 1: 기본 정보 ----
if st.session_state.step == 1:
    st.subheader('Step 1: 기본 정보')
    # key를 설정하면 사용자가 입력한 값이 자동으로 session_state에 저장됩니다.
    name = st.text_input('이름', value=st.session_state.name, key='temp_name')
    age = st.number_input('나이', min_value=1, max_value=100, value=st.session_state.age, key='temp_age')
    
    if st.button('다음 →'):
        if name: 
            st.session_state.name = name
            st.session_state.age = age
            st.session_state.step = 2
            st.rerun() 
        else:
            st.warning('이름을 입력해주세요.')

# ---- Step 2: 관심 분야 ----
elif st.session_state.step == 2:
    st.subheader('Step 2: 관심 분야')
    interests = st.multiselect(
        '관심 분야를 선택하세요 (중복 선택 가능)',
        ['데이터 분석', '웹 개발', 'AI/ML', '모바일', '게임', '보안'],
        default=st.session_state.interests
    )
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button('← 이전'):
            st.session_state.interests = interests # 현재 선택값 저장 후 이동
            st.session_state.step = 1
            st.rerun()
    with col2:
        if st.button('다음 →'):
            if interests:
                st.session_state.interests = interests
                st.session_state.step = 3
                st.rerun()
            else:
                st.warning('최소 하나 이상의 관심 분야를 선택해주세요.')

# ---- Step 3: 확인 및 제출 ----
elif st.session_state.step == 3:
    st.subheader('Step 3: 입력 확인')
    
    # 세션 스테이트에 저장된 실제 값을 가져와서 표시
    st.info("입력하신 내용이 맞는지 확인해주세요.")
    st.write(f"**👤 이름**: {st.session_state.name}")
    st.write(f"**🎂 나이**: {st.session_state.age}세")
    st.write(f"**💡 관심 분야**: {', '.join(st.session_state.interests)}")
    
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button('← 이전'):
            st.session_state.step = 2
            st.rerun()
    with col2:
        if st.button('✅ 제출하기'):
            st.balloons()
            st.success('제출이 완료되었습니다!')
            
            # 모든 데이터 초기화 버튼 (선택 사항)
            if st.button('새로 작성하기'):
                for key in list(st.session_state.keys()):
                    del st.session_state[key]
                st.rerun()