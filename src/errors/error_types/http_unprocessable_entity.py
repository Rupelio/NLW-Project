class HttpUnprocessableEntityError(Exception):

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = "InprocessableEntity"
        self.status_code = 422
