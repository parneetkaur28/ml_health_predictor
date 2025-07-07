import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Multi-predict app", 
    page_icon="house",
)


# Home Page Content
def home_page():
    st.title("WELCOME!")
    st.header("PREDICT YOUR HEALTH STATE")
    st.subheader("~We care for you!")
    st.image(os.path.join("images", "img11.png"), width=500)
    st.markdown("WELCOME! You can now predict the diseases related to the important organs of your body using our app.")
    st.write("Just got your reports done? Enter your test results to take a precautionary prediction for a better tomorrow!")
    

    st.image(os.path.join("images", "homedown.jpg"), width=650)

# About Us Page Content
def about_us_page():
    st.title("About Us")
    st.image(os.path.join("images", "aboutus.png"), width=650)
    st.write("We are committed to providing accurate health predictions to help you manage your well-being effectively.")
    st.write("Our app uses machine learning algorithms to analyze health data and provide insights.")

# Contact Us Page Content
def contact_us_page():
    st.title("Contact Us")
    st.write("For any inquiries, please reach out to us:")
    st.write("Email: healthcareforu@gmail.com")
    st.write("Phone: +91443768298")

# Initialize the current page
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# Navigation Icons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🏠 Home"):
        st.session_state.page = "Home"
        
with col2:
    if st.button("ℹ️ About Us"):
        st.session_state.page = "About Us"

with col3:
    if st.button("📞 Contact Us"):
        st.session_state.page = "Contact Us"

# Render the selected page content
if st.session_state.page == "Home":
    home_page()
elif st.session_state.page == "About Us":
    about_us_page()
elif st.session_state.page == "Contact Us":
    contact_us_page()

# Footer
footer_html = """
<style>
footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #f1f1f1;
    text-align: center;
    padding: 10px;
}
</style>
<footer>
    <p>© 2024 Health Prediction App | <a href="https://www.example.com">Privacy Policy</a> | <a href="https://www.example.com">Terms of Service</a></p>
</footer>
"""

st.markdown(footer_html, unsafe_allow_html=True)
