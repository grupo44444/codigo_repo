import logging


logging.basicConfig(

    filename="excepciones/logs.txt",

    level=logging.INFO,

    format="%(asctime)s - %(levelname)s - %(message)s"
)


def registrar_info(mensaje):

    logging.info(mensaje)


def registrar_error(mensaje):

    logging.error(mensaje)