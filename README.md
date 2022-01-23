# aura-server

## Pre-requisite

- Python 3
- Pip
- Poetry (https://python-poetry.org/docs/)

## Setup

Always run commands within the poetry shell. Create a shell with  
`poetry shell`

Install dependencies with  
`poetry install`

To run the api server:  
`poetry run uvicorn main:app --reload`

### Poetry Shell Commands

Create a new shell `poetry shell`

Add a new dependency with `poetry add abcd`

Exit shell `exit`

Deactivate shell (keep in background): `poetry deactivate`

## Swagger docs

Access swagger docs by visiting `https://127.0.0.1:8000/docs`

## Checking responses with Postman

Install the Postman app to test the HTTP responses during development: https://www.postman.com/

Create a new request in postman, and ping to root endpoint to check server health
