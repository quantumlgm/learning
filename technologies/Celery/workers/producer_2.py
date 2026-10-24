from tasks import show_info


result = show_info.apply_async(args=(10,))
print(result.get(timeout=10))
