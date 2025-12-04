# convertor2

Конвертер валют Консольное приложение для конвертации валют с использованием ExchangeRate-API.

Установка

pip install requests python-dotenv

Использование

Конвертация по умолчанию (100 RUB → USD)
python currency_converter.py

Конвертация с параметрами
python currency_converter.py -b EUR -t GBP -a 50 Параметры: -b, --base - базовая валюта (по умолчанию: RUB)

-t, --target - целевая валюта (по умолчанию: USD)

-a, --amount - сумма (по умолчанию: 1.0)

--api-key - API ключ
