from rest_framework.exceptions import APIException


class BaseAPIException(APIException):
    def response(self):
        return {"code_transaction": self.default_code, "message": self.default_detail}


class SensorAlreadyExistsAPIException(BaseAPIException):
    status_code = 400
    default_detail = "Ya existe un registro con este codigo y marca de sensor"
    default_code = "SENSOR_ALREADY_EXIST"


class SensorDoesNotExistsAPIException(BaseAPIException):
    status_code = 404
    default_detail = "No existe registro del sensor"
    default_code = "SENSOR_DOES_NOT_EXIST"


class SupportFileDoesNotExistsAPIException(BaseAPIException):
    status_code = 404
    default_detail = "No existe registro del propietario"
    default_code = "SupportFile_DOES_NOT_EXIST"
