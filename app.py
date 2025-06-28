import streamlit as st

# Page setup
st.set_page_config(page_title="ChatBoo 🧠", page_icon="💬", layout="wide")

# CSS styling for sidebar and chat
st.markdown("""
    <style>
    .css-1cpxqw2 {padding: 1rem;}
    .stTextInput>div>div>input {
        border: 2px solid #ff69b4;
        border-radius: 10px;
        padding: 8px;
    }
    .stButton>button {
        background-color: #ff69b4;
        color: white;
        border-radius: 10px;
        padding: 0.5em 1em;
    }
    </style>
""", unsafe_allow_html=True)

# Ask for username once
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "name_collected" not in st.session_state:
    st.session_state.name_collected = False
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if not st.session_state.name_collected:
    st.session_state.user_name = st.text_input("👤 Enter your name to start:", "")
    if st.session_state.user_name.strip() != "":
        st.session_state.name_collected = True
        st.session_state.chat_history.append(("🤖 ChatBoo", f"Hey {st.session_state.user_name} 👋,ChatBoo here for you always!"))

# Personality selection
with st.sidebar:
    st.title("⚙️ Settings")
    personality = st.selectbox("🧠 Choose ChatBoo's Mood:", ["🤗 Friendly", "😎 Sassy", "🤓 Nerdy"])
    st.markdown("### 📝 Chat History")
    if "chat_history" in st.session_state:
        for sender, msg in st.session_state.chat_history:
            st.markdown(f"**{sender}**: {msg}")

# Function to handle personality replies
def get_bot_response(user_input, personality):
    user_input = user_input.lower()

    # Friendly
    if "friendly" in personality.lower():
        if "hello" in user_input or "hi" in user_input:
            return f"🌼 Hello {st.session_state.user_name}! I'm happy you're here! 💛"
        elif "joke" in user_input:
            return "😂 Why don't robots panic? Because they have nerves of steel!"
        elif "capital of india" in user_input:
            return "🗺️ New Delhi is the capital of India!"
        elif "bye" in user_input:
            return "👋 Aww bye, take care!"
        else:
            return "✨ I'm here for you! Ask me anything."

    # Sassy
    elif "sassy" in personality.lower():
        if "hello" in user_input or "hi" in user_input:
            return "💅 Oh hey sugar, didn't see you there 😏"
        elif "joke" in user_input:
            return "😎 I'm not a clown, but here's one: I write clean code... said no one ever!"
        elif "capital of india" in user_input:
            return "👑 It’s New Delhi, darling. Basic stuff 😌"
        elif "bye" in user_input:
            return "💄 Leaving me already? Typical. BYE!"
        else:
            return "📱 Could be better, but I’m stuck chatting with you 😘"

    # Nerdy
    elif "nerdy" in personality.lower():
        if "hello" in user_input or "hi" in user_input:
            return f"👓 Hello {st.session_state.user_name}! Ready to initiate chat protocol 0x01?"
        elif "joke" in user_input:
            return "🤖 I would tell you a UDP joke, but you might not get it."
        elif "capital of india" in user_input:
            return "📚 The capital of India is New Delhi — indexed at rank[0] of Indian states."
        elif "bye" in user_input:
            return "🧠 System shutdown in 3...2...Bye, human!"
        else:
            return "📖 That’s beyond my current training data. But let’s explore it together!"

# Chat interaction
if st.session_state.user_name:
    input_container = st.container()
    with input_container:
        user_input = st.text_input("💬 Type your message and press Enter", key="input")

    if user_input:
        bot_response = get_bot_response(user_input, personality)
        st.session_state.chat_history.append((f"🧍‍♀️ {st.session_state.user_name}", user_input))
        st.session_state.chat_history.append((f"{personality}", bot_response))
        st.experimental_rerun()

from pyngrok import ngrok
!streamlit run app.py &> /dev/null &
public_url = ngrok.connect(8501)
print("🌐 App is live at:", public_url)








