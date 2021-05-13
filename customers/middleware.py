from . models import Customer
from django.http import HttpResponse

#http://127.0.0.1:8000/admin/customers/customer/add/ adding new one and getting id data from server
#http://127.0.0.1:8000/admin/customers/customer/ list
#http://127.0.0.1:8000/admin/customers/customer/2/change/ getting one
class faces:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        response = self.get_response(request)
        return response


    def process_request(self, request):
        try:
            request.Customer = Customer.objects.get(id_customer=request.GET['id_customer'])
            print (request.Customer.id_customer)
            return HttpResponse(request.Customer)
        except Customer.DoesNotExists:
            return HttpResponseForbidden()

    def process_view(self,request,view_func,view_args,view_kwargs):
        if request.user.is_authenticated:

            e = view_kwargs.get('object_id')
            if e:
                customer_name = Customer.objects.get(id_customer=e)
                print(customer_name)
            print("user {}" .format(e))
            print("view_args {}" .format(view_args))
            print("view_kwargs {}" .format(view_kwargs))
            if request.method == 'GET':
                print("request.content_params {}" .format(request.content_params))
                print(request.GET)
                print(request)
            elif request.method == 'POST':
                #/admin/customers/customer/add/
                #/admin/customers/customer/5/change/
                print(request.content_params)
                print(request.GET)
                print(request)
        else:
            pass
        return None

    def process_response(self, request, response):
        print("dddddd")
        if request.Customer is not None:
            print(request.Customer)
            request.Customer.save()
        return response
