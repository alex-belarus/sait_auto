from main.models import Brand, Manufacturer


def context_data(request):
    brands = Brand.objects.all()
    manufacturs = Manufacturer.objects.all()
    context = {
        'brand': brands,
        'manufacturer': manufacturs,
    }
    return context