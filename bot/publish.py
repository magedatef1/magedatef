from pathlib import Path

from aiogram import Router
from aiogram.types import Message

from config import OWNER_ID

from services.media_manager import MEDIA_DIR


router = Router()


@router.message()
async def receive_content(message: Message):

    if not message.from_user:
        return

    if message.from_user.id != OWNER_ID:
        return

    if message.photo:

        photo = message.photo[-1]

        filename = (
            f"{message.chat.id}_"
            f"{message.message_id}.jpg"
        )

        destination = MEDIA_DIR / filename

        await message.bot.download(
            photo,
            destination=destination
        )

        await message.answer(
            """
🖼️ <b>تم استلام الصورة</b>

📦 أصبحت جاهزة للنشر.

اكتب مثلًا:

<code>انشرها على فيسبوك</code>

أو:

<code>انشرها على فيسبوك وإنستغرام</code>
            """,
            parse_mode="HTML"
        )

        return

    if message.video:

        filename = (
            f"{message.chat.id}_"
            f"{message.message_id}.mp4"
        )

        destination = MEDIA_DIR / filename

        await message.bot.download(
            message.video,
            destination=destination
        )

        await message.answer(
            """
🎬 <b>تم استلام الفيديو</b>

📦 أصبح جاهزًا للنشر.

اكتب المنصة التي تريد النشر عليها.
            """,
            parse_mode="HTML"
        )

        return
