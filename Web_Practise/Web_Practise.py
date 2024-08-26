import reflex as rx
from Web_Practise.components.navbar import navbar
from Web_Practise.components.footer import footer
from Web_Practise.views.header.header import header
from Web_Practise.views.links.links import links
from Web_Practise.views.sponsors.sponsors import sponsors
from Web_Practise.styles import styles

from rxconfig import config


class State(rx.State):
    pass


def index() -> rx.Component:
    # Contenemos todo en una "caja"
    return rx.box(
        # La barra de navegacion
        navbar(),
        # Centramos todo lo que esta adentro
        rx.center(
            # Un bloque de lo que queremos mostrar
            rx.vstack(
                header(),
                links(),
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=styles.Size.DEFAULT.value,
                padding=styles.Size.BIG.value
            )
        ),
        # Pie de pagina
        footer()
    )

# De esta forma arrancamos pagina
app = rx.App(
    stylesheets=styles.STYLESHEETSS,
    style=styles.BASE_STYLE
)
app.add_page(
    index,
    title= "Blog Personal",
    description= "En esta pagina muestro mis proyectos y redes sociales",
    )
