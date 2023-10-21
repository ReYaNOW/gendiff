### Hexlet tests and linter status:
[![Actions Status](https://github.com/ReYaNOW/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/ReYaNOW/python-project-50/actions) [![Project tests with CI](https://github.com/ReYaNOW/python-project-50/actions/workflows/action_tests.yml/badge.svg)](https://github.com/ReYaNOW/python-project-50/actions/workflows/action_tests.yml) [![Maintainability](https://api.codeclimate.com/v1/badges/f3344950f20704d22db6/maintainability)](https://codeclimate.com/github/ReYaNOW/python-project-50/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/f3344950f20704d22db6/test_coverage)](https://codeclimate.com/github/ReYaNOW/python-project-50/test_coverage)

Этот проект представляет собой программу - Вычислитель отличий

Вычислитель отличий – программа, определяющая разницу между двумя структурами данных. Это популярная задача, для решения которой существует множество [онлайн-сервисов](http://www.jsondiff.com/). Подобный механизм, например, используется при выводе тестов или при автоматическом отслеживании изменений в конфигурационных файлах.

Возможности утилиты:

    Поддержка разных входных форматов: yaml, json
    Генерация отчета в виде plain text, stylish и json


## Установка  

Для установки игры необходимо использовать команду, находясь в корневой директории проекта
```
poetry install
```
  
Так же имеется возможность сделать билд игры с последующей установкой при помощи двух команд
```
poetry build && pip install dist/*.whl
```

Так же можно установить игру без клонирования репозитория, но после этого нужно будет установить зависимости, указанные ниже
```
python3 -m pip install --user git+https://github.com/ReYaNOW/python-project-50.git
```
  
![](https://github.com/ReYaNOW/repo_for_gifs/blob/main/python-project-50-gifs/installv2.gif?raw=true)

Для того чтобы увидеть мануал по программе необходимо использовать команду 
```
gendiff
```
или 
```
gendiff -h
```
```
brain-even
```  
<a href="https://asciinema.org/a/616198?autoplay=1" target="_blank" rel="noreferrer"><img src="https://media.discordapp.net/attachments/324178393161793536/1165089454793437294/image.png?ex=6545951c&is=6533201c&hm=8bf04296d9361b12999d6196665483d43d961f4b8945d276ea49c331a3024399&=" alt="image" /></a>
[Пример работы команды](https://asciinema.org/a/572988?autoplay=1) 

Для сравнения файлов необходимо использовать команду ```gendiff [Путь до файла 1] [Путь до файла 2]```  
[Пример работы команды c **json** файлами](https://asciinema.org/a/572987?autoplay=1)  
[Пример работы команды с **yaml** файлами](https://asciinema.org/a/573331?autoplay=1)  
[Пример работы команды с **yaml** и **json** файлами со вложенными структурами](https://asciinema.org/a/577785?autoplay=1)  
[Пример работы команды в формате **plain text**](https://asciinema.org/a/577804?autoplay=1)  
[Пример работы команды в формате **json**](https://asciinema.org/a/577919?autoplay=1) 