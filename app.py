import streamlit as st
import random

st.set_page_config(
    page_title="Rock Paper Scissors",
    page_icon="🎮",
    layout="centered"
)

if "player_score" not in st.session_state:
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.session_state.draw_score = 0
    st.session_state.player_choice = "❔"
    st.session_state.computer_choice = "❔"
    st.session_state.result = "CHOOSE YOUR MOVE!"
    st.session_state.result_color = "#FFFFFF"

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #101629, #263B60);
    color: white;
}
h1 {
    color: #00E5FF !important;
    text-align: center;
    font-size: 32px !important;
}
.subtitle {
    color: #FFD166;
    text-align: center;
    font-weight: bold;
    font-size: 16px;
}
.score {
    background: #202B45;
    padding: 18px 5px;
    border-radius: 15px;
    text-align: center;
    color: white;
    font-weight: bold;
    font-size: 17px;
}
.player {
    background: #263B60;
    padding: 25px 5px;
    border-radius: 15px;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
}
.computer {
    background: #49305D;
    padding: 25px 5px;
    border-radius: 15px;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
}
.result {
    text-align: center;
    font-size: 25px;
    font-weight: bold;
    padding: 20px 5px;
}
.stButton > button {
    width: 100%;
    min-height: 65px;
    border-radius: 14px;
    font-size: 17px;
    font-weight: bold;
    background: #00A8E8;
    color: white;
    border: none;
}
.stButton > button:hover {
    background: #8E44AD;
    color: white;
    border: none;
}
.footer {
    text-align: center;
    color: #FFD166;
    font-weight: bold;
    padding: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    "<h1>🎮 ROCK PAPER SCISSORS</h1>",
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">⚡ CHALLENGE THE COMPUTER ⚡</div>',
    unsafe_allow_html=True
)

st.write("")

a, b, c = st.columns(3)

with a:
    st.markdown(
        f'<div class="score">YOU<br>{st.session_state.player_score}</div>',
        unsafe_allow_html=True
    )

with b:
    st.markdown(
        f'<div class="score">DRAW<br>{st.session_state.draw_score}</div>',
        unsafe_allow_html=True
    )

with c:
    st.markdown(
        f'<div class="score">COMPUTER<br>{st.session_state.computer_score}</div>',
        unsafe_allow_html=True
    )

st.write("")

left, right = st.columns(2)

with left:
    st.markdown(
        f'<div class="player">{st.session_state.player_choice}<br>YOU</div>',
        unsafe_allow_html=True
    )

with right:
    st.markdown(
        f'<div class="computer">{st.session_state.computer_choice}<br>COMPUTER</div>',
        unsafe_allow_html=True
    )

st.write("")

st.markdown(
    f'<div class="result" style="color:{st.session_state.result_color};">'
    f'{st.session_state.result}</div>',
    unsafe_allow_html=True
)

def play_game(choice):

    emojis = {
        "Rock": "🪨",
        "Paper": "📄",
        "Scissors": "✂️"
    }

    computer = random.choice(
        ["Rock", "Paper", "Scissors"]
    )

    st.session_state.player_choice = emojis[choice]
    st.session_state.computer_choice = emojis[computer]

    if choice == computer:
        st.session_state.result = "IT'S A DRAW! 🤝"
        st.session_state.result_color = "#FFD166"
        st.session_state.draw_score += 1

    elif (
        (choice == "Rock" and computer == "Scissors")
        or (choice == "Paper" and computer == "Rock")
        or (choice == "Scissors" and computer == "Paper")
    ):
        st.session_state.result = "YOU WIN! 🎉"
        st.session_state.result_color = "#00FF99"
        st.session_state.player_score += 1

    else:
        st.session_state.result = "COMPUTER WINS! 😈"
        st.session_state.result_color = "#FF5577"
        st.session_state.computer_score += 1

st.write("### Choose Your Move")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🪨 ROCK"):
        play_game("Rock")

with col2:
    if st.button("📄 PAPER"):
        play_game("Paper")

with col3:
    if st.button("✂️ SCISSORS"):
        play_game("Scissors")

st.write("")

if st.button("🔄 RESET SCORE", use_container_width=True):
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.session_state.draw_score = 0
    st.session_state.player_choice = "❔"
    st.session_state.computer_choice = "❔"
    st.session_state.result = "CHOOSE YOUR MOVE!"
    st.session_state.result_color = "#FFFFFF"

st.markdown(
    '<div class="footer">GOOD LUCK! HAVE FUN! 🎮</div>',
    unsafe_allow_html=True
)
