import streamlit as st
import requests
import json
from dotenv import load_dotenv
import os


load_dotenv()

API_KEY = os.getenv("FIREBASE_API_KEY")

SIGNUP_URL = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={API_KEY}"
SIGNIN_URL = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}"
RESET_URL  = f"https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key={API_KEY}"

def app():
    st.title("👋 Welcome to PathAI Account Page")

    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    def signup(email, password):
        payload = {
            "email": email,
            "password": password,
            "returnSecureToken": True
        }
        r = requests.post(SIGNUP_URL, data=json.dumps(payload))
        return r.ok, r.json()

    def signin(email, password):
        payload = {
            "email": email,
            "password": password,
            "returnSecureToken": True
        }
        r = requests.post(SIGNIN_URL, data=json.dumps(payload))
        return r.ok, r.json()

    def reset_password(email):
        payload = {
            "email": email,
            "requestType": "PASSWORD_RESET"
        }
        r = requests.post(RESET_URL, data=json.dumps(payload))
        return r.ok, r.json()

    if not st.session_state.authenticated:
        choice = st.selectbox("Choose Action", ["Login", "Sign Up", "Reset Password"])

        email = st.text_input("Email")
        password = st.text_input("Password", type="password") if choice != "Reset Password" else None

        if choice == "Sign Up" and st.button("Sign Up"):
            ok, resp = signup(email, password)
            if ok:
                st.success("✅ Account created! Please log in.")
            else:
                st.error(resp.get("error", {}).get("message", "Unknown error"))

        if choice == "Login" and st.button("Login"):
            ok, resp = signin(email, password)
            if ok:
                st.session_state.authenticated = True
                st.session_state.email = resp["email"]
                st.success(f"✅ Logged in as {st.session_state.email}")
            else:
                st.error(resp.get("error", {}).get("message", "Unknown error"))

        if choice == "Reset Password" and st.button("Send Reset Email"):
            ok, resp = reset_password(email)
            if ok:
                st.success("✅ Password reset email sent.")
            else:
                st.error(resp.get("error", {}).get("message", "Unknown error"))

    else:
        st.write(f"🎉 You’re logged in as: `{st.session_state.email}`")
        if st.button("Sign Out"):
            st.session_state.authenticated = False
            st.session_state.email = ""
            st.success("👋 Signed out.")
