import reflex as rx
from Web_Practise.styles import styles

def link_icon(image: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width=styles.Size.LARGE.value,
            height=styles.Size.LARGE.value,
            alt= alt
        ),
        href= url,
        is_external=True
    )