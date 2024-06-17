import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
# Set the page configuration
st.set_page_config(page_title="Paveen Paul Portfolio", layout="wide")

# Load your profile image
# profile_image = Image.open("pyspider.jpg")
imgg = "https://lottie.host/8594cc0c-276f-4b07-b4f0-b338b8bbda93/JiPuh4wvqB.json"
# Sidebar with navigation
# st.sidebar.image(profile_image, width=150)
# st.sidebar.title("    Paveen Paul")
# st.sidebar.write("    Paveen Paul")  # Add empty space
# st.sidebar.title("Paveen Paul") 
# st.sidebar.markdown("**Aspiring Data Analyst/Product Manager**")
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

demo_image = load_lottieurl(imgg)
# Sidebar navigation
# section = st.sidebar.radio("Navigation", ["About Me", "Experience", "Education", "Projects", "Technical Skills", "Certifications", "Contact"])
with st.sidebar:
    with st.container():
        l, m, r = st.columns((1,3,1))
        with l:
            st.empty()
        with m:
            st.image(Image.open("fotor-202406171942.png"), width=175)
        with r:
            st.empty()
        section = option_menu(
                                "Paveen Paul", 
                                ["About Me", "Experience", "Education", "Technical Skills", "Projects", "Certifications", "Contact"],
                                icons=['person fill', 'globe', 'clock history', 'tools', 'book half', 'clipboard', 'trophy fill', 'heart', 'pencil square', 'image', 'paperclip', 'star fill', 'envelope'],
                                menu_icon="mortarboard", 
                                default_index=0,
                                styles={
                "container": {"padding": "0!important", "background-color": "#f0f2f6"},
                "icon": {"color": "black", "font-size": "20px"}, 
                "nav-link": {"font-size": "17px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "#cfcfb4"},
    }
    )


def load_about_me():
    st.title('About Me')
    
    # Set up columns for layout
    col1, col2 = st.columns([3, 2])

    # Column 1: Text content
    with col1:
        st.markdown("""
    👋 Hi, I'm Paveen Paul! I'm currently pursuing my Master's in Robotics and Artificial Intelligence.

    💼 In my previous roles, I've served as a team lead and software developer, gaining valuable experience in Python and Django.

    🚀 I have a strong foundation in various fields including Natural Language Processing (NLP), Machine Learning, Deep Learning, and more.

    🌟 My skills include Python programming, Django web framework, data analysis, and creating intelligent systems.

    🎓 Academic Pursuits: Mastering Robotics and Artificial Intelligence to innovate and solve complex problems.

    🌐 I'm passionate about leveraging technology to build impactful solutions and continuously learning in the ever-evolving field of AI.

    🔍 I'm currently exploring opportunities to apply my skills and contribute to exciting projects in AI and robotics.

    """)

    # Column 2: Image
    with col2:
        # st.image('AI-and-its-uses-topper.gif', use_column_width=True)
        st_lottie(demo_image,height=450,width=450)

def load_experience():
    st.title("Experience")
    
    # Create a two-column layout
    col1, col2 = st.columns([0.3, 3])
    
    with col1:
        st.image("mynextfilmmnf_logo.jpeg", width=100)  # Adjust width as needed
    
    with col2:
        st.write("""
        ### Technical Lead
        **My Next Film Pvt. Ltd.**  
        New Delhi, India (01/2023 - 02/2024)
        - Architected full-fledged auction house with blockchain security using Python-Django, driving 50% of the company’s revenue per year.
        - Orchestrated and executed serverless uploading of all the media files and static files to cloud storage from web application, resulting in reduced network congestion and server CPU usage by 20% by leveraging AWS Lambda and S3 integration.
        - Provided video subtitling and dubbing in 114 languages across the globe using speech-to-text, translation, and text-to-speech APIs from Google, Amazon, and Microsoft.
        - Implemented cost-effective and efficient Digital Payment Gateways, integrating Razorpay for Indian clients and Stripe for international transactions.
        - Created audio-visual narrations and one-pagers of film scripts using MoviePy, FPDF, pillow Python libraries.
        - Created a text format correction script using Pandas and Python-docx libraries, improving script formatting accuracy and consistency.
        - Created a beat sheet generation tool by implementing OpenAI API and threading.
        """)

def load_education():
    st.title("Education")
    col1, col2 = st.columns([0.5, 3])
    
    with col1:
        st.image("images.png", width=150)
        st.write("")
        st.write("")
        st.image("images.png", width=150)
        st.write("")
        st.write("")
        st.image("rpt.png", width=150)
    with col2:
        st.write("""
        ### Masters of Technology
        **M S Ramaiah Institute of Technology**  
        Bangalore, India (01/2024 - Present)
        - Major in Robotics and Artificial Intelligence Engineering
        """)
        st.write("___")
        ### Bachelor of Technology
        st.write("""
        **M S Ramaiah University of Applied Sciences**  
        Bangalore, India (08/2019 - 05/2022)
        - Major in Automotive Engineering
        """)
        st.write("___")
        ### Diploma
        st.write("""
        **Rajeev Polytechnic**  
        Bangalore, India (05/2016 - 06/2019)
        - Major in Mechatronics Engineering
        """)
        

        
# Projects section
def load_projects():
    st.title("Projects")
    st.write("""
    ### A* Pathfinding Algorithm
    - Implemented an efficient pathfinding algorithm in Python with multiple distance metrics and Pygame Visualization. (05/2024)
    
    ### TriViBot: Bluetooth Controlled Bot Using Arduino Mega
    - Designed a Bluetooth-controlled robot using Arduino Mega for precise wireless operation. (04/2024)
    
    ### Gesture Writing Using OpenCV
    - Created a gesture-based writing application using OpenCV for real-time hand tracking and gesture recognition. (01/2024)
    
    ### Face Mask and Social Distance Detection Using OpenCV
    - Developed a real-time detection system for face masks and social distancing using OpenCV. (12/2023)
    
    ### Spam Email Classification
    - Developed a machine learning model for high-accuracy spam email detection using natural language processing. (09/2023)
    
    ### Text Emotion Classification
    - Implemented a system to classify emotions in text using machine learning algorithms. (07/2023)
    
    ### Easy Plug and Play Electric Conversion for Two-Wheelers
    - Engineered a user-friendly electric conversion kit for two-wheelers to promote sustainable transportation. (03/2023)
    """)

# Technical Skills section
def load_technical_skills():
    st.title("Technical Skills")
    col1, colmid, col2 = st.columns([1,0.1, 3])
    with col1:
        st.write("""
        Programming Languages
        
        Web Development & Frameworks
        
        Databases
        
        Cloud & DevOps
        
        Operating Systems
        
        Data Analysis & AI Libraries
        
        Machine Learning & Deep Learning
        
        Engineering & Design Tools
        
        Domain Specific Knowledge
        
        Languages
        """)
    with colmid:
        st.write("""
                 :
                 
                 :
                 
                 :
                 
                 :
                 
                 :
                 
                 :
                 
                 :
                 
                 :
                 
                 :
                 
                 :
                 """)
    with col2:
        st.write("""
        Python 🐍, C++
        
        Django 🌐, Flask
        
        MSSQL, NoSQL
        
        AWS ☁️, Docker 🐳, Git
        
        Linux 🐧
        
        Pandas 🐼, NumPy, SciPy
        
        Machine Learning 🤖, Deep Learning 🧠, TensorFlow, PyTorch
        
        Catiav5, Autodesk, MATLAB
        
        Cricket Analysis 🏏, GenAI
        
        English 🌍, Kannada 🟢, Hindi 🟠
        """)

def load_certifications():
    st.title("Certifications")
    st.write("""
    - **Python Full Stack Development (PySpider)**
      - Mastered fundamental Python syntax, control flow, loops, and Data Structures
      - Acquired expertise in Django and SQL
      
    - **DevOps and Data Visualization (MSRIT)**
      - Hands-on Workshop on Cutting Edge Tools in Data Visualization and Software Development
    """)

# Contact section
def load_contact():
    st.title("Contact")
    st.write("""
    - LinkedIn: [Paveen Paul](https://www.linkedin.com/in/paveen-paul/)
    - Email: paveenpaul01@gmail.com
    - Phone: +91-7259192008
    """)

# Main function to control the layout and dynamic loading
def main():
    # Load the selected section
    if section == "About Me":
        load_about_me()
    elif section == "Experience":
        load_experience()
    elif section == "Education":
        load_education()
    elif section == "Projects":
        load_projects()
    elif section == "Technical Skills":
        load_technical_skills()
    elif section == "Certifications":
        load_certifications()
    elif section == "Contact":
        load_contact()

# Run the app
if __name__ == "__main__":
    main()
