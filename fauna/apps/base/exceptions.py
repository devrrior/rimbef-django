from rest_framework.exceptions import APIException


class BaseAPIException(APIException):
    def response(self):
        return {"code_transaction": self.default_code, "message": self.default_detail}


class ReportServiceAPIException(BaseAPIException):
    status_code = 500
    default_code = "REPORT_SERVICE_ERROR"

    def response(self):
        return {"code_transaction": self.default_code, "message": self.detail}
