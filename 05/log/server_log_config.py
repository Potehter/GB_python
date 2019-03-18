# logging - стандартный модуль для организации логирования
import logging      
import datetime
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

if __name__ == '__main__':
     logger.info('Тестовый запуск логирования')
