import vk_api
import time
from random import randint
conv = 1
conv2 = 1
conv = 2000000000 + conv
conv2 = 2000000000 + conv2
id_to_duel = "id0"
vk = vk_api.VkApi(token="First account")
vk2 = vk_api.VkApi(token="Second account")
while True:
    vk.method("messages.send",{"peer_id":conv,"random_id":randint(0,1000),"message":"@toadbot Завершить работу"})
    time.sleep(5)
    vk2.method("messages.send",{"peer_id":conv2,"random_id":randint(0,1000),"message":"@toadbot Завершить работу"})
    time.sleep(5)
    vk.method("messages.send",{"peer_id":conv,"random_id":randint(0,1000),"message":"Дуэль "+id_to_duel})
    time.sleep(5)
    vk2.method("messages.send",{"peer_id":conv2,"random_id":randint(0,1000),"message":"Дуэль принять"})
    time.sleep(5)
    vk.method("messages.send",{"peer_id":conv,"random_id":randint(0,1000),"message":"Дуэль старт"})
    time.sleep(30)
    vk.method("messages.send",{"peer_id":conv,"random_id":randint(0,1000),"message":"Покормить жабу"})
    time.sleep(5)
    vk2.method("messages.send",{"peer_id":conv2,"random_id":randint(0,1000),"message":"Покормить жабу"})
    time.sleep(5)
    vk.method("messages.send",{"peer_id":conv,"random_id":randint(0,1000),"message":"Дуэль "+ id_to_duel})
    time.sleep(5)
    vk2.method("messages.send",{"peer_id":conv2,"random_id":randint(0,1000),"message":"Дуэль принять"})
    time.sleep(5)
    vk.method("messages.send",{"peer_id":conv,"random_id":randint(0,1000),"message":"Дуэль старт"})
    time.sleep(30)
    vk.method("messages.send", {"peer_id": conv, "random_id": randint(0, 1000), "message": "реанимировать жабу"})
    time.sleep(5)
    vk2.method("messages.send", {"peer_id": conv2, "random_id": randint(0, 1000), "message": "реанимировать жабу"})
    time.sleep(5)
    vk.method("messages.send", {"peer_id": conv, "random_id": randint(0, 1000), "message": "Дуэль " + id_to_duel})
    time.sleep(5)
    vk2.method("messages.send", {"peer_id": conv2, "random_id": randint(0, 1000), "message": "Дуэль принять"})
    time.sleep(5)
    vk.method("messages.send", {"peer_id": conv, "random_id": randint(0, 1000), "message": "Дуэль старт"})
    time.sleep(30)
    vk.method("messages.send",{"peer_id":conv,"random_id":randint(0,1000),"message":"@toadbot Работа крупье"})
    time.sleep(5)
    vk2.method("messages.send",{"peer_id":conv2,"random_id":randint(0,1000),"message":"@toadbot Работа крупье"})
    time.sleep(5)
    vk.method("messages.send",{"peer_id":conv,"random_id":randint(0,1000),"message":"@toadbot Поход в столовую"})
    time.sleep(5)
    vk2.method("messages.send",{"peer_id":conv2,"random_id":randint(0,1000),"message":"@toadbot Поход в столовую"})
    time.sleep(2*60*59)
