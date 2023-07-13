from . models import SportsCategory, Sport

def sport_ctg(request):
    sportscatagory= SportsCategory.objects.all().order_by('order_number')
    return({
        'sport_ctg':sportscatagory,'recentcat':sportscatagory
    })


    