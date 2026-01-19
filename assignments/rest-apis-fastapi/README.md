# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build REST APIs using the FastAPI framework in Python. You will create endpoints to handle HTTP requests, work with path and query parameters, and return JSON responses.

## 📝 Tasks

### 🛠️ Set Up a FastAPI Project

#### Description
Install FastAPI and create a basic application with a root endpoint.

#### Requirements
Completed program should:

- Install FastAPI and uvicorn packages
- Create a FastAPI application instance
- Define a root endpoint (`/`) that returns a welcome message
- Run the server successfully on `http://localhost:8000`

Example response for the root endpoint:
```json
{"message": "Welcome to the API"}
```


### 🛠️ Create CRUD Endpoints for Items

#### Description
Build a complete set of endpoints to Create, Read, Update, and Delete items.

#### Requirements
Completed program should:

- Define an `Item` model using Pydantic with fields: `id`, `name`, `description`, and `price`
- Create a `GET /items` endpoint that returns all items
- Create a `GET /items/{item_id}` endpoint that returns a single item by ID
- Create a `POST /items` endpoint that adds a new item
- Create a `PUT /items/{item_id}` endpoint that updates an existing item
- Create a `DELETE /items/{item_id}` endpoint that removes an item
- Return appropriate HTTP status codes (200, 201, 404) for each operation


### 🛠️ Add Query Parameters and Validation

#### Description
Enhance your API with query parameters for filtering and input validation.

#### Requirements
Completed program should:

- Add optional query parameters to `GET /items` for filtering by name or price range
- Use Pydantic validation to ensure `price` is a positive number
- Return a `422 Unprocessable Entity` error for invalid input
- Add docstrings to endpoints so they appear in the auto-generated docs at `/docs`

Example filtered request:
```
GET /items?min_price=10&max_price=50
```
