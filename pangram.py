s="The quick brown fox jumps over the lazy dog."
a="abcdefghijklmnopqrstuvwxyz"
count = 0

for ch in a :
    if ch not in (s).lower():
        print("NOT pangram")
        break;
else:
    print("pangram")

