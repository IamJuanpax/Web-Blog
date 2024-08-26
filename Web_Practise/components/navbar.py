import reflex as rx
from Web_Practise.styles import styles
from Web_Practise.styles.colors import Color_Text, Color

def navbar() -> rx.Component:
    return rx.hstack(
        rx.image(
            src="JUANPAX.png",
            width="100px",
            height="auto"
            ),
            position="sticky",
            bg=Color.CONTENT.value,
            padding_x=styles.Size.BIG.value,
            padding_y=styles.Size.DEFAULT.value,
            z_index="999",
            top="0",
    )