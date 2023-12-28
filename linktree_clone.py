# link_tree_clone.py
import streamlit as st


def create_custom_button(icon_type, url, label, icon_size):
    """
    Function to create custom buttons with icons.
    Parameters:
        - icon_type: Type of icon (e.g., 'portfolio', 'github', 'tableau', 'linkedin')
        - url: URL for the button
        - label: Label for the button
        - icon_size: Size of the icon
    """
    if icon_type == "portfolio":
        icon_image = "portfolio-logo.png"
    elif icon_type == "github":
        icon_image = "github-logo.png"
    elif icon_type == "tableau":
        icon_image = "tableau-logo.png"
    elif icon_type == "linkedin":
        icon_image = "linked-logo.png"
    else:
        st.error("Invalid icon type")

    # Apply styling for button text and box
    button_style = (
        f"background-color: #685344; color: #cfcfcf; border: 2px solid #685344; "
        "border-radius: 5px; padding: 5px; margin: 10px;"
    )

    # Create button with styling
    st.image(icon_image, use_container_width=True)
    st.button(label, on_click=open_url, args=(url,), style=button_style)


def open_url(url):
    """
    Function to open URL in a new tab.
    """
    js = f"window.open('{url}','_blank')"
    html = f"<script>{js}</script>"
    st.markdown(html, unsafe_allow_html=True)


def main():
    # Apply background color to the whole page
    st.markdown(
        "<style>" "body { background-color: #cfcfcf; }" "</style>",
        unsafe_allow_html=True,
    )

    # Display Photo
    st.image("profile-pic.png", width=300, caption="Nikita Prasad")

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

    # Creating buttons for social media links
    create_custom_button(
        "portfolio",
        "https://www.notion.so/Hi-ya-I-m-Nikita-Prasad-f7115123c49e418ebebe6adca109b406?pvs=4",
        "See My Work: Portfolio",
        icon_size=(50, 50),
    )
    create_custom_button(
        "github",
        "https://github.com/nikitaprasad21",
        "Checkout My Latest Projects: GitHub Repositories",
        icon_size=(50, 50),
    )
    create_custom_button(
        "tableau",
        "https://public.tableau.com/app/profile/nikita.prasad",
        "Explore My Data Stories: Tableau Dashboards",
        icon_size=(50, 50),
    )
    create_custom_button(
        "linkedin",
        "https://www.linkedin.com/in/nikita-prasad-analyst/",
        "Let's Connect: LinkedIn",
        icon_size=(50, 50),
    )


if __name__ == "__main__":
    main()
