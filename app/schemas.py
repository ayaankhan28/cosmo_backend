from pydantic import BaseModel
from typing import Optional, Dict

class CreateStudentSchema(BaseModel):
    name: str
    age: int
    address: Dict[str, str]

class UpdateStudentSchema(BaseModel):
    name: Optional[str]
    age: Optional[int]
    address: Optional[Dict[str, str]]

class StudentResponseSchema(CreateStudentSchema):
    id: str
