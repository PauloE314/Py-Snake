class FontNameError(BaseException):
    """
    Exception para nome de fontes repetidos
    """
    def __init__(self, message = "A fonte já foi utilizada anteriormente"):
        self.message = message
        super().__init__(self.message)


class FontNotFoundError(BaseException):
    """
    Exception para fontes inexistentes
    """
    def __init__(self, message = "Essa fonte não foi encontrada"):
        self.message = message
        super().__init__(self.message)

class SnakeOutOfAxis(BaseException):
    """
    Exception para caso a cobra esteja fora de um dos eixos
    """
    def __init__(self, axis = None):
        self.message = "A cobra está fora do eixo " + str(axis)

        if not axis:
            self.message = "A cobra está fora de um dos eixos"

class StateDoesNotExist(BaseException):
    """
    Exception para um estado que não exista
    """
    def __init__(self, state_name: str = None):
        self.message = f"O estado '{state_name}' não existe"

class NextStateException(BaseException):
    """
    Exception para avançar para o próximo estado
    """
    def __init__(self, message = None):
        assert message, "O próximo estado deve ter um nome"
        self.message = message


class EndGameException(BaseException):
    """
    Exception para terminar jogo
    """
    def __init__(self):
        self.message = None