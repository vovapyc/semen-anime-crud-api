# Semen-anime-crud-api

## Installation

1. Clone the repository: `git clone <repository-url>`
2. Navigate into the project directory: `cd <project-directory>`
3. Install the dependencies: `pip install -r requirements.txt`

## Tokens

This application uses tokens for authentication. The valid tokens are "token1", "token2", and "token3". These tokens are used in the `authenticate` function in `main.py` to validate incoming requests. Tokens can always be changed in `main.py`

## How to Run

1. Start the server using `python main.py`
2. The application will be available at `http://127.0.0.1:8000`

## Database

This application uses SQLite database. After first run there will be file `app/anime.db`

## Swagger

FastAPI automatically generates a Swagger UI for your API. Once you've started the server, you can access the Swagger UI at `http://127.0.0.1:8000/docs`.