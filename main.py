import streamlit as st
from streamlit_option_menu import option_menu
import home
import movie_details
import Genres

# Set page configuration
st.set_page_config(
    page_title="Project"
)

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title="Recommendation",
                options=['Home', 'Movie Details','Genres'],
                 icons=['house-fill', 'person-circle'],
                  menu_icon='chat-text-fill',
                default_index=0,
                 styles={
                    "container": { "padding": "5!important", "background-color": "#C0C0C0" },
                    "icon": {"color": "orange", "font-size": "25px"},
                    "nav-link": {
                        "font-size": "16px",
                        "text-align": "left",
                        "margin": "0px",
                        "color": "black",  # Text color for menu items
                        "--hover-color": "#D3D3D3" ,
                    },
                    "nav-link-selected": {"background-color": "#02ab21"},
                    "menu-title": {"color": "black"}  # Text color for menu title
                }
            )

        # Run the corresponding app based on the selected option
        if app == 'Home':
            home.app()
        elif app == 'Movie Details':
            movie_details.app()
        elif app == 'Genres':
            Genres.app()

# Example usage
app = MultiApp()
app.add_app('Home', home.app)
app.add_app('Movie Details', movie_details.app)
app.add_app('Genres search',Genres.app)
app.run()
