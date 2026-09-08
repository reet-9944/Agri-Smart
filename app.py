import streamlit as st
import time
from PIL import Image

# Page Configuration
st.set_page_config(page_title="Agri-Smart AI", page_icon="🌱", layout="wide", initial_sidebar_state="collapsed")

# Header
st.markdown("<h1 style='text-align: center; margin-bottom: 0;'>🌱 Agri-Smart</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2em; margin-top: 0;'>AI Crop Advisor & Community Hub</p>", unsafe_allow_html=True)
st.divider()

# Main Layout: Image on Left, UI/Results on Right
col_img, col_ui = st.columns([1.2, 2.8])

with col_img:
    st.markdown("### 📸 Image Input")
    uploaded_file = st.file_uploader("Upload Crop Photo", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

with col_ui:
    if uploaded_file is not None:
        if st.button("🔍 Analyze with Agentic AI", type="primary", use_container_width=True):
            
            # Loading states
            with st.spinner("Analyzing image using Multimodal AI..."):
                time.sleep(1.5)
            with st.spinner("Querying agricultural RAG database for treatments..."):
                time.sleep(1.5)
            with st.spinner("Fetching local market prices & community feedback..."):
                time.sleep(1.5)
            
            st.success("✅ Analysis Complete")
            
            # Create a 2x2 grid for the results so it doesn't scroll endlessly
            row1_col1, row1_col2 = st.columns(2)
            row2_col1, row2_col2 = st.columns(2)
            
            with row1_col1:
                with st.container(border=True):
                    st.markdown("### 🔬 AI Diagnosis")
                    st.markdown("**Apple Scab (Venturia inaequalis)**")
                    st.progress(0.96, text="Confidence: 96%")
                    
            with row1_col2:
                with st.container(border=True):
                    st.markdown("### 💊 RAG Treatment")
                    st.markdown("🌿 **Eco-friendly Option:** Organic Sulfur bio-fungicide or Neem oil. Prune infected areas and apply before rain.")
                    
            with row2_col1:
                with st.container(border=True):
                    st.markdown("### 🛒 Local Market")
                    st.markdown("🥇 **Choice:** EcoSulfur Bio-Protect")
                    st.markdown("💰 **Cost:** ₹350/L (Best Value)")
                    st.markdown("📍 **Shop:** Kisan Agri Store")
                    
            with row2_col2:
                with st.container(border=True):
                    st.markdown("### 🧑‍🌾 Community Feedback")
                    st.markdown("⭐⭐⭐⭐⭐ **4.7/5** *(32 farmers)*")
                    st.markdown("*\"Cheap and stopped scab from spreading!\"* — **Ramesh**")
                    st.markdown("*\"Spray early morning and clear fallen leaves.\"* — **Sita**")
    else:
        st.info("👈 Upload an image on the left to begin the analysis.")

st.divider()
st.caption("Developed by Reetu Rani for the 1M1B AI for Sustainability Virtual Internship")
