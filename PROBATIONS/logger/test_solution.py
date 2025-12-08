from datetime import datetime
from file_logger import FileLogger
from console_logger import ConsoleLogger


def test_file_logger_write_message(tmpdir):
    filename = tmpdir.join('test.log')
    logger = FileLogger(filename)

    logger.info('Test message')

    with open(filename, 'r') as file:
        content = file.read()

    timestamp = datetime.now().strftime('%Y-%m-%d')
    assert timestamp in content
    assert '[INFO]: Test message' in content


def test_file_logger_log_level(tmpdir):
    filename = tmpdir.join('test.log')
    logger = FileLogger(level='WARNING', filename=filename)

    logger.info('Info message')
    logger.warning('Warning message')

    with open(filename, 'r') as file:
        content = file.read()

    assert 'Info message' not in content
    assert 'Warning message' in content


def test_file_logger_invalid_filename(capsys):
    logger = FileLogger('/invalid/path/test.log')
    logger.info('Test message')

    captured = capsys.readouterr()
    assert 'Ошибка записи в файл' in captured.out


def test_console_logger_write_message(capsys):
    logger = ConsoleLogger()

    logger.info('Test message')
    captured = capsys.readouterr()
    timestamp = datetime.now().strftime('%Y-%m-%d')

    assert timestamp in captured.out
    assert '[INFO]: Test message\n' in captured.out


def test_console_logger_log_level(capsys):
    logger = ConsoleLogger('WARNING')

    logger.info('Info message')
    logger.warning('Warning message')

    captured = capsys.readouterr()
    assert 'Info message' not in captured.out
    assert 'Warning message' in captured.out
