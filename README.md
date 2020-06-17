# dz28 Mock
Результат в папке mock_tests
1) Модуль constants.py содержит url api-сервиса
2) Модуль services.py содержит описание методов для обрашения к API
3) Модуль test_dog_api_with_mock.py содержит mock-тесты, которые не образаются на реальный сервис

# dz24 Jenkins
1) Создан Dockerfile для сборки образа с тестами.
2) Создан Jenkinsfile для запуска Pipeline в Jenkins.

# otus-qa-course-dz4-api-testing

1) Запустить все тесты: 
$pytest -v tests/*

2) Запустить тест с параметрами командной строки:
$pytest -v -m withparams [--url=https://ya.ru/fgfgfhfhfhfhhf] [--status_code=404]
или
$pytest -v tests/test_addoption_using.py [--url=https://ya.ru/fgfgfhfhfhfhhf] [--status_code=404] 
