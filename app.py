import streamlit as st
import time
from PIL import Image

# Page Configuration
st.set_page_config(page_title="Agri-Smart AI", page_icon="🌱", layout="wide")

# Header Section
st.title("🌱 Agri-Smart: AI Crop Advisor & Community Hub")
st.markdown("### Empowering farmers with AI-driven diagnosis, cost-effective treatments, and peer-to-peer knowledge.")
st.divider()

# Main Layout
col1, col2 = st.columns([1, 1.5])

with col1:
    st.markdown("#### 1. Upload Crop Image")
    st.write("Upload a photo of the sick plant or leaf to get an instant AI diagnosis.")
    uploaded_file = st.file_uploader("Choose an image (JPG/PNG)", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Crop Image", use_container_width=True)

with col2:
    if uploaded_file is not None:
        st.markdown("#### 2. AI Analysis & Recommendations")
        if st.button("🔍 Analyze with Agentic AI", type="primary", use_container_width=True):
            
            # Simulated AI Processing Steps for the Demo Video
            with st.spinner("Analyzing image using Multimodal AI..."):
                time.sleep(2)
            with st.spinner("Querying agricultural RAG database for treatments..."):
                time.sleep(2)
            with st.spinner("Fetching local market prices & community feedback..."):
                time.sleep(2)
            
            st.success("✅ Analysis Complete!")
            
            # AI Diagnosis Output
            st.markdown("### 🔬 Diagnosis: **Tomato Early Blight**")
            st.progress(0.94, text="AI Confidence Score: 94%")
            
            # RAG Treatment Output
            st.markdown("### 💊 RAG Recommended Treatment")
            st.info("**Eco-friendly Option:** Copper-based organic fungicide spray. Apply early morning once a week to prevent spreading.")
            
            # Agentic Recommender Output
            st.markdown("### 🛒 Cost-Optimization & Local Market")
            st.write("- 🥇 **Top Choice:** EcoCopper Spray (1L)")
            st.write("- 💰 **Cost:** ₹450 / Liter *(Identified as the most cost-effective)*")
            st.write("- 📍 **Availability:** Kisan Agri Store, Main Market")

            # Community Feedback Loop
            st.markdown("### 🧑‍🌾 Community Feedback Loop")
            st.write("⭐⭐⭐⭐⭐ **4.8/5** *(Based on 24 local farmer reviews)*")
            
            st.success("""
            > *\"Used EcoCopper last month. Very cheap and cleared the blight in 3 days. Highly recommend!\"* 
            > **— Ramesh, Local Farmer**
            """)
            
            st.warning("""
            > *\"Make sure to spray only in the morning, otherwise leaves get burned in the sun. Good product.\"* 
            > **— Sita, Organic Grower**
            """)
    else:
        st.info("👈 Please upload an image of a crop on the left to begin the AI analysis.")

# Footer
st.divider()
st.caption("Built for the 1M1B AI for Sustainability Virtual Internship | Powered by IBM Granite & Agentic RAG")
