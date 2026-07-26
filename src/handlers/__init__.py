from aiogram import Router

from src.handlers.chat import router as chat_router

router = Router()

router.include_router(chat_router)
