# import streamlit as st
# from streamlit_webrtc import webrtc_streamer
# from streamlit_lottie import st_lottie
# from streamlit_code_editor import code_editor
# import json

# from utils.mock_interviewer import MockInterviewer

# st.set_page_config(page_title="Mock Interview Pro", page_icon="🎤", layout="wide")

# # 🔷 Load lottie animation
# def load_lottie(filepath):
#     with open(filepath, "r") as f:
#         return json.load(f)

# ai_animation = load_lottie("assets/ai_animation.json")

# st.markdown("""
# <style>
# h1, h2 {color: #2E86C1;}
# .report-card {
#     background-color: #F2F4F4;
#     padding: 10px;
#     border-radius: 10px;
# }
# .sidebar-title {
#     font-size:18px;
#     font-weight:bold;
# }
# </style>
# """, unsafe_allow_html=True)

# # Sidebar
# with st.sidebar:
#     st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
#     st.markdown("<div class='sidebar-title'>👀 Live Proctoring</div>", unsafe_allow_html=True)
#     webrtc_streamer(key="camera")
#     st.markdown("---")
#     st.info("Proctoring keeps you honest! Camera is ON.")

# st.title("🎤 Mock Interview Pro")
# st.write("Welcome! I’m your **AI Interviewer**, here to boost your confidence & skills.")
# st_lottie(ai_animation, height=200)

# # Resume
# resume = st.file_uploader("📄 Upload your resume", type=["pdf", "docx"])
# if resume:
#     st.success("✅ Resume uploaded successfully!")
#     mock_interviewer = MockInterviewer(resume.read())  # bytes

#     st.info("Press **Start Interview** when you’re ready.")
#     if st.button("🚀 Start Interview"):
#         st.session_state.started = True
#         st.session_state.current_q = 0
#         st.session_state.questions = mock_interviewer.generate_questions()
#         st.session_state.answers = []
#         st.session_state.feedback = []

# if "started" in st.session_state and st.session_state.started:
#     tab1, tab2, tab3, tab4 = st.tabs(
#         ["📝 Questions", "👀 Proctoring", "💻 Coding Challenge", "📋 Feedback Report"]
#     )

#     with tab1:
#         st.subheader("Current Question")
#         current_q = st.session_state.current_q
#         questions = st.session_state.questions

#         if current_q < len(questions):
#             question = questions[current_q]
#             st.markdown(f"### Q{current_q+1}: {question}")

#             if "coding" in question.lower():
#                 st.info("This is a coding question. Please use the Coding Challenge tab.")
#             else:
#                 st.info("Please speak your answer now, then press Submit.")
#                 answer = st.text_area("✍️ Or type your answer here")
#                 if st.button("✅ Submit Answer"):
#                     feedback = mock_interviewer.analyze_answer(question, answer)
#                     st.session_state.feedback.append((question, answer, feedback))
#                     st.session_state.current_q += 1

#                     if st.session_state.current_q == len(questions):
#                         st.success("🎉 Interview completed!")

#         else:
#             st.balloons()
#             st.write("You’ve completed all questions. Please check the Feedback tab.")

#     with tab2:
#         st.header("Live Proctoring")
#         st.warning("Your camera feed is shown here to monitor throughout the interview.")

#     with tab3:
#         st.header("💻 Coding Challenge")

#         coding_questions = [q for q in st.session_state.questions if "coding" in q.lower()]
#         if coding_questions:
#             idx = min(len(st.session_state.feedback), len(coding_questions)-1)
#             coding_q = coding_questions[idx]

#             st.markdown(f"### {coding_q}")

#             default_code = "# Write your code here\n"
#             editor_content = code_editor(default_code, height=300, language="python", theme="light")

#             if st.button("🏃 Run Code"):
#                 # ⚠️ This is just a simulation; secure sandbox is recommended for real execution
#                 test_case_passed = mock_interviewer.evaluate_code(coding_q, editor_content["text"])
#                 if test_case_passed:
#                     st.success("✅ Test cases passed!")
#                 else:
#                     st.error("❌ Test cases failed. Please try again.")

#     with tab4:
#         st.header("📋 Feedback Report")
#         if st.session_state.feedback:
#             for idx, (q, a, f) in enumerate(st.session_state.feedback):
#                 st.markdown(f"""
#                 <div class='report-card'>
#                 <b>Q{idx+1}:</b> {q} <br>
#                 <b>Your Answer:</b> {a} <br>
#                 <b>Feedback:</b> {f}
#                 </div>
#                 """, unsafe_allow_html=True)

