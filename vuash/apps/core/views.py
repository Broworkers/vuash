from django.shortcuts import render

from vuash.apps.core.forms import MessageForm


def create_message(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save()
            return render(request, "message_created.html", {"message": message})
    else:
        form = MessageForm()
    return render(request, "message_form.html", {"form": form})
