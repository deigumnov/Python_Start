from filecmp import cmp
from os import system

# количество тестов
TEST_COUNT = 16
# путь к проекту
INPUT_PATH = 'C:\\Users\\Dmitrii\\Desktop\\Дима\\DEV\\Python\\Projects\\pythonProject\\'
# количество успешно пройденных тестов
SUCCESS = 0
# запускаемая программа
TEST_PROG = INPUT_PATH + 's_141.py'
# отчет
REPORT = INPUT_PATH + 'report.txt'

report_f = open(REPORT, 'w', encoding='utf8')
for i in range(TEST_COUNT):
    file_in_eta = INPUT_PATH + 'test\\input_' + str(i) + '.txt'
    file_in = INPUT_PATH + 'input.txt'
    with open(file_in_eta, 'r', encoding='utf8') as inf:
        with open(file_in, 'w', encoding='utf8') as outf:
            for line in inf:
                outf.write(line)
    system('python ' + TEST_PROG)
    file_out_eta = INPUT_PATH + 'test\\output_' + str(i) + '.txt'
    file_out = INPUT_PATH + 'output.txt'
    test_result = cmp(file_out, file_out_eta, shallow=True)
    if test_result:
        report_f.write(f"Тест {i} пройден успешно\n")
        SUCCESS += 1
    else:
        report_f.write(f"Тест {i} провален\n")
if SUCCESS == TEST_COUNT:
    report_f.write("Все тесты пройдены успешно")
else:
    report_f.write(f"{TEST_COUNT - SUCCESS} тестов пройдено с ошибкой")
report_f.close()
