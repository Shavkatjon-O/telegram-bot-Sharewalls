from aiogram.fsm.state import StatesGroup, State


class UploadStates(StatesGroup):
    UPLOAD_IMAGE = State()
    CONFIRMATION = State()
    FINISH = State()
