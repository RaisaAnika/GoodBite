from django.http import JsonResponse
from vertexai import init
from vertexai.language_models import TextGenerationModel
from django.http import JsonResponse

class VertexAIMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Initialize Vertex AI SDK
        init(project="your-project", location="your-location")

        if request.method == "POST" and request.path == "/your-endpoint":
            # Process the request and call Vertex AI
            response = self.process_request(request)
            return JsonResponse({"response": response.text})

        return self.get_response(request)

    def process_request(self, request):
        # Extract relevant data from the request
        food_item = request.POST.get("food_item")
        diet_type = request.POST.get("diet_type")

        # Initialize the TextGenerationModel
        parameters = {
            "candidate_count": 1,
            "max_output_tokens": 1024,
            "temperature": 0.2,
            "top_p": 0.8,
            "top_k": 40
        }
        model = TextGenerationModel.from_pretrained("text-bison")

        # Prepare the input text for TextGenerationModel
        input_text = f"input: Dish: {food_item}\nCalorie goal: 900\nDiet: {diet_type}\noutput:"

        # Call TextGenerationModel
        response = model.predict(input_text, **parameters)

        return response

