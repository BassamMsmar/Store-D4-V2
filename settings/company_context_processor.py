from .models import Company

<<<<<<< HEAD



def get_company_data(request):
    data = Company.objects.last()
    return {'company_data':data}
=======
def get_company_data(requset):
    data = Company.objects.all().last
    return {'company_data': data}
>>>>>>> 32443c625f8fabfd4890b4bcf1e943ebadb0dfbd
