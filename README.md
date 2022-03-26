# aura-server

## Run in Production
1. Install docker or docker desktop
2. Run `docker compose up -d`
3. Profit

## Pre-requisite

- Python 3 (via Pyenv - https://github.com/pyenv/pyenv)
- Pip
- Poetry (https://python-poetry.org/docs/master/#installing-with-the-official-installer)

## Setup

Install pyenv
// todo

Install the latest version of python with pyenv
`pyenv install 3.10.3`
`pyenv local 3.10.3`


Always run commands within the poetry shell. Create a shell with  
`poetry shell`

Install dependencies with  
`poetry install`

To run the api server:  
`poetry run dev`

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

## Running Test Suites

Run `poetry run pytest`
