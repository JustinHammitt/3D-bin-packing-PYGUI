class ValidationService:
    @staticmethod
    def require_text(value, field_name):
        text = str(value).strip()
        if not text:
            raise ValueError(f"{field_name} is required.")
        return text

    @staticmethod
    def require_float(value, field_name, *, min_value=None, allow_zero=True):
        text = str(value).strip()
        if text == "":
            raise ValueError(f"{field_name} is required.")

        try:
            number = float(text)
        except ValueError:
            raise ValueError(f"{field_name} must be a valid number.")

        if not allow_zero and number == 0:
            raise ValueError(f"{field_name} must be greater than 0.")

        if min_value is not None and number < min_value:
            if min_value == 0 and not allow_zero:
                raise ValueError(f"{field_name} must be greater than 0.")
            raise ValueError(f"{field_name} must be at least {min_value}.")

        return number

    @staticmethod
    def require_int(value, field_name, *, min_value=None):
        text = str(value).strip()
        if text == "":
            raise ValueError(f"{field_name} is required.")

        try:
            number = int(text)
        except ValueError:
            raise ValueError(f"{field_name} must be a whole number.")

        if min_value is not None and number < min_value:
            raise ValueError(f"{field_name} must be at least {min_value}.")

        return number