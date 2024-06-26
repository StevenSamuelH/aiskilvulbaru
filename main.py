import streamlit as st
from streamlit_option_menu import option_menu
import os
from dotenv import load_dotenv
import dashboard, account, prediction, chatbot, about, watson, data_input

# Load environment variables from .env file
load_dotenv()

st.set_page_config(
    page_title="UMKMAI",
)

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        with st.sidebar:
            selected_option = option_menu(
                menu_title='UMKMAI',
                options=['Account', 'Google Sheet Link', 'Dashboard', 'Prediction', 'Prediction with IBM Watson','Chatbot', 'About'],
                icons=['person-circle', 'bar-chart-fill', 'bi bi-table','bi bi-graph-up','bi bi-cloud', 'chat-fill', 'info-circle-fill'],
                menu_icon='bi bi-robot',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "18px", "text-align": "left", "margin": "0px", "--hover-color": " #6FC276"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

        if selected_option == "Account":
            account.app()
        elif 'useremail' not in st.session_state or st.session_state['useremail'] == '':
            st.warning('Please log in to access other sections')
        elif selected_option == 'Google Sheet Link':
            data_input.app()
        elif selected_option == "Dashboard":
            dashboard.app()
        elif selected_option == "Prediction":
            prediction.app()
        elif selected_option == "Prediction with IBM Watson":
            watson.app()
        elif selected_option == 'Chatbot':
            chatbot.app()
        elif selected_option == 'About':
            about.app()z

if __name__ == "__main__":
    app = MultiApp()
    app.run()
