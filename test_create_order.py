import requests

# URL 
BASE_URL = "https://4365f57f-77fe-46d9-9d1b-66becc3a730d.serverhub.praktikum-services.ru/"

def test_create_order_and_get_by_track():
    # --- Шаг 1: Выполнить запрос на создание заказа ---
    payload = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK"]
    }
    
    # Отправляем POST-запрос на создание заказа
    response_create = requests.post(f"{BASE_URL}/api/v1/orders", json=payload)
    
    # Проверяем, что заказ создан (код 201)
    assert response_create.status_code == 201, f"Ошибка создания заказа: {response_create.status_code}"
    
    # --- Шаг 2: Сохранить номер трека заказа ---
    track_number = response_create.json().get("track")
    assert track_number is not None, "В ответе нет трека заказа"
    print(f"\nСоздан заказ с треком: {track_number}")

    # --- Шаг 3: Выполнить запрос на получение заказа по треку ---
    params = {"t": track_number}
    response_get = requests.get(f"{BASE_URL}/api/v1/orders/track", params=params)

    # --- Шаг 4: Проверить, что код ответа равен 200 ---
    assert response_get.status_code == 200, f"Ошибка получения заказа: {response_get.status_code}"
    print(f"Заказ успешно получен по треку {track_number}")