import streamlit as st 
from streamlit_lottie import st_lottie 
import requests
import json

st.set_page_config(page_title='DeepIntoAI', page_icon=':smiley:', layout='wide')

st.markdown("<h1 style='text-align: center; color: #8425eb;'>Deep Into AI 😍  </h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;'> Let's Learn Build Explore </h2>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center;'> A community of AI enthusiasts </h3>", unsafe_allow_html=True)

def load_lottieurl(url: str):
    r = requests.get(url)
    return None if r.status_code != 200 else r.json()
# Load the Lottie animation from URL
lottie_url = "https://assets3.lottiefiles.com/packages/lf20_M9p23l.json"
lottie_json = load_lottieurl(lottie_url)
st_lottie(lottie_json)

# github_link = "https://github.com/your_username/your_repository"
# github_logo_url = "https://cdn-icons-png.flaticon.com/512/25/25231.png"

# st.markdown(f'<a href="{github_link}"><img src="{github_logo_url}" style="align:center;" alt="GitHub logo" width="50"></a>', unsafe_allow_html=True)

st.caption('Built with ❤️ by Zoya Jamadar')






