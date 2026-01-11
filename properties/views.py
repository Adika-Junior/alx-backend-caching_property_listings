from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .utils import get_all_properties


@cache_page(60 * 15)  # Cache for 15 minutes
def property_list(request):
    """
    View to list all properties.
    Uses view-level caching (@cache_page) and low-level caching (get_all_properties).
    """
    properties = get_all_properties()
    
    # Serialize properties to JSON
    properties_data = [
        {
            'id': prop.id,
            'title': prop.title,
            'description': prop.description,
            'price': str(prop.price),
            'location': prop.location,
            'created_at': prop.created_at.isoformat(),
        }
        for prop in properties
    ]
    
    return JsonResponse({'properties': properties_data}, safe=False)
