import streamlit as st
import google.generativeai as genai
# Configure API
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

# Page setup
st.set_page_config(page_title="CareerCoach AI", page_icon="🚀")
st.title("🚀 CareerCoach AI")
st.subheader("Your free AI-powered career advisor")
st.write("Tell me about your current job, skills, or career situation — I'll guide you forward!")

# Input
user_input = st.text_area("✍️ Describe your current situation:", 
    placeholder="Example: I'm a data entry operator with 2 years experience, what's next for me?",
    height=150)

# Button
if st.button("🎯 Get My Career Advice"):
    if user_input.strip() == "":
        st.warning("Please describe your situation first!")
    else:
        with st.spinner("Thinking..."):
            prompt = f"""
You are CareerCoach AI — a friendly, expert career advisor.
The user says: {user_input}

Respond with:
1. 👋 A warm acknowledgment of their current position
2. 🎯 3 skill gaps they should fill
3. 🚀 3 realistic next career moves
4. 📚 2 free resources to learn those skills

Keep it clear, encouraging, and under 250 words.
"""
            response = model.generate_content(prompt)
            st.success("Here's your personalized career roadmap!")
            st.markdown(response.text)

st.markdown("---")
st.caption("Built with Gemini AI ✨ | Google Prompt War Hackathon")
