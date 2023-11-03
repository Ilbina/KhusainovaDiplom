import requests
import configuration
import data

# функция создания заказа с получением трека
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,
                             json=body,
                             headers=data.headers)


response = post_new_order(data.order_body)
order_track = response.json().get('track')
data.order_track = order_track  # Сохраняем номер трека в переменной из файла data
print(order_track)
print(response.status_code)
print(response.json())

# функция получения информации о заказе по его треку
def get_about_order(order_track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_TRACK_PATH,
                            params={"t": order_track}, headers=data.headers)

# Получаем информацию о заказе по его треку
response = get_about_order(data.order_track)
print(response.status_code)
print(response.json())