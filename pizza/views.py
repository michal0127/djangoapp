from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("<h1><center>Witaj w barze pizza!</h1></center>")

def komunikat(request):
    return HttpResponse("<h1><center>Dla Pana pizza peperoni!</h1></center>")

def napoj(request):
    return HttpResponse("<h1><center>Sok pomarańczowy – niesfermentowany sok owocowy otrzymany przez wyciśnięcie miąższu dojrzałych pomarańczy Citrus sinensis[1]. Prawdziwy sok ze świeżych pomarańczy jest nietrwały (zaledwie kilka godzin) i w związku z tym trudny do komercjalizacji[1]. Dlatego produkowany na skalę przemysłową sok pomarańczowy musi zostać poddany obróbce technologicznej, która wydłuża jego trwałość i zapewnia bezpieczeństwo spożycia[1]. W związku z tym wyciśnięty świeży sok jest filtrowany, chłodzony i ewentualnie pasteryzowany, zanim trafi na sklepowe półki jako sok pomarańczowy nieotrzymany z koncentratu (skrót NFC od terminu ang. Not From Concentrate). Świeży sok może też zostać poddawany procesowi zagęszczenia[1], aż do uzyskania koncentratu soku pomarańczowego. Koncentrat ma dłuższy okres przydatności do spożycia, jest łatwiejszy do przechowywania i transportu, w ten sposób obniżając koszty produkcji[1]. Następnie przez dolanie wody do koncentratu sok trafia na rynek jako sok pomarańczowy (otrzymany) z koncentratu[1]. </h1></center>")