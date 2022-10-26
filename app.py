import requests
import streamlit as st
from streamlit_lottie import st_lottie

# https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="JohnMartin", page_icon=":computer:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# LOAD ASSETS (Animation:LottieFlies.com)
lottie_programming = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_wci9dxrs.json")

# HEADER SECTION
with st.container():

    st.subheader("Hi, I am John Martin! :wave:")
    st.title("A Computer Engineering Student. :computer:")
    st.write("This is the first website I created as a beginner Web Developer.")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("About Me:")
        st.write("##")
        st.write(
            """
            I am currently studying Computer Engineering at Northwestern University. I spend most of my 
            free time on learning how to code because
            I want to be a professional with it. 
            
            I am passionate about Web Development, App Development and 
            Software Engineering/Development.

            If you want to know more about me, consider following my social media accounts.

            Feel free also to visit my Github account if you want to check some of my projects.
            """
        )
        st.write("[Instagram >](https://www.instagram.com/jmartin0301/)")
        st.write("[Facebook >](https://web.facebook.com/john.martin003/)")
        st.write("[Github>](https://github.com/JohnMartin0301/My-Python-Projects)")
    with right_column:
        st_lottie(lottie_programming, height="300", key="programming")