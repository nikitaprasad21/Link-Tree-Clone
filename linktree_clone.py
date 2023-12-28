# link_tree_clone.py
import streamlit as st
from PIL import Image
from st_functions import load_css, create_custom_button

load_css()

# Display Photo
col1, col2, col3 = st.columns(3)
# Open the image
image = Image.open("profile-pic.png")

# Add image to col2 with a specified width
col2.image(image, width=300)

# Apply background color to the whole page
st.markdown(
    "<style>" "body { background-color: #cfcfcf; }" "</style>",
    unsafe_allow_html=True,
)

# User name and small description
st.title("Hi-ya!!!👋, I'm Nikita Prasad")
st.write("Data Analyst | Machine Learning and Data Analytics Practitioner")

# Apply styling for title and description
st.markdown(
    "<p style='color: #685344; font-size: 18px; text-align: center;'>"
    "Your Name\n\nSmall description about you."
    "</p>",
    unsafe_allow_html=True,
)

icon_size = 20

# Creating buttons for social media links
create_custom_button(
    "portfolio",
    "https://www.notion.so/Hi-ya-I-m-Nikita-Prasad-f7115123c49e418ebebe6adca109b406?pvs=4",
    "See My Work: Portfolio",
    icon_size,
)

create_custom_button(
    "github",
    "https://github.com/nikitaprasad21",
    "Checkout My Latest Projects: GitHub Repositories",
    icon_size,
)

create_custom_button(
    "tableau",
    "https://public.tableau.com/app/profile/nikita.prasad",
    "Explore My Data Stories: Tableau Dashboards",
    icon_size,
)

create_custom_button(
    "linkedin",
    "https://www.linkedin.com/in/nikita-prasad-analyst/",
    "Let's Connect: LinkedIn",
    icon_size,
)