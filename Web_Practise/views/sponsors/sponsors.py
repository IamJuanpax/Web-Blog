import reflex as rx
from Web_Practise.components.title import title
from Web_Practise.components.link_sponsor import link_sponsor
from Web_Practise.views import constants as cs
from Web_Practise.styles import styles

def sponsors() -> rx.Component:
    return rx.vstack(
        title("Sponsors"),
        rx.hstack(
                link_sponsor(
                    "redbull.jpg",
                    cs.REDBULL,
                    "logo de redbull"
                    ),
                link_sponsor(
                    "pepsi.jpg",
                    cs.PEPSI,
                    "logo de pepsi"
                    ),
                link_sponsor(
                    "spotify.jpg",
                    cs.SPOTIFY,
                    "logo de spotify"
                    ),
                link_sponsor(
                    "netflix.jpg",
                    cs.NETFLIX,
                    "logo de netflix"
                    ),
                spacing=styles.Size.MEDIUM.value
            ),
            width="100%",
            align_items="start",
        )