# Abstração
from pathlib import Path
from datetime import datetime

LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método _log')

    def log_error(self, msg):
        self._log(f'Error: {msg}')

    def log_success(self, msg):
        self._log(f'Success: {msg}')

class LogFileMixing(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando no log...', msg_formatada)
        with open(LOG_FILE, 'a', encoding='utf-8') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\r\n')


class LogPrintMixing(Log):
    def _log(self, msg):
        timestamp = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        print(f'[{timestamp}] {msg} ({self.__class__.__name__})')


if __name__ == '__main__':
    log = LogPrintMixing()
    log.log_error('Anything')
    log.log_success('Nice')
    lf = LogFileMixing()
    lf.log_error('Anything')
    lf.log_success('Nice')