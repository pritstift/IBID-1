import autocomplete_light.shortcuts as al
from django.contrib.auth.models import User, Group

al.register(User,
    # SomeModel is already registered, re-register with custom name
    search_fields=['first_name'],
    name='UserAutocomplete')