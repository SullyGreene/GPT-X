
# 🚀 Initial Setup and Structure 🏗️
import streamlit as st

# 💉 Importing pages for GPT-X Starship 📑
from src.homepage import show_homepage
from src.dashboard import show_dashboard
from src.customize_model import show_customize_page
from src.train_model import show_train_page
from src.personalize_model import show_personalize_page
from src.model_testing import show_model_testing_page
from src.gpt_x import show_gpt_x_page

# 🏗️ Mapping of page names to their respective functions ✨
PAGES = {
    "🏠 HomePage": show_homepage,
    "📊 Dashboard": show_dashboard,
    "🤖 GPT-X": show_gpt_x_page,
    "🎨 Customize Model": show_customize_page,
    "🏋️‍♂️ Train Model": show_train_page,
    "🎭 Personalize Model": show_personalize_page,
    "🛠️ Model Testing": show_model_testing_page,
    # Future pages can be added here as the project grows 🚀
}

def main():
    # Sidebar for navigation 🧭
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    # Display the selected page
    page = PAGES[selection]
    page()  # Call the page function to render it

# Ensures this script runs directly (not imported)
if __name__ == "__main__":
    main()
    # 🌟 Launching the GPT-X Starship Interface! Ready for an interstellar journey! 🌌✨
