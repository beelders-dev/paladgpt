# PaladGPT — Developer Guide

PaladGPT is a hackathon project that generates humorous, fictional career predictions from palm scans.

The repository contains a React frontend, FastAPI backend, and independently developed Career Predictor service.

## Architecture

```text
React Frontend
      |
      | HTTP
      v
FastAPI Backend
  ├── API
  ├── Orchestrator
  ├── Scanner
  └── Predictor Client
          |
          | HTTP + JSON
          v
    Career Predictor
```

| Component        | Responsibility                           |
| ---------------- | ---------------------------------------- |
| Frontend         | User interface and API communication     |
| Backend API      | Request validation and HTTP responses    |
| Orchestrator     | Coordinates application workflows        |
| Scanner          | Processes input and extracts data        |
| Predictor Client | Communicates with the prediction service |
| Career Predictor | Generates predictions                    |

The scanner is an internal backend module, not a separate service. The Career Predictor runs independently to support separate development and deployment.

## Repository Structure

```text
paladgpt/
├── contracts/
│   └── openapi.yaml
├── frontend/
├── services/
│   ├── backend/
│   │   ├── src/paladgpt/
│   │   ├── tests/
│   │   ├── pyproject.toml
│   │   └── README.md
│   └── career-predictor/
│       ├── src/
│       ├── tests/
│       └── README.md
└── README.md
```

This is the initial structure, not a rigid requirement. Follow the conventions of the chosen framework and add complexity only when needed.

## Engineering Principles

### Required

- **Separation of concerns:** Give each component a clear responsibility.
- **Contract-first development:** Agree on API interfaces before integrating independently developed components.
- **Testability:** Test individual components and verify integration between them.
- **Explicit error handling:** Handle expected failures and return predictable, documented errors.
- **Change coordination:** Communicate changes that affect other components before merging.
- **Maintainability:** Write code that teammates can understand, test, and modify.

### Helpful Practices

- **Dependency inversion:** Depend on stable interfaces rather than concrete implementations when replaceability is useful.
- **Configuration outside code:** Use environment variables for environment-specific settings and keep secrets out of Git.
- **Automation:** Use CI to run relevant tests and checks.
- **Simplicity:** Avoid unnecessary abstractions, services, and infrastructure.

## API Contracts

API contracts define how components communicate, including endpoints, request and response schemas, data types, and errors.

- Keep `contracts/openapi.yaml` accurate for the API it describes.
- Agree on the Career Predictor's interface before integrating it.
- Update affected implementations and tests when contracts change.
- Coordinate breaking changes with dependent developers.

OpenAPI documents an API; it does not implement it. FastAPI can generate an OpenAPI specification from its routes and models.

## Parallel Development

Developers may work independently using agreed contracts and mock responses.

- **Frontend:** Build the interface, handle loading and errors, and test against mock responses.
- **Backend:** Implement endpoints, coordinate workflows, and test dependencies independently.
- **Career Predictor:** Implement the agreed interface and test valid and invalid requests.

Mocks should follow the same contracts as the real services.

## Testing

Use the appropriate level of testing for each change:

- **Unit tests:** Verify individual functions and components.
- **Contract tests:** Verify request and response formats.
- **Integration tests:** Verify that dependent components work together.

Test expected failures as well as successful requests. A successful startup alone does not prove the application works correctly.

## Configuration and Security

- Keep environment-specific settings outside source code.
- Commit example configuration files, not real secrets or `.env` files.
- Validate required configuration and inputs.
- Return safe error messages without exposing stack traces, credentials, or internal details.

## Git Workflow

Create a feature branch before making changes. Do not work directly on `main`.

```bash
git switch main
git pull origin main
git switch -c feat/your-feature
```

Use descriptive branch names:

- `feat/` — new functionality
- `fix/` — bug fixes
- `docs/` — documentation
- `test/` — tests
- `refactor/` — restructuring without intended behavior changes

Commit and push your work:

```bash
git add .
git commit -m "feat: describe your change"
git push -u origin feat/your-feature
```

Open a pull request into `main`.

Before merging, check that relevant tests pass, documentation and contracts are updated when needed, and affected developers have reviewed incompatible changes.

## Deployment

The frontend, backend, and Career Predictor can be deployed independently. Changes to an internal backend module generally require redeploying the backend, but not other services unless their interfaces or dependencies are affected.

Docker Compose and additional infrastructure are optional until they solve an actual development or deployment need.

## Definition of Done

A change is complete when:

- Its behavior meets the agreed requirements.
- Relevant tests pass.
- Expected failures are handled.
- Necessary documentation and contracts are updated.
- The change has been reviewed and merged.
- Affected integrations are verified.

**When requirements or contracts are unclear, clarify them with the affected developers instead of relying on assumptions.**
