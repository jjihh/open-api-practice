"""Run both Open API practice services from one Streamlit app."""

import streamlit as st


page = st.navigation(
    [
        st.Page("met_app.py", title="Explore Artworks", icon="🎨", default=True),
        st.Page("weather_map.py", title="Weather Map", icon="🌤️"),
    ]
)
page.run()
