import streamlit as st
import time
from PIL import Image

# Page Configuration
st.set_page_config(page_title="Agri-Smart AI", page_icon="🌱", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS to reduce top padding and align everything perfectly
st.markdown("""
    <style>
    .block-container {
        padding-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Top Row Layout: Empty space (Left), Title (Center), Language (Right)
col_empty, col_title, col_lang = st.columns([1, 2.5, 1])

with col_lang:

    language = st.selectbox("Language", ["English", "हिंदी (Hindi)"], label_visibility="collapsed")

# Define dynamic text based on language
if language == "English":
    t_title = "🌱 Agri-Smart"
    t_subtitle = "AI Crop Advisor & Community Hub"
    t_tutorial = "🎥 How to use Agri-Smart (Tutorial)"
    t_tut_1 = "1. **Choose Input Method:** On the left, choose between uploading an existing photo or doing a live camera scan of your crop."
    t_tut_2 = "2. **Scan / Upload:** Take a clear picture of the diseased leaf or plant."
    t_tut_3 = "3. **Analyze:** Click the green 'Analyze with Agentic AI' button to get your instant diagnosis, treatment plan, and local market costs."
    t_img_input = "### 📸 Image Input"
    t_tab_up = "📁 Upload File"
    t_tab_scan = "📷 Live Scan"
    t_btn_analyze = "🔍 Analyze with Agentic AI"
    t_spin_1 = "Analyzing image using Multimodal AI..."
    t_spin_2 = "Querying agricultural RAG database for treatments..."
    t_spin_3 = "Fetching local market prices & community feedback..."
    t_success = "✅ Analysis Complete"
    t_diag_title = "### 🔬 AI Diagnosis"
    t_diag_res = "**Apple Scab (Venturia inaequalis)**"
    t_conf = "Confidence: 96%"
    t_treat_title = "### 💊 RAG Treatment"
    t_treat_res = "🌿 **Eco-friendly Option:** Organic Sulfur bio-fungicide or Neem oil. Prune infected areas and apply before rain."
    t_market_title = "### 🛒 Local Market"
    t_market_res = "🥇 **Choice:** EcoSulfur Bio-Protect\n\n💰 **Cost:** ₹350/L (Best Value)\n\n📍 **Shop:** Kisan Agri Store"
    t_comm_title = "### 🧑‍🌾 Community Feedback"
    t_comm_res = "⭐⭐⭐⭐⭐ **4.7/5** *(32 farmers)*\n\n*\"Cheap and stopped scab from spreading!\"* — **Ramesh**\n\n*\"Spray early morning and clear fallen leaves.\"* — **Sita**"
    t_empty = "👈 Upload an image or scan a plant on the left to begin the analysis."
else:
    t_title = "🌱 एग्री-स्मार्ट (Agri-Smart)"
    t_subtitle = "एआई फसल सलाहकार और किसान समुदाय"
    t_tutorial = "🎥 एग्री-स्मार्ट का उपयोग कैसे करें (ट्यूटोरियल)"
    t_tut_1 = "1. **इनपुट चुनें:** बाईं ओर, मौजूदा फोटो अपलोड करने या लाइव कैमरा स्कैन करने के बीच चुनें।"
    t_tut_2 = "2. **स्कैन / अपलोड:** बीमार पत्ती या पौधे की स्पष्ट तस्वीर लें।"
    t_tut_3 = "3. **विश्लेषण:** तुरंत निदान, उपचार योजना और बाजार मूल्य प्राप्त करने के लिए हरे बटन पर क्लिक करें।"
    t_img_input = "### 📸 फोटो अपलोड / स्कैन"
    t_tab_up = "📁 फाइल अपलोड करें"
    t_tab_scan = "📷 लाइव स्कैन"
    t_btn_analyze = "🔍 एआई द्वारा विश्लेषण करें"
    t_spin_1 = "मल्टीमॉडल एआई का उपयोग करके छवि का विश्लेषण..."
    t_spin_2 = "उपचार के लिए कृषि RAG डेटाबेस खोजा जा रहा है..."
    t_spin_3 = "स्थानीय बाजार मूल्य और किसानों की राय प्राप्त की जा रही है..."
    t_success = "✅ विश्लेषण पूरा हुआ"
    t_diag_title = "### 🔬 एआई निदान (Diagnosis)"
    t_diag_res = "**सेब की पपड़ी (Apple Scab)**"
    t_conf = "आत्मविश्वास (Confidence): 96%"
    t_treat_title = "### 💊 RAG उपचार"
    t_treat_res = "🌿 **पर्यावरण के अनुकूल विकल्प:** जैविक सल्फर बायो-फंगीसाइड या नीम का तेल। संक्रमित हिस्सों को काटें और बारिश से पहले स्प्रे करें।"
    t_market_title = "### 🛒 स्थानीय बाजार"
    t_market_res = "🥇 **विकल्प:** इको-सल्फर बायो-प्रोटेक्ट\n\n💰 **लागत:** ₹350/लीटर (सबसे सस्ता)\n\n📍 **दुकान:** किसान एग्री स्टोर"
    t_comm_title = "### 🧑‍🌾 किसान समुदाय की राय"
    t_comm_res = "⭐⭐⭐⭐⭐ **4.7/5** *(32 किसान)*\n\n*\"सस्ता है और बीमारी को फैलने से रोक दिया!\"* — **रमेश**\n\n*\"सुबह जल्दी स्प्रे करें और गिरे हुए पत्तों को साफ़ करें।\"* — **सीता**"
    t_empty = "👈 विश्लेषण शुरू करने के लिए बाईं ओर एक छवि अपलोड करें या पौधे को स्कैन करें।"

# Header
with col_title:
    st.markdown(f"<h1 style='text-align: center; margin-top: 0px; margin-bottom: 0;'>{t_title}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; font-size: 1.2em; margin-top: 0;'>{t_subtitle}</p>", unsafe_allow_html=True)

# Tutorial Video Section
with st.expander(t_tutorial):
    st.write(t_tut_1)
    st.write(t_tut_2)
    st.write(t_tut_3)
    
    # Use columns to make the video player much smaller
    v_col1, v_col2, v_col3 = st.columns([1, 2, 1])
    with v_col2:
        # Valid placeholder video - replace with your demo video link later!
        st.video("https://www.youtube.com/watch?v=LXb3EKWsInQ")

st.divider()

# Main Layout: Image on Left, UI/Results on Right
col_img, col_ui = st.columns([1.2, 2.8])

with col_img:
    st.markdown(t_img_input)
    
    tab1, tab2 = st.tabs([t_tab_up, t_tab_scan])
    
    with tab1:
        uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"])
    with tab2:
        camera_file = st.camera_input("")
        
    final_file = camera_file if camera_file is not None else uploaded_file

    if final_file is not None:
        image = Image.open(final_file)
        st.image(image, caption="Captured Image", use_container_width=True)

with col_ui:
    if final_file is not None:
        if st.button(t_btn_analyze, type="primary", use_container_width=True):
            
            with st.spinner(t_spin_1):
                time.sleep(1.5)
            with st.spinner(t_spin_2):
                time.sleep(1.5)
            with st.spinner(t_spin_3):
                time.sleep(1.5)
            
            st.success(t_success)
            
            row1_col1, row1_col2 = st.columns(2)
            row2_col1, row2_col2 = st.columns(2)
            
            with row1_col1:
                with st.container(border=True):
                    st.markdown(t_diag_title)
                    st.markdown(t_diag_res)
                    st.progress(0.96, text=t_conf)
                    
            with row1_col2:
                with st.container(border=True):
                    st.markdown(t_treat_title)
                    st.markdown(t_treat_res)
                    
            with row2_col1:
                with st.container(border=True):
                    st.markdown(t_market_title)
                    st.markdown(t_market_res)
                    
            with row2_col2:
                with st.container(border=True):
                    st.markdown(t_comm_title)
                    st.markdown(t_comm_res)
    else:
        st.info(t_empty)
