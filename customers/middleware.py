from . models import Customer
from django.http import HttpResponse
import requests

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
            print("view_args {}" .format(view_args))
            print("view_kwargs {}" .format(view_kwargs))
            if request.method == 'GET':
                ######
                # change existing user true
                # /admin/customers/customer/5/change/
                e = view_kwargs.get('object_id')
                if e:
                    print("user {}" .format(e))
                    customer_name = Customer.objects.get(id_customer=e)
                    print(customer_name)
                    print(self.call_to_biostar2(e))
                print("request.content_params {}" .format(request.content_params))
                print(request.GET)
                print(request)
            elif request.method == 'POST':
                # /admin/customers/customer/add/
                print(request.content_params)
                print(request.POST)
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

    def call_to_biostar2(self,id_user):
        url="http://127.0.0.1:8000/?id_user={}".format(id_user)
        newuser = requests.get(url)
        return """[{ "access_groups": [ { "id": 0, "included_by_user_group": "string", "name": "string" } ], "card_count": 0, "email": "string", "expiry_datetime": "string", "face_template_count": 0, "fingerprint_template_count": 0, "last_modify": 0, "login_id": "string", "name": "string", "password_exist": true, "permission": { "id": 0, "name": "string", "permissions": [ { "allowed_group_id_list": [ "long" ], "module": "string", "read": true, "write": true } ] }, "phone_number": "string", "photo": "string", "pin_exist": true, "security_level": "string", "start_datetime": "string", "status": "string", "user_group": { "id": 0, "name": "string" }, "user_id": "string" }]"""
