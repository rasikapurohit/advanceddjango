from rest_framework.views import APIView
from rest_framework.response import Response
# from django.contrib.auth.models import User
from .models import Form, Question, Choice, User
from .seralizer import FormSeralizer
class FormAPI(APIView):
    def get(self, request):
        # This is a placeholder for the GET method
        return Response({"message": "GET method called"})

    def post(self, request):
        # This is a placeholder for the POST method
        try:
            data = request.data
            user = User.objects.first()
            form = Form.create_blank_form(user)
            serializer =  FormSeralizer(form)
            return Response({
                'status': True,
                'message': 'Form created successfully',
                'form': serializer.data
            })
        except Exception as e:
            print(f"Error creating form: {e}")
            return Response({"error": str(e), 'message': 'Failed to create form'}, status=400 )  

        # return Response({"message": "POST method called"})
    
    def put(self, request):
        # This is a placeholder for the PUT method
        return Response({"message": "PUT method called"})
    
    def delete(self, request):
        # This is a placeholder for the DELETE method
        return Response({"message": "DELETE method called"})
    
    def patch(self, request):
        # This is a placeholder for the PATCH method
        return Response({"message": "PATCH method called"})