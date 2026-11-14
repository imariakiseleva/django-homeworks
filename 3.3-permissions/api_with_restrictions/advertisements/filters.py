from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    created_at = filters.DateFromToRangeFilter()

    status = filters.CharFilter(field_name="status")

    # TODO: задайте требуемые фильтры

    class Meta:
        model = Advertisement
        fields = ["status", "created_at"]
