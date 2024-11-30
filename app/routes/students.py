from fastapi import APIRouter, HTTPException, Query
from app.schemas import CreateStudentSchema, UpdateStudentSchema
from app.models import StudentModel
from app.database import db
from bson.objectid import ObjectId

router = APIRouter()

@router.post("/", response_model=dict, status_code=201)
async def create_student(student: CreateStudentSchema):
    result = await db.database["students"].insert_one(student.dict())
    return {"id": str(result.inserted_id)}


@router.get("/", response_model=dict)
async def list_students(country: str = Query(None), age: int = Query(None)):
    query = {}
    if country:
        query["address.country"] = country
    if age:
        query["age"] = {"$gte": age}

    print("no problem here")

    students = await db.database["students"].find(query).to_list(100)

    # Convert _id to string for JSON serialization
    for student in students:
        student["_id"] = str(student["_id"])

    return {"data": students}
@router.get("/{id}", response_model=StudentModel)
async def fetch_student(id: str):
    student = await db.database["students"].find_one({"_id": ObjectId(id)})
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.patch("/{id}", status_code=204)
async def update_student(id: str, student: UpdateStudentSchema):
    updated_data = {k: v for k, v in student.dict(exclude_unset=True).items()}
    if not updated_data:
        raise HTTPException(status_code=400, detail="No fields to update")

    result = await db.database["students"].update_one({"_id": ObjectId(id)}, {"$set": updated_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")

@router.delete("/{id}", response_model=dict)
async def delete_student(id: str):
    result = await db.database["students"].delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}
