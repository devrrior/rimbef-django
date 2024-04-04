from django.core.exceptions import ValidationError


def validate_file_size(value):

    try:
        filesize = value.size

        if filesize > 4485760:
            raise ValidationError("El tamaño máximo debe ser de 4 MB")
        return value
    except Exception as e:
        raise ValidationError(str(e))
