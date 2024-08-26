import reflex as rx
from Web_Practise.components.link_button import link_button
from Web_Practise.components.title import title
from Web_Practise.views import constants as cs

def links() -> rx.Component:
    return rx.center(
        rx.vstack(
            # Primer VStack con los botones de redes sociales
            rx.vstack(
                title("Redes Sociales"),

                link_button("Instagram",
                            "Mira mis fotos",
                            "icons/instagram.svg",
                            cs.INSTAGRAM),

                link_button("Github",
                            "mis proyectos",
                            "icons/github.svg",
                            cs.GITHUB),

                link_button("LinkedIn",
                            "Mi pagina de Linkedin",
                            "icons/linkedin.svg",
                            cs.LINKEDIN),

                link_button("Gmail",
                            "Enviame un mensaje",
                            "icons/mensaje.svg",
                            cs.GMAIL),

                align_items="center",  # Alinea los botones dentro del vstack
                spacing="10px",        # Espaciado entre botones
                width="100%"
            ),

            # Segundo VStack con los botones de links de interés
            rx.vstack(
                title("Links de Interes"),

                link_button("YouTube-MoureDev",
                            "Donde aprendi todo sobre python",
                            "icons/youtube.svg",
                            cs.YOUTUBE_MOUREDEV_PYTHON),

                link_button("UTN",
                            "Universidad donde estudio",
                            "icons/universidad.svg",
                            cs.UTN),

                align_items="center",  # Alinea los botones dentro del vstack
                spacing="10px",        # Espaciado entre botones
                width="100%"
            ),
            spacing="20px",  # Espaciado entre los dos VStack
            width="100%"     # Asegura que el contenedor ocupe el 100% del ancho
        ),
        width="100%"          # Asegura que el contenedor ocupe el 100% del ancho
    )
