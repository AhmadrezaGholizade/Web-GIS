from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

def GetPNG(request, z, x, y):
    url = f'http://localhost:7373/geoserver/ne/gwc/service/wmts?layer=ne%3Arasht_roads_free_1&style=&tilematrixset=EPSG%3A4326&Service=WMTS&Request=GetTile&Version=1.0.0&Format=image%2Fpng&TileMatrix=EPSG%3A4326%3A{z}&TileCol={x}&TileRow={y}'
    try:
        response = requests.get(url)
    except:
        return HttpResponse("Can't Reach The Geoserver", status = 503)
    
    if response.status_code == 200:
        return HttpResponse(response.content, content_type='image/png')
    else:
        print(response.text.split('<ExceptionText>')[1].split('</ExceptionText>')[0])
        return HttpResponse(response.text.split('<ExceptionText>')[1].split('</ExceptionText>')[0], status=404)