from pydantic import BaseModel, validator
from datetime import datetime
from email_validator import validate_email, EmailNotValidError

class Account_API_Model(BaseModel):

    name : str
    email : str
    password : str

    what_am_i: str
    age: int
    gender: str
    i_currently_live_in: str
    i_can_give_advices_for: str
    travel_experiences_preferences: str
    
    @validator("name")
    def name_validation(cls, value):
        if not value:
            raise ValueError("Class must not be empty")
        return value
    
    @validator("email")
    def email_validation(cls, value):
        if not value:
            raise ValueError("Email must not be empty")
        email = "my+address@mydomain.tld"
        value=email
        is_new_account = True
        try:
            # Check that the email address is valid.
            validation = validate_email(value, check_deliverability=is_new_account)
            email = validation.value
        except EmailNotValidError:
            raise ValueError("Email doesn't exist")
        return value

    @validator("password")
    def password_validation(cls, value):
        if not value:
            raise ValueError("Password must not be empty")