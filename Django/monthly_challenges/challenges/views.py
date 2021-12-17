from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

monthly_challenges = {
    "january": "Thang 1",
    "february": "Thang 2",
    "march": "Thang 3"
}


def monthly_challenge_by_number(request, month):
    return HttpResponse(month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("This month is not found!")
    return HttpResponse(challenge_text)
