from aiogram import Bot,Dispatcher,types,executor
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from buttons.inline_keyboards import forced_chanel
from db.connect import startup_table
from model.models import create_user,get_users,delet_user,statika_user,delete_movie,create_movie,created_chanel,delet_chenel,satistika_movie,statistika_chanel,get_movie,get_user,get_chanel,get_chanels
from aiogram.dispatcher.filters import Text
from buttons.reply_keyboard import admin_btn, movie_btn,chanel_btn,exist_btn
from states.states import AddKino, DeletChannelState, DeletMovieState, AddChanelState, ReklamaState
from aiogram.dispatcher.filters.state import StatesGroup,State
from aiogram.dispatcher import FSMContext
# loglar uchun


# Admin uchun
ADMIN=[5789205002]


# Bot token

API_TOKEN="6822306738:AAHIJedS4BeJGfrhSeuTS5ZxiFNHUWQJvuA"

bot=Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)






@dp.message_handler(commands="start")
async def start_menyu(message:types.Message):
    telegram_id=message.from_user.id
    create_user(telegram_id)

    user=message.from_user.first_name
    text=f" Assalomu aleykum {user} \n"
    text+=f" Kodli kino botga xush kelibsiz \n"
    text+=f" Iltimos botga kino kodlarini yuborind \n"
    await message.answer(text)






@dp.message_handler(commands="user")
async def user_get(message:types.Message):
    if str(message.from_user.id==str(ADMIN[0])):
        users=get_users()
        await message.answer(users)

    else:
        await message.answer("Siz admin emasiz")




@dp.message_handler(commands='statistika')
async def statistic(message:types.Message):
    if str(message.from_user.id)==str(ADMIN[0]):
        statis=statika_user()
        await message.answer(statis)
    else:
        await message.answer("Bu komanda faqat adminlar uchun")






@dp.message_handler(comands='admin')
async def admin_funksion(message:types.Message):
    try:
        if str(message.from_user.id)==str(ADMIN[0]):
            await message.answer("Assalomu aleykum xush kelibsiz \n"
                                 f"Admin sahifasiga\n",reply_markup=admin_btn())
        else:
            await message.answer("Siz admin emassiz")
    except Exception as e:
        await message.answer(f"{e}")



@dp.message_handler(Text("Kino o'chirish 🗑"))
async def handle_delete_media_func(msg: types.Message):
    if msg.from_user.id == int(ADMIN[0]):
        await DeletMovieState.post_id.set()
        await msg.answer("Kinoni Kodini yuborishingiz mumkin 🎬", reply_markup=exist_btn())
    else:
        await msg.answer("Siz admin emassiz ❌", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=DeletMovieState.post_id)
async def handle_delete_media(msg: types.Message, state: FSMContext):
    try:
        if msg.text == "❌":
            await msg.answer("Kino o'chirish bekor qilindi ❌", reply_markup=movie_btn())
            await state.finish()
        else:
            data = delete_movie(int(msg.text))
            await msg.reply(text=data, reply_markup=movie_btn())
            await state.finish()
    except:
        await msg.answer("Iltimos Kod sifatida Raqam yuboring!", reply_markup=exist_btn())


