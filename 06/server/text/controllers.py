from protocol import make_response, make_400
import logging

logger = logging.getLogger('app.server')


def get_upper_text(request):
    logger.debug('Call func: get_upper_text')
    data = request.get('data')
    if not data:
        return make_400(request)
    return make_response(
        request,
        200,
        data.upper()
    )


def get_lower_text(request):
    logger.debug('Call func: get_upper_text')
    data = request.get('data')
    if not data:
        return make_400(request)
    return make_response(
        request,
        200,
        data.lower()
    )
