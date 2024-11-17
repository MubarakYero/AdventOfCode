import hashlib

secret_code = "yzbqklnj"

for i in range (1000000):
    string_to_hash = secret_code + str(i)
     
    hash_code = hashlib.md5(string_to_hash.encode()).hexdigest()
    
    if hash_code[:5] == "00000": # For part 2 change the index to 6 and also add a Zere to the string
        print(f"Requirement Met: {hash_code}")
        print(i)
        break