import os

# def check_free_space(dir_name):
#     """Returns the free space in megabytes."""
#     if platform.system() == 'Windows':
#         free_bytes = ctypes.c_ulonglong(0)
#         ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(dir_name), None, None, ctypes.pointer(free_bytes))
#         return free_bytes.value / (1024 ** 2)  # Convert to MB
#     else:  # For Linux and macOS
#         stat = os.statvfs(dir_name)
#         return stat.f_bavail * stat.f_frsize / (1024 ** 2)  # Convert to MB

def disk_space(dir):
    stat = os.statvfs(dir)

    space = int(stat.f_bavail * stat.f_frsize / (1024 ** 2))

    if space < 1000:
        return f'{space} MB'
    elif space >= 1024:
        return f'{space / 1000} GB'
    else:
        return False

    #print(f'available: {stat.f_bavail}')
    #print(f'size: {stat.f_frsize}')


#print(f"Free space in {'/'}: {disk_space('/')} MB")

print(disk_space('/'))