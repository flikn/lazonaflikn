from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect
from .forms import RequiredExtraDataForm


def require_extra_data(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('home_app:signup'))

    try:
        pipeline = request.session.get('partial_pipeline')
        details = pipeline.get('kwargs').get('details')
        details["first_name"] = details.get("first_name").title()
        details["last_name"] = details.get("last_name").title()
    except Exception, e:
        return HttpResponseRedirect(reverse('home_app:subscribe'))

    message = ""
    if request.method == 'POST':
        email = request.POST.get('email') or details.get("email")
        first_name = request.POST.get(
            'first_name') or details.get("first_name")
        last_name = request.POST.get('last_name') or details.get("last_name")
        password = request.POST.get('password')
        data = {
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "password": password,
        }
        form = RequiredExtraDataForm(data)
        if form.is_valid():
            request.session['saved_email'] = form.cleaned_data['email']
            request.session['first_name'] = form.cleaned_data['first_name']
            request.session['last_name'] = form.cleaned_data['last_name']
            request.session['raw_password'] = form.cleaned_data['password']
            backend = pipeline.get('backend')
            return redirect('social:complete', backend=backend)
        message = ("Cuenta no valida. Es muy probable que esta cuenta ya se"
                   "encuentre asociada.")
    ctx = {
        'message': message,
        'details': details,
    }
    return render_to_response(
        'home/require-extra-data.html',
        ctx,
        RequestContext(request),
    )
