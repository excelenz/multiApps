import requests

class integration:
    def call_to_biostar2(self,**kwargs):
        for key in ('id_customer','customer_name','method'):
            try:
                setattr(self, key, kwargs[key])
            except:
                setattr(self, key, "")
        try:
            url="http://127.0.0.1:8000/?id_user={}".format(self.id_customer)
            response = requests.get(url)
            if response.status_code not in [200,201]:
                response.raise_for_status()
        except:
            print("here we will handle problems")
        a=  """[{ "access_groups": [ { "id": 0, "included_by_user_group": "string", "name": "string" } ], "card_count": 0, "email": "string", "expiry_datetime": "string", "face_template_count": 0, "fingerprint_template_count": 0, "last_modify": 0, "login_id": "string", "name": "string", "password_exist": true, "permission": { "id": 0, "name": "string", "permissions": [ { "allowed_group_id_list": [ "long" ], "module": "string", "read": true, "write": true } ] }, "phone_number": "string", "photo": "string", "pin_exist": true, "security_level": "string", "start_datetime": "string", "status": "string", "user_group": { "id": 0, "name": "string" }, "user_id": "string" }]"""
        return 1
