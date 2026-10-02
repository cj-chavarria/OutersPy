from datetime import UTC, datetime, timedelta


def _dates() -> tuple[str, str]:
    now = datetime.now(tz=UTC)
    week = now + timedelta(days=6)
    return now.strftime("%Y-%m-%d"), week.strftime("%Y-%m-%d")


start_time, stop_time = _dates()
