from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from social.pipeline.partial import partial
from apps.customuser.forms import UserSignupForm


@partial
def associate_by_email_or_username(strategy, details, user=None, is_new=False,
                                   *args, **kwargs):
    try:
        email = details.get('email')
        User = get_user_model()
        if email:
            kwargs['user'] = User.objects.get(email=email)
    except:
        pass
    return kwargs


@partial
def require_extra_data(strategy, details, user=None, is_new=False,
                       *args, **kwargs):
    if user and user.email:
        return
    elif is_new:
        if strategy.session_get('saved_email'):
            details['email'] = strategy.session_pop('saved_email')
        if strategy.session_get('first_name'):
            details['first_name'] = strategy.session_pop('first_name')
        if strategy.session_get('last_name'):
            details['last_name'] = strategy.session_pop('last_name')
        if strategy.session_get('raw_password'):
            details['raw_password'] = strategy.session_pop('raw_password')
        else:
            return redirect('customuser_app:complete-signup')


def create_user(strategy, details, user=None, *args, **kwargs):
    USER_FIELDS = [
        'username',
        'email',
        'first_name',
        'last_name,',
        'raw_password',
    ]

    if user:
        return {'is_new': False}

    fields = dict((name, kwargs.get(name) or details.get(name))
                  for name in strategy.setting('USER_FIELDS', USER_FIELDS))
    if not fields:
        return
    fields["password"] = fields.pop("raw_password")

    form = UserSignupForm(data=fields)
    if form.is_valid():
        username = fields.get("username")
        email = form.cleaned_data['email']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        password = form.cleaned_data['password']
        MyUser = get_user_model()
        new_user = MyUser.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        return {
            'is_new': True,
            'user': new_user,
        }
