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