from rest_framework import serializers, viewsets

import django_filters
from munigeo import api as munigeo_api
from resources.api.base import NullableDateTimeField, TranslatedModelSerializer, register_view
from resources.models import Unit


class UnitFilterSet(django_filters.FilterSet):
    resource_group = django_filters.Filter(name='resources__groups__identifier', lookup_expr='in',
                                           widget=django_filters.widgets.CSVWidget, distinct=True)

    class Meta:
        model = Unit
        fields = ('resource_group',)


class UnitSerializer(TranslatedModelSerializer, munigeo_api.GeoModelSerializer):
    opening_hours_today = serializers.DictField(
        source='get_opening_hours',
        child=serializers.ListField(
            child=serializers.DictField(
                child=NullableDateTimeField())
        )
    )
    reservable_days_in_advance = serializers.ReadOnlyField()
    reservable_before = serializers.SerializerMethodField()

    def get_reservable_before(self, obj):
        request = self.context.get('request')
        user = request.user if request else None

        if user and obj.is_admin(user):
            return None
        else:
            return obj.get_reservable_before()

    class Meta:
        model = Unit
        fields = '__all__'


class UnitViewSet(munigeo_api.GeoModelAPIView, viewsets.ReadOnlyModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = UnitFilterSet


register_view(UnitViewSet, 'unit')
