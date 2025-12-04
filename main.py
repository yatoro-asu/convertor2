import requests
from dotenv import load_dotenv
import argparse
import os


def get_convert_amount(api_key, base_rate, target_rate, amount_money):
    try:
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_rate}/{target_rate}/{amount_money}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()['conversion_result']
    except requests.exceptions.HTTPError as e:
        print(f"Ошибка: {e.response.status_code})")


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description="Конвертер валют")
    parser.add_argument("-b", "--base", help="Код базовой валюты (например, RUB)", default="RUB")
    parser.add_argument("-t", "--target", help="Код целевой валюты (например, USD)", default="USD")
    parser.add_argument("-a", "--amount", type=float, help="Сумма денег (числом)", default=1.0)
    parser.add_argument("--api-key", help="API ключ (можно задать через EXCHANGE_API_KEY)", default=None)

    args = parser.parse_args()

    api_key = args.api_key or os.getenv("EXCHANGE_API_KEY")
    if not api_key:
        parser.error("API key not provided. Use --api-key or set EXCHANGE_API_KEY in .env")

    base_rate = args.base.upper()
    target_rate = args.target.upper()
    amount_money = args.amount

    convert_amount = get_convert_amount(api_key, base_rate, target_rate, amount_money)
    if convert_amount:
        print(f"Конвертировання сумма: {convert_amount} {target_rate}")


if __name__ == "__main__":
    main()