#             if st.button("⬇️ Download PDF Report"):
#                 pdf = mock_interviewer.generate_feedback_pdf(st.session_state.feedback)
#                 st.download_button("Download Feedback", pdf, file_name="feedback.pdf", mime="application/pdf")




import streamlit as st
from utils.mock_interviewer import MockInterviewer
# app.py

# app.py


from streamlit_webrtc import webrtc_streamer
import av
import cv2
from PyPDF2 import PdfReader

st.set_page_config(page_title="AI Mock Interviewer", layout="wide")
st.title("🤖 AI Mock Interviewer")

if "interviewer" not in st.session_state:
    st.session_state.interviewer = MockInterviewer()
    st.session_state.question_idx = 0

interviewer = st.session_state.interviewer

# --- Webcam Proctoring ---
def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    cv2.putText(img, "Proctoring Active", (30, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    return av.VideoFrame.from_ndarray(img, format="bgr24")

with st.sidebar:
    st.header("📹 Proctoring")
    webrtc_streamer(key="proctor", video_frame_callback=video_frame_callback)

# --- Step 1: Choose Resume Upload or Role ---
st.subheader("Step 1: Provide your background")

col1, col2 = st.columns(2)

resume_text = ""
job_role = ""

with col1:
    uploaded_file = st.file_uploader("📄 Upload your Resume (PDF)", type=["pdf"])
    if uploaded_file:
        reader = PdfReader(uploaded_file)
        resume_text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
        st.success("✅ Resume text extracted.")
        st.text_area("Extracted Resume Text", value=resume_text, height=200)

with col2:
    st.write("Or…")
    job_role = st.selectbox(
        "💼 Select a Job Role",
        ["", "Software Engineer", "Data Scientist", "Product Manager", "UI/UX Designer", "Cybersecurity Analyst"]
    )

if st.button("🎯 Generate Questions"):
    base_text = ""
    if resume_text.strip():
        base_text = resume_text
    elif job_role:
        base_text = f"Preferred Job Role: {job_role}"
    else:
        st.error("Please upload a resume or select a job role.")
    
    if base_text:
        with st.spinner("Generating interview questions..."):
            interviewer.generate_questions(base_text)
            st.session_state.question_idx = 0
        st.success("🎉 Questions generated! Scroll down to begin.")

# --- Question Loop ---
if interviewer.questions:
    idx = st.session_state.question_idx
    total = len(interviewer.questions)

    if idx < total:
        q = interviewer.questions[idx]
        st.markdown(f"### Question {idx + 1} of {total}")
        st.write(q)

        # Detect coding question
        is_coding = idx < len(interviewer.coding_test_cases) and interviewer.coding_test_cases[idx]

        # 🎙️ Voice Input
        with st.expander("🎤 Speak your answer (optional)"):
            if st.button(f"🎙️ Listen to Answer Q{idx}", key=f"mic_{idx}"):
                with st.spinner("Listening..."):
                    spoken = interviewer.listen_to_answer(timeout=10)
                st.write("🗣️ You said:", spoken)
                st.session_state[f"answer_{idx}"] = spoken

        # Answer input
        if is_coding:
            code = st.text_area("✍️ Write your Code Answer", height=200, key=f"code_{idx}")
        else:
            answer = st.text_area("✍️ Write your Answer", key=f"answer_{idx}")

        if st.button("✅ Submit Answer", key=f"submit_{idx}"):
            if is_coding:
                if not code.strip():
                    st.error("Please provide code before submitting.")
                else:
                    results = interviewer.check_code(code, interviewer.coding_test_cases[idx])
                    st.markdown("#### Code Test Results")
                    st.text(results)
                    interviewer.feedback.append((q, "[code submitted]", results))
                    st.session_state.question_idx += 1
            else:
                ans = st.session_state.get(f"answer_{idx}", "").strip()
                if not ans:
                    st.error("Please provide an answer.")
                else:
                    with st.spinner("AI analyzing your answer..."):
                        fb = interviewer.analyze_answer(q, ans)
                    st.markdown("✅ Feedback:")
                    st.write(fb)
                    st.session_state.question_idx += 1

    else:
        st.success("🎓 Interview complete! Download your report below.")
        if st.button("📄 Download Feedback Report"):
            path = "feedback_report.pdf"
            interviewer.generate_pdf_feedback(path)
            with open(path, "rb") as f:
                st.download_button("Download PDF", f, "feedback_report.pdf", "application/pdf")
else:
    st.info("Your interview session will appear here once you generate questions.")
