import random
from django.shortcuts import render, redirect
from django.contrib import messages


def home(request):
    quotes = [
        "Believe you can and you're halfway there.",
        "Your limitation—it's only your imagination.",
        "Push yourself, because no one else is going to do it for you.",
        "Great things never come from comfort zones.",
        "Dream it. Wish it. Do it."
    ]
    quote = random.choice(quotes)
    return render(request, "quotes/home.html", {"quote": quote})


def about(request):
    return render(request, "quotes/about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if name and email and message: 
            messages.success(request, f"Thank you {name}! 🎉 We will reach you soon.")
            return redirect("contact")
        else:
            messages.error(request, "⚠️ Please fill out all fields before submitting.")
            return redirect("contact")

    return render(request, "quotes/contact.html")
