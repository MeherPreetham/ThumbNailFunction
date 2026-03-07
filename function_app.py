import azure.functions as func
import cv2
import numpy as np

app = func.FunctionApp()

@app.function_name(name="create_thumbnail")
@app.route(route="create_thumbnail", auth_level=func.AuthLevel.ANONYMOUS)
def create_thumbnail(req: func.HttpRequest) -> func.HttpResponse:
    """ Azure Function that resizes an image to a thumbnail """
    try:
        # Get the image data from the request
        image_data = req.get_body()
        if not image_data:
            return func.HttpResponse("No image provided", status_code=400)

        # Convert byte data to numpy array
        image_array = np.frombuffer(image_data, np.uint8)
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

        if image is None:
            return func.HttpResponse("Invalid image", status_code=400)

        # Resize the image to a thumbnail (100x100)
        thumbnail = cv2.resize(image, (100, 100), interpolation=cv2.INTER_AREA)

        # Encode the resized image back to JPEG format
        _, encoded_image = cv2.imencode('.jpg', thumbnail)

        return func.HttpResponse(encoded_image.tobytes(), mimetype="image/jpeg")

    except Exception as e:
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
