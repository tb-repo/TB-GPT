import streamlit as st
from langchain_openai import ChatOpenAI

# Title and description
st.title("🤖 TB-GPT")
st.markdown("🚀 Generate LinkedIn posts on Generative AI like [Thiagarajan](https://www.linkedin.com/in/thiagagarjanb/)") 
st.markdown("❤️ Powered by GPT-4o fine-tuned model.")

# Text input for topic
topic = st.text_input("Please enter the topic")

st.code("""
            Try:
            Explain Transformers Architecture
            How does RAG work?
            """, language= None)

# Initialize the models
base_model = ChatOpenAI(model="gpt-4o-2024-08-06")
ft_model = ChatOpenAI(model="ft:gpt-4o-2024-08-06:personal::AKSobHDd")

def generate_linkedin_post(prompt, base_model=base_model, ft_model=ft_model):
    response1 = base_model.invoke(prompt)
    response2 = ft_model.invoke(prompt)
    return response1.content, response2.content

if st.button("Generate Posts"):
    if topic:
        with st.spinner("Generating posts..."):
            base_response, ft_response = generate_linkedin_post(f"Generate a LinkedIn post about {topic}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Base Model (gpt-4o-mini) 🔗")
            st.markdown(f'<div class="output-text">{base_response}</div>', unsafe_allow_html=True)
        
        with col2:
            st.subheader("TB-GPT (Fine-tuned Model)")
            st.markdown(f'<div class="output-text">{ft_response}</div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter a topic before generating posts.")

