from aiogram.types import ReplyKeyboardMarkup,KeyboardButton





def admin_btn():
    btn=ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True,row_width=3)
    statistika=KeyboardButton('statistika')
    movie=KeyboardButton('Kinolar')
    reklama=KeyboardButton('Reklama')
    add_chanel=KeyboardButton(" Kanallar")
    return btn.add(statistika,movie,reklama,add_chanel)




def movie_btn():
    btn=ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True,row_width=2)
    statistika=KeyboardButton("Kino statistikasi")
    addmovie=KeyboardButton("Kino Qo'shish ")
    delmovie=KeyboardButton("Kino O'shirish ")
    exist_btn=KeyboardButton("Chiqish")
    return btn.add(statistika,addmovie,delmovie,exist_btn)



def chanel_btn():
    btn=ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True,row_width=2)
    statistika=KeyboardButton("Kanallar statistikasi")
    addchanel=KeyboardButton("Kanal Qo'shish ")
    delchanel=KeyboardButton("Kanal O'shirish ")
    exist_btn=KeyboardButton("Chiqish")
    return btn.add(statistika,addchanel,delchanel,exist_btn)


def exist_btn():
    btn=ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True,row_width=2)
    return btn.add("Chiqish")






