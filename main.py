
#Task_1
def get_visits(geo_logs: list, country: str):
    geo_logs_new = []
    for dic_visit in geo_logs:
        for visit in list(dic_visit.values()):
            if country in visit:
                geo_logs_new.append(list(dic_visit.keys())[0])
    return geo_logs_new

#Task_2

def get_unique_num(ids):
    geo_id = []
    for id in ids.values():
        geo_id.extend(id)
    return list(set(geo_id))

#Task_3

def per_of_search_queries(queries):
    len_queries = []
    distrib = []
    per_of_search_queries_list = {}
    # Создаем список с уникальными количествами слов в запросах
    for querie in queries:
        quantity = len(querie.split())
        len_queries.append(quantity)
    unique_quantitys = list(set(len_queries))

    # Цикл для создания списка distrib с нулевыми значениями для последующего его заполнения, если оставить список пустым команда += 1 в следующем цикле не срабатывает
    for i in unique_quantitys:
        distrib.append(0)

    # Заполняем цикл distrib числами "встречаемости" с вычислением процента
    for unique_quantity in unique_quantitys:
        for len_querie in len_queries:
            if unique_quantity == len_querie:
                distrib[unique_quantitys.index(unique_quantity)] += 1
        percent = (distrib[unique_quantitys.index(unique_quantity)] / len(queries)) * 100
        per_of_search_queries_list[unique_quantity] = round(percent)
    return per_of_search_queries_list

#Task_4

def max_sales(stats):
    max_sales = 0
    for company, sales in stats.items():
        if sales >= max_sales:
            max_sales = sales
            top_company = company
    return top_company

#Task_5

def list_to_dic(random_list):
    for ind in range(len(random_list) - 1, -1, -1):
        if ind == 0:
            break
        key_ = random_list[ind - 1]
        values_ = random_list[ind]
        if ind == (len(random_list) - 1):
            random_dict = {key_: values_}
        else:
            random_dict = {key_: random_dict}
    return random_dict

if __name__ == '__main__':
    geo_logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]
    # print(get_visits(geo_logs, 'Россия'))

    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}
    # print(get_unique_num(ids))

    queries = [
        'смотреть сериалы онлайн',
        'новости спорта',
        'афиша кино',
        'курс доллара',
        'сериалы этим летом',
        'курс по питону',
        'сериалы про спорт',
        'курс ЦБ доллара к рублю',
        'смотреть',

    ]
    # print(per_of_search_queries(queries))

    stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
    # print(max_sales(stats))

    random_list = ['2018-01-01', 'yandex', 'cpc', 100]
    # print(list_to_dic(random_list))