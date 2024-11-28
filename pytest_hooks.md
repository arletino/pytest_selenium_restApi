Основные хуки pytest
1. pytest_configure(config)
Этот хук вызывается после инициализации конфигурации pytest, но до запуска тестов. Он позволяет настроить поведение тестового окружения.

def pytest_configure(config):
    config.addinivalue_line(
        "markers", "custom_marker: описание вашего маркера"
    )
2. pytest_collection_modifyitems(config, items)
Этот хук вызывается после того, как все тесты собраны, но до их запуска. Он позволяет изменять или фильтровать список тестов.

def pytest_collection_modifyitems(config, items):
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(pytest.mark.skip(reason="Пропускаем медленные тесты"))
3. pytest_runtest_setup(item)
Этот хук вызывается перед запуском каждого теста. Он позволяет настроить окружение для каждого теста.

def pytest_runtest_setup(item):
    if "need_env" in item.keywords and not os.getenv("MY_ENV_VAR"):
        pytest.skip("Требуется переменная окружения MY_ENV_VAR")
4. pytest_runtest_teardown(item, nextitem)
Этот хук вызывается после выполнения каждого теста. Он используется для очистки окружения после теста.

def pytest_runtest_teardown(item, nextitem):
    if "temp_file" in item.keywords:
        os.remove("/tmp/tempfile")
5. pytest_terminal_summary(terminalreporter, exitstatus)
Этот хук вызывается после завершения всех тестов и используется для добавления пользовательских данных к итоговому отчету.

def pytest_terminal_summary(terminalreporter, exitstatus):
    terminalreporter.write_sep("=", "Мой пользовательский отчет")
    terminalreporter.write_line("Все тесты выполнены успешно!")
Примеры использования хуков
Пример 1: Счетчик выполненных тестов
Создадим хук, который будет считать количество выполненных тестов и выводить эту информацию после завершения тестирования.

# conftest.py

def pytest_sessionstart(session):
    session.tests_ran = 0

def pytest_runtest_logreport(report):
    if report.when == 'call' and report.passed:
        session.tests_ran += 1

def pytest_terminal_summary(terminalreporter, exitstatus):
    terminalreporter.write_sep("=", f"Количество успешно выполненных тестов: {session.tests_ran}")
Пример 2: Условное пропускание тестов
Пропустим все тесты, если они отмечены маркером skip_if_no_db, и база данных не доступна.

# conftest.py

def pytest_runtest_setup(item):
    if "skip_if_no_db" in item.keywords and not check_database_connection():
        pytest.skip("База данных недоступна")
Пример 3: Добавление пользовательского маркера
Добавим новый маркер и будем использовать его для выполнения дополнительных действий перед тестами.

# conftest.py

def pytest_configure(config):
    config.addinivalue_line(
        "markers", "dbtest: тесты, требующие подключения к базе данных"
    )

def pytest_runtest_setup(item):
    if "dbtest" in item.keywords:
        setup_database()
Хуки pytest предоставляют мощные возможности для настройки и расширения тестового процесса. Используя хуки, можно настроить сбор тестов, подготовку окружения, выполнение тестов и обработку результатов. Это делает pytest невероятно гибким и расширяемым инструментом для автоматизации тестирования.