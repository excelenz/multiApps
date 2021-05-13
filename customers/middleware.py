from . models import Customer

class faces:
    def __init__(self, get_response):
        self.get_response = get_response
        print("adafsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfdsfsd")
        self.user = Customer()


    def __call__(self, request):
        response = self.get_response(request)
        return response


