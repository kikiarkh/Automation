from smartphone import Smartphone

catalog = []

phone1 = Smartphone('Apple', '15 pro max', '+79600981002')
phone2 = Smartphone('Samsung', 'Galaxy s23', '+79994587788')
phone3 = Smartphone('Xiaomi', 'Mi 11', '+79857885544')
phone4 = Smartphone('Apple', 'S8', '+79069942299')
phone5 = Smartphone('Samsung', 'A54', '+79062227766')

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone4)

for phone in catalog:
    print(f'<{phone.mark}> - <{phone.model}>. {phone.number}')
