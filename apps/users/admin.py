"""`users` app admin."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User


# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Custom `UserAdmin` for `User` model.

    This class defines settings and fields to be displayed in `Django Admin` panel.
    """

    model: type[User] = User
    list_display: tuple[str] = ('email', 'first_name', 'last_name', 'is_staff')
    ordering: tuple[str] = ('email', )

    fieldsets: tuple[tuple[str | None | dict[str, tuple[str]]]] = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets: tuple[tuple[str | None | dict[str, tuple[str]]]] = (
        (None, {
            'classes': ('wide', ),  # noqa: WPS317
            'fields': (
                'email', 'first_name', 'last_name',
                'password1', 'password2',
                'is_staff', 'is_superuser',
            ),
        }),
    )
