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
            st.markdown("### 🔬 Diagnosis: **Apple Scab (Venturia inaequalis)**")
            st.progress(0.96, text="AI Confidence Score: 96%")
            
            # RAG Treatment Output
            st.markdown("### 💊 RAG Recommended Treatment")
            st.info("**Eco-friendly Option:** Organic Sulfur-based bio-fungicide or Neem oil spray. Prune infected areas and apply before predicted rain to prevent spore spread.")
            
            # Agentic Recommender Output
            st.markdown("### 🛒 Cost-Optimization & Local Market")
            st.write("- 🥇 **Top Choice:** EcoSulfur Bio-Protect (1L)")
            st.write("- 💰 **Cost:** ₹350 / Liter *(Identified as the most cost-effective)*")
            st.write("- 📍 **Availability:** Kisan Agri Store, Main Market")

            # Community Feedback Loop
            st.markdown("### 🧑‍🌾 Community Feedback Loop")
            st.write("⭐⭐⭐⭐⭐ **4.7/5** *(Based on 32 local orchard farmers)*")
            
            st.success("""
            > *\"Used EcoSulfur in my apple orchard last season. Very cheap and stopped the scab from spreading to my healthy apples. Highly recommend!\"* 
            > **— Ramesh, Local Orchard Farmer**
            """)
            
            st.warning("""
            > *\"Make sure to spray early in the morning and clear away any fallen leaves around the tree trunk!\"* 
            > **— Sita, Organic Apple Grower**
            """)
    else:
        st.info("👈 Please upload an image of a crop on the left to begin the AI analysis.")

# Footer
st.divider()
st.caption("Built for the 1M1B AI for Sustainability Virtual Internship | Powered by IBM Granite & Agentic RAG")
