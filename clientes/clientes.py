from excepciones import (
    ClienteError,
    registrar_info,
    registrar_error
)


class Cliente:

    lista_clientes = []

    def __init__(

        self,
        nombre,
        cedula,
        correo

    ):

        self.__nombre = nombre
        self.__cedula = cedula
        self.__correo = correo

        self.validar_datos()

        Cliente.lista_clientes.append(self)

        registrar_info(
            f"Cliente registrado: {nombre}"
        )

    # ==================================
    # VALIDACIONES
    # ==================================

    def validar_datos(self):

        try:

            if len(self.__nombre.strip()) < 3:

                raise ClienteError(
                    "Nombre inválido"
                )

            if not self.__cedula.isdigit():

                raise ClienteError(
                    "Cédula inválida"
                )

            if "@" not in self.__correo:

                raise ClienteError(
                    "Correo inválido"
                )

        except ClienteError as error:

            registrar_error(str(error))

            raise

    # ==================================
    # GETTERS
    # ==================================

    @property
    def nombre(self):

        return self.__nombre

    @property
    def cedula(self):

        return self.__cedula

    @property
    def correo(self):

        return self.__correo

    # ==================================
    # MOSTRAR
    # ==================================

    def mostrar_cliente(self):

        return (

            f"Nombre: {self.__nombre}\n"

            f"Cédula: {self.__cedula}\n"

            f"Correo: {self.__correo}"

        )
