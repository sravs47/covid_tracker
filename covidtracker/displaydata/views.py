from django.shortcuts import render
from .models import Summary,WorldTotal
import requests

# Create your views here.
# country = models.CharField(max_length=50)
#     country_code = models.CharField(max_length=10)
#     slug = models.CharField(max_length=50)
#     new_confirmed = models.IntegerField()
#     total_confirmed = models.IntegerField()
#     new_deaths = models.IntegerField()
#     total_deaths = models.IntegerField()
#     new_recovered = models.IntegerField()
#     total_recovered = models.IntegerField()
#     date = models.DateTimeField()
#     insert_time = models.DateTimeField(default=now())
# {'Country': 'Yemen', 'CountryCode': 'YE', 'Slug': 'yemen', 'NewConfirmed': 12, 'TotalConfirmed': 209, 'NewDeaths': 0, 'TotalDeaths': 33, 'NewRecovered': 6, 'TotalRecovered': 11, 'Date': '2020-05-23T06:54:36Z'}, {'Country': 'Zambia', 'CountryCode': 'ZM', 'Slug': 'zambia', 'NewConfirmed': 54, 'TotalConfirmed': 920, 'NewDeaths': 0, 'TotalDeaths': 7, 'NewRecovered': 34, 'TotalRecovered': 336, 'Date': '2020-05-23T06:54:36Z'}, {'Country': 'Zimbabwe', 'CountryCode': 'ZW', 'Slug': 'zimbabwe', 'NewConfirmed': 0, 'TotalConfirmed': 51, 'NewDeaths': 0, 'TotalDeaths': 4, 'NewRecovered': 0, 'TotalRecovered': 18, 'Date': '2020-05-23T06:54:36Z'}]

def summary_insert(request):
    response = requests.get('https://api.covid19api.com/summary')
    summary = response.json()
    countries = summary['Countries']
    for countrie in countries:
        form = Summary.objects.create(country=countrie.get('Country'),
                                 country_code =countrie.get('CountryCode'),
                                 slug = countrie.get('Slug'),
                                 new_confirmed = countrie.get('NewConfirmed'),
                                 total_confirmed = countrie.get('TotalConfirmed'),
                                 new_deaths = countrie.get('NewDeaths'),
                                 total_deaths = countrie.get('TotalDeaths'),
                                 new_recovered = countrie.get('NewRecovered'),
                                 total_recovered = countrie.get('TotalRecovered'),
                                 date = countrie.get('Date'))
        form.save()
    return render(request, "test_view.html", {})

def summary_view(request):
    queryset = Summary.objects.all()
    # print(queryset)
    context = {
        'all_country_data' : queryset
    }
    return render(request, "test_view.html", context)

