
import openpyxl
import json
import os
from datetime import datetime
from openpyxl.cell import cell

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
        
        
# Пример использования
if __name__ == "__main__":
    # Укажите правильный путь к вашему файлу
    excel_file = r'C://Users//Ev-gen//Documents//TEHNODAYS//excel//input.xlsx'  # Укажите путь к вашему Excel файлу
    json_file = r'C://Users//Ev-gen//Documents//TEHNODAYS//excel//output.json'  # Укажите путь для сохранения JSON файла
    
    # Проверяем текущий рабочий каталог
    print(f"Текущий рабочий каталог: {os.getcwd()}")
    
    excel_to_json(excel_file, json_file)

