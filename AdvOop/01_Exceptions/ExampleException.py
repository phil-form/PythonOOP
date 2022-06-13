class ExampleException(Exception):
    def __init__(self, message = None, errors = None) -> None:
        super().__init__(message if message != None else "Super message!!!!!")

raise ExampleException("Un autre message super intéressent !!!")
