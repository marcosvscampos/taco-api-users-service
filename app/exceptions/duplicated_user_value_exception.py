from fastapi import HTTPException

class DuplicatedUserValueException(HTTPException):

    def __init__(self, value:str):
        message = f"Já existe um usuário cadastrado como {value}"
        print(f">>> ERROR: {message}")
        super().__init__(status_code=412, detail=message)