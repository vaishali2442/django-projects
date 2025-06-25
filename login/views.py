from django.shortcuts import render

# Create your views here.
def register_user(request):
    responseResult = {}
    try:
        pass
    except Exception as error:
        responseResult['status'] = 500
        responseResult['message'] = f'{str(error)}'
