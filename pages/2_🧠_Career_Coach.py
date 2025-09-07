# import streamlit as st
# from utils.gemini_ai import get_career_advice

# st.set_page_config(page_title="🧠 Career Coach", page_icon="🧠", layout="wide")

# st.title("🧠 AI Career Coach")

# st.markdown(
#     """
#     Ask your career-related questions and get AI-powered guidance.
#     """
# )

# query = st.text_area("💬 What's on your mind?", placeholder="E.g., How can I transition to a Data Scientist role?")

# if st.button("🤖 Get Advice") and query:
#     with st.spinner("Thinking..."):
#         try:
#             advice = get_career_advice(query)
#             st.success("✅ Here's the advice:")
#             st.write(advice)
#         except Exception as e:
#             st.error(f"Error: {e}")



# import streamlit as st
# from utils.gemini_ai import get_career_advice

# st.set_page_config(page_title="🧠 Career Coach", page_icon="🧠", layout="wide")

# st.title("🧠 AI Career Coach")

# st.markdown(
#     """
#     <style>
#     .chat-container {
#         max-width: 600px;
#         margin: auto;
#         background-color: #fafafa;
#         padding: 20px;
#         border-radius: 12px;
#         box-shadow: 0 0 10px rgba(0,0,0,0.1);
#     }
#     .msg {
#         display: flex;
#         margin: 10px 0;
#     }
#     .msg.user {
#         justify-content: flex-end;
#     }
#     .msg.ai {
#         justify-content: flex-start;
#     }
#     .bubble {
#         padding: 10px 15px;
#         border-radius: 20px;
#         max-width: 70%;
#         word-wrap: break-word;
#         font-size: 15px;
#     }
#     .user .bubble {
#         background-color: #3797f0;
#         color: white;
#         border-bottom-right-radius: 0;
#     }
#     .ai .bubble {
#         background-color: #efefef;
#         color: black;
#         border-bottom-left-radius: 0;
#     }
#     .input-area {
#         display: flex;
#         gap: 10px;
#         margin-top: 20px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# if 'career_chat' not in st.session_state:
#     st.session_state.career_chat = []  # [(sender, message), ...]

# st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# # Display chat history
# for sender, msg in st.session_state.career_chat:
#     alignment = "user" if sender == "user" else "ai"
#     html = f"""
#     <div class="msg {alignment}">
#         <div class="bubble">{msg}</div>
#     </div>
#     """
#     st.markdown(html, unsafe_allow_html=True)

# st.markdown('</div>', unsafe_allow_html=True)

# # Input field & button
# query_col, btn_col = st.columns([5, 1])

# with query_col:
#     query = st.text_input("Type your question:", placeholder="E.g., How can I transition to a Data Scientist role?", label_visibility="collapsed", key="career_input")

# with btn_col:
#     if st.button("➤") and query:
#         st.session_state.career_chat.append(("user", query))
#         with st.spinner("Thinking..."):
#             try:
#                 advice = get_career_advice(query)
#                 st.session_state.career_chat.append(("ai", advice))
#             except Exception as e:
#                 st.session_state.career_chat.append(("ai", f"⚠️ Error: {e}"))




# import streamlit as st
# from utils.gemini_ai import get_career_advice

# st.set_page_config(page_title="🧠 Career Coach", page_icon="🧠", layout="wide")

# st.title("🧠 AI Career Coach")

# # Inject custom CSS for chat bubbles & input
# st.markdown(
#     """
#     <style>
#     .chat-container {
#         max-width: 600px;
#         margin: auto;
#         background-color: #121212;
#         padding: 20px;
#         border-radius: 12px;
#     }
#     .msg {
#         display: flex;
#         margin: 10px 0;
#     }
#     .msg.user {
#         justify-content: flex-end;
#     }
#     .msg.ai {
#         justify-content: flex-start;
#     }
#     .bubble {
#         padding: 10px 15px;
#         border-radius: 20px;
#         max-width: 70%;
#         word-wrap: break-word;
#         font-size: 15px;
#     }
#     .user .bubble {
#         background-color: #3797f0;
#         color: white;
#         border-bottom-right-radius: 0;
#     }
#     .ai .bubble {
#         background-color: #efefef;
#         color: black;
#         border-bottom-left-radius: 0;
#     }
#     .input-row {
#         display: flex;
#         gap: 10px;
#     }
#     .stTextInput>div>div>input {
#         border-radius: 20px !important;
#         padding: 10px !important;
#     }
#     .stButton>button {
#         border-radius: 20px !important;
#         background-color: #3797f0;
#         color: white;
#         padding: 8px 20px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# if 'career_chat' not in st.session_state:
#     st.session_state.career_chat = []  # [(sender, message), ...]
# if 'thinking' not in st.session_state:
#     st.session_state.thinking = False
# if 'pending_input' not in st.session_state:
#     st.session_state.pending_input = ""  # store typed text

