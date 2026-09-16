from database import get_connection


class SchedulerService:

    def schedule(
        self,
        platform,
        media_path,
        caption,
        publish_at
    ):

        with get_connection() as db:

            db.execute("""
                INSERT INTO schedules
                (
                    platform,
                    caption,
                    media_path,
                    publish_at,
                    status
                )
                VALUES (?, ?, ?, ?, ?)
            """, (
                platform,
                caption,
                media_path,
                publish_at,
                "scheduled"
            ))

            db.commit()

        return True
