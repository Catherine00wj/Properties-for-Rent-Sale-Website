from django.shortcuts import render

# Create your views here.
from InforRealease import models

from django.http import HttpResponse

#-------search matching result with the input information---------------------
#-------method :post-----------------
def search_buy(request):
    if request.method == "POST":
        city = request.POST.get("city", None).lower()
        bedrooms = request.POST.get("bedrooms", None).lower()
        bathrooms = request.POST.get("bathrooms", None).lower()
        parking = request.POST.get("parking", None).lower()
        # expectmoney = request.POST.get("expectmoney", None)
        community = request.POST.get("community", None).lower()
        search = request.POST.get("search", None).lower()
        #---if the search key word has some words , then search this word matching of the description,and return all the results---
        if search != None:
            test_buy = models.ResourceInfor.objects.filter(city=city, bedrooms=bedrooms, bathrooms=bathrooms,
                                                         parking=parking, community=community, type= "sell").filter(description__contains=search)
            if len(test_buy) != 0:
                for resource in test_buy:
                    # if len(resource.img)>0:
                    resource.img = resource.img.strip(';').split(';')[0]
            else:
                #------if there is no matching information, will return all the information of selling house-----
                test_buy = models.ResourceInfor.objects.all().filter(type= "sell")
                for resource in test_buy:
                    # if len(resource.img)>0:
                    resource.img = resource.img.strip(';').split(';')[0]
            return render(request, "search_buy.html", {"Searbuy": test_buy})
        if search == None:
            test_buy = models.ResourceInfor.objects.filter(city=city, bedrooms=bedrooms, bathrooms=bathrooms, parking=parking,community = community ,type="sell")
            if len(test_buy) != 0:
                for resource in test_buy:
                    # if len(resource.img)>0:
                    resource.img = resource.img.strip(';').split(';')[0]
            else :
                test_buy = models.ResourceInfor.objects.all().filter(type= "sell")
                for resource in test_buy:
                    # if len(resource.img)>0:
                    resource.img = resource.img.strip(';').split(';')[0]
            return render(request, "search_buy.html", {"Searbuy": test_buy})
    test_buy = models.ResourceInfor.objects.filter(type ="sell")
    for resource in test_buy:
        # if len(resource.img)>0:
        resource.img = resource.img.strip(';').split(';')[0]
    return  render(request, "search_buy.html", {"Searbuy": test_buy})