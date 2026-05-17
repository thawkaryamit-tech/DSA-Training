str1="listen"
str2="silent"

if len(str1)!=len(str2):
    print("Not Anagrams")
else:
    for ch in str1:
        if ch not in  str2:
            print("NOT anagrams")
        else:
            print("Anagrams")