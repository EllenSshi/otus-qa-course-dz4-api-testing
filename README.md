# otus-qa-course-dz4-api-testing

1) Запустить все тесты: 
$pytest -v tests/*

2) Запустить тест с параметрами командной строки:
$pytest -v -m withparams [--url=https://ya.ru/fgfgfhfhfhfhhf] [--status_code=404]
или
$pytest -v tests/test_addoption_using.py [--url=https://ya.ru/fgfgfhfhfhfhhf] [--status_code=404] 
