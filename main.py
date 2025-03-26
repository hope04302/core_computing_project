import streamlit as st
import requests as req


st.set_page_config(
    page_title="Yoon's Computing Portfolio",
    page_icon=':computer:',
    layout='wide',
)


def sidebar_profile(github_nickname="hope04302"):

    github_api_url = f"https://api.github.com/users/{github_nickname}"

    github_api = req.request('GET', github_api_url).json()
    github_name = github_api['name']
    github_image_url = github_api['avatar_url']
    github_url = github_api['html_url']

    st.sidebar.image(github_image_url)
    st.sidebar.write(f"## Manager:")
    st.sidebar.write(f"## {github_nickname} ({github_name})")
    st.sidebar.page_link(label="Go to Github Page", page=github_url, icon="➡️")


st.sidebar.title("한결같은 자료공장")
sidebar_profile(github_nickname="hope04302")

# pg = st.navigation({
#     "Your Account": ["page1.py", "page2.py"]
# })
# pg.run()
