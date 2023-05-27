"""
2020 Black
developer : #ABS
"""
from django.shortcuts import render


# 404 Error view (Page not found)
def page_not_found_error(request, exception):
    return render(request, 'utils/404.html', status=404)
    
    
# 500 Error view (Server Error)
def server_error(request):
    return render(request, 'utils/500.html', status=404)

