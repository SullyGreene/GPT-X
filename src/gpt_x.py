import streamlit as st
from src.modules import nltk_module, gpt

def show_gpt_x_page():
    st.title("🌌 GPT-X Galactic Interface 🛸")

    st.markdown("""
    Welcome, Galactic Explorer! You've docked at the GPT-X Galactic Interface, where the art of language analysis meets the science of artificial generation. 🌠🤖

    Initiate with your textual data sample, witness it undergo analysis by our linguistic algorithms, and then observe as it's transformed by the cosmic intellect of GPT. Ready to launch into the textual unknown? 🚀📚
    """)

    # Option to select or download a new model
    model_name = st.selectbox("Select GPT-2 Model Version", ["gpt2", "gpt2-medium", "gpt2-large", "gpt2-xl"], index=0, help="Choose your GPT-2 model version.")
    download_model = st.button("Download/Load Model")

    if download_model:
        with st.spinner(f"Downloading/loading {model_name} model..."):
            gpt.download_and_save_model(model_name=model_name)
        st.success(f"{model_name} model is ready for action!")

    user_input = st.text_area("🪐 Enter your text for analysis and expansion:", value="", height=150, help="Dispatch your textual data into the analysis vortex.")

    analyze_button, generate_button = st.columns(2)
    with analyze_button:
        if st.button("🔬 Analyze Text"):
            if user_input:
                with st.spinner('🌠 Parsing through the linguistic cosmos...'):
                    analysis_results = nltk_module.analyze_text(user_input)
                st.write("📊 Linguistic Analysis Results:")
                st.json(analysis_results)
            else:
                st.error("🚫 Transmission void detected. Please input textual data for analysis.")

    with generate_button:
        if st.button("🌈 Generate with GPT"):
            if user_input:
                with st.spinner('🛰 Engaging GPT hyperdrive for text generation...'):
                    model_response = gpt.generate_text(user_input, model_name=model_name)
                st.text_area("📝 GPT-Expanded Universe:", value=model_response, height=300)
            else:
                st.error("🚫 Transmission void detected. Please input textual data for expansion.")

# This update integrates model management directly into the user interface, offering explorers the ability to choose, download, and utilize different versions of the GPT-2 model. Such flexibility empowers users to customize their AI companion according to the needs of their interstellar textual adventures. 🌠🛰
