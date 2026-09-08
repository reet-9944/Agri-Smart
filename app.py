import streamlit as st
import time
from PIL import Image

# Page Configuration
st.set_page_config(page_title="Agri-Smart AI", page_icon="🌱", layout="wide", initial_sidebar_state="collapsed")

# Header
st.markdown("<h1 style='text-align: center; margin-bottom: 0;'>🌱 Agri-Smart</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2em; margin-top: 0;'>AI Crop Advisor & Community Hub</p>", unsafe_allow_html=True)

# Tutorial Video Section
with st.expander("🎥 How to use Agri-Smart (Tutorial)"):
    st.write("1. **Choose Input Method:** On the left, choose between uploading an existing photo or doing a live camera scan of your crop.")
    st.write("2. **Scan / Upload:** Take a clear picture of the diseased leaf or plant.")
    st.write("3. **Analyze:** Click the green 'Analyze with Agentic AI' button to get your instant diagnosis, treatment plan, and local market costs.")
    
    # Placeholder video - the user can replace this URL with their actual recorded demo video link later!
    st.video("https://www.youtube.com/watch?v=Fj2AEEr3uEU") 

st.divider()

# Main Layout: Image on Left, UI/Results on Right
col_img, col_ui = st.columns([1.2, 2.8])

with col_img:
    st.markdown("### 📸 Image Input")
    
    # Added Tabs for Upload vs Live Scan
    tab1, tab2 = st.tabs(["📁 Upload File", "📷 Live Scan"])
    
    with tab1:
        uploaded_file = st.file_uploader("Upload Crop Photo", type=["jpg", "png", "jpeg"])
    with tab2:
        camera_file = st.camera_input("Scan plant with camera")
        
    # Determine which input method the user used
    final_file = camera_file if camera_file is not None else uploaded_file

    if final_file is not None:
        image = Image.open(final_file)
        st.image(image, caption="Captured Image", use_container_width=True)

with col_ui:
    if final_file is not None:
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
        st.info("👈 Upload an image or scan a plant on the left to begin the analysis.")

st.divider()
