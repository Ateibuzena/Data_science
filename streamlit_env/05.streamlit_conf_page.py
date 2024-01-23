import streamlit as st
from PIL import Image

from modules.page_config_dict import PAGE_CONFIG

# st.set_page_config(page_title = "DSBXXRT",
#                    # page_icon = ":panda_face:",
#                    page_icon = Image.open("sources/curiosidades-del-oso-panda-1280x720x80xX.jpg"),
#                    layout = "wide",
#                    initial_sidebar_state = "collapsed",)

st.set_page_config(**PAGE_CONFIG)

# Emoji: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/

def main():
    st.title("Streamlit App.")
    st.sidebar.success("Hello")


if __name__ == "__main__":
    main()
