from . models import Customer
from django.http import HttpResponse
import requests

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
            print("view_kwargs {}" .format(view_kwargs))
            if request.method == 'GET':
                e = view_kwargs.get('object_id') #change existing user /admin/customers/customer/5/change/
                if e:
                    print("user {}" .format(e))
                    customer_name = Customer.objects.get(id_customer=e)
                    print(customer_name)
                    print(self.call_to_biostar2(e))
            elif request.method == 'POST':
                print(request.POST.get('url_name'))
                if 'customers_customer_add' in request.POST.get('url_name'):
                    print("YYYYESS")
                # /admin/customers/customer/add/
                #<QueryDict: {'csrfmiddlewaretoken': ['JGuf8KOFRr0GuifcnWawUAM6t7djm5s5hF7qizzUSQAwQ1m3j5xmJQCVjHaYNZcQ'], 'name': ['newnew'], '_save': ['Save']}>
                #<QueryDict: {'csrfmiddlewaretoken': ['2HDTnIV3dJYmL9dG5BjDBhvl8mmDmPn5AGg4xxGie8yc7Skx1KGtqxlaYWjiNJ7Q'], 'action': ['delete_selected'], 'select_across': ['0'], 'index': ['0'], '_selected_action': ['11', '10', '9', '8', '7']}>
                print(request.content_params)
                print(request.POST)
                #print(request.__dict__)
                print(request)
                print(request.POST.get('name'))
                #http://127.0.0.1:8000/admin/customers/customer/ list
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
