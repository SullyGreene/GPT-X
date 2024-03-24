import streamlit as st
import os
from src.modules import gpt

# Assuming the models/ directory is at the root of your project
MODEL_DIR = 'models/'

def show_model_testing_page():
    st.title("🛰 AI Communication Interface 🌌")

    st.markdown("""
    Welcome, Explorer! 🌠 You're at the control panel of the AI Communication Interface aboard the interstellar vessel, CodeCraft. Each AI entity within our database possesses unique insights, ready to assist you in unraveling the mysteries of the cosmos. 🛸🪐

    Select an AI entity for consultation and input your inquiry below. Await the wisdom that spans galaxies. 🌌📚
    """)

    # Check for available AI entities (models) in the models/ directory
    available_models = os.listdir(MODEL_DIR) if os.path.exists(MODEL_DIR) else []
    selected_model = st.selectbox("🔄 Select AI Entity for Consultation", available_models, help="Choose an AI entity for your inquiry.")

    # High-tech text input for user inquiry
    user_prompt = st.text_input("💬 Enter your inquiry:", placeholder="What secrets do you hold, universe?", help="Type your inquiry and await the AI's wisdom.")

    # Activation button for AI response
    generate_button = st.button("🔍 Analyze Inquiry")

    if generate_button:
        if user_prompt:
            # Displaying a futuristic loading animation
            with st.spinner('Analyzing inquiry through the quantum neural network...'):
                # Simulate a delay for dramatic effect if needed
                # time.sleep(2)

                # Dynamically load the selected model for generating text
                model_response = gpt.generate_text(user_prompt, model_name=selected_model, model_dir=MODEL_DIR)

            st.text_area("📡 AI Entity Response:", value=model_response, height=300, help="Insights from beyond the known.")
        else:
            st.error("🚫 Inquiry required. Please provide input to proceed with the analysis.")

    # Sidebar for galactic exploration resources
    st.sidebar.markdown("""
    ## 🚀 Galactic Exploration Resources
    - Unlock AI technologies at [The Galactic AI Hub](https://example.com).
    - Expand your cosmic knowledge with [Interstellar AI Workshops](https://example.com/workshops).
    - Join the dialogue with other spacefarers in [The Quantum Forum](https://example.com/forum).
    """)

# Implementing this page with dynamic model selection and testing provides a richer, more engaging user experience, simulating real interactions with various AI entities aboard the spacecraft. Each entity, represented by a different model version, offers a unique perspective, encouraging users to explore diverse responses and insights. 🌠👨‍🚀🤖