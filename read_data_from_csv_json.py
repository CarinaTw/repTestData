# Скрипт читает из двух файлов данные и на их основании создаст json файл со структурой из файла example.json

# Каждому пользователю нужно добавить одну книгу из списка.
# Если количество книг меньше количества пользователей, то остальным добавить пустой массив.
# Если книг больше чем пользователей, то просто прекратить раздавать книги.

import csv
import json



def read_from_csv_to_dict(file):
    books_list_of_dict = []
    with open(file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            books_list_of_dict.append(row)
    return books_list_of_dict
# данные по книгам в формате список словарей:
# [{'Title': 'Fundamentals of Wavelets', 'Author': 'Goswami, Jaideva', 'Genre': 'signal_processing', 'Height': '228', 'Publisher': 'Wiley'},{}]


def read_from_json_to_dict(file):
    users_list_of_dicts = []
    with open(file, 'r') as file:
        js_file = file.read()
        list_of_dicts_users = json.loads(js_file)
        # for u in dict_users:
        #     users_list_of_dicts.append(u)
    #return users_list_of_dicts
    return list_of_dicts_users


# данные по юзерам в формате список словарей:
# [
# {'_id': '5e2696e561fdc6df60d43b5f', 'index': 0, 'guid': '3e518b31-20f0-4dea-8de8-039af5afbd33', 'isActive': False, 'balance': '$3,646.47', 'picture': 'http://placehold.it/32x32', 'age': 34, 'eyeColor': 'brown', 'name': 'Lolita Lynn', 'gender': 'female', 'company': 'HIVEDOM', 'email': 'lolitalynn@hivedom.com', 'phone': '+1 (842) 513-2979', 'address': '389 Neptune Avenue, Belfair, Iowa, 6116', 'about': 'Ea irure labore culpa proident sint cupidatat minim laboris labore eu exercitation aliqua duis aute. Consectetur pariatur commodo enim pariatur mollit. Laborum nisi cillum do consectetur laboris nulla id laboris eu voluptate sit consequat commodo aute. Ad minim eiusmod pariatur non cupidatat esse fugiat et laborum ullamco commodo. Sint fugiat enim elit pariatur consequat ipsum Lorem qui qui Lorem proident mollit culpa. In enim commodo culpa nostrud reprehenderit nostrud incididunt elit labore. Aute proident mollit pariatur proident enim commodo.\r\n', 'registered': '2014-03-19T10:39:24 -06:00', 'latitude': 0.246756, 'longitude': -96.404056, 'tags': ['ad', 'ut', 'do', 'dolor', 'qui', 'quis', 'enim'], 'friends': [{'id': 0, 'name': 'Joan Weaver'}, {'id': 1, 'name': 'Morris Wheeler'}, {'id': 2, 'name': 'Morton Noble'}], 'greeting': 'Hello, Lolita Lynn! You have 2 unread messages.', 'favoriteFruit': 'banana'}
# ]


# def write_to_json_file(file_csv, file_json, file_example_format, result_file="result.json"):
#     books = read_from_csv_to_dict(csv_file)
#     users = read_from_json_to_dict(json_file)
#
#     users_template = users
#     books_template = books
#
#     #to_json = {"users": users_template}
#     to_json = {"books": books_template}
#     # to_json = {"users": users_template, "books": books_template}
#
#     with open(result_file, "w") as f:
#         f.write(json.dumps(to_json))

def write_to_json_file(file_csv, file_json, file_example_format, result_file="result.json"):

    # в отдельный список сохраняем json данные по книгам - список словарей
    books = read_from_csv_to_dict(csv_file)

    # в отдельный список сохраняем json данные по юзерам - список словарей
    list_of_dicts_users = read_from_json_to_dict(json_file)

    # берем ключи из файла с примером
    keys_list = list(read_from_json_to_dict(file_example_format))
    print(keys_list)

    # делаем из ключей словарь с путыми значениями
    dict_from_key_list = {}.fromkeys(keys_list)
    print(dict_from_key_list)

    # в отдельный словарь заносим ключи+значения для ключей ['name', 'gender', 'address']
    new_list_of_dicts_usr = []
    # for row in list_of_dicts_users:
    #     for key, value in row.items():
    #         if key in keys_list:
    #             #print(key,value)
    #             dict_from_key_list[key] = value
    #     print(dict_from_key_list)

    for row in list_of_dicts_users:
        for key, value in row.items():
            if key in keys_list:
                #print(key,value)
                item = key, value
                #print(item)
                new_list_of_dicts_usr.append(item)
    print(new_list_of_dicts_usr)




        #new_list_of_dicts_usr.append(dict_from_key_list)
    #print(new_list_of_dicts_usr) #!!! НЕ РАБОТАЕТ ((((

    # дописываем по ключу 'books' каждому пользователю по книге
    #print(new_list_of_dicts_usr[0])

    # for i in range(len(new_list_of_dicts_usr)):
    #     for row_user in new_list_of_dicts_usr:
    #         for row_book in books:
    #             row_user.update({"books": row_book})
    #
    # print(new_list_of_dicts_usr)



    #print(dict(zip(keys_list[0:-1], new_dict_user_data)))

    #print(dict(zip(keys_list[0:-1], new_dict_user_data)))


    # new_dict = []
    # for key,value in users.items():
    #     #print(user['name'], user['gender'], user['address'])
    #     new_dict.append(key)
    # print(new_dict)


    # users_template = users
    # books_template = books

    # to_json = {"users": users_template}

    # with open(result_file, "w") as f:
    #     f.write(json.dumps(to_json))



csv_file="books.csv"
json_file = "users.json"
file_example_format = "example.json"
result_file = "result.json"

#read_from_json_to_dict(json_file)
write_to_json_file(csv_file, json_file, file_example_format)

# with open(result_file, 'r') as f:
#     rr = json.loads(f.read())
#     print(rr["users"][0])










