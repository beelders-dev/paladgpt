# PaladGPT Frontend

## Overview

The PaladGPT frontend provides the user interface for a humorous palm-scanning application that generates fictional career predictions.

Users can submit a palm image and view their generated career title, kapalaran score, and explanation.

## Responsibilities

The frontend is responsible for:

- Providing an interface for capturing or uploading a palm image.
- Validating user input before submission where practical.
- Sending scan requests to the PaladGPT backend.
- Displaying the generated career prediction and related results.
- Handling loading, success, and error states.
- Providing clear feedback when an image cannot be processed or a request fails.

The frontend must not implement palm image processing or career prediction logic. These responsibilities belong to the backend and Career Predictor service.

## Architecture

The frontend communicates exclusively with the PaladGPT backend through its HTTP API.

```text
User
  |
  v
Frontend
  |
  | HTTP requests
  v
PaladGPT Backend
  |
  v
Career Predictor
```

The frontend must not call the Career Predictor service directly.

## Project Setup

Development setup instructions, required tools, dependency installation, and run commands should be documented once the frontend technology and tooling have been finalized.

Keep frontend-specific dependencies and configuration within this directory.

## API Integration

The frontend must follow the shared API contract defined in:

`../contracts/openapi.yaml`

Before implementing API-dependent features, coordinate with the backend developer to confirm the request formats, response schemas, and error handling behavior.

Backend communication should be isolated from presentation components where practical, making API calls easier to maintain, test, and replace.

The backend URL must be configurable through environment-specific settings rather than hardcoded throughout the application.

## User Experience

The interface should provide:

- A clear entry point for submitting a palm image.
- Feedback while a scan is being processed.
- A readable presentation of the generated prediction.
- Helpful messages for invalid input, failed requests, and unavailable services.
- A way to retry a failed request where appropriate.

Avoid presenting fictional predictions as scientifically validated palmistry, career assessments, or professional advice.

## Development Guidelines

- Keep UI components focused on presentation and user interaction.
- Separate API communication from UI rendering where practical.
- Follow the agreed API contract.
- Use mock responses when developing features before the backend is available.
- Avoid hardcoding backend URLs, prediction results, or environment-specific values.
- Do not expose credentials, secrets, or private configuration in client-side code.
- Keep changes focused and submit them through feature branches and pull requests.

## Testing

Test relevant behavior, including:

- User input validation.
- Successful API requests and result rendering.
- Loading and error states.
- Invalid or unsupported image submissions.
- Handling of unexpected or malformed API responses.

Use mocked API responses for isolated frontend tests. Verify integration against the actual backend before considering a feature complete.

## Definition of Done

A frontend feature is considered complete when:

- Its intended behavior is implemented.
- It follows the agreed API contract.
- Relevant success and failure states are handled.
- Applicable tests pass.
- Setup or usage documentation is updated when necessary.
- Changes have been reviewed and integrated into the shared project.

## Scope

PaladGPT is an entertainment-focused hackathon project. Its generated career titles and scores are fictional and intended for humor.
