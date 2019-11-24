filename = "xyz.txt"
buffer = ''
with open(filename) as f:
  while True:
    c = f.read(10)
    if not c:
      break
    buffer =  buffer + c
print(buffer)