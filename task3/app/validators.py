from django.core.exceptions import ValidationError


class PasswordValidator:
    def __init__(self, min_length=8):
        self.min_length = min_length

    def __call__(self, value):
        if len(value) < self.min_length:
            raise ValidationError(
                f"Password must be at least {self.min_length} characters long."
            )
