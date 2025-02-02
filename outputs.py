from prettytable import PrettyTable

def control_output(results, cli_args):
    if cli_args.pretty:
        pretty_output(results)
    else:
        default_output(results)

def default_output(results):
    for row in results:
        print(*row)

def pretty_output(results):
    table = PrettyTable()
    # В качестве заголовков устанавливаем первый элемент списка.
    table.field_names = results[0]
    table.align = 'l'
    # Добавляем все строки, начиная со второй (с индексом 1).
    table.add_rows(results[1:])
    print(table)