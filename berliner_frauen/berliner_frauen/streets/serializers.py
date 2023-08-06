from .models import District, Street
from rest_framework import serializers
from taggit.serializers import TagListSerializerField, TaggitSerializer


class DistrictSerializer(serializers.ModelSerializer):
    streets = serializers.SlugRelatedField(
        many=True,
        slug_field="street_slug",
        queryset=Street.objects.all()
    )

    class Meta:
        model = District
        fields = (
            "id",
            "name",
            "district_slug",
            "number_of_added_streets",
            "number_of_completed_streets",
            "streets",
            "image_path"
        )
        read_only_fields = fields


class StreetSerializer(TaggitSerializer, serializers.ModelSerializer):
    district = serializers.SerializerMethodField()
    district_slug = serializers.SerializerMethodField()
    geocode = serializers.SerializerMethodField()
    geocode = serializers.SerializerMethodField()
    tags = TagListSerializerField()

    class Meta:
        model = Street
        fields = (
            "id",
            "name",
            "district",
            "district_slug",
            "street_slug",
            "map_link",
            "geocode",
            "eponym_name",
            "eponym_date_of_birth",
            "eponym_date_of_death",
            "eponym_place_of_birth",
            "eponym_place_of_death",
            "eponym_description",
            "image",
            "tags",
        )
        read_only_fields = fields

    def get_district(self, obj):
        return obj.district.name

    def get_district_slug(self, obj):
        return obj.district.district_slug

    def get_geocode(self, obj):
        try:
            coords = obj.map_link.partition("@")[-1]
            coords = coords.split(",")
            return [float(coord) for coord in coords]
        except ValueError:
            print("Error: please check that all coordinates are float[] type")
            return None


