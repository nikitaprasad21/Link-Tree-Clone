import streamlit as st


def load_css():
    """
    The function `load_css()` loads a CSS file and applies its styles to the current web page.
    """
    with open("style.css") as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    st.markdown(
        '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
        unsafe_allow_html=True,
    )


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
