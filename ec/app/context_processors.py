from .models import Cart


def cart_count(request):
    if not request.user.is_authenticated:
        return {'cart_count': 0}
    return {
        'cart_count': Cart.objects.filter(user=request.user).count(),
    }
