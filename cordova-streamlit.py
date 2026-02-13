import streamlit as st

st.set_page_config(
    page_title="Johann's Portfolio",
    page_icon=":wave:",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About Me", "Portfolio", "Contact"])

# Home Page
if page == "Home":
    st.markdown("<h1 style='text-align: center;'>Welcome to My Portfolio</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Hello, I am Johann Anthony P. Cordova</h1>", unsafe_allow_html=True)
    st.markdown("""
<p style='text-align: center; font-size: px; line-height: 1.6;'>
I am a passionate student and aspiring developer with a deep interest in <strong>coding</strong> and <strong>data analytics</strong>. 
I love turning complex data into meaningful insights and building interactive applications that solve real-world problems.  

Alongside technology, I am also fascinated by <strong>financial markets</strong> and trading. 
I enjoy learning and applying the <strong>Wyckoff Methodology</strong> and <strong>Elliott Wave Theory</strong> to understand market behavior and improve my trading strategies.  

Through my portfolio, I aim to showcase my projects, skills, and journey in both <strong>tech</strong> and <strong>trading analysis</strong>. 
Feel free to explore my work and connect with me!
</p>
""", unsafe_allow_html=True)

# About Me Page
elif page == "About Me":
    st.markdown("<h1 style='text-align: center;'>About Me</h1>", unsafe_allow_html=True)
    st.image("me.jpg", caption="Me")
    st.write("""
    My name is Johann Cordova. I am a student passionate about coding, data analytics, and web development.)
    
    **Interests & Skills:**
    - Python, JavaScript, Streamlit
    - Data Analysis & Visualization
    - Trading & Financial Markets
    - Graphic Design
    """)
    st.subheader("🎉 Fun Facts")
    st.markdown("""
        - I love creating interactive apps with **Streamlit**.  
        - I enjoy exploring and analyzing financial markets.  
        - Coffee is my fuel! ☕  
        - I am a huge fan of **fantasy films and series**, especially **The Lord of the Rings (LOTR)** and **Game of Thrones (GOT)**.  
        - I enjoy learning new skills and continuously improving in both coding and trading.
        """)

# Portfolio Page
elif page == "Portfolio":
    st.header("My Portfolio Projects")
    
    # Project 1
    st.subheader("QuickCheck : Attendance made Easy!")
    st.write("Github: [github.com/QuickCheck](https://github.com/Veranojoel/QuickCheck)")
    st.write("Co-created an application that utilizes QR code scanning to simplify attendance tracking for students and teachers. Built with Streamlit and Python, it provides a user-friendly interface for managing attendance records efficiently.")

    # Project 2
    st.subheader("Crypto-based notestaking app")
    st.write("Github: [github.com/BlockNotes](https://github.com/johanngwapo/blockchain-popularmonster)")
    st.write("Built a note-taking application that integrates blockchain technology to ensure secure and tamper-proof storage of notes. The app allows users to create, edit, and store their notes on the blockchain, providing enhanced security and accessibility.")

    # Project 3
    st.subheader("Video Editing & Cinematography")
    st.image("davinci.png", caption="Project 3 Screenshot")
    st.write("Created visually appealing video content for various platforms using DaVinci Resolve. Developed skills in video editing, color grading, and cinematography to produce engaging and high-quality videos for social media and personal projects.")
    

# Contact Page
elif page == "Contact":
    st.header("Contact Me")
    st.write("Feel free to reach out via email or connect on LinkedIn!")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send Message")
        if submitted:
            st.success(f"Thank you {name}! Your message has been sent successfully.")

    st.write("---")
    st.write("📧 Email: johannanthony.cordova@cit.edu")
    st.write("🔗 Github: [github.com/johanngwapo](https://github.com/johanngwapo)")
    st.write("🔗 LinkedIn: [linkedin.com/in/johann](https://linkedin.com/in/johann)")
