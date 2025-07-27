import shutil

total, used, free = shutil.disk_usage(__file__)

print(round(total/1024 ** 3, 1), round(used/1024 ** 3, 1), round(free/1024 ** 3, 1))