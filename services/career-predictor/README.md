# Career Predictor

## Overview

The Career Predictor is an independent service responsible for generating humorous, fictional career predictions based on palm scan features received from the backend.

This service is part of PaladGPT, an entertainment project. Predictions are fictional and are not scientifically validated.

## Responsibilities

- Receive palm scan features from the backend.
- Generate a fictional job title, a `kapalaran_score` from 0 to 100, and a humorous explanation.
- Return predictions in the agreed response format.
- Validate incoming requests and handle errors appropriately.

## Architecture

The Career Predictor runs independently from the FastAPI backend.

The backend sends the extracted palm features to this service over HTTP. The predictor processes the input and returns a prediction to the backend, which then responds to the frontend.

## API Contract

The request format, response schema, endpoint, and error responses must be agreed upon with the backend developer before implementation.

Refer to the shared API contract in `contracts/openapi.yaml` at the repository root for the frontend-facing API.

## Development Setup

Add the language-specific installation and run instructions once the implementation language and framework have been chosen.

## Testing

Add tests for request validation, prediction generation, response formatting, and error handling.

## Definition of Done

- [ ] Agreed upon the API contract with the backend developer.
- [ ] Implemented the prediction endpoint.
- [ ] Added input validation and error handling.
- [ ] Added tests.
- [ ] Documented setup and execution instructions.
