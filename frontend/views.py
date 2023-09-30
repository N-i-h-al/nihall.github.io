from django.shortcuts import render
import requests


def index(request):
    api_url = 'http://127.0.0.1:8000/topsites/TopSite/'  # Update with your actual API endpoint
    response = requests.get(api_url)
    topsites = response.json() if response.status_code == 200 else []

    # Print the image URLs to the console for verification
    for site in topsites:
        print(site['image'])

    return render(request, 'index.html', {'topsites': topsites})



