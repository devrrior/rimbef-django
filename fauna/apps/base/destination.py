import logging

logger = logging.getLogger(__name__)


class DestinationFile:
    def __init__(self, file) -> None:
        self.file = file

    def destination_folder(self, file):
        try:
            destination = open(file.name, "wb+")
            for chunk in file.chunks():
                destination.write(chunk)
            destination.close()
        except Exception as e:
            logger.exception(e)

    def destination(self):
        try:
            self.destination_folder(self.file)
        except Exception as e:
            logger.exception(e)
