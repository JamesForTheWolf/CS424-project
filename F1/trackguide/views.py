from django.shortcuts import render

from trackguide.models import Track
from django.http import HttpResponse
from IPython import embed

def track(request,track_id):

    track = Track.objects.get(id=track_id)



    response = render(request,'trackguide/track_detail.html',{
        'track':track
    })

    return response



def tracks(request):

    tracks = Track.objects.all()



    response=render(request,'trackguide/track_list.html',{

            'tracks':tracks

    })

    return response