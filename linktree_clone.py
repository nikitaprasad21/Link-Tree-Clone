# link_tree_clone.py
import streamlit as st
from PIL import Image
from st_functions import load_css, st_button

load_css()

# Display Photo
col1, col2, col3 = st.columns(3)
# Open the image
image = Image.open("profile-pic.png")

# Add image to col2 with a specified width
col2.image(image, width=180)


# User name and small description
st.title("Hi-ya!!!👋,")
st.title("I'm Nikita Prasad")

st.write("Data Analyst | Machine Learning and Data Analytics Practitioner")

icon_size = 20

# Creating buttons for social media links
st_button(
    "portfolio",
    "https://www.notion.so/Hi-ya-I-m-Nikita-Prasad-f7115123c49e418ebebe6adca109b406?pvs=4",
    "See My Work: Portfolio",
    icon_size,
)
st_button(
    "github",
    "https://github.com/nikitaprasad21",
    "Checkout My Projects: GitHub Repositories",
    icon_size,
)
st_button(
    "tableau",
    "https://public.tableau.com/app/profile/nikita.prasad",
    "Explore My Data Stories: Tableau Dashboards",
    icon_size,
)
st_button(
    "linkedin",
    "https://www.linkedin.com/in/nikita-prasad-analyst/",
    "Let's Connect: LinkedIn",
    icon_size,
)
