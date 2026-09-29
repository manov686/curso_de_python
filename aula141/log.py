# Abstração
from datetime import datetime


class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método _log')

    def log_error(self, msg):
        self._log(f'Error: {msg}')

    def log_success(self, msg):
        self._log(f'Success: {msg}')


class LogPrintMixin(Log):
    def _log(self, msg):
        timestamp = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        print(f'[{timestamp}] {msg} ({self.__class__.__name__})')


if __name__ == '__main__':
    log = LogPrintMixin()

    log.log_error('Anything')
    log.log_success('Nice')