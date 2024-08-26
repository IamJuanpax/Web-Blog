import reflex as rx
from Web_Practise.styles import styles

def link_sponsor(image: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            height=styles.Size.VERY_BIG.value,
            width="auto",
            alt= alt
            ),
            href=url,
            is_external=True
    )