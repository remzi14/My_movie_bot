from aiogram.dispatcher.filters.state import State,StatesGroup




class ReklamaState(StatesGroup):
    rek=State()





class AddKino(StatesGroup):
    media=State()
    media_id=State()





class AddChanelState(StatesGroup):
    username=State()
    channel_id=State()




class DeletChannelState(StatesGroup):
    username=State()



class DeletMovieState(StatesGroup):
    post_id=State()





