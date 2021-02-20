from django.conf.urls import include, url
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter


# Create a router and register our viewsets with it.
from pokedex import viewsets


router = DefaultRouter()
router.register(r'pokemon', viewsets.PokemonViewSet)
router.register(r'species', viewsets.SpecieViewSet)
router.register(r'growth_rates', viewsets.GrowthRateViewSet)
router.register(r'shapes', viewsets.ShapeViewSet)
router.register(r'habitats', viewsets.HabitatViewSet)
router.register(r'generations', viewsets.GenerationViewSet)
router.register(r'regions', viewsets.RegionViewSet)


schema_view = get_schema_view(
   openapi.Info(
      title="Pokédex API",
      default_version='v1',
      description="Demo project",
      terms_of_service="https://github.com/Nekmo/django-rest-framework-presentacion",
      contact=openapi.Contact(email="contacto@nekmo.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('docs/', include_docs_urls(title='Pokédex'))
]
