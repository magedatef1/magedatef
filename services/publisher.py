class Publisher:

    async def publish(
        self,
        platform,
        media_path=None,
        caption=""
    ):

        raise NotImplementedError(
            f"لم يتم ربط API الرسمي لمنصة {platform} بعد."
        )
