from . models import Customer
from django.http import HttpResponse
import requests
from . face_data import integration

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
        face = integration()
        if request.user.is_authenticated:
            print("view_kwargs {}" .format(view_kwargs))
            if request.method == 'GET':

                e = view_kwargs.get('object_id') #change existing user /admin/customers/customer/5/change/
                if e:
                    print("user {}" .format(e))
                    customer_name = Customer.objects.get(id_customer=e)
                    print("new name {}".format(customer_name))
                    payload={'id_customer':e,'customer_name':customer_name,'method':'update'}
                    face.call_to_biostar2(**payload)

            elif request.method == 'POST':
                if request.path:
                    if 'customers/customer/add' in request.path: #add new user
                        payload={'id_customer':0,'customer_name':request.POST.get('name'),'method':'add'}
                        face.call_to_biostar2(**payload)

                print(request.content_params)
                print(request.POST.get('PATH_INFO'))
                print(request.__dict__)
                print(request)
                print(request.POST.get('name'))

                # also to catch:
                # http://127.0.0.1:8000/admin/customers/customer/ list
                # <QueryDict: {'csrfmiddlewaretoken': ['2HDTnIV3dJYmL9dG5BjDBhvl8mmDmPn5AGg4xxGie8yc7Skx1KGtqxlaYWjiNJ7Q'], 'action': ['delete_selected'], 'select_across': ['0'], 'index': ['0'], '_selected_action': ['11', '10', '9', '8', '7']}>

        else:
            pass
        return None

    def process_response(self, request, response):
        print("dddddd")
        if request.Customer is not None:
            print(request.Customer)
            request.Customer.save()
        return response
