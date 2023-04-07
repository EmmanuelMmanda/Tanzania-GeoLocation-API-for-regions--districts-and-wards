import json
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.conf import settings
from os.path import join
from json import load


# entry point
def index(request):
    return JsonResponse({
        "data": [{
            "message": "Hello, Users. You're at the Tanzania GeoData API index.",
            "regions_endpoint": "/api/v1/regions/",
            "districts_endpoint": "/api/v1/districts/",
            "wards_endpoint": "/api/v1/wards/",
        }]

    })

# fetch all regions


@require_http_methods(["GET"])
def allRegions(request):
    try:
        with open("geodataapi/Countries/Tanzania/Regions.json", "r") as f:
            data = load(f)
        regions = []
        for regionObject in data["features"]:
            regions.append(regionObject["properties"]["region"])
        return JsonResponse({"regions": regions})
    except Exception as e:
        return JsonResponse({"error": str(e)})

# fetch all districts


@require_http_methods(["GET"])
def allDistricts(request):
    try:
        with open("geodataapi/Countries/Tanzania/Districts.json", "r") as f:
            data = load(f)
        districts = []
        for regionObject in data["features"]:
            districts.append(regionObject["properties"]["District"])
        return JsonResponse({"districts": districts})
    except Exception as e:
        return JsonResponse({"error": str(e)})

# fetch all wards


@require_http_methods(["GET"])
def allWards(request):
    try:
        with open("geodataapi/Countries/Tanzania/Wards.json", "r",  encoding='utf-8') as f:
            data = load(f)
        wards = []
        for wardObject in data["features"]:
            wards.append(wardObject["properties"]["Ward"])
        return JsonResponse({"wards": wards})
    except Exception as e:
        return JsonResponse({"error": str(e)})


# fetch districts per region
@require_http_methods(["GET"])
def districtsPerRegion(request, region_name):
    region_name = str(region_name.capitalize()) + " Region"
    print(region_name)
    try:
        with open("geodataapi/Countries/Tanzania/Districts.json", "r") as f:
            data = json.load(f)
        districts = []
        for feature in data['features']:
            if feature['properties']['region'] == region_name:
                districts.append(feature['properties']['District'])
        return JsonResponse({'districts': districts})
    except (FileNotFoundError, json.JSONDecodeError, KeyError) as err:
        return JsonResponse({'error': str(err)})


# fetch wards per district
@require_http_methods(["GET"])
def wardsPerDistrict(request, district_name):
    district_name = str(district_name)

    try:
        with open("geodataapi/Countries/Tanzania/Wards.json", "r",  encoding='utf-8') as f:
            data = json.load(f)
        wards = []
        for feature in data['features']:
            if feature['properties']['District'].lower().find(district_name.lower()) != -1:
                wards.append(feature['properties']['Ward'])
        return JsonResponse({'wards': wards})
    except (FileNotFoundError, json.JSONDecodeError, KeyError) as err:
        return JsonResponse({'error': str(err)})
