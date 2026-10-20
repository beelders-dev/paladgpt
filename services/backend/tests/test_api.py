import io

from PIL import Image
from fastapi.testclient import TestClient
from paladgpt.main import app

client = TestClient(app)


def create_test_image():
    buffer = io.BytesIO()
    image = Image.new("RGB", (10, 10), color="red")

    image.save(buffer, "png")

    return buffer.getvalue()


def test_valid_image_returns_success():
    image_bytes = create_test_image()

    response = client.post(
        "/api/v1/palm-scan-prediction",
        files={"image": ("test.png", image_bytes, "image/png")},
    )

    assert response.status_code == 200
    assert response.json() == {
        "status": "success",
        "message": "Image validated successfully",
    }


def test_invalid_image_returns_400():
    response = client.post(
        "/api/v1/palm-scan-prediction",
        files={"image": ("fake.jpg", b"this is not an image", "image/jpeg")},
    )

    assert response.status_code == 400


def test_oversized_image_returns_413():
    oversized_data = b"x" * (5 * 1024 * 1024 + 1)

    response = client.post(
        "/api/v1/palm-scan-prediction",
        files={"image": ("large.jpg", oversized_data, "image/jpeg")},
    )

    assert response.status_code == 413


def test_image_exceeding_dimensions_returns_413():
    buffer = io.BytesIO()
    image = Image.new("RGB", (4001, 10), color="red")
    image.save(buffer, format="PNG")

    response = client.post(
        "/api/v1/palm-scan-prediction",
        files={
            "image": (
                "wide.png",
                buffer.getvalue(),
                "image/png",
            )
        },
    )

    assert response.status_code == 413


def test_image_exceeding_height_returns_413():
    buffer = io.BytesIO()
    image = Image.new("RGB", (10, 4001), color="red")
    image.save(buffer, format="PNG")

    response = client.post(
        "/api/v1/palm-scan-prediction",
        files={
            "image": (
                "tall.png",
                buffer.getvalue(),
                "image/png",
            )
        },
    )

    assert response.status_code == 413
