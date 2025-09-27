from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from cfg import TOKEN
from utils import Anon
import asyncio

bot = Bot(TOKEN)
dp = Dispatcher()
anon = Anon(bot)

@dp.message(Command("start"))
async def start(message: types.Message):
    await anon.start(message)
    
@dp.message(Command("showmychatid"))
async def showmychatid(message: types.Message):
    await message.answer(f'<code>{str(message.chat.id)}</code>', parse_mode="HTML")
    
@dp.message(F.text)
async def process_name(message: types.Message):
    await anon.text_handler(message)

@dp.message(F.photo)
async def process_name(message: types.Message):
    await anon.photo_handler(message)

@dp.message(F.sticker)
async def process_name(message: types.Message):
    await anon.sticker_handler(message)

@dp.message(F.video)
async def process_name(message: types.Message):
    await anon.video_handler(message)

@dp.message(F.audio)
async def process_name(message: types.Message):
    await anon.audio_handler(message)

@dp.message(F.voice)
async def process_name(message: types.Message):
    await anon.voice_handler(message)
    
@dp.message(F.animation)
async def process_name(message: types.Message):
    await anon.animation_handler(message)

@dp.message(F.document)
async def process_name(message: types.Message):
    await anon.document_handler(message)

@dp.message(F.contact)
async def process_name(message: types.Message):
    await anon.contact_handler(message)

@dp.message(F.video_note)
async def process_name(message: types.Message):
    await anon.video_note_handler(message)

async def main():
    print('[+] The bot has been launched successfully!')
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    asyncio.run(main())