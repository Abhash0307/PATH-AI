




# import streamlit as st

# # App config
# st.set_page_config(
#     page_title="PathAI - Your Career Assistant",
#     page_icon="🛣️",
#     layout="wide"
# )
           

# # Inject custom CSS
# st.markdown("""
# <style>
# body {
#     background-color: #f9fafb;
#     font-family: 'Segoe UI', sans-serif;
# }
# .hero {
#     text-align: center;
#     padding: 20px 50px;
#     background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
#     color: white;
#     border-radius: 20px;
#     margin-bottom: 30px;
# }
# .hero img {
#     width: 1200px;
#     margin-bottom: 12px;
# }
# .hero h1 {
#     font-size: 5rem;
#     margin: 0;
# }
# .hero p {
#     font-size: 1.2rem;
#     margin: 50px 0 0;
# }
# .card-container {
#     display: flex;
#     justify-content: space-around;
#     flex-wrap: wrap;
#     gap: 20px;
#     margin-top: 30px;
# }
# .card {
#     background: white;
#     box-shadow: 0 2px 6px rgba(0,0,0,0.1);
#     border-radius: 10px;
#     padding: 20px;
#     flex: 1 1 200px;
#     max-width: 250px;
#     text-align: center;
#     transition: transform 0.2s ease;
# }
# .card:hover {
#     transform: translateY(-5px);
#     box-shadow: 0 4px 12px rgba(0,0,0,0.2);
# }
# .card h3 {
#     margin: 10px 0;
#     color: #333;
# }
# .card p {
#     font-size: 0.95rem;
#     color: #666;
# }
# </style>
# """, unsafe_allow_html=True)

# # Hero section
# st.markdown(f"""
# <div class="hero">
#     <img src="https://specials-images.forbesimg.com/imageserve/653a685374ac18a072c8eb46/In-this-article--we-explore-five-industries-where-there-are-great-opportunities-for/960x0.jpg?fit=scale" alt="PathAI logo">
#     <h1>PathAI</h1>
#     <p>Your AI-powered Career Assistant</p>
# </div>
# """, unsafe_allow_html=True)

# # Features cards
# st.markdown("""
# <div class="card-container">

# <div class="card">
#     <h3>📄 Resume Analyzer</h3>
#     <p>Get insights and suggestions to improve your resume and stand out to recruiters.</p>
# </div>

# <div class="card">
#     <h3>🧠 Career Coaching</h3>
#     <p>Ask career-related questions and get advice tailored to your goals.</p>
# </div>

# <div class="card">
#     <h3>💼 Job Finder</h3>
#     <p>Discover job openings that match your profile and preferences.</p>
# </div>

# <div class="card">
#     <h3>🎤 Mock Interviews</h3>
#     <p>Practice with AI-driven mock interviews to sharpen your skills and boost confidence.</p>
# </div>

# </div>
# """, unsafe_allow_html=True)

# # Footer
# st.markdown("""
# <hr>
# <div style='text-align: center; font-size: 0.9rem; color: #888;'>
#     Made with ❤️ using Streamlit | © 2025 PathAI
# </div>
# """, unsafe_allow_html=True)



import streamlit as st
import  account  # your account.py from earlier

# App config
st.set_page_config(
    page_title="PathAI - Your Career Assistant",
    page_icon="🛣️",
    layout="wide"
)

def main():
    st.sidebar.title("PathAI Navigation")
    menu = st.sidebar.radio("Go to", ["Home", "Account Page"])

    if menu == "Home":
        show_home()
    elif menu == "Account Page":
        account.app()


def show_home():
    # Inject custom CSS
    st.markdown("""
    <style>
    body {
        background-color: #f9fafb;
        font-family: 'Segoe UI', sans-serif;
    }
    .hero {
        text-align: center;
        padding: 20px 50px;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 20px;
        margin-bottom: 30px;
    }
    .hero img {
        width: 50px;
        margin-bottom: 10px;
    }
    .hero h1 {
        font-size: 5rem;
        margin: 0;
    }
    .hero p {
        font-size: 1.2rem;
        margin: 50px 0 0;
    }
    .card-container {
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        gap: 20px;
        margin-top: 30px;
    }
    .card {
        background: white;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        border-radius: 10px;
        padding: 20px;
        flex: 1 1 200px;
        max-width: 250px;
        text-align: center;
        transition: transform 0.2s ease;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }
    .card h3 {
        margin: 10px 0;
        color: #333;
    }
    .card p {
        font-size: 0.95rem;
        color: #666;
    }
    </style>
    """, unsafe_allow_html=True)

    # Hero section
    st.markdown(f"""
    <div class="hero">
        <img src="https://specials-images.forbesimg.com/imageserve/653a685374ac18a072c8eb46/In-this-article--we-explore-five-industries-where-there-are-great-opportunities-for/960x0.jpg?fit=scale" alt="PathAI logo">
        <h1>PathAI</h1>
        <p>Your AI-powered Career Assistant</p>
    </div>
    """, unsafe_allow_html=True)

    # Features cards
    st.markdown("""
    <div class="card-container">

    <div class="card">
        <h3>📄 Resume Analyzer</h3>
        <p>Get insights and suggestions to improve your resume and stand out to recruiters.</p>
    </div>

    <div class="card">
        <h3>🧠 Career Coaching</h3>
        <p>Ask career-related questions and get advice tailored to your goals.</p>
    </div>

    <div class="card">
        <h3>💼 Job Finder</h3>
        <p>Discover job openings that match your profile and preferences.</p>
    </div>

    <div class="card">
        <h3>🎤 Mock Interviews</h3>
        <p>Practice with AI-driven mock interviews to sharpen your skills and boost confidence.</p>
    </div>

    </div>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <hr>
    <div style='text-align: center; font-size: 0.9rem; color: #888;'>
        Made with ❤️ using Streamlit | © 2025 PathAI
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
