import shutil
import psutil
def check_disk_usage(disk):
    du=shutil.disk_usage(disk)
    free=du.free/du.total*100
    return free>20
def check_cpu_usage():
    usage=psutil.cpu_percent(0.5)
    return usage>75
if not check_disk_usage("/"):
    print("Error in Disk!")
elif not check_cpu_usage():
    print("Error in CPU!")
else:
    print("Everything is a OK!")
