from app.validators.business.user.user_validator import UserValidator
from app.validators.business.user.unique_user_email_validator import UniqueUserEmailValidator
from app.validators.business.user.unique_user_name_validator import UniqueUserNameValidator

def get_instance() -> list[UserValidator]:
    return [UniqueUserEmailValidator(), UniqueUserNameValidator()]
