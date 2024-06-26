import streamlit as st

from streamlit_option_menu import option_menu

import home,about,trending,test
import you
import post
import prediction
import History
import Task

st.set_page_config(
    page_title="DiaPredict",
)


class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:
            app = option_menu(
                menu_title='DiaPredict',
                options=['Home','Account','Prediction','Your Posts','Through Time','History','Task','Trending','About'],
                icons=['house-fill', 'person-circle', 'trophy-fill', 'chat-fill', 'info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"}, }

            )

        if app == "Home":
            home.app()
        if app == "Account":
            test.app()
        if app == 'Your Posts':
            you.app()
        if app =='Task':
            Task.app()
        if app == "Through Time":
            post.app()
        if app == 'Prediction':
            prediction.app()
        if app == 'History':
            History.app()
        if app == "Trending":
            trending.app()
        if app == 'About':
            about.app()

    run()