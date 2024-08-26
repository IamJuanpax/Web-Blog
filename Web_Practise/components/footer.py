import reflex as rx
import datetime
from Web_Practise.styles import styles
from Web_Practise.styles.colors import Color_Text
from Web_Practise.views import constants as cs

def footer()  -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.image(
                src="logo.jpg",
                style=styles.footer_style,
                alt= "logotipo de la pagina"
            ),
            rx.link(
                    "Si queres aprender mas sobre programacion clickea aqui",
                    href=cs.YOUTUBE_MOUREDEV,
                    is_external=True,
                    font_size=styles.Size.MEDIUM.value,
                    margin_bottom="2px"
                    ),
            rx.text(
                    f"""Este texto acompaña a la imagen para que 
                    no se sienta sola, y la fecha de hoy es: {datetime.date.today().day}""",
                    font_size=styles.Size.MEDIUM.value,
                    margin_top="0px",
                    text_align="center"
                    ),
            align_items="center", # Alinea todos los elementos del vstack al centro
            spacing="0px",
            color=Color_Text.FOOTER.value,
            padding_y = styles.Size.DEFAULT.value,
            margin_x = styles.Size.DEFAULT.value
        ),
        width="100%",  # Que ocupe el 100% del ancho del vstack
        margin_bottom= styles.Size.BIG.value,
    )