import streamlit as st
import random

# --------------------------------------------------
# 페이지 기본 설정
# --------------------------------------------------
st.set_page_config(
    page_title="MBTI 여행지 추천 💕",
    page_icon="🌷",
    layout="centered"
)

# --------------------------------------------------
# CSS
# --------------------------------------------------
st.markdown("""
<style>

/* 전체 배경 */
.stApp {
    background: linear-gradient(
        135deg,
        #fff1f5 0%,
        #fff8e8 45%,
        #f3efff 100%
    );
}

/* 기본 글씨 */
html, body, [class*="css"] {
    font-family: "Pretendard", "Apple SD Gothic Neo", sans-serif;
}

/* 제목 */
.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    color: #ff6f91;
    margin-top: 10px;
    margin-bottom: 5px;
}

.sub-title {
    text-align: center;
    color: #8f7a86;
    font-size: 17px;
    margin-bottom: 28px;
}

/* MBTI 선택 안내 */
.question-box {
    background: rgba(255,255,255,0.75);
    padding: 20px;
    border-radius: 25px;
    text-align: center;
    box-shadow: 0px 5px 20px rgba(255, 137, 166, 0.12);
    margin-bottom: 15px;
    border: 2px solid #ffe1ea;
}

.question-title {
    color: #765866;
    font-size: 21px;
    font-weight: 700;
}

/* 여행 카드 */
.travel-card {
    background: rgba(255,255,255,0.90);
    padding: 22px;
    border-radius: 24px;
    margin-top: 15px;
    margin-bottom: 15px;
    box-shadow: 0px 7px 20px rgba(183, 137, 165, 0.13);
    border: 2px solid #ffe4ed;
    transition: 0.3s;
}

.travel-title {
    font-size: 24px;
    font-weight: 800;
    color: #ff7195;
    margin-bottom: 5px;
}

.travel-country {
    color: #9b8090;
    font-size: 15px;
    margin-bottom: 12px;
}

.travel-description {
    color: #66525e;
    font-size: 16px;
    line-height: 1.7;
}

/* MBTI 결과 */
.mbti-result {
    text-align: center;
    padding: 18px;
    margin-top: 25px;
    margin-bottom: 18px;
    border-radius: 25px;
    background: linear-gradient(
        135deg,
        #ffdbe7,
        #f2e4ff
    );
    color: #795767;
    box-shadow: 0 5px 15px rgba(211, 147, 176, 0.15);
}

.mbti-big {
    font-size: 32px;
    font-weight: 900;
    color: #ff658c;
}

/* 작은 태그 */
.tag {
    display: inline-block;
    background: #fff0f5;
    color: #e7698a;
    padding: 5px 11px;
    margin: 3px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 600;
}

/* 하단 */
.footer {
    text-align: center;
    color: #af96a2;
    font-size: 13px;
    margin-top: 35px;
    margin-bottom: 20px;
}

/* 버튼 */
.stButton > button {
    width: 100%;
    border-radius: 25px;
    border: none;
    background: linear-gradient(
        90deg,
        #ff8fac,
        #cda8ff
    );
    color: white;
    font-size: 17px;
    font-weight: 700;
    padding: 12px;
}

.stButton > button:hover {
    border: none;
    color: white;
    box-shadow: 0 5px 15px rgba(255, 120, 160, 0.25);
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# 여행지 데이터
# --------------------------------------------------
travel_data = {

    "INTJ": {
        "message": "계획적이고 깊이 있는 여행을 좋아하는 당신 🖤",
        "tags": ["조용한 여행", "역사", "건축", "혼자 여행"],
        "places": [
            ("🏰", "프라하", "체코",
             "중세 건축과 골목을 천천히 탐험하기 좋은 도시야. 복잡하지 않으면서도 볼거리가 많아서 계획적인 여행에 딱!"),
            ("📚", "에든버러", "영국",
             "고풍스러운 건축물과 문학적인 분위기가 가득해. 혼자 사색하며 걷는 여행을 좋아한다면 잘 맞아."),
            ("⛰️", "루체른", "스위스",
             "차분한 호수와 웅장한 알프스를 동시에 즐길 수 있어. 자연 속에서 조용히 쉬고 싶은 사람에게 추천!")
        ]
    },

    "INTP": {
        "message": "호기심을 따라 자유롭게 탐험하는 당신 🔍",
        "tags": ["박물관", "자유여행", "탐험", "과학"],
        "places": [
            ("🧪", "런던", "영국",
             "과학박물관과 자연사박물관 등 흥미로운 장소가 가득해. 관심 가는 곳을 즉흥적으로 찾아다니기 좋아."),
            ("🚲", "암스테르담", "네덜란드",
             "자유로운 분위기와 독특한 문화가 매력적인 도시야. 자전거를 타며 골목을 탐험해봐!"),
            ("🌌", "레이캬비크", "아이슬란드",
             "화산과 빙하, 오로라까지 지구과학 교과서 속 풍경을 직접 볼 수 있는 곳!")
        ]
    },

    "ENTJ": {
        "message": "새로운 도시를 정복하는 여행이 잘 어울리는 당신 👑",
        "tags": ["도시", "랜드마크", "액티비티", "효율적인 여행"],
        "places": [
            ("🗽", "뉴욕", "미국",
             "볼거리와 할 일이 끝없이 이어지는 도시야. 알찬 일정으로 핵심 명소를 모두 정복하기 좋아."),
            ("🌃", "싱가포르", "싱가포르",
             "교통이 편리하고 도시가 잘 정돈되어 있어서 효율적인 여행을 즐기기에 최고야."),
            ("🏙️", "두바이", "아랍에미리트",
             "화려한 건축과 다양한 액티비티가 가득해. 스케일 큰 여행을 좋아한다면 추천!")
        ]
    },

    "ENTP": {
        "message": "예측할 수 없는 재미를 사랑하는 당신 🎲",
        "tags": ["즉흥여행", "새로운 경험", "도시 탐험", "맛집"],
        "places": [
            ("🌈", "방콕", "태국",
             "시장, 사원, 야경, 음식까지 매일 새로운 경험을 할 수 있는 활기찬 도시야."),
            ("🎭", "베를린", "독일",
             "예술과 역사, 독특한 문화가 섞여 있는 도시라 새로운 자극을 좋아하는 사람에게 잘 맞아."),
            ("🌮", "멕시코시티", "멕시코",
             "음식과 문화, 역사적인 장소가 넘쳐나는 도시야. 계획 없이 돌아다녀도 재미있는 곳!")
        ]
    },

    "INFJ": {
        "message": "감성과 의미를 모두 담은 여행을 원하는 당신 🌙",
        "tags": ["감성", "힐링", "문화", "산책"],
        "places": [
            ("🌸", "교토", "일본",
             "고즈넉한 사찰과 작은 골목을 걸으며 마음을 정리하기 좋은 곳이야."),
            ("🌊", "산토리니", "그리스",
             "푸른 바다와 하얀 마을이 만들어내는 풍경을 바라보며 여유를 느껴봐."),
            ("📖", "포르투", "포르투갈",
             "잔잔하고 따뜻한 분위기의 도시야. 강변을 천천히 걷는 것만으로도 특별한 여행이 돼.")
        ]
    },

    "INFP": {
        "message": "동화 같은 순간을 간직하고 싶은 당신 🦋",
        "tags": ["동화", "사진", "자연", "감성"],
        "places": [
            ("🏡", "콜마르", "프랑스",
             "알록달록한 집과 작은 운하가 있어 마치 동화 속에 들어온 것 같은 도시야."),
            ("🌷", "브뤼헤", "벨기에",
             "중세 분위기가 그대로 남아 있어 천천히 걸으며 감성을 충전하기 좋아."),
            ("🌿", "퀸스타운", "뉴질랜드",
             "호수와 산이 어우러진 아름다운 자연에서 여유로운 시간을 보낼 수 있어.")
        ]
    },

    "ENFJ": {
        "message": "사람들과 특별한 추억을 만드는 당신 💗",
        "tags": ["친구여행", "문화", "사진", "맛집"],
        "places": [
            ("💃", "바르셀로나", "스페인",
             "활기찬 거리와 독특한 건축물이 가득해서 친구들과 추억을 만들기 좋아."),
            ("🍝", "로마", "이탈리아",
             "역사적인 명소와 맛있는 음식이 모두 있어 함께 즐기는 여행에 딱이야."),
            ("🌺", "호놀룰루", "미국",
             "바다와 쇼핑, 다양한 액티비티를 한 번에 즐길 수 있는 밝은 여행지야.")
        ]
    },

    "ENFP": {
        "message": "설렘 가득한 모험을 찾아 떠나는 당신 🌈",
        "tags": ["모험", "즉흥", "액티비티", "친구"],
        "places": [
            ("🏄", "발리", "인도네시아",
             "서핑부터 카페 탐방까지 매일 다른 여행을 즐길 수 있는 자유로운 섬이야."),
            ("🎡", "오사카", "일본",
             "맛집과 쇼핑, 테마파크까지 즐길 거리가 넘치는 도시야."),
            ("🌴", "세부", "필리핀",
             "푸른 바다에서 다양한 액티비티를 즐기며 신나는 추억을 만들 수 있어.")
        ]
    },

    "ISTJ": {
        "message": "깔끔하고 안정적인 여행이 좋은 당신 🧳",
        "tags": ["계획", "역사", "편리함", "안정"],
        "places": [
            ("🏯", "도쿄", "일본",
             "교통과 관광 인프라가 잘 갖춰져 있어서 계획대로 여행하기 편리해."),
            ("🏛️", "비엔나", "오스트리아",
             "궁전과 박물관, 클래식 문화까지 차분하게 즐길 수 있는 도시야."),
            ("🏔️", "취리히", "스위스",
             "깔끔하고 안정적인 도시 분위기와 아름다운 자연을 함께 즐길 수 있어.")
        ]
    },

    "ISFJ": {
        "message": "편안하고 따뜻한 여행을 좋아하는 당신 🧸",
        "tags": ["힐링", "카페", "산책", "편안함"],
        "places": [
            ("🍵", "교토", "일본",
             "조용한 골목과 전통적인 분위기 속에서 여유로운 여행을 즐기기 좋아."),
            ("🌿", "제주", "대한민국",
             "바다와 숲, 예쁜 카페까지 편안하게 쉬어가기 좋은 여행지야."),
            ("🌼", "잘츠부르크", "오스트리아",
             "작고 평화로운 도시라 천천히 걷고 풍경을 감상하기 좋아.")
        ]
    },

    "ESTJ": {
        "message": "알차게 꽉 채운 여행을 좋아하는 당신 📋",
        "tags": ["랜드마크", "도시", "효율", "관광"],
        "places": [
            ("🗼", "파리", "프랑스",
             "랜드마크와 박물관, 쇼핑까지 일정에 맞춰 알차게 즐길 수 있어."),
            ("🏙️", "홍콩", "홍콩",
             "짧은 시간에도 맛집, 쇼핑, 야경까지 효율적으로 즐길 수 있는 도시야."),
            ("🏛️", "워싱턴 D.C.", "미국",
             "박물관과 역사적 명소가 잘 모여 있어 계획적인 여행에 잘 맞아.")
        ]
    },

    "ESFJ": {
        "message": "함께여서 더 행복한 여행을 좋아하는 당신 💞",
        "tags": ["친구", "사진", "맛집", "쇼핑"],
        "places": [
            ("🛍️", "서울", "대한민국",
             "쇼핑, 맛집, 카페, 사진 명소가 많아 친구들과 즐기기 좋아."),
            ("🌸", "후쿠오카", "일본",
             "맛있는 음식과 편리한 교통 덕분에 부담 없이 함께 여행하기 좋아."),
            ("🍕", "밀라노", "이탈리아",
             "쇼핑과 음식, 아름다운 건축까지 함께 즐길 수 있는 매력적인 도시야.")
        ]
    },

    "ISTP": {
        "message": "직접 경험하며 탐험하는 여행이 좋은 당신 🏕️",
        "tags": ["자연", "액티비티", "자유", "탐험"],
        "places": [
            ("🏔️", "인터라켄", "스위스",
             "패러글라이딩과 하이킹 등 다양한 야외 활동을 즐길 수 있어."),
            ("🌋", "아이슬란드", "아이슬란드",
             "폭포, 화산, 빙하를 직접 찾아다니며 자연을 탐험하기 좋아."),
            ("🌊", "오키나와", "일본",
             "스노클링과 드라이브를 즐기며 자유로운 여행을 할 수 있어.")
        ]
    },

    "ISFP": {
        "message": "예쁜 풍경 속에서 행복을 찾는 당신 🎨",
        "tags": ["풍경", "사진", "힐링", "감성"],
        "places": [
            ("🍋", "아말피", "이탈리아",
             "파란 바다와 알록달록한 마을이 어우러진 감성적인 여행지야."),
            ("🌺", "하와이", "미국",
             "아름다운 자연 속에서 여유롭게 쉬며 순간을 즐기기 좋아."),
            ("🌿", "치앙마이", "태국",
             "예쁜 카페와 자연, 여유로운 분위기를 모두 즐길 수 있어.")
        ]
    },

    "ESTP": {
        "message": "신나는 경험이라면 놓칠 수 없는 당신 ⚡",
        "tags": ["액티비티", "야경", "모험", "핫플"],
        "places": [
            ("🎰", "라스베이거스", "미국",
             "화려한 볼거리와 다양한 엔터테인먼트가 가득한 도시야."),
            ("🌃", "방콕", "태국",
             "밤낮없이 활기찬 도시에서 맛집과 시장, 다양한 체험을 즐겨봐."),
            ("🏄", "골드코스트", "호주",
             "서핑과 테마파크 등 액티비티를 좋아한다면 최고의 여행지!")
        ]
    },

    "ESFP": {
        "message": "즐거움과 설렘이 가득해야 여행이지! 🎀",
        "tags": ["핫플", "사진", "맛집", "친구"],
        "places": [
            ("🎢", "오사카", "일본",
             "테마파크부터 먹거리까지 하루 종일 즐길 거리가 가득해."),
            ("🌴", "괌", "미국",
             "예쁜 바다와 쇼핑, 액티비티까지 친구들과 즐기기 좋아."),
            ("💃", "바르셀로나", "스페인",
             "활기찬 거리와 아름다운 건축, 맛있는 음식이 기다리고 있어.")
        ]
    }
}


# --------------------------------------------------
# 제목
# --------------------------------------------------
st.markdown(
    '<div class="main-title">🌷 MBTI TRIP 💕</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">'
    '나의 MBTI와 찰떡인 여행지는 어디일까? ✈️☁️'
    '</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="question-box">
    <div style="font-size:35px;">🧸 💌 🌸</div>
    <div class="question-title">
        MBTI를 골라주세요!
    </div>
    <div style="color:#a98c9a; margin-top:5px;">
        당신에게 어울리는 여행지를 찾아드릴게요 ♡
    </div>
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# MBTI 선택
# --------------------------------------------------
mbti_list = [
    "선택해주세요 💕",
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

selected_mbti = st.selectbox(
    "MBTI 선택",
    mbti_list,
    label_visibility="collapsed"
)


# --------------------------------------------------
# 추천 결과
# --------------------------------------------------
if selected_mbti != "선택해주세요 💕":

    data = travel_data[selected_mbti]

    st.markdown(
        f"""
        <div class="mbti-result">
            <div style="font-size:15px;">
                당신의 MBTI는
            </div>

            <div class="mbti-big">
                {selected_mbti} 💕
            </div>

            <div style="font-size:16px; margin-top:7px;">
                {data["message"]}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 태그
    tag_html = ""

    for tag in data["tags"]:
        tag_html += f'<span class="tag">#{tag}</span>'

    st.markdown(
        f"""
        <div style="text-align:center; margin-bottom:25px;">
            {tag_html}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="
            text-align:center;
            color:#735b67;
            font-size:22px;
            font-weight:800;
            margin-bottom:10px;
        ">
            💌 이런 여행지는 어때?
        </div>
        """,
        unsafe_allow_html=True
    )

    # 여행 카드
    for emoji, city, country, description in data["places"]:

        st.markdown(
            f"""
            <div class="travel-card">

                <div class="travel-title">
                    {emoji} {city}
                </div>

                <div class="travel-country">
                    📍 {country}
                </div>

                <div class="travel-description">
                    {description}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    # 랜덤 여행지 뽑기
    if st.button("🎀 셋 중 하나만 골라줘! 🎀"):

        random_place = random.choice(data["places"])

        st.balloons()

        st.success(
            f"✈️ 오늘의 운명 여행지는 "
            f"**{random_place[1]} ({random_place[2]})**! 💕"
        )


else:

    st.markdown(
        """
        <div style="
            text-align:center;
            margin-top:45px;
            padding:30px;
            color:#aa8d9b;
            font-size:17px;
        ">
            ☁️<br><br>
            아직 MBTI를 선택하지 않았어요!<br>
            위에서 MBTI를 골라주세요 🌷
            <br><br>
            🐰ྀི ♡ 🧁 ♡ 🎀
        </div>
        """,
        unsafe_allow_html=True
    )


# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown(
    """
    <div class="footer">
        🌸 MBTI TRIP 🌸<br>
        MBTI 추천은 재미로만 봐주세요 ♡
    </div>
    """,
    unsafe_allow_html=True
)
