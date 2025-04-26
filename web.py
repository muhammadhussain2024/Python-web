
import streamlit as st
from PIL import Image, ImageDraw

# ============================================
# PAGE CONFIGURATION
# ============================================
st.set_page_config(
    page_title="Syed Muhammad Hussain | Portfolio",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================
# CUSTOM STYLING (Dark Theme)
# ============================================
st.markdown("""
<style>
.stApp {
    background-color: #0E1117;
    color: #FAFAFA;
}
.st-expander {
    background-color: #1E1E1E;
    border: 1px solid #333;
    border-radius: 8px;
}
.stButton>button {
    border: 1px solid #4F4F4F;
    background-color: #262730;
    color: #FAFAFA;
    border-radius: 4px;
}
.stTextInput>div>div>input, 
.stTextArea>div>div>textarea {
    background-color: #1E1E1E;
    color: #FAFAFA;
}
.profile-img {
    border-radius: 50%;
    object-fit: cover;
    width: 250px;
    height: 250px;
    border: 3px solid #444;
}
</style>
""", unsafe_allow_html=True)

# ============================================
# IMAGE PROCESSING FUNCTIONS
# ============================================
def create_perfect_circle(image_path, size=250):
    """Create perfectly circular image without distortion"""
    try:
        img = Image.open(image_path)
        
        # Crop to square (center-weighted)
        width, height = img.size
        min_dim = min(width, height)
        left = (width - min_dim)/2
        top = (height - min_dim)/2
        right = (width + min_dim)/2
        bottom = (height + min_dim)/2
        img = img.crop((left, top, right, bottom))
        
        # Resize and create circular mask
        img = img.resize((size, size))
        mask = Image.new('L', (size, size), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, size, size), fill=255)
        
        # Apply mask
        result = Image.new('RGBA', (size, size))
        result.paste(img, (0, 0), mask=mask)
        return result
        
    except Exception as e:
        st.error(f"Error processing image: {e}")
        return Image.new('RGBA', (size, size), (100, 100, 100, 255))

# ============================================
# PROFILE SECTION
# ============================================
st.header("", divider="rainbow")  # Empty header for spacing

col1, col2 = st.columns([1, 3], gap="large")
with col1:
    profile_img = create_perfect_circle("profile_picture.jpg")
    st.image(profile_img, width=250)

with col2:
    st.title("Syed Muhammad Hussain")
    st.subheader("Professional Title | Specialty")
    st.write("""
    Currently learning coding to transition into tech, I combine my two years of teaching experience with a strong analytical mindset. I'm eager to apply my growing technical skills to develop practical and user-friendly solutions. With a focus on continuous learning, I aim to contribute effectively to tech-driven projects and teams.
    """)
    
    # Social badges
    st.write("""
    [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin)](https://www.linkedin.com/in/syed-muhammad-hussain-44b994346/)
    [![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github)](https://github.com/muhammadhussain2024)
    [![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit)](https://share.streamlit.io/?utm_source=streamlit&utm_medium=referral&utm_campaign=main&utm_content=-ss-streamlit-io-topright)
    """)

# ============================================
# ABOUT ME SECTION
# ============================================
st.header("📝 About Me", divider="gray")
about_col1, about_col2, about_col3 = st.columns(3)
with about_col1:
    st.subheader("Education")
    st.write("""
    🎓 **Intermediate**  
    Govt.Degree Boys Collage Korangi 2/1/2  
    2022 - 2024
    """)
    
with about_col2:
    st.subheader("Experience")
    st.write("""
    💼 **Teacher**  
    Al-Habib Grammar School  
    2022 - 2024
    """)

with about_col3:
    st.subheader("Skills")
    st.write("""
    🛠️ **Technical**  
    - Python  
    - Streamlit
    - Typescript
    - HTML and CSS  
    - Data Visualization  
    
    🎯 **Professional**  
    - Project Management  
    - Student
    """)

# ============================================
# PROJECTS SECTION
# ============================================
st.header("🚀 Featured Projects", divider="gray")

# Project 1
with st.expander("🔍 Project 1: BMI Calculator", expanded=True):
    proj_col1, proj_col2 = st.columns([1, 3])
    with proj_col1:
        try:
            st.image("BMI.png", use_container_width=True)
        except:
            st.image(Image.new('RGB', (600, 400), color='#333'))
    with proj_col2:
        st.write("""
        ### Technologies Used
        - Python, Streamlit
        - Machine Learning
        - Cloud Deployment
        
        ### Key Features
        - Real-time analytics dashboard
        - Predictive modeling
        - Automated reporting
        """)
        st.link_button("View on GitHub", "https://github.com/muhammadhussain2024/BMI-calculator/blob/main/cal.py")
        st.link_button("View on Streamlit","https://muhammadhussain2024-bmi-calculator-cal-sl2pqk.streamlit.app/")

# Project 2
with st.expander("📊 Project 2: Cooldown Timer"):
    proj_col1, proj_col2 = st.columns([1, 3])
    with proj_col1:
        try:
            st.image("cooldown.png", use_container_width=True)
        except:
            st.image(Image.new('RGB', (600, 400), color='#333'))
    with proj_col2:
        st.write("""
        ### Technologies Used
        - Python
        - Streamlit
        
        ### Key Features
        - Interactive visualizations
        - Custom dashboard creation
        - Team collaboration tools
        """)
        st.link_button("View code on Github", "https://github.com/muhammadhussain2024/cooldown-timer/blob/main/cool.py")
        st.link_button("View on Streamlit","https://muhammadhussain2024-cooldown-timer-cool-pwfwtp.streamlit.app/")

# ============================================
# CONTACT SECTION WITH EMAIL FUNCTIONALITY
# ============================================
st.header("📨 Get In Touch", divider="gray")

contact_form = """
<form action="https://formsubmit.co/syedmuhammadhussain2020@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="hidden" name="_subject" value="New Portfolio Message">
     <input type="hidden" name="_next" value="https://your-portfolio-url.com/thank-you">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message" required></textarea>
     <button type="submit">Send Message</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Add custom CSS for the contact form
st.markdown("""
<style>
input[type="text"], input[type="email"], textarea {
    width: 100%;
    padding: 12px;
    border: 1px solid #4F4F4F;
    border-radius: 4px;
    box-sizing: border-box;
    margin-top: 6px;
    margin-bottom: 16px;
    resize: vertical;
    background-color: #1E1E1E;
    color: white;
}
textarea {
    height: 120px;
}
button[type="submit"] {
    background-color: #4CAF50;
    color: white;
    padding: 12px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
}
button[type="submit"]:hover {
    background-color: #45a049;
}
</style>
""", unsafe_allow_html=True)

# ============================================
# FOOTER
# ============================================
st.markdown("---")
st.markdown("© 2025 Syed Muhammad Hussain | Made with Streamlit")