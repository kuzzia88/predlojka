from aiogram import Bot, types, F
from aiogram.fsm.state import State, StatesGroup
import random
from cfg import CHAT_ID
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class UserStates(StatesGroup):
    waiting_for_message = State()

class Anon:
    def __init__(self, bot: Bot):
        self.bot = bot
    async def start(self, message: types.Message):
        lst = ['Халло', 'Дароу', 'Ку', 'Привет']
        if message.from_user.username != None:
            await message.answer(f'{random.choice(lst)}, {message.from_user.username}, ты можешь мне отправить любое сообщение, я его передам')
        else: 
            await message.answer(f'{random.choice(lst)}, {message.from_user.first_name}, ты можешь мне отправить любое сообщение, я его передам')
    async def data(id, username, Fname):
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=f"🆔 {id}", callback_data=f"copy_{id}"),
                    InlineKeyboardButton(text=f"👤 {username}", callback_data=f"copy_{username}")
                ],
                [
                    InlineKeyboardButton(text=f"🤵 {Fname}", callback_data=f"copy_{Fname}")
                ]
                ]
        )
        return keyboard
    async def text_handler(self, message):
        kb = await Anon.data(message.from_user.id, message.from_user.username, message.from_user.first_name)
        await self.bot.send_message(chat_id=CHAT_ID, text=message.text, reply_markup=kb)
    async def photo_handler(self, message):
        kb = await Anon.data(message.from_user.id, message.from_user.username, message.from_user.first_name)
        photo = message.photo[-1]
        await self.bot.send_photo(chat_id=CHAT_ID, photo=photo.file_id, reply_markup=kb)
    async def sticker_handler(self, message):
        kb = await Anon.data(message.from_user.id, message.from_user.username, message.from_user.first_name)
        await self.bot.send_sticker(chat_id=CHAT_ID, sticker=message.sticker.file_id, reply_markup=kb)
    async def video_handler(self, message):
        video = message.video
        kb = await Anon.data(message.from_user.id, message.from_user.username, message.from_user.first_name)
        await self.bot.send_video(chat_id=CHAT_ID, video=video.file_id, reply_markup=kb)
    async def audio_handler(self, message):
        audio = message.audio
        kb = await Anon.data(message.from_user.id, message.from_user.username, message.from_user.first_name)
        await self.bot.send_audio(chat_id=CHAT_ID, audio=audio.file_id, reply_markup=kb)
    async def voice_handler(self, message):
        voice = message.voice
        kb = await Anon.data(message.from_user.id, message.from_user.username, message.from_user.first_name)
        await self.bot.send_voice(chat_id=CHAT_ID, voice=voice.file_id, reply_markup=kb)
    async def animation_handler(self, message):
        animation = message.animation
        kb = await Anon.data(message.from_user.id, message.from_user.username, message.from_user.first_name)
        await self.bot.send_animation(chat_id=CHAT_ID, animation=animation.file_id, reply_markup=kb)
    async def document_handler(self, message):
        document = message.document
        kb = await Anon.data(message.from_user.id, message.from_user.username, message.from_user.first_name)
        await self.bot.send_document(chat_id=CHAT_ID, document=document.file_id, reply_markup=kb)
    async def contact_handler(self, message):
        contact = message.contact
        kb = await Anon.data(message.from_user.id, message.from_user.username, message.from_user.first_name)
        await self.bot.send_contact(chat_id=CHAT_ID, phone_number=contact.phone_number, first_name=contact.first_name, reply_markup=kb)
    async def video_note_handler(self, message):
        video_note = message.video_note
        kb = await Anon.data(message.from_user.id, message.from_user.username, message.from_user.first_name)
        await self.bot.send_video_note(chat_id=CHAT_ID, video_note=video_note.file_id, reply_markup=kb)