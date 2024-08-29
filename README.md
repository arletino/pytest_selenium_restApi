## Тестирование UI и REST API   

Тестирование сайта [test-stand.gb.ru](http://test-stand.gb.ru  )

### Содержание

[1. Содержание](#содержание)  
[2. Описание](#описание)  
[3. Установка](#установка)  
[4. Использование](#использование)  
[5. Структура проекта](#структура-проекта)  
[6. Тестирование](#тестирование)  
[7. Технологии](#технологии)  
[8. Автор](#автор)  
[9. GitHub](#github)  
[10. Лицензия](#лицензия)  
  

### Описание
Этот проект представляет собой набор тестов для проверки работоспособности сервиса.  
Целью проекта является обеспечение качества и стабильности работы кода.  

Основные функции:
Функция 1: Тестирование REST API.
Функция 2: Тестирование UI.

### Установка
Чтобы установить проект, выполните следующие шаги:

Клонируйте репозиторий:   
>```git clone https://github.com/arletino/pytest_selenium_restApi.git```  

Перейдите в каталог проекта:

>```cd pytest_selenium_restApi```  

Установите необходимые зависимости:

>```pip install -r requirements.txt```  

### Использование  
Запустите тесты, используя следующую команду:  
>```pytest```  

Вы также можете использовать дополнительные параметры, например:  

>```pytest -v -m rest```  

'rest' - start test only for rest  
'ui' - start test only for rest    
'exc' - start only not exclude tests  
В файле 'tests/test_ui/service/config.yaml' какой браузер использовать для тестирования, доступно browser:  
1. Firefox - 'firefox'  
2. Chrome - 'chrome'  
3. Edge - 'edge'  

### Структура проекта  
pytest_selenium_restApi.git/  
│  
├── tests/&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;# Директория с тестами  
│&emsp;&emsp;├── test_api/  
│&emsp;&emsp;│&emsp;├── test_rest&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;# Директория с тестами для REST  
│&emsp;&emsp;│&emsp;│&emsp;    ├── test_test-gb.py&emsp;&emsp;# Тесты для REST  
│&emsp;&emsp;│&emsp;│&emsp;    ├── conftest.py&emsp;&emsp;&emsp;&emsp;# Файл с фикстурами  
│&emsp;&emsp;│&emsp;│&emsp;    └── __init__.py  
│&emsp;&emsp;│&emsp;├── config.yaml&emsp;&emsp;&emsp;&emsp;&emsp;# Конфигурационный файл  
│&emsp;&emsp;│&emsp;├── conftest.py&emsp;&emsp;&emsp;&emsp;&emsp;# Файл с фикстурами  
│&emsp;&emsp;│&emsp;└── __init__.py     
│&emsp;&emsp;│  
│&emsp;&emsp;└── test_ui  
│&emsp;&emsp;&emsp;├── service&emsp;&emsp;&emsp;#Папка модуля PageObject  
│&emsp;&emsp;&emsp;│&emsp;├── BaseApp.py&emsp;# Базовый модуль операций  
│&emsp;&emsp;&emsp;│&emsp;├── config.yaml&emsp;# Файл с данными для теста  
│&emsp;&emsp;&emsp;│&emsp;├── locators.py&emsp;# Файл загрузки локаторов  
│&emsp;&emsp;&emsp;│&emsp;├── locators.yaml&emsp;# Файл данные локаторов  
│&emsp;&emsp;&emsp;│&emsp;├── testpage.py&emsp;# Модуль страницы  
│&emsp;&emsp;&emsp;│&emsp;└── __init__.py  
│&emsp;&emsp;&emsp;├── conftest.py&emsp;# Фикстуры для теста UI  
│&emsp;&emsp;&emsp;├── test_01.py&emsp;# Тесты UI  
│&emsp;&emsp;&emsp;└── __init__.py  
│&emsp;&emsp;&emsp;  
├── requirements.txt&emsp;# Список зависимостей проекта  
├── pyproject.toml&emsp;# Конфигурационный файл для проекта  
├── README.md&emsp;# Файл с описанием проекта  
├── pyproject.toml&emsp;# Конфигурационный файл для pytest  
└── LICENSE&emsp;# Лицензия  

### Тестирование  
Для запуска тестов используется PyTest, Selenium, Requests, Webdriver-Manager. Все тесты расположены в директории tests/.  
### Основные виды тестирования, реализованные в проекте:  
Unit-тесты: Проверяют отдельные функции и методы.
Интеграционные тесты: Проверяют взаимодействие различных компонентов.
Кросс-браузерные тесты: Проверяют работу компонентов в различных браузерах(Chrome, Firefox, Edge)  
### Запуск тестов
Чтобы запустить тесты, выполните команду:
>```pytest```  
### Технологии  
Python - Основной язык программирования  
PyTest - Фреймворк для тестирования  
Selenium - Фремворк для автоматизированного тестирования веб приложений  
Webdriver-Manager - Модуль для управления webdriver
### Автор
Titkov Arkady
### GitHub 
[GitHub](https://github.com/arletino)  
### Лицензия  
Этот проект лицензирован под лицензией MIT — подробности см. в файле LICENSE.