from fastapi import HTTPException

class RequestDataValidationException(HTTPException):

    def __init__(self, message:str):
        print(f">>> ERROR: {message}")
        super().__init__(status_code=422, detail=message)