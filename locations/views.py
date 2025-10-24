import json

from django.views.generic import TemplateView, View
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .models import Place


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        features = []
        for p in Place.objects.all():
            features.append({
                "type": "Feature",
                "geometry": {"type": "Point", "coordinates": [float(p.lng), float(p.lat)]},
                "properties": {
                    "title": p.title,
                    "placeId": p.id,
                    "detailsUrl": reverse('place_details', kwargs={'pk': p.pk}),
                },
            })
        places_geojson = {"type": "FeatureCollection", "features": features}
        ctx['places_geojson_json'] = json.dumps(places_geojson, ensure_ascii=False)
        return ctx


class PlaceDetailsView(View):
    def get(self, request, pk):
        place = get_object_or_404(
            Place.objects.prefetch_related('imgs'),
            pk=pk
        )
        imgs = [request.build_absolute_uri(img.image.url) for img in place.imgs.all()]
        data = {
            "title": place.title,
            "imgs": imgs,
            "description_short": place.description_short,
            "description_long": place.description_long,
            "coordinates": {"lng": str(place.lng), "lat": str(place.lat)},
        }
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False})
