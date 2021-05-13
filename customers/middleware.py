from . models import Customer

#http://127.0.0.1:8000/admin/customers/customer/add/ adding new one and getting id data from server
#http://127.0.0.1:8000/admin/customers/customer/ list
#http://127.0.0.1:8000/admin/customers/customer/2/change/ getting one
class faces:
    def __init__(self, get_response):
        self.get_response = get_response
        print("adafsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfdsfsd")
        self.user = Customer()


    def __call__(self, request):
        response = self.get_response(request)
        return response


