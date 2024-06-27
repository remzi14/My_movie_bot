from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from model.models import chanel




def forced_chanel():
    chanels=chanel.get_datas()
    btn=InlineKeyboardMarkup(row_width=2)
    for i,v in enumerate(chanels):
        btn.add(InlineKeyboardButton(f"{int(i)+1}- kanal",url=f"{v['username']}"))
        return




