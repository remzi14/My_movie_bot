from model.orm import MediaClass,ChannelClass,Base


user=Base("users")
movie=MediaClass("movies")
chanel=ChannelClass("channel")



#foydalanuvchini qo'shish uchun funkisiya

def create_user(telegram_id:int):
    data=user.get_data(telegram_id)
    if not data:
        user.create_data(telegram_id=str(telegram_id))
        return True
    else:
        return False



def delet_user(telegram_id:int):
    data=user.delet_data(telegram_id)
    if not data:
        user.delet_data(telegram_id=str(telegram_id))
        return True
    else:
        return False




def get_users():
    return user.get_datas()




#filim qo'shish



def create_movie(post_id:str):
    data=movie.get_data(post_id)
    if not data:
        movie.create_data(post_id=str(post_id))
        return True
    else:
        return False


def get_user():
    return movie.get_data()






# channel yaratish



def create_chanel(chanel_id:str):
    data=chanel.create_data(chanel_id)
    if not data:
        chanel.create_data(chanel_id=str(chanel_id))
        return True
    else:
        return False


def get_chanel():
    return movie.get_data()




def statika_user():
    data=user.statistica()
    all_data=user.get_datas()
    if data:
        return (f"Adminlar uchun userlar statikasi \n\n"
                f"Oxirgi 30 kun ichida ro'yxatdan o'tgan userlar soni {len(data['month'])} ta \n"
                f"Oxirgi yetti kun ichida ro'yxatdan o'tgnlar soni {len(data['week'])} ta \n"
                f"Oxirgi 24 soat ichida botga qo'shilgan userlar soni {len(data['day'])} ta \n"
                f" Barcha foydalanuvchilar soni {len(all_data)} ta")
    else:
        return False





# movie uchun models

def created_movie(post_id:int,file_id:str,caption:str):
    data=movie.get_movie(file_id)
    if not data:
        movie.create_data(post_id,file_id,caption)
        return post_id
    else:
        return data.get('post_id',None)


def get_movie(post_id:int):
    data=movie.get_data(post_id)
    if data:
        return [data['file_id']],[data['caption']]

    else:
        return False


def delete_movie(post_id:int):
    data=movie.get_data(post_id=post_id)
    if data:
        try:
            movie.delete_movie(post_id=post_id)
            return f"Kino yaxshi o'chirildi "
        except:
            return f"Kino o'chirishda xatolik yuz berdi"
        else:
            return f"{post_id} - Id bilan kino topilmadi"


def satistika_movie():
    data=movie.statistica()
    all_data=movie.get_datas()
    if data:
        return (f"Adminlar uchun kinolar statikasi \n\n"
                f"Oxirgi 30 kun ichida qo'shilgan kinolar  soni {len(data['month'])} ta \n"
                f"Oxirgi 7 kun ichida o'shilgan kinolar  soni {len(data['week'])} ta \n"
                f"Oxirgi 24 soat o'shilgan kinolar  soni {len(data['day'])} ta \n"
                f" Barcha kinolar soni {len(all_data)} ta")
    else:
        return False





# chanel uchun models


def created_chanel(chanel_id:str):
    data=chanel.get_data(chanel_id)
    if not data:
        chanel.create_data(chanel_id)
        return chanel_id
    else:
        return data.get('chanel_id',None)



def get_chanels(chanel_id:str):
    data=chanel.get_data(chanel_id)
    if data:
        return [data['chanel_id']]

    else:
        return False




def delet_chenel(chanel_id:str):
    data=chanel.get_data(chanel_id=chanel_id)
    if data:
        try:
            chanel.delet_data(chanel_id=chanel_id)
            return f"Kanal yaxshi o'chirildi "
        except:
            return f"kanal o'chirishda xatolik yuz berdi"
        else:
            return f" {chanel_id} - Id bilan kanl topilmadi"






def statistika_chanel():
    data=chanel.statistica()
    all_data=chanel.get_data()
    if data:
        return (f"Adminlar uchun kanallar statikasi \n\n"
                f"Oxirgi 30 kun ichida qo'shilgan kanallar soni {len(data['month'])} ta \n"
                f"Oxirgi 7 kun ichida o'shilgan kanallar soni {len(data['week'])} ta \n"
                f"Oxirgi 24 soat ichida o'shilgan kanallar soni {len(data['day'])} ta \n"
                f" Barcha kanallar soni {len(all_data)} ta")
    else:
        return False