# st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# # Display chat history
# for sender, msg in st.session_state.career_chat:
#     alignment = "user" if sender == "user" else "ai"
#     html = f"""
#     <div class="msg {alignment}">
#         <div class="bubble">{msg}</div>
#     </div>
#     """
#     st.markdown(html, unsafe_allow_html=True)

# # Show spinner if thinking
# if st.session_state.thinking:
#     html = """
#     <div class="msg ai">
#         <div class="bubble"><i>Thinking...</i></div>
#     </div>
#     """
#     st.markdown(html, unsafe_allow_html=True)

# st.markdown('</div>', unsafe_allow_html=True)

# # Input + Send button
# st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# col1, col2 = st.columns([6,1])
# with col1:
#     user_input = st.text_input(
#         "Type your message",
#         placeholder="Ask me about your career...",
#         label_visibility="collapsed",
#         key="career_input",
#         value=st.session_state.pending_input,
#     )
#     st.session_state.pending_input = user_input  # save current typed text

# with col2:
#     send_clicked = st.button("Send")

# st.markdown('</div>', unsafe_allow_html=True)

# # When Enter or Send clicked
# if (send_clicked or user_input.endswith("\n")) and user_input.strip() != "" and not st.session_state.thinking:
#     # Remove trailing newline
#     clean_input = user_input.strip()
#     st.session_state.career_chat.append(("user", clean_input))
#     st.session_state.pending_input = ""  # clear input box
#     st.session_state.thinking = True
#     st.rerun()

# # If thinking: process AI response
# if st.session_state.thinking:
#     user_msg = st.session_state.career_chat[-1][1]
#     try:
#         advice = get_career_advice(user_msg)
#     except Exception as e:
#         advice = f"⚠️ Error: {e}"
#     st.session_state.career_chat.append(("ai", advice))
#     st.session_state.thinking = False
#     st.rerun()


import streamlit as st
from utils.gemini_ai import get_career_advice

st.set_page_config(page_title="🧠 Career Coach", page_icon="🧠", layout="wide")

st.title("🧠 AI Career Coach")

# Inject CSS
st.markdown(
    """
    <style>
    .chat-container {
        max-width: 600px;
        margin: auto;
        background-color: #121212;
        padding: 20px;
        border-radius: 12px;
    }
    .msg {
        display: flex;
        margin: 10px 0;
    }
    .msg.user {
        justify-content: flex-end;
    }
    .msg.ai {
        justify-content: flex-start;
    }
    .bubble {
        padding: 10px 15px;
        border-radius: 20px;
        max-width: 70%;
        word-wrap: break-word;
        font-size: 15px;
    }
    .user .bubble {
        background-color: #3797f0;
        color: white;
        border-bottom-right-radius: 0;
    }
    .ai .bubble {
        background-color: #efefef;
        color: black;
        border-bottom-left-radius: 0;
    }
    .input-row {
        display: flex;
        gap: 10px;
    }
    .stTextInput>div>div>input {
        border-radius: 20px !important;
        padding: 10px !important;
    }
    .stButton>button {
        border-radius: 20px !important;
        background-color: #3797f0;
        color: white;
        padding: 8px 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if 'career_chat' not in st.session_state:
    st.session_state.career_chat = []
if 'thinking' not in st.session_state:
    st.session_state.thinking = False
if 'clear_input' not in st.session_state:
    st.session_state.clear_input = False

st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# Chat history
for sender, msg in st.session_state.career_chat:
    alignment = "user" if sender == "user" else "ai"
    html = f"""
    <div class="msg {alignment}">
        <div class="bubble">{msg}</div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

if st.session_state.thinking:
    html = """
    <div class="msg ai">
        <div class="bubble"><i>Thinking...</i></div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Input row
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
col1, col2 = st.columns([6,1])

default_input = "" if st.session_state.clear_input else None

with col1:
    user_input = st.text_input(
        "Type your message",
        value=default_input,
        placeholder="Ask me about your career...",
        label_visibility="collapsed",
        key="career_input"
    )

with col2:
    send_clicked = st.button("Send")

st.markdown('</div>', unsafe_allow_html=True)

# Reset clear_input flag
st.session_state.clear_input = False

# Detect message sent
message_sent = False
if user_input and send_clicked:
    message_sent = True

if message_sent and not st.session_state.thinking:
    clean_input = user_input.strip()
    if clean_input != "":
        st.session_state.career_chat.append(("user", clean_input))
        st.session_state.thinking = True
        st.session_state.clear_input = True  # tell next rerun to clear input
        st.rerun()

if st.session_state.thinking:
    user_msg = st.session_state.career_chat[-1][1]
    try:
        advice = get_career_advice(user_msg)
    except Exception as e:
        advice = f"⚠️ Error: {e}"
    st.session_state.career_chat.append(("ai", advice))
    st.session_state.thinking = False
    st.rerun()
