from rest_framework import serializers

from pokedex.models import Pokemon, Specie, Generation, Habitat, Shape, GrowthRate, Region


class DemoSerializerMixin(object):
    def get_field_names(self, declared_fields, info):
        expanded_fields = super(DemoSerializerMixin, self).get_field_names(declared_fields, info)

        if getattr(self.Meta, 'extra_fields', None):
            fields = expanded_fields + self.Meta.extra_fields
        else:
            fields = expanded_fields
        if 'id' not in fields:
            fields += ['id']
        return fields


class SimpleSpecieSerializer(DemoSerializerMixin, serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Specie
        exclude = ('growth_rate', 'shape', 'habitat', 'generation', 'evolves_from_specie')


class RegionSerializer(DemoSerializerMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Region
        exclude = ()


class GenerationSerializer(DemoSerializerMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Generation
        exclude = ()


class HabitatSerializer(DemoSerializerMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Habitat
        exclude = ()


class ShapeSerializer(DemoSerializerMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shape
        exclude = ()


class GrowthRateSerializer(DemoSerializerMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GrowthRate
        exclude = ()


class SpecieSerializer(SimpleSpecieSerializer):
    growth_rate = GrowthRateSerializer()
    shape = ShapeSerializer()
    habitat = HabitatSerializer()
    generation = GenerationSerializer()
    evolves_from_specie = serializers.HyperlinkedRelatedField(
        queryset=Specie.objects.all(), view_name='specie-detail', style={'base_template': 'input.html'}
    )

    class Meta(SimpleSpecieSerializer.Meta):
        exclude = ()


class PokemonSerializer(DemoSerializerMixin, serializers.HyperlinkedModelSerializer):
    specie = SimpleSpecieSerializer()

    class Meta:
        model = Pokemon
        exclude = ()


class DetailPokemonSerializer(PokemonSerializer):
    specie = SpecieSerializer()

    class Meta(PokemonSerializer.Meta):
        pass
