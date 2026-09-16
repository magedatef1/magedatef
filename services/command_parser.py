def parse_command(text: str):

    text = (text or "").strip()

    command = {
        "raw": text,
        "action": None,
        "platforms": []
    }

    if not text:
        return command

    lower = text.lower()

    if "انشر" in text:
        command["action"] = "publish"

    elif "احذف" in text:
        command["action"] = "delete"

    elif "إحصائ" in text or "احصائ" in text:
        command["action"] = "analytics"

    elif "جدول" in text:
        command["action"] = "schedule"

    platforms = {
        "فيسبوك": "facebook",
        "فيس بوك": "facebook",
        "انستغرام": "instagram",
        "إنستغرام": "instagram",
        "ثريدز": "threads",
        "تيك توك": "tiktok",
        "يوتيوب": "youtube",
        "إكس": "x",
        "تويتر": "x",
        "سناب": "snapchat",
        "سناب شات": "snapchat",
        "كواي": "kwai",
        "لايكي": "likee",
        "ماستودون": "mastodon",
        "في كيه": "vk"
    }

    for arabic, platform in platforms.items():

        if arabic in text:
            command["platforms"].append(platform)

    return command
