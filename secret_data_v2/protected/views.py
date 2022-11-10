from django.http import HttpResponse
from django.shortcuts import render
from .models import Person


def main(request):
    return render(
        request=request,
        template_name='protected/main.html'
    )


def secret_reference(request):
    if request.method == "GET":
        person_data = request.GET.get('text')
        person_pin = request.GET.get('pin')
        person = Person(data=person_data, pin=person_pin)
        person.save()
        reference = person.unique_value
    return render(
        request=request,
        template_name='protected/secret_reference.html',
        context={'reference': reference}
    )


def enter_pin_code(request, reference):
    pin = request.GET.get('pin')
    secret_data = Person.objects.get(unique_value=reference)
    if not pin and secret_data:
        return render(
            request=request,
            template_name="protected/enter_pin_code.html",
            context={'reference_uuid': reference}
        )
    return render(
        request=request,
        template_name="protected/person_data.html",
        context={
            'data': secret_data.data
        }
    )









