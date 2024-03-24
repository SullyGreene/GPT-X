# src/homepage.py
import streamlit as st

def show_homepage():
    # 🌌 Image or Graphic of the GPT-X Interface 🌌
    st.image('src/img/gptx.png', caption='The GPT-X Starship Interface in action!')
    #st.title("🌟 Welcome to GPT-X Starship Interface! 🚀")
    st.markdown("""
    Embark on an interstellar journey through the cosmos of Natural Language Processing with GPT-X. Here, innovation meets imagination, allowing you to explore, train, and interact with AI models in a universe filled with possibilities. 🌌✨

    Ready to launch? Navigate through the sidebar to customize, train, or interact with your models. Let's discover the unknown together!
    """)

    # 🎉 Getting Started Guide 🎉
    st.header("🚀 Getting Started")
    st.markdown("""
    - **Customize Your Model**: Dive into the customization section to tailor your GPT-X model's parameters for your specific needs.
    - **Train Your Model**: Visit the training module to prepare your model using diverse datasets from across the digital universe.
    - **Engage with Your Model**: Test the limits of your AI by querying it in the model testing area.
    - **Explore More**: Each section of this interface offers unique tools and insights. Don't hesitate to explore!

    Together, we'll explore the frontiers of AI, pushing the boundaries of what's possible.
    """)

    # 🌐 Connect with Us 🌐
    st.header("📡 Connect with Us")
    st.markdown("""
    Your journey through the GPT-X cosmos is important to us. Connect with fellow explorers and share your discoveries, insights, and feedback. Together, we can shape the future of AI.
    
    - **GitHub**: [Visit our repository](https://github.com/SullyGreene/GPT-X)
    - **Twitter**: Follow us [@SullyGGx](https://twitter.com/SullyGGx) for the latest updates.
    - **Support**: Encounter any space anomalies? [Report here](https://github.com/SullyGreene/GPT-X/issues).

    Let's make this journey unforgettable! 🌠
    """)

# 🌈 Crafting pathways through the digital cosmos, one line of code at a time. 🌈
