import django_filters
from django.forms import CharField, TextInput
from django_filters.rest_framework import FilterSet

from pokedex.models import Pokemon, Specie, Region, Generation, Habitat, Shape, GrowthRate


class SpecieFilter(FilterSet):

    class Meta:
        model = Specie
        fields = {
            'identifier': ['exact', 'icontains'],
            'generation': ['exact', 'in'],
            'evolves_from_specie': ['exact', 'isnull'],
            'color': ['exact', 'in'],
            'shape': ['exact'],
            'habitat': ['exact'],
            'gender_rate': ['exact'],
            'capture_rate': ['exact'],
            'base_happiness': ['exact'],
            'is_baby': ['exact'],
            'hatch_counter': ['exact'],
            'has_gender_differences': ['exact'],
            'growth_rate': ['exact'],
            'forms_switchable': ['exact'],
            'order': ['exact'],
            'conquest_order': ['exact']
        }

    @property
    def form(self):
        form = super().form
        form.fields['evolves_from_specie'].widget = TextInput()
        return form


class RegionFilter(FilterSet):

    class Meta:
        model = Region
        fields = {
            'id': ['exact', 'in'],
            'identifier': ['exact', 'icontains'],
        }


class GenerationFilter(FilterSet):

    class Meta:
        model = Generation
        fields = {
            'id': ['exact', 'in'],
            'main_region': ['exact', 'in'],
            'identifier': ['exact', 'icontains'],
        }


class HabitatFilter(FilterSet):

    class Meta:
        model = Habitat
        fields = {
            'id': ['exact', 'in'],
            'identifier': ['exact', 'icontains'],
        }


class ShapeFilter(FilterSet):

    class Meta:
        model = Shape
        fields = {
            'id': ['exact', 'in'],
            'identifier': ['exact', 'icontains'],
        }


class GrowthRateFilter(FilterSet):

    class Meta:
        model = GrowthRate
        fields = {
            'id': ['exact', 'in'],
            'identifier': ['exact', 'icontains'],
            'formula': ['exact', 'icontains'],
        }


class PokemonFilter(FilterSet):

    class Meta:
        model = Pokemon
        fields = {
            'id': ['exact', 'in'],
            'identifier': ['exact', 'icontains'],
            'specie__identifier': ['exact', 'icontains'],
            'specie__generation': ['exact'],
            'specie': ['exact'],
            'height': ['exact'],
            'weight': ['exact'],
            'base_experience': ['exact'],
            'is_default': ['exact'],
        }

    @property
    def form(self):
        form = super().form
        form.fields['specie'].widget = TextInput()
        return form
