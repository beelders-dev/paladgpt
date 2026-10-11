# PaladGPT Backend

The PaladGPT backend is a FastAPI application responsible for handling API requests, coordinating the scanning and prediction workflow, and communicating with the independently deployed Career Predictor service.

## Responsibilities

- Expose and validate API endpoints.
- Coordinate the scanning and prediction workflow.
- Process input through the scanner module.
- Communicate with the Career Predictor over HTTP.
- Handle errors and return predictable API responses.
- Test individual components and their integration.

## Architecture

```text
Frontend
   |
   | HTTP
   v
FastAPI API
   |
   v
Orchestrator
   ├── Scanner
   └── Predictor Client
            |
            | HTTP + JSON
            v
      Career Predictor
```

The scanner is an internal Python module, not a separate service. Keep its implementation isolated from the orchestration logic so it can be replaced without unnecessarily changing the rest of the backend.

## Project Structure

```text
backend/
├── src/
│   └── paladgpt/
│       ├── main.py
│       ├── api.py
│       ├── orchestrator.py
│       ├── scanner.py
│       ├── predictor_client.py
│       └── config.py
├── tests/
├── pyproject.toml
├── .env.example
├── .gitignore
├── Dockerfile
└── README.md
```

Follow the existing structure and add modules only when they provide a clear benefit.

## Development Setup

Use Python 3.12 for local development unless the project configuration specifies otherwise.

From this directory, create and activate a virtual environment in PowerShell:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

Install the project and its dependencies according to `pyproject.toml`. If editable installation is configured:

```powershell
pip install -e .
```

Keep the virtual environment local; do not commit `.venv/` to Git.

## Configuration

Use environment variables for environment-specific settings.

Example `.env.example`:

```dotenv
PREDICTOR_BASE_URL=http://localhost:8001
PREDICTOR_TIMEOUT_SECONDS=5
```

These values are illustrative. Update them to match the actual service configuration.

Never commit real secrets or private environment files.

## Running the Backend

Once the package and dependencies are configured, start the development server from this directory:

```powershell
uvicorn paladgpt.main:app --reload
```

The application should expose its interactive API documentation at `/docs` and its generated OpenAPI specification at `/openapi.json`, using the default FastAPI configuration.

## Testing

Run the backend tests using the project's configured test runner. If `pytest` is configured:

```powershell
pytest
```

Tests should cover:

- API request validation and response formats.
- Scanner behavior and failure cases.
- Orchestration logic.
- Predictor client responses, timeouts, and errors.
- Integration between components.

Use mocks when testing components independently
