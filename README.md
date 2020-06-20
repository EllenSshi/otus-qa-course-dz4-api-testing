# dz25 Wheel package
1) Собрать wheel-пакет можно командой $ python setup.py bdist_wheel. 
Установить: pip install dist/api_tests_lib-1.0.2-py3-none-any.whl
2) Опубликовать пакет на https://test.pypi.org/ можно командой python3 -m twine upload --repository testpypi dist/*.
Установить: pip install -i https://test.pypi.org/simple/ api-tests-lib

# dz28 Mock
Результат в папке mock_tests
1) Модуль constants.py содержит url api-сервиса
2) Модуль services.py содержит описание методов для обращения к API
3) Модуль test_dog_api_with_mock.py содержит mock-тесты, которые не обращаются на реальный сервис

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
