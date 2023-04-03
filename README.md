### Hexlet tests and linter status:
[![Actions Status](https://github.com/ReYaNOW/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/ReYaNOW/python-project-50/actions) [![Project tests with CI](https://github.com/ReYaNOW/python-project-50/actions/workflows/action_tests.yml/badge.svg)](https://github.com/ReYaNOW/python-project-50/actions/workflows/action_tests.yml) [![Maintainability](https://api.codeclimate.com/v1/badges/f3344950f20704d22db6/maintainability)](https://codeclimate.com/github/ReYaNOW/python-project-50/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/f3344950f20704d22db6/test_coverage)](https://codeclimate.com/github/ReYaNOW/python-project-50/test_coverage)

Этот проект представляет собой программу - Вычислитель отличий

Вычислитель отличий – программа, определяющая разницу между двумя структурами данных. Это популярная задача, для решения которой существует множество [онлайн-сервисов](http://www.jsondiff.com/). Подобный механизм, например, используется при выводе тестов или при автоматическом отслеживании изменений в конфигурационных файлах.

Возможности утилиты:

    Поддержка разных входных форматов: yaml, json
    Генерация отчета в виде plain text, stylish и json


Для установки игры необходимо использовать команду ```make package-install``` находясь в корневой директории проекта. [Запись установки.](https://asciinema.org/a/572985)  

Для того чтобы увидеть мануал по програме необходимо использовать команду ```gendiff``` или ```gendiff -h``` [Пример работы команды.](https://asciinema.org/a/572988) 

Для сравнения двух json файлов необходимо использовать команду ```gendiff [Путь до файла 1] [Путь до файла 2]``` [Пример работы команды.](https://asciinema.org/a/572987)  

Для сравнения двух yaml файлов необходимо использовать команду ```gendiff [Путь до файла 1] [Путь до файла 2]``` [Пример работы команды.](https://asciinema.org/a/573331)
