import os
import logging
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
)

# ==========================================
# Logging
# ==========================================

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


# ==========================================
# Environment Variables
# ==========================================

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

if not TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN غير موجود")


# ==========================================
# التحقق من المدير
# ==========================================

def is_admin(user_id: int) -> bool:
    if not ADMIN_ID:
        return True

    try:
        return user_id == int(ADMIN_ID)
    except ValueError:
        return False


# ==========================================
# HTTP Server لـ Render
# ==========================================

class HealthHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(
            b"Social Manager Bot is running."
        )

    def log_message(self, format, *args):
        return


def start_health_server():
    port = int(os.getenv("PORT", "10000"))

    server = HTTPServer(
        ("0.0.0.0", port),
        HealthHandler
    )

    logger.info(
        f"Health server running on port {port}"
    )

    server.serve_forever()


# ==========================================
# القائمة الرئيسية
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
            )
        ],
        [
            InlineKeyboardButton(
                "🤖 الرد التلقائي",
                callback_data="auto_reply"
            ),
            InlineKeyboardButton(
                "📊 الإحصائيات",
                callback_data="stats"
            )
        ],
        [
            InlineKeyboardButton(
                "⚙️ الإعدادات",
                callback_data="settings"
            )
        ]
    ])


# ==========================================
# /start
# ==========================================

async def start(
    update: Update,
    context
):

    user = update.effective_user

    if not user:
        return

    if not is_admin(user.id):

        await update.message.reply_text(
            "⛔ غير مصرح لك باستخدام هذا البوت."
        )

        return

    await update.message.reply_text(
        "🤖 *Social Manager*\n\n"
        "مرحبًا بك في لوحة التحكم.\n\n"
        "سنستخدم هذا البوت لإدارة حساباتك "
        "على منصات التواصل الاجتماعي.\n\n"
        "اختر من القائمة:",
        reply_markup=main_menu_keyboard(),
        parse_mode="Markdown"
    )


# ==========================================
# التعامل مع الأزرار
# ==========================================

