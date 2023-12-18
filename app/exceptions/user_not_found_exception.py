from fastapi import HTTPException

class UserNotFoundException(HTTPException):

    def __init__(self):
        message = f"Usuário não encontrado"
        print(f">>> ERROR: {message}")
        super().__init__(status_code=404, detail=message)