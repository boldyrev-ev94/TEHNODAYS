
import openpyxl
import json
import os
from datetime import datetime
from openpyxl.cell import cell

CATEGOR_PROPERTY = [
    ("SMS-T", "value", "main_zone"),
    ("Карандаш кассета", "time_down", "main_zone"),
    ("Домашний телефон", "time_down", "main_zone"),
    ("Словарь без инета", "time_down", "main_zone"),
    ("Старый комп VS Новый", "value", "main_zone"),
    ("Железный конструктор", "time_down", "main_zone"),
    ("Перо VS ручка VS Граф.планшет", "time_down", "main_zone"),
    ("Перемотать ДВД", "time_down", "main_zone"),
    ("За рулём", "time_up", "main_zone"),
    ("НТО", "time_down", "main_zone"),
    ("Гонки", "time_down", "cyber_zone"),
    ("Пакман", "value", "cyber_zone"),
    ("Fruit ninja", "value", "cyber_zone"),
    ("Тетрис", "value", "cyber_zone")
]


CATEGORY = [
    {"rank": 1, "name": "SMS-T", "category": "рекорд",
        "score": 0, "user_name": ""},
    {"rank": 2, "name": "Карандаш кассета",
        "category": "время (наименьшее)", "score": 0, "user_name": ""},
    {"rank": 3, "name": "Домашний телефон",
        "category": "время (наименьшее)", "score": 0, "user_name": ""},
    {"rank": 4, "name": "Словарь без инета",
        "category": "время (наименьшее)", "score": 0, "user_name": ""},
    {"rank": 5, "name": "Старый комп VS Новый",
        "category": "рекорд", "score": 0, "user_name": ""},
    {"rank": 6, "name": "Железный конструктор",
        "category": "время (наименьшее)", "score": 0, "user_name": ""},
    {"rank": 7, "name": "Перо VS ручка VS Граф.планшет",
        "category": "время (наименьшее)", "score": 0, "user_name": ""},
    {"rank": 8, "name": "Перемотать ДВД",
        "category": "время (наименьшее)", "score": 0, "user_name": ""},
    {"rank": 9, "name": "За рулём",
        "category": "время (наибольшее)", "score": 0, "user_name": ""},
    {"rank": 10, "name": "НТО",
        "category": "время (наименьшее)", "score": 0, "user_name": ""},
]

def excel_to_json(excel_file, json_file):
    try:
        # Проверяем существование файла
        if not os.path.exists(excel_file):
            raise FileNotFoundError(f"Файл {excel_file} не найден")

        # Открываем Excel файл
        wb = openpyxl.load_workbook(excel_file, data_only=True)
        
        # Получаем активный лист
        sheet = wb.active
        
        # Создаем список для хранения данных
        data = []
        
        # Получаем заголовки столбцов
        headers = [cell.value for cell in sheet[1]]
        
        # Функция для преобразования значений
        def convert_value(value):
            if isinstance(value, datetime):
                return value.strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(value, cell.Cell):
                return value.value
            return value

        # Проходим по строкам начиная со второй (пропускаем заголовки)
        for row in sheet.iter_rows(min_row=2, values_only=True):
            # Проверяем, не пустая ли строка
            if all(value is None for value in row):
                continue  # Пропускаем пустую строку
                
            # Создаем словарь для каждой строки
            row_data = {}
            for i, value in enumerate(row):
                # Преобразуем значение перед добавлением
                converted_value = convert_value(value)
                row_data[headers[i]] = converted_value
            
            # Добавляем только непустые строки
            if any(row_data.values()):
                data.append(row_data)
        
        # Сохраняем данные в JSON файл
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4, default=str)
        
        print(f"Данные успешно сохранены в {json_file}")
        
    except FileNotFoundError as fnf_error:
        print(f"Ошибка: {fnf_error}")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")



def categoryes(json_file, json_category):
    try:
        res = []
        with open(json_file, 'r', encoding='utf-8') as f:
            print("start open")
            # print(json.dumps(f, ensure_ascii=False, indent=2))
            for categ in CATEGOR_PROPERTY:
                # list_categories = []
                # for item in f:
                #     cate = {
                #         "name": f"{f['Фамилия']} {f['Имя']}",
                #         "id": f["Код учатника"],
                #         "value": f[categ[0]]                        
                #     }
                #     list_categories.append(cate)
                print(categ)
            res.append(list_categories)
        print(res)
            
        
    except FileNotFoundError as fnf_error:
        print(f"Ошибка: {fnf_error}")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        
        
    
        
# Пример использования
if __name__ == "__main__":
    # Укажите правильный путь к вашему файлу
    excel_file = r'C://Users//Ev-gen//Documents//TEHNODAYS//excel//input.xlsx'  # Укажите путь к вашему Excel файлу
    json_file = r'C://Users//Ev-gen//Documents//TEHNODAYS//excel//output.json'  # Укажите путь для сохранения JSON файла
    
    # Проверяем текущий рабочий каталог
    print(f"Текущий рабочий каталог: {os.getcwd()}")
    
    excel_to_json(excel_file, json_file)
    categoryes(json_file, "")

