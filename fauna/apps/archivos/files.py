import os
import uuid


def archivos_files_path(filename, directory=""):
    _, ext = os.path.splitext(filename)
    hash = uuid.uuid4().hex
    return f"media/archivos/{directory}{hash}{ext}"


def archivos_image_path(instance, extension="jpg"):
    return archivos_files_path(f"{instance.id}.{extension}", "images/")
