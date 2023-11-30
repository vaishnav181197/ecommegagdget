from account.models import Cart

def count_cart(request):
    if request.user.is_authenticated:
        cnt=Cart.objects.filter(user=request.user,status='cart').count()
        return {'count':cnt}
    else:
        return {'count':0}