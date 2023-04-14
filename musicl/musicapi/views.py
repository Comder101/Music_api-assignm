
import requests
from django.shortcuts import render


def search_music(request):
    if request.method == 'POST':
        search_term = request.POST.get('search_term')
        url = f'https://itunes.apple.com/search?term={search_term}&media=music&entity=album'
        response = requests.get(url)
        data = response.json()
        results = data.get('results')
        context = {'results': results}
        return render(request, 'search_results.html', context)
    return render(request, 'search_music.html')


# Create your views here.
