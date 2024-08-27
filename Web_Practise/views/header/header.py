import reflex as rx
from Web_Practise.components.title import title
from Web_Practise.components.link_icon import link_icon
from Web_Practise.styles import styles
from Web_Practise.styles.colors import Color_Text, Color
from Web_Practise.views import constants as cs

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                size="xl",
                src="logo_titulo.png",
                radius="full",
                border="4px solid",
                border_color=Color.PRIMARY.value,
                width="100px",  # Ancho de la imagen
                height="100px"  # Alto de la imagen
            ),
            rx.vstack(
                rx.heading(
                    "Juanpa Britos",
                    color=Color_Text.HEADER.value
                    ),
                rx.text(
                    "Estudiante de Sistemas | Programador",
                    margin_top="0px",
                    color=Color_Text.BODY.value
                ),

                rx.hstack(
                    link_icon("icons/linkedin.svg", cs.LINKEDIN, "Linkedin"), 
                    link_icon("icons/instagram.svg", cs.INSTAGRAM, "Instagram"), 
                    link_icon("icons/github.svg", cs.GITHUB, "Github"), 
                    spacing=styles.Size.LARGE.value
                ),
                
                width="auto",
                align_items="start",
                spacing="0px"
            ),
            spacing=styles.Size.DEFAULT.value,
            align_items="start",
            justify_content="start",
            width="100%"
        ),
            title("Un poco de mi"),
            rx.text(
                    f"""Soy un estudiante de Ingenieria en Sistemas con una gran
                    vocacion hacia la programacion. Esta pagina esta creada
                    en Python con la libreria Reflex para probar mis conocimientos
                    en Programacion. Aca encontraran links a mis disintas redes""",
                    color=Color_Text.BODY.value
                    ),

            align_items="start",  # Alinea los elementos dentro del vstack
            text_align="start"     # Alinea el texto al centro
        )

