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


def st_button(icon, url, label, iconsize):
    if icon == "portfolio":
        button_code = f"""
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                <svg
                xmlns="http://www.w3.org/2000/svg"
                x="0px" y="0px"
                width={iconsize} height={iconsize}
                viewBox="0 0 50 50"
                style=" fill:#26e07f;"><g fill="none" fill-rule="nonzero" stroke="none" stroke-width="1" stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="10" stroke-dasharray="" stroke-dashoffset="0" font-family="none" font-weight="none" font-size="none" text-anchor="none" style="mix-blend-mode: normal"><path d="M0,172v-172h172v172z" fill="none"></path><g fill="#1fb141"><path d="M21.5,21.5v129h64.5v-32.25v-64.5v-32.25zM86,53.75c0,17.7805 14.4695,32.25 32.25,32.25c17.7805,0 32.25,-14.4695 32.25,-32.25c0,-17.7805 -14.4695,-32.25 -32.25,-32.25c-17.7805,0 -32.25,14.4695 -32.25,32.25zM118.25,86c-17.7805,0 -32.25,14.4695 -32.25,32.25c0,17.7805 14.4695,32.25 32.25,32.25c17.7805,0 32.25,-14.4695 32.25,-32.25c0,-17.7805 -14.4695,-32.25 -32.25,-32.25z"></path></g></g></svg>
                {label}
            </a>
        </p>"""

    elif icon == "github":
        button_code = f"""
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width={iconsize} height={iconsize} viewBox="0 0 50 50">
                    <path d="M17.791,46.836C18.502,46.53,19,45.823,19,45v-5.4c0-0.197,0.016-0.402,0.041-0.61C19.027,38.994,19.014,38.997,19,39 c0,0-3,0-3.6,0c-1.5,0-2.8-0.6-3.4-1.8c-0.7-1.3-1-3.5-2.8-4.7C8.9,32.3,9.1,32,9.7,32c0.6,0.1,1.9,0.9,2.7,2c0.9,1.1,1.8,2,3.4,2 c2.487,0,3.82-0.125,4.622-0.555C21.356,34.056,22.649,33,24,33v-0.025c-5.668-0.182-9.289-2.066-10.975-4.975 c-3.665,0.042-6.856,0.405-8.677,0.707c-0.058-0.327-0.108-0.656-0.151-0.987c1.797-0.296,4.843-0.647,8.345-0.714 c-0.112-0.276-0.209-0.559-0.291-0.849c-3.511-0.178-6.541-0.039-8.187,0.097c-0.02-0.332-0.047-0.663-0.051-0.999 c1.649-0.135,4.597-0.27,8.018-0.111c-0.079-0.5-0.13-1.011-0.13-1.543c0-1.7,0.6-3.5,1.7-5c-0.5-1.7-1.2-5.3,0.2-6.6 c2.7,0,4.6,1.3,5.5,2.1C21,13.4,22.9,13,25,13s4,0.4,5.6,1.1c0.9-0.8,2.8-2.1,5.5-2.1c1.5,1.4,0.7,5,0.2,6.6c1.1,1.5,1.7,3.2,1.6,5 c0,0.484-0.045,0.951-0.11,1.409c3.499-0.172,6.527-0.034,8.204,0.102c-0.002,0.337-0.033,0.666-0.051,0.999 c-1.671-0.138-4.775-0.28-8.359-0.089c-0.089,0.336-0.197,0.663-0.325,0.98c3.546,0.046,6.665,0.389,8.548,0.689 c-0.043,0.332-0.093,0.661-0.151,0.987c-1.912-0.306-5.171-0.664-8.879-0.682C35.112,30.873,31.557,32.75,26,32.969V33 c2.6,0,5,3.9,5,6.6V45c0,0.823,0.498,1.53,1.209,1.836C41.37,43.804,48,35.164,48,25C48,12.318,37.683,2,25,2S2,12.318,2,25 C2,35.164,8.63,43.804,17.791,46.836z"></path>
                </svg>
                {label}
            </a>
        </p>"""

    elif icon == "tableau":
        button_code = f"""
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width={iconsize} height={iconsize} viewBox="0 0 48 48">
                <rect width="1.5" height="9" x="22.75" y="1" fill="#78909c"></rect><rect width="9" height="1.5" x="19" y="4.75" fill="#78909c"></rect><rect width="1.5" height="9" x="40.75" y="19" fill="#5c6bc0"></rect><rect width="9" height="1.5" x="37" y="22.75" fill="#5c6bc0"></rect><rect width="1.5" height="9" x="4.75" y="19" fill="#78909c"></rect><rect width="9" height="1.5" x="1" y="22.75" fill="#78909c"></rect><rect width="1.5" height="9" x="22.75" y="37" fill="#5c6bc0"></rect><rect width="9" height="1.5" x="19" y="40.75" fill="#5c6bc0"></rect><rect width="17" height="3" x="15" y="22" fill="#e8762d"></rect><rect width="3" height="17" x="22" y="15" fill="#e8762d"></rect><rect width="2" height="14" x="11" y="6" fill="#ffa000"></rect><rect width="14" height="2" x="5" y="12" fill="#ffa000"></rect><rect width="2" height="14" x="34" y="6" fill="#607d8b"></rect><rect width="14" height="2" x="28" y="12" fill="#607d8b"></rect><rect width="2" height="14" x="11" y="27" fill="#c62828"></rect><rect width="14" height="2" x="5" y="33" fill="#c62828"></rect><rect width="2" height="14" x="34" y="27" fill="#0d47a1"></rect><rect width="14" height="2" x="28" y="33" fill="#0d47a1"></rect>
                </svg>
                {label}
            </a>
        </p>"""

    elif icon == "linkedin":
        button_code = f"""
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width={iconsize} height={iconsize} viewBox="0 0 48 48">
                <path fill="#0288D1" d="M42,37c0,2.762-2.238,5-5,5H11c-2.761,0-5-2.238-5-5V11c0-2.762,2.239-5,5-5h26c2.762,0,5,2.238,5,5V37z"></path><path fill="#FFF" d="M12 19H17V36H12zM14.485 17h-.028C12.965 17 12 15.888 12 14.499 12 13.08 12.995 12 14.514 12c1.521 0 2.458 1.08 2.486 2.499C17 15.887 16.035 17 14.485 17zM36 36h-5v-9.099c0-2.198-1.225-3.698-3.192-3.698-1.501 0-2.313 1.012-2.707 1.99C24.957 25.543 25 26.511 25 27v9h-5V19h5v2.616C25.721 20.5 26.85 19 29.738 19c3.578 0 6.261 2.25 6.261 7.274L36 36 36 36z"></path>
                </svg>
                {label}
            </a>
        </p>"""

    elif icon == "":
        button_code = f"""
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                {label}
            </a>
        </p>"""
    return st.markdown(button_code, unsafe_allow_html=True)
