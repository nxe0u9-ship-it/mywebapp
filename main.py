st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gamja+Flower&family=Jua&display=swap');

/* 전체 기본 폰트 */
html, body, [class*="css"], .stApp {
    font-family: 'Jua', sans-serif;
}

/* 제목 */
.main-title {
    text-align: center;
    font-size: 46px;
    font-weight: 800;
    color: #ff6f91;
    margin-top: 10px;
    margin-bottom: 5px;
    font-family: 'Jua', sans-serif;
}

.sub-title {
    text-align: center;
    color: #9c7d8b;
    font-size: 20px;
    margin-bottom: 28px;
    font-family: 'Gamja Flower', cursive;
}

/* MBTI 선택 안내 */
.question-box {
    background: rgba(255,255,255,0.8);
    padding: 22px;
    border-radius: 25px;
    text-align: center;
    box-shadow: 0px 5px 20px rgba(255, 137, 166, 0.12);
    margin-bottom: 15px;
    border: 2px solid #ffe1ea;
}

.question-title {
    color: #765866;
    font-size: 24px;
    font-family: 'Jua', sans-serif;
}

/* 여행지 카드 */
.travel-card {
    background: rgba(255,255,255,0.92);
    padding: 23px;
    border-radius: 25px;
    margin-top: 16px;
    margin-bottom: 16px;
    box-shadow: 0px 7px 20px rgba(183, 137, 165, 0.13);
    border: 2px solid #ffe4ed;
}

.travel-title {
    font-family: 'Jua', sans-serif;
    font-size: 27px;
    color: #ff7195;
    margin-bottom: 4px;
}

.travel-country {
    font-family: 'Gamja Flower', cursive;
    color: #a18391;
    font-size: 20px;
    margin-bottom: 10px;
}

.travel-description {
    font-family: 'Gamja Flower', cursive;
    color: #66525e;
    font-size: 21px;
    line-height: 1.6;
}

/* MBTI 결과 */
.mbti-result {
    text-align: center;
    padding: 20px;
    margin-top: 25px;
    margin-bottom: 18px;
    border-radius: 25px;
    background: linear-gradient(135deg, #ffdbe7, #f2e4ff);
    color: #795767;
    box-shadow: 0 5px 15px rgba(211, 147, 176, 0.15);
}

.mbti-big {
    font-family: 'Jua', sans-serif;
    font-size: 35px;
    color: #ff658c;
}

.tag {
    display: inline-block;
    background: #fff0f5;
    color: #e7698a;
    padding: 6px 12px;
    margin: 3px;
    border-radius: 20px;
    font-family: 'Gamja Flower', cursive;
    font-size: 18px;
}

/* 버튼 */
.stButton > button {
    width: 100%;
    border-radius: 25px;
    border: none;
    background: linear-gradient(90deg, #ff8fac, #cda8ff);
    color: white;
    font-family: 'Jua', sans-serif;
    font-size: 18px;
    padding: 12px;
}

/* selectbox 글씨 */
div[data-baseweb="select"] {
    font-family: 'Jua', sans-serif;
}

.footer {
    text-align: center;
    color: #af96a2;
    font-family: 'Gamja Flower', cursive;
    font-size: 17px;
    margin-top: 35px;
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)
