from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def bfhl(request):
    if request.method == 'GET':
        response_data = {
            "operation_code": 1
        }
        return Response(response_data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        user_id = "john_doe_17091999"  # Replace with your dynamic user_id logic if needed
        email = "john@xyz.com"  # Replace with your dynamic email logic if needed
        roll_number = "ABCD123"  # Replace with your dynamic roll_number logic if needed

        data = request.data.get('data')
        
        if not data or not isinstance(data, list):
            return Response({"is_success": False, "message": "Invalid input data. Must be a list of strings."},
                            status=status.HTTP_400_BAD_REQUEST)

        numbers = [item for item in data if isinstance(item, str) and item.isdigit()]
        alphabets = [item for item in data if isinstance(item, str) and item.isalpha()]
        lowercase_alphabets = [item for item in alphabets if item.islower()]
        highest_lowercase_alphabet = [max(lowercase_alphabets)] if lowercase_alphabets else []

        response_data = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase_alphabet
        }

        return Response(response_data, status=status.HTTP_200_OK)