from telegram_bot import send_message
import asyncio
from api import gold_price, euro_price, usd_price
from datetime import datetime
import schedule

async def job():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    message = f"""
    📅 **Data:** `{current_date}`

    💰 **Ceny walut i złota:**
    - 🪙 **Złoto:** `{gold_price} PLN`
    - 💶 **Euro (EUR):** `{euro_price} PLN`
    - 💵 **Dolar (USD):** `{usd_price} PLN`

    📊 *Dane pochodzą z Narodowego Banku Polskiego (NBP).*
    """
    await send_message(message)

def run_job():
    loop = asyncio.get_event_loop()
    loop.create_task(job())

async def main():
    schedule.every().day.at("07:00").do(run_job)

    while True:
        schedule.run_pending()
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
