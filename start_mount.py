import os

os.system("""sudo mkdir -p /mnt/disk10001 && sudo mount -t cifs //192.168.3.2/DATA\ HARDDISK1TB /mnt/disk10001 -o workgroup=workgroup,iocharset=utf8,uid=hirusha,gid=hirusha,username=hirushaserver,password=123""")
os.system("""sudo mkdir -p /mnt/disk5001 && sudo mount -t cifs //192.168.3.2/500GB\ Disk\ 12 /mnt/disk5001 -o workgroup=workgroup,iocharset=utf8,uid=hirusha,gid=hirusha,username=hirushaserver,password=123""")
os.system("sudo mkdir -p /mnt/disk5002 && sudo mount -t cifs //192.168.3.2/500GB\ Disk\ 2 /mnt/disk5002 -o workgroup=workgroup,iocharset=utf8,uid=hirusha,gid=hirusha,username=hirushaserver,password=123")
os.system("sudo mkdir -p /mnt/disk5003 && sudo mount -t cifs //192.168.3.2/500GB\ Disk\ 3 /mnt/disk5003 -o workgroup=workgroup,iocharset=utf8,uid=hirusha,gid=hirusha,username=hirushaserver,password=123")





