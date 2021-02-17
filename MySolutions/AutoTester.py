from filecmp import cmp
from os import system

# количество тестов
test_count = 16
# путь к проекту
input_path = 'C:\\Users\\Dmitrii\\Desktop\\Дима\\DEV\\Python\\Projects\\pythonProject\\'
# количество успешно пройденных тестов
success = 0
# запускаемая программа
test_program = input_path + 's_141.py'
# отчет
report = input_path + 'report.txt'

report_f = open(report, 'w', encoding='utf8')
for i in range(test_count):
    file_in_eta = input_path + 'test\\input_' + str(i) + '.txt'
    file_in = input_path + 'input.txt'
    with open(file_in_eta, 'r', encoding='utf8') as inf:
        with open(file_in, 'w', encoding='utf8') as outf:
            for line in inf:
                outf.write(line)
    system('python ' + test_program)
    file_out_eta = input_path + 'test\\output_' + str(i) + '.txt'
    file_out = input_path + 'output.txt'
    test_result = cmp(file_out, file_out_eta, shallow=True)
    if test_result:
        report_f.write(f"Тест {i} пройден успешно\n")
        success += 1
    else:
        report_f.write(f"Тест {i} провален\n")
if success == test_count:
    report_f.write("Все тесты пройдены успешно")
else:
    report_f.write(f"{test_count - success} тестов пройдено с ошибкой")
report_f.close()
