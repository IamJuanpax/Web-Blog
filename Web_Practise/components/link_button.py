import reflex as rx
from Web_Practise.styles import styles

# Creamos un boton personalizado
def link_button(title: str, body: str, image: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=styles.Size.BIG.value,
                    height=styles.Size.BIG.value,
                    alt= title
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    align_items="start",
                    spacing="0px",
                ),
                align_items="center",  # Alinea verticalmente el contenido en hstack
            ),
            justify_content="start",  # Alinea el contenido del botón hacia la izquierda
        ),
        href=url,
        is_external=True,
        width="100%"
    )
