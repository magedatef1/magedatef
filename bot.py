import os
import logging

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

# ==========================================
# إعدادات التسجيل
# ==========================================

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


# ==========================================
# التحقق من المستخدم
# ==========================================

ADMIN_ID = os.getenv("ADMIN_ID")


def is_admin(user_id: int) -> bool:
    if not ADMIN_ID:
        return True

    try:
        return user_id == int(ADMIN_ID)
    except ValueError:
        return False


# ==========================================
# /start
# ==========================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    if not user or not is_admin(user.id):
        await update.message.reply_text(
            "⛔ غير مصرح لك باستخدام هذا البوت."
        )
        return

    keyboard = [
        [
            InlineKeyboardButton(
                "🔗 الحسابات",
                callback_data="accounts"
            )
        ],
        [
            InlineKeyboardButton(
                "📤 نشر محتوى",
                callback_data="publish"
            ),
            InlineKeyboardButton(
                "💬 التعليقات",
                callback_data="comments"
            ),
        ],
        [
            InlineKeyboardButton(
                "🤖 الرد التلقائي",
                callback_data="auto_reply"
            ),
            InlineKeyboardButton(
                "📊 الإحصائيات",
                callback_data="stats"
            ),
        ],
        [
            InlineKeyboardButton(
                "⚙️ الإعدادات",
                callback_data="settings"
            )
        ],
    ]

    await update.message.reply_text(
        "🤖 *Social Manager*\n\n"
        "مرحبًا بك في لوحة التحكم.\n\n"
        "سنستخدم هذا البوت لإدارة حساباتك "
        "ومتابعة التعليقات والردود تلقائيًا.\n\n"
        "اختر من القائمة:",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown",
    )


# ==========================================
# زر الرجوع للقائمة الرئيسية
# ==========================================

def main_menu_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "🔗 الحسابات",
                callback_data="accounts"
            )
        ],
        [
            InlineKeyboardButton(
                "📤 نشر محتوى",
                callback_data="publish"
            ),
            InlineKeyboardButton(
                "💬 التعليقات",
                callback_data="comments"
            ),
        ],
        [
            InlineKeyboardButton(
                "🤖 الرد التلقائي",
                callback_data="auto_reply"
            ),
            InlineKeyboardButton(
                "📊 الإحصائيات",
                callback_data="stats"
            ),
        ],
        [
            InlineKeyboardButton(
                "⚙️ الإعدادات",
                callback_data="settings"
            )
        ],
    ])


# ==========================================
# معالجة الأزرار
# ==========================================

