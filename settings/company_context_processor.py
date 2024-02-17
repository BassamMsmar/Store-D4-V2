from .models import Company

def get_company_data(requset):
    data = Company.objects.all().last
    return {'company_data': data}