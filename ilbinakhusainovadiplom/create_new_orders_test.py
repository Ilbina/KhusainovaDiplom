import sender_stand_request
import data

# Функция для получения номера трека
def get_order_track_number():
    order_response = sender_stand_request.post_new_order(data.order_body)
    order_track = order_response.json().get('track')
    data.order_track = order_track  # Сохраняем номер трека в переменной из файла data
    return data.order_track
    print(order_response.status_code)
    print(order_response.json())

# Функция для теста
def test_get_about_order_on_track():
    order_track = get_order_track_number()
    get_order_response = sender_stand_request.get_about_order(order_track)
    print(get_order_response.status_code)
    print(get_order_response.json())

    assert get_order_response.status_code == 200

# Ильбина Хусаинова, 10-я когорта — Финальный проект. Инженер по тестированию плюс
test_get_about_order_on_track()