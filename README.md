### Hexlet tests and linter status:
[![Actions Status](https://github.com/ReYaNOW/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/ReYaNOW/python-project-50/actions) [![Project tests with CI](https://github.com/ReYaNOW/python-project-50/actions/workflows/action_tests.yml/badge.svg)](https://github.com/ReYaNOW/python-project-50/actions/workflows/action_tests.yml) [![Maintainability](https://api.codeclimate.com/v1/badges/f3344950f20704d22db6/maintainability)](https://codeclimate.com/github/ReYaNOW/python-project-50/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/f3344950f20704d22db6/test_coverage)](https://codeclimate.com/github/ReYaNOW/python-project-50/test_coverage)

Этот проект представляет собой программу - Вычислитель отличий

Вычислитель отличий – программа, определяющая разницу между двумя структурами данных. Это популярная задача, для решения которой существует множество [онлайн-сервисов](http://www.jsondiff.com/). Подобный механизм, например, используется при выводе тестов или при автоматическом отслеживании изменений в конфигурационных файлах.

Возможности утилиты:

    Поддержка разных входных форматов: yaml, json
    Генерация отчета в виде plain text, stylish и json


## Установка  

Для установки программы необходимо использовать команду, находясь в корневой директории проекта
```
poetry install
```
  
Так же имеется возможность сделать билд проекта с последующей установкой при помощи двух команд
```
poetry build && pip install dist/*.whl
```

Так же можно установить программу без клонирования репозитория, но после этого нужно будет установить зависимости, указанные ниже
```
python3 -m pip install --user git+https://github.com/ReYaNOW/python-project-50.git
```  
  
![](https://github.com/ReYaNOW/repo_for_gifs/blob/main/python-project-50-gifs/installv2.gif?raw=true)  
  
###### Устанавливать программу стоит в отдельном окружении для избежания проблем с зависимостями  

#### Как создать окружение и активировать его
Windows  PowerShell
```
python -m venv venv; ./venv/Scripts/activate.ps1
```
  
Linux  
```
python3 -m venv venv && source venv/bin/activate
```
   
  
## Использование  
  
Для того чтобы увидеть мануал по программе, необходимо использовать команду 
```
gendiff
```
или 
```
gendiff -h
``` 
<a href="https://asciinema.org/a/616198?autoplay=1" target="_blank" rel="noreferrer"><img src="https://cdn.discordapp.com/attachments/324178393161793536/1165092906365898833/image.png?ex=65459853&is=65332353&hm=f3207a585d7425955ec91531777f8b7dcea3819902f965ee263a649eec3952ff&" alt="image" /></a>

Для сравнения файлов необходимо использовать команду 
```  
gendiff [Путь до файла 1] [Путь до файла 2]  
```  
  
#### [Пример работы](https://asciinema.org/a/572987?autoplay=1) команды c json файлами 
![](https://github.com/ReYaNOW/repo_for_gifs/blob/main/python-project-50-gifs/json_stylish.gif?raw=true)  
  
#### [Пример работы](https://asciinema.org/a/577785?autoplay=1) команды с yaml и json файлами со вложенными структурами  
![](https://github.com/ReYaNOW/repo_for_gifs/blob/main/python-project-50-gifs/json_yaml_recursive_v2.gif?raw=true)  
  
#### [Пример работы](https://asciinema.org/a/616200?autoplay=1) команды в формате plain text  
![](https://github.com/ReYaNOW/repo_for_gifs/blob/main/python-project-50-gifs/json_plain.gif?raw=true)  
  
#### [Пример работы](https://asciinema.org/a/616201?autoplay=1) команды в формате json  
![](https://github.com/ReYaNOW/repo_for_gifs/blob/main/python-project-50-gifs/json_format_json__v2.gif?raw=true)  
  
### Минимальные требования:  
[Python^3.10](https://www.python.org/)  
[Poetry](https://python-poetry.org/)  
#### Библиотеки Python:  
[Flake8](https://pypi.org/project/flake8/)  
[Pytest](https://pypi.org/project/pytest/)  
[Pytest-cov](https://pypi.org/project/pytest-cov/)    
[PyYAML](https://pypi.org/project/pytest-cov/)  