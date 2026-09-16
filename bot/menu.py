from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.main_menu import main_menu, back_button


router = Router()


@router.callback_query(F.data == "home")
async def home(call: CallbackQuery):

    await call.message.edit_text(
        """
👑 <b>Maged Atef</b>

━━━━━━━━━━━━━━━━━━

🎛️ <b>مركز التحكم الشخصي</b>

اختر العملية التي تريد تنفيذها:
        """,
        reply_markup=main_menu(),
        parse_mode="HTML"
    )

    await call.answer()


@router.callback_query(F.data == "publish")
async def publish_menu(call: CallbackQuery):

    await call.message.edit_text(
        """
📤 <b>نشر محتوى</b>

أرسل الآن صورة أو فيديو أو نص.

مثال:

<code>انشر هذه الصورة على فيسبوك</code>

أو:

<code>انشر الفيديو على فيسبوك وإنستغرام</code>
        """,
        reply_markup=back_button(),
        parse_mode="HTML"
    )

    await call.answer()


@router.callback_query(F.data == "accounts")
async def accounts(call: CallbackQuery):

    await call.message.edit_text(
        """
🌐 <b>حساباتي</b>

📘 Facebook
📸 Instagram
🧵 Threads
𝕏 X
🎵 TikTok
👻 Snapchat
▶️ YouTube
🟢 Kwai
🟣 Likee
🦣 Mastodon
🔵 VK

سيتم تفعيل كل منصة من خلال API/OAuth الرسمي.
        """,
        reply_markup=back_button(),
        parse_mode="HTML"
    )

    await call.answer()


@router.callback_query(F.data == "analytics")
async def analytics(call: CallbackQuery):

    await call.message.edit_text(
        """
📊 <b>الإحصائيات</b>

سيتم عرض الإحصائيات الحقيقية
بعد ربط حساباتك بالـ APIs الرسمية.

📈 المشاهدات
❤️ التفاعلات
💬 التعليقات
👥 المتابعون
📊 أداء المنشورات
        """,
        reply_markup=back_button(),
        parse_mode="HTML"
    )

    await call.answer()


@router.callback_query(F.data == "posts")
async def posts(call: CallbackQuery):

    await call.message.edit_text(
        """
📋 <b>منشوراتي</b>

سيتم هنا عرض المنشورات من الحسابات
المرتبطة وإدارتها.
        """,
        reply_markup=back_button(),
        parse_mode="HTML"
    )

    await call.answer()


@router.callback_query(F.data == "schedule")
async def schedule(call: CallbackQuery):

    await call.message.edit_text(
        """
📅 <b>الجدولة</b>

يمكنك تجهيز منشور وتحديد:
🗓️ التاريخ
⏰ الوقت
🌐 المنصة

وسيتم نشره تلقائيًا عند الموعد.
        """,
        reply_markup=back_button(),
        parse_mode="HTML"
    )

    await call.answer()


@router.callback_query(F.data == "comments")
async def comments(call: CallbackQuery):

    await call.message.edit_text(
        """
💬 <b>التعليقات</b>

ستظهر هنا التعليقات المتاحة
من المنصات المرتبطة.

يمكن إضافة الرد والإدارة
بحسب صلاحيات كل API.
        """,
        reply_markup=back_button(),
        parse_mode="HTML"
    )

    await call.answer()


@router.callback_query(F.data == "manage")
async def manage(call: CallbackQuery):

    await call.message.edit_text(
        """
🗑️ <b>إدارة المنشورات</b>

اختر منشورًا لعرض تفاصيله.

يمكن تنفيذ الحذف فقط عندما
تسمح المنصة والـ API المستخدم بذلك.
        """,
        reply_markup=back_button(),
        parse_mode="HTML"
    )

    await call.answer()


@router.callback_query(F.data == "media")
async def media(call: CallbackQuery):

    await call.message.edit_text(
        """
📁 <b>مكتبة الوسائط</b>

ستحتوي على:
🖼️ الصور
🎬 الفيديوهات
📝 النصوص
📦 المحتوى المحفوظ
        """,
        reply_markup=back_button(),
        parse_mode="HTML"
    )

    await call.answer()


@router.callback_query(F.data == "settings")
async def settings(call: CallbackQuery):

    await call.message.edit_text(
        """
⚙️ <b>الإعدادات</b>

🔐 الأمان
🌐 الحسابات
🔔 الإشعارات
📊 الإحصائيات
🤖 أوامر المساعد
        """,
        reply_markup=back_button(),
        parse_mode="HTML"
    )

    await call.answer()
