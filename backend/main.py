from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from bson import ObjectId
from database import todos_collection

app = FastAPI()

# Allow CORS (Cross-Origin Resource Sharing) for our React app
origins = [
    "http://localhost:80",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/todos")
def get_todos():
    todos = []
    for todo in todos_collection.find():
        todo["_id"] = str(todo["_id"])
        todos.append(todo)
    return todos

@app.post("/api/todos")
def add_todo(todo: str):
    if not todo:
        raise HTTPException(status_code=400, detail="Todo cannot be empty")
    todo_id = todos_collection.insert_one({"todo": todo})
    return {"message": "Todo added successfully", "todo": {"_id": str(todo_id.inserted_id), "todo": todo}}

@app.delete("/api/todos/{id}")
def delete_todo(id: str):
    todo = todos_collection.find_one({"_id": ObjectId(id)})
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todos_collection.delete_one({"_id": ObjectId(id)})
    return {"message": "Todo deleted successfully"}


def main():
    import uvicorn
    uvicorn.run(app)



if __name__ == "__main__":
    main()
