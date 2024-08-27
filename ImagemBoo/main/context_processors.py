from .models import Category

def side_menu(request):
    side_menu_categories = Category.objects.all()
    return {'side_menu_categories': side_menu_categories}