@dp.message_handler(Text("Kanallar 🖇"))
async def channels_handler(msg: types.Message):
    if msg.from_user.id == int(ADMIN[0]):
        await msg.answer(text=get_chanel(), reply_markup=chanel_btn())
    else:
        await msg.answer("Siz admin emassiz ❌", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(Text("Kanal qo'shish ⚙️"))
async def add_channel_handler(msg: types.Message):
    if msg.from_user.id == int(ADMIN[0]):
        await AddChanelState.username.set()
        await msg.answer(text="Qo'shish kerak bo'lgan kanal Usernameni kiriting ✍️", reply_markup=exist_btn())
    else:
        await msg.answer("Siz admin emassiz ❌", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=AddChanelState.username)
async def add_channel_username_handler(msg: types.Message, state: FSMContext):
    try:
        if msg.text == "❌":
            await msg.answer("Kanal qo'shish bekor qilindi ❌", reply_markup=chanel_btn())
            await state.finish()
        else:
            async with state.proxy() as data:
                data['username'] = msg.text
            await AddChanelState.channel_id.set()
            await msg.answer(text="Iltimos Kanal ID kiriting: ", reply_markup=exist_btn())
    except Exception as e:
        pass


@dp.message_handler(state=AddChanelState.channel_id)
async def add_channel_handler_func(msg: types.Message, state: FSMContext):
    if msg.text == "❌":
        await msg.answer("Kanal qo'shish bekor qilindi ❌", reply_markup=chanel_btn())
        await state.finish()
    else:
        async with state.proxy() as data:
            data = created_chanel(data['username'], msg.text)
        if data:
            await msg.answer("Kanal muvaffaqiyatli qo'shildi ✅", reply_markup=chanel_btn())
            await state.finish()
        else:
            await msg.answer("Bu kanal oldin qo'shilgan ❌", reply_markup=chanel_btn())
            await state.finish()


@dp.message_handler(Text("Kanal o'chirish 🗑"))
async def movie_delete_handler(msg: types.Message):
    if msg.from_user.id == int(ADMIN[0]):
        await DeletChannelState.username.set()
        await msg.answer(text="O'chirish kerak bo'lgan kanal ID kiriting ✍️", reply_markup=exist_btn())
    else:
        await msg.answer("Siz admin emassiz ❌", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=.username)
async def delete_channel_handler_func(msg: types.Message, state: FSMContext):
    if msg.text == "❌":
        await msg.answer("Kanal o'chirish bekor qilindi ❌", reply_markup=chanel_btn())
        await state.finish()
    else:
        data = delet_chenel(msg.text)
        if data:
            await msg.answer("Kanal muvaffaqiyatli o'chirildi ✅", reply_markup=chanel_btn())
        else:
            await msg.answer("Bunday ID uchun kanal mavjud emas ❌", reply_markup=chanel_btn())
        await state.finish()




@dp.message_handler(Text("Reklama 🎁"))
async def reklama_handler(msg: types.Message):
    if msg.from_user.id == int(ADMIN[0]):
        await ReklamaState.rek.set()
        await bot.send_message(chat_id=msg.chat.id, text="Reklama tarqatish bo'limi 🤖", reply_markup=exist_btn())
    else:
        await bot.send_message(chat_id=msg.chat.id, text="Siz admin emassiz ❌", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=ReklamaState.rek, content_types=types.ContentType.ANY)
async def rek_state(msg: types.Message, state: FSMContext):
    if msg.text == "❌":
        await bot.send_message(chat_id=msg.chat.id, text="Reklama yuborish bekor qilindi 🤖❌", reply_markup=admin_btn())
        await state.finish()
    else:
        await bot.send_message(chat_id=msg.chat.id, text="Reklama yuborish boshlandi 🤖✅", reply_markup=admin_btn())
        await state.finish()
        try:
            summa = 0
            for user in get_users():
                if int(user['telegram_id']) != int(ADMIN):
                    try:
                        await msg.copy_to(int(user['telegram_id']), caption=msg.caption, caption_entities=msg.caption_entities, reply_markup=msg.reply_markup)
                    except Exception as e:
                        print(f"Send Error: {e}")
                        summa += 1
            await bot.send_message(int(ADMIN), text=f"Botni bloklagan Userlar soni: {summa}")
        except Exception as e:
            print(f"Error: {e}")


@dp.callback_query_handler(lambda x: x.data == "channel_check")
async def channel_check_handler(callback: types.CallbackQuery):
    check = await check_sub_channels(callback.from_user.id)
    if check:
        await callback.message.delete()
        await callback.answer("Obuna bo'lganingiz uchun rahmat ☺️")
    else:
        await callback.message.answer("Iltimos quidagi kanallarga obuna bo'ling", reply_markup=forced_chanel())


@dp.message_handler(Text("❌"))
async def exit_handler(msg: types.Message):
    if msg.from_user.id == int(ADMIN):
        await msg.answer("Bosh menyu 🔮", reply_markup=admin_btn())


@dp.message_handler(lambda x: x.text.isdigit())
async def forward_last_video(msg: types.Message):
    check = await check_sub_channels(int(msg.from_user.id))
    if check:
        data = get_movie(int(msg.text))
        if data:
            try:
                await bot.send_video(chat_id=msg.from_user.id, video=data[0], caption=f"{data[1]}\n\n🤖 Bizning bot: @Tarjimalar_Tv_bot")
            except:
                await msg.reply(f"{msg.text} - id bilan hech qanday kino topilmadi ❌")
        else:
            await msg.reply(f"{msg.text} - id bilan hech qanday kino topilmadi ❌")
    else:
        await msg.answer("Iltimos quidagi kanallarga obuna bo'ling", reply_markup=forced_chanel())


async def check_sub_channels(user_id):
    channels = get_users()
    for channel in channels:
        try:
            chat_member = await bot.get_chat_member(chat_id=channel[2], user_id=user_id)
            if chat_member['status'] == 'left':
                return False
        except:
            await bot.send_message(ADMIN, f"{channel[1]}\nBu kanal mavjud emas yoki Botning kanalga adminlik huquqi yo'q!")
    return True








# @dp.message_handler(commands="info",chat_id=ADMIN[0])
# async def info_users(message:types.Message):
#     text=f"<b> Hamma Foydalanuvchilardan Malumotlarni </b> \n\n"
#     users=get_users()
#     for user in users:
#         text+=f"<b>Telegram ID</b>: {user[1]}\n"
#     await message.answer(text)






#Foydalanuvchiga Reklama Yuboruvchi handler
# class ReklamaState(StatesGroup):
#     reklamacontent=State()
#
# @dp.message_handler(commands='reklama',chat_id=ADMIN[0])
# async def send_reklama(message:types.Message):
#     await message.answer("Reklama Yuborish uchun matn yoki Faylni yuboring")
#     await ReklamaState.reklamacontent.set()




# @dp.message_handler(content_types=[types.ContentType.ANY],state=ReklamaState.reklamacontent)
# async def send_reklama_content(message:types.Message,state:FSMContext):
#     content_type=message.content_type
#     await state.finish()
#     users=get_users()
#     if content_type==types.ContentType.TEXT:
#         text=message.text
#         for user in users:
#             try:
#                 await bot.send_message(chat_id=user[1],text=text)
#             except Exception as e:
#                 await bot.send_message(chat_id=ADMIN[0],text=f"Matnni foydalanuvchga yuborishda qandeydir xatolik bor {e}")
#
#     elif content_type==types.ContentType.PHOTO:
#         photo=message.photo[-1]
#         text=message.caption
#         for user in users:
#             try:
#                 await bot.send_photo(chat_id=user[1],photo=photo.file_id,caption=text)
#             except Exception as e:
#                 await bot.send_message(chat_id=ADMIN[0],text=f"Rasmni foydalanuvchga yuborishda qandeydir xatolik bor {e}")
#
#     elif content_type==types.ContentType.VIDEO:
#         video=message.video
#         text=message.caption
#         for user in users:
#             try:
#                 await bot.send_video(chat_id=user[1],video=video.file_id,caption=text)
#             except Exception as e:
#                 await bot.send_message(chat_id=ADMIN[0],text=f'Videoni foydalanuvchga yuborishda qandeydir xatolik bor {e}')









async def start(dp):
    startup_table()





if __name__=='__main__':
    executor.start_polling(dp,on_startup=start,skip_updates=True)

