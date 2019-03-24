from protocol import make_response, make_400
import logging
from log import log

logger = logging.getLogger('app.server')

@log
def get_upper_text(request):
    #logger.debug('Call func: get_upper_text')
    data = request.get('data')
    if not data:
        return make_400(request)
    return make_response(
        request,
        200,
        data.upper()
    )

@log
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
