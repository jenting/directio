import os
import mmap

### Write

f = os.open('file', os.O_CREAT | os.O_DIRECT | os.O_RDWR)
m = mmap.mmap(-1, 512)
s = b' ' * 512

m.write(s)
os.write(f, m)

os.close(f)
m.close()

### Read

f = os.open('file', os.O_DIRECT | os.O_RDWR)
fo = os.fdopen(f, 'rb+', 0)
m = mmap.mmap(-1, 512)

print(fo.readinto(m))

os.close(f)
m.close()

