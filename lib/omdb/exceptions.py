from rest_framework.exceptions import APIException

class OMDBBadRequestException(APIException):
    status_code = 400
    detail = ''
    default_code = 'bad request'

class OMDBServiceUnavailable(APIException):
    status_code = 503
    detail = 'Servicio no disponible'
    default_code = 'service_unavailable'