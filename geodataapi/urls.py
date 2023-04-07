from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("api/v1/regions/", views.allRegions,
         name="regions"),  # fetching all regions

    path("api/v1/regions/<str:region_name>/districts/",
         views.districtsPerRegion, name="districtsPerRegion"),  # fetching districts per region

    path("api/v1/districts/", views.allDistricts,
         name="districts"),  # fetching all districts

    path("api/v1/districts/<str:district_name>/wards/",
         views.wardsPerDistrict, name="wardsPerDistrict"),  # fetching wards per district in a region
   
    path("api/v1/wards/", views.allWards, name="wards"),  # fetching all wards in Tanzania


]
