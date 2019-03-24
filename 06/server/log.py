# logging - стандартный модуль для организации логирования
import logging      
import datetime
from functools import wraps
# Можно выполнить более расширенную настройку логирования.

# Создаем объект-логгер с именем app.main:
logger = logging.getLogger('app.server')

# Создаем объект форматирования:
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s ")

# Создаем файловый обработчик логирования (можно задать кодировку):
now = datetime.datetime.now()
file_name = "{0}.log".format(now.strftime("%Y-%m-%d")) 
fh = logging.FileHandler(file_name, encoding='utf-8')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

# Добавляем в логгер новый обработчик событий и устанавливаем уровень логирования
logger.addHandler(fh)
logger.setLevel(logging.DEBUG)

def log(func):
    @wraps(func)
    def wrap(request, *args, **kwargs):
        logger.info('{0} Функция {1} вызвана из функции {2}'.format(
            now.strftime("%Y-%m-%d"), func.__name__, func.__module__
        ))
        return func(request, *args, **kwargs)
    return wrap

if __name__ == '__main__':
     logger.info('Тестовый запуск логирования')
