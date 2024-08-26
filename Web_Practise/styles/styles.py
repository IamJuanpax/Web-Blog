import reflex as rx
from enum import Enum
from .colors import Color, Color_Text
from .fonts import Font, FontWeight

# Constants
MAX_WIDTH = "600px"

STYLESHEETSS = [
    "https://fonts.googleapis.com/css?family=Poppins:wght@300;500&display=swap"     # En caso de que no agarre la fuente, cambiar "css" por "css2"
]

# Sizes
class Size(Enum):
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"


# Style
BASE_STYLE={
    "font_family":Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color":Color.BACKGROUND.value,     # el color que le queremos dar al fondo de la pagina
    "heading":{
        "size":"md",
        "color":Color_Text.HEADER.value,
        "font_family":Font.TITLE.value,
        "font_weight": FontWeight.MEDIUM.value
    },
    rx.button:{             # aca modificamos el aspecto de los botones
        "width":"100%",
        "height":"100%",
        "padding":Size.SMALL.value,
        "border_radius":Size.DEFAULT.value,
        "color":Color_Text.HEADER.value,
        "background_color":Color.CONTENT.value,   # el color que le querramos dar a los botones
        "_hover":{
            "background_color": Color.SECONDARY.value,  # Cambia el color de fondo al pasar el cursor
            "cursor": "pointer",  # Cambia el cursor al de presionar
        }
    },
    rx.link:{
        "text_decoration":"none",
        "_hover": {}
    }
}

title_style = dict(
    width= "100%",
    font_family=Font.TITLE.value,
    font_weight= FontWeight.MEDIUM.value,
    padding_top=Size.DEFAULT.value,
    color=Color_Text.HEADER.value
)

button_title_style = dict(
    font_size=Size.DEFAULT.value,
    color=Color_Text.HEADER.value,
    font_family=Font.TITLE.value,
    font_weight= FontWeight.MEDIUM.value
)

button_body_style = dict(
    font_size=Size.MEDIUM.value,
    color=Color_Text.BODY.value,
    font_family=Font.DEFAULT.value,
    font_weight= FontWeight.LIGHT.value
)

footer_style = dict(
    width=Size.BIG.value,  # Ancho de la imagen
    height=Size.BIG.value,  # Altura de la imagen
    margin_bottom=Size.MEDIUM.value,
    font_family=Font.DEFAULT.value
)