from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import OWNER_ID
from keyboards.main_menu import main_menu


router = Router()


@router.message(CommandStart())
async def start_command(message: Message):

    if message.from_user.id != OWNER_ID:
        await message.answer(
            "🔐 هذا البوت خاص بصاحبه فقط."
        )
        return

    await message.answer(
        """
👑 <b>Maged Atef</b>

━━━━━━━━━━━━━━━━━━

مرحباً بك في مركز التحكم الشخصي.

🎛️ تحكم في حساباتك
📤 انشر المحتوى
📋 إدارة المنشورات
📊 الإحصائيات
📅 الجدولة
🌐 الحسابات المرتبطة

━━━━━━━━━━━━━━━━━━

اختر من القائمة:
        """,
        reply_markup=main_menu(),
        parse_mode="HTML"
    )
