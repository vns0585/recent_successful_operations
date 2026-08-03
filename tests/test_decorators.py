from os import remove

import pytest
from _pytest.capture import CaptureFixture

from src.decorators import log


def test_log_ok_console(capsys: CaptureFixture[str]) -> None:
    @log()
    def my_function(x: int, y: int) -> int:
        return x + y
    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function Ok\n"


def test_log_ok_file() -> None:
    @log("mylog.txt")
    def my_function(x: int, y: int) -> int:
        return x + y
    my_function(1, 2)
    with open("mylog.txt", "r", encoding="utf-8") as file:
        assert file.read() == "my_function Ok\n"
    remove("mylog.txt")


def test_log_error_console(capsys: CaptureFixture[str]) -> None:
    @log()
    def my_function(x: int, y: int) -> int:
        raise Exception("Тестовая ошибка")
    with pytest.raises(Exception, match="Тестовая ошибка"):
        my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function error: Тестовая ошибка. Inputs: (1, 2), {}\n"


def test_log_error_file() -> None:
    @log("mylog.txt")
    def my_function(x: int, y: int) -> int:
        raise Exception("Тестовая ошибка")
    with pytest.raises(Exception, match="Тестовая ошибка"):
        my_function(1, 2)
    with open("mylog.txt", "r", encoding="utf-8") as file:
        assert file.read() == "my_function error: Тестовая ошибка. Inputs: (1, 2), {}\n"
    remove("mylog.txt")


def test_log_wrong_filename() -> None:
    @log(1)
    def my_function(x: int, y: int) -> int:
        return x + y
    with pytest.raises(Exception, match="Имя файла должно быть строкового типа"):
        my_function(1, 2)
