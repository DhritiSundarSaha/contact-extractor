from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Contact(BaseModel):
    name: Optional[str] = Field(None, description="Person's full name")
    age: Optional[int] = Field(None, description="Person's age")
    email: Optional[EmailStr] = Field(None, description="Valid email address")
    phone: Optional[str] = Field(None, description="Phone number in E.164 format")
