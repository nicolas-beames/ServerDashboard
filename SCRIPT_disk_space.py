import shutil


def disk_space(dir):
    total, used, free = shutil.disk_usage(__file__)

    return round(used/1024 ** 3, 1), round(free/1024 ** 3, 1)

#print(f"Free space in {'/'}: {disk_space('/')} MB")


print(disk_space('/'))