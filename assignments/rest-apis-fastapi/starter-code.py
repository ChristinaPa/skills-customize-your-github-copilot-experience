"""
REST APIs with FastAPI - Starter Code
Complete the TODOs to build your API!
"""

from fastapi import FastAPI

# TODO: Import additional modules you'll need (HTTPException, Query, etc.)

# TODO: Create your Pydantic Item model here


# Create the FastAPI application instance
app = FastAPI(
    title="Items API",
    description="A simple API for managing items",
    version="1.0.0"
)

# In-memory storage for items (replace with a database in real applications)
items_db = {}


# TODO: Create your root endpoint here
# @app.get("/")


# TODO: Create your CRUD endpoints here
# GET /items - Get all items
# GET /items/{item_id} - Get a single item
# POST /items - Create a new item
# PUT /items/{item_id} - Update an item
# DELETE /items/{item_id} - Delete an item


# TODO: Add query parameter filtering to GET /items


# Run the server (for development)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
