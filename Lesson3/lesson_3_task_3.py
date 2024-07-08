from address import Address
from mailing import Mailing

to_address = Address('1234567', 'г. Москва', 'ул. Новый Арбат', 'д.1', 'кв.1')
from_address = Address('456788','г. Йошкар ола', 'ул. Советская', 'д.31', 'кв.2')
mailing = Mailing(to_address, from_address, '1500', '123456789')

print(f'Отправление {mailing.track} из {mailing.from_address.index} {mailing.from_address.city} {mailing.from_address.street} {mailing.from_address.house} {mailing.from_address.flat} в {mailing.to_address.index} {mailing.to_address.city} {mailing.to_address.street} {mailing.to_address.house} {mailing.to_address.flat}. Cтоимость {mailing.cost} рублей.')

