from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


def main_menu():

    return InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="📤 نشر محتوى",
                    callback_data="publish"
                ),
                InlineKeyboardButton(
                    text="🌐 حساباتي",
                    callback_data="accounts"
                )
            ],

            [
                InlineKeyboardButton(
                    text="📋 منشوراتي",
                    callback_data="posts"
                ),
                InlineKeyboardButton(
                    text="📊 الإحصائيات",
                    callback_data="analytics"
                )
            ],

            [
                InlineKeyboardButton(
                    text="📅 الجدولة",
                    callback_data="schedule"
                ),
                InlineKeyboardButton(
                    text="💬 التعليقات",
                    callback_data="comments"
                )
            ],

            [
                InlineKeyboardButton(
                    text="🗑️ إدارة وحذف",
                    callback_data="manage"
                ),
                InlineKeyboardButton(
                    text="📁 مكتبة الوسائط",
                    callback_data="media"
                )
            ],

            [
                InlineKeyboardButton(
                    text="⚙️ الإعدادات",
                    callback_data="settings"
                )
            ]

        ]
    )


def back_button():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🏠 الرئيسية",
                    callback_data="home"
                )
            ]
        ]
    )
