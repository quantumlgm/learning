from taskiq import Context, TaskiqDepends


def get_formatter(service: Context = TaskiqDepends()):
    service_name = service.message.labels.get("service_name")
    def formatter_func(msg: str) -> str:
        return f"[{service_name.upper()}]: {msg}"

    return formatter_func
