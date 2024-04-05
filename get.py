import requests  # Импорт модуля для отправки HTTP-запросов
import json  # Импорт модуля для работы с JSON

def get_organization_ids_by_inn(inn):
    # URL-адрес для отправки POST-запроса для получения списка организаций по ИНН
    url = 'https://reestr.nopriz.ru/api/sro/all/member/list'
    
    # Заголовки запроса, указывающие тип содержимого
    headers = {
        'Content-Type': 'application/json',
    }
    
    # Параметры запроса, включая ИНН
    payload = {
        "searchString": inn
    }
    
    # Отправка POST-запроса с заголовками и параметрами
    response = requests.post(url, headers=headers, json=payload)
    
    # Получение JSON-ответа от сервера
    json_response = response.json()
    
    # Извлечение идентификаторов организаций из JSON-ответа
    organization_ids = [data['id'] for data in json_response['data']['data']]
    
    return organization_ids

def get_organization_info_by_id(organization_id):
    # Формирование URL-адреса для запроса информации об организации по ее ID
    url = f'https://reestr.nopriz.ru/api/member/{organization_id}/info'
    
    # Отправка POST-запроса для получения информации об организации
    response = requests.post(url)
    
    # Получение JSON-ответа от сервера
    return response.json()

def save_organization_info_as_json(inn, organization_id, organization_info):
    # Формирование имени файла для сохранения информации об организации
    file_name = f'{inn}_{organization_id}.json'
    
    # Сохранение информации об организации в файл в формате JSON
    with open(file_name, 'w') as file:
        json.dump(organization_info, file, indent=4, ensure_ascii=False)
    
    # Вывод сообщения о сохранении информации в файл (номер ИНН_id организации.json)
    print(f'Информация об организации с ИНН {inn} и ID {organization_id} сохранена в файл {file_name}')

# Вводим нужный ИНН
inn = "7202112366" # Пример ИНН с 3 организациями

inn = "6672244390" # Пример ИНН с 1 организацией

# Получение id организаций по ИНН
organization_ids = get_organization_ids_by_inn(inn)
print('ID найденных организаций по ИНН', inn, ':', organization_ids)

# Получение информации о каждой организации и сохранение в файл
for organization_id in organization_ids:
    organization_info = get_organization_info_by_id(organization_id)
    save_organization_info_as_json(inn, organization_id, organization_info)
