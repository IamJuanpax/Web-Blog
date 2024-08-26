import reflex as rx
from Web_Practise.styles import styles

def title(text: str)  -> rx.Component:
    return rx.heading(
        text,
        size="lg",
        style=styles.title_style
    )