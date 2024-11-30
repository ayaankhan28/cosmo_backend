from fastapi import FastAPI
from app.routes.students import router as students_router
from app.database import connect_to_mongo, disconnect_from_mongo

app = FastAPI(
    title="Backend Intern Hiring Task",
    version="1.0.0",
    description="API for managing student data."
)

@app.on_event("startup")
async def startup():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown():
    await disconnect_from_mongo()

app.include_router(students_router, prefix="/students", tags=["Students"])


#674b1f897b7d1ed08ac866d0 anuj
#674b1e827b7d1ed08ac866cf ayaan