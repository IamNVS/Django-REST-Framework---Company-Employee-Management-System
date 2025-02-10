from django.http import HttpResponse, JsonResponse

def home_page(request):
    print("THis is home page request")
    frinds= [
        "niraj",
        "prasad",
        "maya",
        "vasant"
        ]
    # return HttpResponse("<h1>This is return in home_mage method</h1>")
    return JsonResponse(frinds, safe=False)
