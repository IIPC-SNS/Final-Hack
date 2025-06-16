import streamlit as st
import requests
from datetime import date

# --- Replace this with your actual webhook URL ---
WEBHOOK_URL = "https://dterp.app.n8n.cloud/webhook-test/cb66492e-5f8f-450d-a71c-a5877db83477"

 # --- Streamlit Page Config ---
st.set_page_config(page_title="HRMS Employee Onboarding/Offboarding", layout="centered")
st.title("🏢 HRMS Onboarding / Offboarding Form")

# --- Form Start ---
with st.form("hrms_webhook_form"):
    name = st.text_input("👤 Full Name")
    email = st.text_input("✉️ Email Address")
    role = st.text_input("🧑‍💻 Role / Designation")

    formtype = st.radio("📋 Form Type", ["Onboard", "Offboard"])
    department = st.selectbox("🏬 Department", ["HR", "Finance", "Ihub"])
    location = st.text_input("📍 Location")
    form_date = st.date_input("🗓️ Date", value=date.today())

    submit = st.form_submit_button("🚀 Submit Form")

# --- Webhook Submit Logic ---
if submit:
    payload = {
        "name": name,
        "email": email,
        "role": role,
        "formtype": formtype.lower(),
        "department": department,
        "location": location,
        "date": form_date.strftime("%Y-%m-%d")
    }

    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        if response.status_code == 200:
            st.success("✅ Submitted successfully to webhook!")
        else:
            st.error(f"❌ Failed! Status code: {response.status_code}")
    except Exception as e:
        st.error(f"🚨 Error submitting: {e}")
