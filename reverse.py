passwd = input("Enter the password\n")
passw = "<salt_dhdsjke>"+passwd #salt password to prevent dictionary attacks
correct = "O\x12\r\x18+;\x0c\x0c\x17\x19\x01\x0e[\x0f\x01WVR<n\x04j9\x13\x1bR"
d = ""
for i in range(0,len(passw)):
    l = [ord(a) ^ ord(b) for a,b in zip(passw[i],passw[(i+1)%len(passw)])]
    d+=chr(l[0])
if(d==correct):
    print("Correct password, here's your flag: ctf{"+passwd+"}")
else:
    print("Incorrect password")
