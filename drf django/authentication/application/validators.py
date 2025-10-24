from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
import re


class MaxLengthPasswordValidator:
    def __init__(self, max_length=16):
        self.max_length = max_length

    def validate(self, password, user=None):
        if len(password) > self.max_length:
            raise ValidationError(
                _(f"Password must be {self.max_length} characters or fewer."),
                code="password_too_long",
            )

    def get_help_text(self):
        return _(f"Your password must be {self.max_length} characters or fewer.")


class StrongPasswordValidator:
    def validate(self, password, user=None):
        if not re.search(r"[A-Z]", password):
            raise ValidationError(_("Password must contain at least 1 uppercase letter"), code="password_no_upper")
        if not re.search(r"[a-z]", password):
            raise ValidationError(_("Password must contain at least 1 lowercase letter"), code="password_no_lower")
        if not re.search(r"[0-9]", password):
            raise ValidationError(_("Password must contain at least 1 digit"), code="password_no_digit")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            raise ValidationError(_("Password must contain at least 1 special character"), code="password_no_symbol")

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 uppercase letter, 1 lowercase letter, "
            "1 digit, and 1 special character (!@#$%^&* etc.)."
        )
