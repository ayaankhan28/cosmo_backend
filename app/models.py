from bson import ObjectId
from pydantic import BaseModel, Field
from typing import Optional, Dict

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        if not ObjectId.is_valid(value):
            raise ValueError("Invalid ObjectId")
        return ObjectId(value)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class StudentModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    name: str
    age: int
    address: Dict[str, str]

    class Config:
        json_encoders = {ObjectId: str}
