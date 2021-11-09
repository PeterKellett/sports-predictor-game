from django.shortcuts import render
from .models import Matches

# Create your views here.
def all_matches(request):
    """ A view to all products, including sorting and search queries """

    matches = Matches.objects.all()

    context = {
        'matches': matches,
    }
    return render(request, 'matches/matches.html', context)
