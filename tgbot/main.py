import asyncio
import asyncpg
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
#from tgbot.handlers import router
#token="Your token was replaced with a new one. You can use this token to access HTTP API:
token ='7600730617:AAFsVcwR2GI23MnsturSya50ajaF1IT7lb4'
webhook_url = 'https://simple-tg-bot-aiogram.vercel.app'
connection_string = 'postgresql://neondb_owner:npg_rzqOTvaJiP01@ep-frosty-morning-a2z2rgqi-pooler.eu-central-1.aws.neon.tech/neondb?sslmode=require'
router = Router()
@router.message(CommandStart())
async def process_start_command(message: Message):
    pool = await asyncpg.create_pool(connection_string)
    async with pool.acquire() as conn:
    # Execute a statement to create a new table.
        await conn.execute("INSERT INTO users (\"user\") VALUES('" + str(message.from_user.id) + "')")
    await pool.close()
    await message.answer('/start')
class TGBot:
    def __init__(self, router: Router) -> None:
       #token = config('TOKEN')
       self.bot = Bot(token)
       self.dp = Dispatcher()
       self.dp.include_router(router)

    async def send_message(self, message: str):
        pool = await asyncpg.create_pool(connection_string)
        async with pool.acquire() as conn:
            # Execute a statement to create a new table.
            users = await conn.fetch("SELECT \"user\" FROM users")
            print(users)
        await pool.close()
        #await self.bot(
    async def update_bot(self, update: dict) -> None:
        await self.dp.feed_raw_update(self.bot, update)
        await self.bot.session.close()

    async def set_webhook(self):
        #webhook_url = config('WEBHOOK_U
        # WEBHOOK_URL = адрес сайта/api/bot
        await self.bot.set_webhook(webhook_url)
        await self.bot.session.close()

tgbot = TGBot(router)