async def button_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    query = update.callback_query

    await query.answer()

    user = query.from_user

    if not is_admin(user.id):
        await query.edit_message_text(
            "⛔ غير مصرح لك باستخدام هذا البوت."
        )
        return

    if query.data == "accounts":

        keyboard = [
            [
                InlineKeyboardButton(
                    "📘 Facebook",
                    callback_data="connect_facebook"
                )
            ],
            [
                InlineKeyboardButton(
                    "📸 Instagram",
                    callback_data="connect_instagram"
                )
            ],
            [
                InlineKeyboardButton(
                    "▶️ YouTube",
                    callback_data="connect_youtube"
                )
            ],
            [
                InlineKeyboardButton(
                    "💼 LinkedIn",
                    callback_data="connect_linkedin"
                )
            ],
            [
                InlineKeyboardButton(
                    "⬅️ الرئيسية",
                    callback_data="home"
                )
            ],
        ]

        await query.edit_message_text(
            "🔗 *إدارة الحسابات*\n\n"
            "الحسابات التي سنربطها بالنظام:\n\n"
            "📘 Facebook — 🔴 غير متصل\n"
            "📸 Instagram — 🔴 غير متصل\n"
            "▶️ YouTube — 🔴 غير متصل\n"
            "💼 LinkedIn — 🔴 غير متصل\n\n"
            "سنضيف الربط الرسمي OAuth لكل منصة لاحقًا.",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown",
        )

    elif query.data == "publish":

        await query.edit_message_text(
            "📤 *نشر المحتوى*\n\n"
            "هذه الوظيفة سنبنيها بعد الانتهاء من ربط الحسابات.\n\n"
            "سيكون بإمكانك لاحقًا إرسال صورة أو فيديو "
            "وكتابة النص واختيار المنصات.",
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "⬅️ الرئيسية",
                        callback_data="home"
                    )
                ]
            ]),
            parse_mode="Markdown",
        )

    elif query.data == "comments":

        await query.edit_message_text(
            "💬 *إدارة التعليقات*\n\n"
            "النظام سيستقبل التعليقات من المنصات "
            "المرتبطة، ثم يحدد اللغة ويجهز الرد.",
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "⬅️ الرئيسية",
                        callback_data="home"
                    )
                ]
            ]),
            parse_mode="Markdown",
        )

    elif query.data == "auto_reply":

        await query.edit_message_text(
            "🤖 *الرد التلقائي*\n\n"
            "سيتم بناء النظام بحيث:\n\n"
            "🌍 يكتشف لغة التعليق\n"
            "🧠 يستخدم الذكاء الاصطناعي لإنشاء الرد\n"
            "💬 يرد بنفس لغة المستخدم\n"
            "🛡️ يمنع الردود المكررة\n"
            "🔔 يرسل لك التنبيهات المهمة\n\n"
            "سنفعّل هذه الوظيفة بعد ربط المنصات.",
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "⬅️ الرئيسية",
                        callback_data="home"
                    )
                ]
            ]),
            parse_mode="Markdown",
        )

    elif query.data == "stats":

        await query.edit_message_text(
            "📊 *الإحصائيات*\n\n"
            "ستظهر هنا لاحقًا إحصائيات:\n\n"
            "📤 المنشورات\n"
            "💬 التعليقات\n"
            "🤖 الردود\n"
            "🌍 اللغات\n"
            "📱 أداء كل منصة",
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "⬅️ الرئيسية",
                        callback_data="home"
                    )
                ]
            ]),
            parse_mode="Markdown",
        )

    elif query.data == "settings":

        await query.edit_message_text(
            "⚙️ *الإعدادات*\n\n"
            "سنضع هنا لاحقًا:\n\n"
            "🤖 تشغيل/إيقاف الرد التلقائي\n"
            "🌍 اللغات\n"
            "🧠 إعدادات الذكاء الاصطناعي\n"
            "🛡️ حماية من التكرار\n"
            "🔔 الإشعارات",
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "⬅️ الرئيسية",
                        callback_data="home"
                    )
                ]
            ]),
            parse_mode="Markdown",
        )

    elif query.data.startswith("connect_"):

        platform = query.data.replace(
            "connect_",
            ""
        )

        names = {
            "facebook": "Facebook",
            "instagram": "Instagram",
            "youtube": "YouTube",
            "linkedin": "LinkedIn",
        }

        platform_name = names.get(
            platform,
            platform
        )

        await query.edit_message_text(
            f"🔗 *ربط {platform_name}*\n\n"
            "هذه الخطوة ستكون عبر OAuth الرسمي.\n\n"
            "لن نطلب منك كلمة مرور حسابك، "
            "ولن نضع كلمات المرور داخل GitHub.\n\n"
            "سنبرمج زر الربط الفعلي بعد تشغيل البوت.",
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "⬅️ الحسابات",
                        callback_data="accounts"
                    )
                ]
            ]),
            parse_mode="Markdown",
        )

    elif query.data == "home":

        await query.edit_message_text(
            "🤖 *Social Manager*\n\n"
            "اختر من لوحة التحكم:",
            reply_markup=main_menu_keyboard(),
            parse_mode="Markdown",
        )


# ==========================================
# تشغيل البوت
# ==========================================

def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")

    if not token:
        raise RuntimeError(
            "TELEGRAM_BOT_TOKEN غير موجود في Environment Variables"
        )

    application = (
        Application.builder()
        .token(token)
        .build()
    )

    application.add_handler(
        CommandHandler("start", start)
    )

    application.add_handler(
        CallbackQueryHandler(button_handler)
    )

    logger.info("Telegram bot is starting...")

    application.run_polling(
        drop_pending_updates=True
    )


# ==========================================
# نقطة البداية
# ==========================================

if __name__ == "__main__":
    main()
