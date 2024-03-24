# src/dashboard.py
import streamlit as st
import pandas as pd
import numpy as np

def show_dashboard():
    st.title("🌌 GPT-X Dashboard 🌠")
    st.markdown("""
        Welcome aboard the GPT-X Command Center! 🚀 Your one-stop hub for steering through the galaxy of functionalities.
        
        Customize, train, and personalize your GPT models with cosmic precision right here! 🌈✨
    """)

    # 🌟 System Status Galaxy 🌟
    st.subheader("🛰 System Status")
    status_data = {
        "Component": ["Model Training 🏋️", "Model Customization 🎨", "Model Personalization 💖"],
        "Status": ["✅ Operational", "✅ Operational", "🔧 Maintenance"]
    }
    df_status = pd.DataFrame(status_data)
    st.dataframe(df_status.style.applymap(lambda x: "background-color: lightgreen" if "Operational" in x else "background-color: salmon"))

    # 🚀 Interactive Model Metrics Universe 🚀
    st.subheader("📊 Model Metrics")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("👾 Active Users", "1,024", "4%")
    with col2:
        st.metric("🛠 Models Trained", "287", "-3%")
    with col3:
        st.metric("💡 Personalizations Applied", "150", "5%")

    # ⚡ Quick Actions Nebula ⚡
    st.subheader("⚡ Quick Actions")
    if st.button("🔄 Refresh Data"):
        st.experimental_rerun()  # Refreshes the data and the page
        st.success("🌌 Data cosmos refreshed!")

    # 📈 Training Activity Constellation Over Time 📈
    st.subheader("🕰 Training Activity Over Time")
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['Customization 🎨', 'Training 🏋️', 'Personalization 💖']
    )
    st.line_chart(chart_data)

    # 💌 Galactic Feedback Form 💌
    st.subheader("💌 Your Feedback")
    with st.form(key='feedback_form'):
        feedback = st.text_area("How can we improve? Share your cosmic insights!", help="Your feedback helps us navigate better!")
        submit_feedback = st.form_submit_button("Submit 🚀")
        if submit_feedback:
            st.balloons()
            st.write("🌟 Thank you for your stellar feedback!")

    # 📚 Knowledge Base Satellite 📚
    st.sidebar.subheader("🔭 About")
    st.sidebar.markdown("""
        GPT-X is a celestial tool for managing and enhancing GPT models. Dive into the functionalities to customize, train, and personalize your models like never before! 🛸💫
        
        [Learn More](https://example.com) 🌐
    """)

# 🎇 Let's continue to navigate through the cosmos of code and creativity together! 🎇