async def button_handler(
    update: Update,
    context
):

    query = update.callback_query

    await query.answer()

    user = query.from_user

    if not is_admin(user.id):

        await query.edit_message_text(
            "⛔ غير مصرح لك باستخدام هذا البوت."
        )

        return

    # --------------------------------------
    # الحسابات
    # --------------------------------------

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
            ]
        ]

        await query.edit_message_text(
            "🔗 *إدارة الحسابات*\n\n"

            "📘 Facebook — 🔴 غير متصل\n"
            "📸 Instagram — 🔴 غير متصل\n"
            "▶️ YouTube — 🔴 غير متصل\n"
            "💼 LinkedIn — 🔴 غير متصل\n\n"

            "سنضيف الربط الرسمي لكل منصة "
            "بعد تشغيل البوت.",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
        )

    # --------------------------------------
    # نشر
    # --------------------------------------

    elif query.data == "publish":

        await query.edit_message_text(
            "📤 *نشر المحتوى*\n\n"

            "سيتمكن النظام لاحقًا من:\n\n"

            "📷 إرسال صورة\n"
            "🎥 إرسال فيديو\n"
            "✍️ كتابة الوصف\n"
            "📱 اختيار المنصات\n"
            "📅 جدولة النشر",
            
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "⬅️ الرئيسية",
                        callback_data="home"
                    )
                ]
            ]),
            parse_mode="Markdown"
        )

    # --------------------------------------
    # التعليقات
    # --------------------------------------

    elif query.data == "comments":

        await query.edit_message_text(
            "💬 *إدارة التعليقات*\n\n"

            "سيقوم النظام لاحقًا بـ:\n\n"

            "📥 استقبال التعليقات\n"
            "🌍 معرفة لغة التعليق\n"
            "🧠 تحليل التعليق\n"
            "🤖 إنشاء الرد\n"
            "📤 نشر الرد\n"
            "📝 تسجيل العملية",

            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "⬅️ الرئيسية",
                        callback_data="home"
                    )
                ]
            ]),
            parse_mode="Markdown"
        )

    # --------------------------------------
    # الرد التلقائي
    # --------------------------------------

    elif query.data == "auto_reply":

        await query.edit_message_text(
            "🤖 *الرد التلقائي*\n\n"

            "النظام الذي سنبنيه سيقوم بـ:\n\n"

            "🌍 اكتشاف لغة التعليق\n"
            "🧠 استخدام الذكاء الاصطناعي\n"
            "💬 الرد بنفس لغة المستخدم\n"
            "🛡️ منع الردود المكررة\n"
            "⏱️ التحكم في سرعة الرد\n"
            "🔔 إرسال التنبيهات المهمة",

            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "⬅️ الرئيسية",
                        callback_data="home"
                    )
                ]
            ]),
            parse_mode="Markdown"
        )

    # --------------------------------------
    # الإحصائيات
    # --------------------------------------

    elif query.data == "stats":

        await query.edit_message_text(
            "📊 *الإحصائيات*\n\n"

            "سيتم إضافة:\n\n"

            "📤 المنشورات\n"
            "💬 التعليقات\n"
            "🤖 الردود\n"
            "🌍 اللغات\n"
            "📱 إحصائيات كل منصة",

            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "⬅️ الرئيسية",
                        callback_data="home"
                    )
                ]
            ]),
            parse_mode="Markdown"
        )

    # --------------------------------------
    # الإعدادات
    # --------------------------------------

    elif query.data == "settings":

        await query.edit_message_text(
            "⚙️ *الإعدادات*\n\n"

            "سيتم إضافة:\n\n"

            "🤖 تشغيل / إيقاف الرد التلقائي\n"
            "🌍 اللغات\n"
            "🧠 إعدادات الذكاء الاصطناعي\n"
            "🛡️ الحماية\n"
            "🔔 الإشعارات",

            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "⬅️ الرئيسية",
                        callback_data="home"
                    )
                ]
            ]),
            parse_mode="Markdown"
        )

    # --------------------------------------
    # ربط المنصات
    # --------------------------------------

    elif query.data.startswith("connect_"):

        platform = query.data.replace(
            "connect_",
            ""
        )

        names = {
            "facebook": "Facebook",
            "instagram": "Instagram",
            "youtube": "YouTube",
            "linkedin": "LinkedIn"
        }

        platform_name = names.get(
            platform,
            platform
        )

        await query.edit_message_text(
            f"🔗 *ربط {platform_name}*\n\n"

            "سيتم فتح صفحة تسجيل الدخول "
            "الرسمية للمنصة هنا لاحقًا.\n\n"

            "🔐 لن نطلب كلمة المرور منك.\n"
            "🔐 لن نضع بيانات الحساب في GitHub.\n"
            "🔐 سيتم استخدام OAuth الرسمي.",

            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "⬅️ الحسابات",
                        callback_data="accounts"
                    )
                ]
            ]),
            parse_mode="Markdown"
        )

    # --------------------------------------
    # الرئيسية
    # --------------------------------------

    elif query.data == "home":

        await query.edit_message_text(
            "🤖 *Social Manager*\n\n"
            "اختر من لوحة التحكم:",

            reply_markup=main_menu_keyboard(),
            parse_mode="Markdown"
        )


# ==========================================
# تشغيل البوت
# ==========================================

def main():

    logger.info("Starting Social Manager Bot...")

    # تشغيل خادم Render
    health_thread = threading.Thread(
        target=start_health_server,
        daemon=True
    )

    health_thread.start()

    # إنشاء تطبيق Telegram
    application = (
        Application.builder()
        .token(TOKEN)
        .build()
    )

    # Handlers
    application.add_handler(
        CommandHandler(
            "start",
            start
        )
    )

    application.add_handler(
        CallbackQueryHandler(
            button_handler
        )
    )

    logger.info(
        "Telegram bot is starting..."
    )

    # تشغيل Telegram
    application.run_polling(
        drop_pending_updates=True
    )


# ==========================================
# Start
# ==========================================

if __name__ == "__main__":
    main()
