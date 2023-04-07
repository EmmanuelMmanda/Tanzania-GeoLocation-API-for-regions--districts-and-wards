# Tanzania Regions Districts Wards API
[![View on GitHub](https://img.shields.io/badge/View%20on%20GitHub-black.svg?logo=github&style=flat-square)](https://github.com/EmmanuelMmanda) 
[![API](https://img.shields.io/badge/API-v1.0-green)](http://api.example.com)
[![Django](https://img.shields.io/badge/Django-3.2-green.svg)](https://docs.djangoproject.com/en/3.2/)
[![Powered by Vercel](https://www.datocms-assets.com/31049/1618983297-powered-by-vercel.svg)](https://tzgeodata.vercel.app/)



## Overview
The Tanzania GeoData API provides endpoints for accessing data on regions, districts, and wards in Tanzania. This API is useful for applications that need to display or analyze data on the administrative regions of Tanzania.

## Base URL
The base URL for the Tanzania API is https://tzgeodata.vercel.app/.

## Authentication
Authentication is not required to access any of the endpoints in this API.

Endpoints
Fetching All Regions
Endpoint: 
```
GET /api/v1/regions/
```

This endpoint returns a list of all the regions in Tanzania.

Response
The response is a JSON object with a single key, regions, which contains a list of region names.

Example Response:
```json
{
  "regions": [
    "Arusha",
    "Dar es Salaam",
    "Dodoma",
    "Geita",
    "Iringa",
    ...
  ]
}
```

Fetching Districts per Region
Endpoint: 
```
  GET /api/v1/regions/<str:region_name>/districts/
```

This endpoint returns a list of all the districts in the specified region.

Path Parameters
``` region_name ``` - The name of the region to fetch districts for.

Response
The response is a JSON object with a single key, districts, which contains a list of district names.

Example Response:
```json
{
  "districts": [
    "Arusha City",
    "Arusha Rural",
    "Karatu",
    "Longido",
    "Monduli",
    ...
  ]
}
```

Fetching All Districts
Endpoint: 
```http
      GET /api/v1/districts/ 
```

This endpoint returns a list of all the districts in Tanzania.

Response:
The response is a JSON object with a single key, districts, which contains a list of district names.

Example Response:
```json
{
  "districts": [
    "Arusha City",
    "Arusha Rural",
    "Babati Rural",
    "Babati Town",
    "Bagamoyo",
    ...
  ]
}
```

#### Fetching Wards per District in a Region
Endpoint:
```
GET /api/v1/districts/<str:district_name>/wards/
```

This endpoint returns a list of all the wards in the specified district.

Path Parameters
``` district_name ``` - The name of the district to fetch wards for.

Response
The response is a JSON object with a single key, wards, which contains a list of ward names.

Example Response:
```json
{
  "wards": [
    "Baraa",
    "Bwawani",
    "Endabash",
    "Engutoto",
    "Kaloleni",
    ...
  ]
}

```
Fetching All Wards in Tanzania
Endpoint: 
```http
GET /api/v1/wards/
```

This endpoint returns a list of all the wards in Tanzania.

Response
The response is a JSON object with a single key, wards, which contains a list of ward names.

Example Response:
```json
{
  "wards": [
    "Aghondi",
    "Agunga",
    "Ajira",
    "Alango",
    "Albina",
    ...
  ]
}
```

### Error Responses
If the API encounters an error, it will return an error response with an appropriate status code and message.

Example Error Response
```json

{
  "error": "Resource not found"
}

~~~
