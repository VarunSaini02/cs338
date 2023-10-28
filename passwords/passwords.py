from hashlib import sha256

def crack1():
    words = [line.strip().lower() for line in open('words.txt')]
    
    hash_user = {} 
    with open('passwords1.txt', "r") as f:
        for line in f:
            user, hash = line.split(":")[0:2]
            if hash not in hash_user.keys():
                hash_user[hash] = [user]
            else:
                hash_user[hash].append(user)
                
    hashed_passwords = set(hash_user.keys())
    correct = set()

    num_hashes = 0

    for word in words:
        hash = sha256(word.encode()).hexdigest()
        num_hashes += 1
        if hash in hashed_passwords:
            for user in hash_user[hash]:
                correct.add(f"{user}:{word}\n")

    with open("cracked1.txt", "w") as f:
        f.writelines(correct)
    with open("cracked1.txt", "a") as f:
        f.write(f"\nNumber of hashes computed: {num_hashes}")

def crack2():
    words = [line.strip().lower() for line in open('words.txt')]

    hash_user = {line.split(":")[1] : line.split(":")[0] for line in open('passwords2.txt')}
    hashed_passwords = set(hash_user.keys())
    correct = set()

    num_hashes = 0

    for word1 in words:
        if len(correct) == 50:
            with open("cracked2.txt", "a") as f:
                f.write(f"\nNumber of hashes computed: {num_hashes}")
            return
        for word2 in words:
            word = word1 + word2
            hash = sha256(word.encode()).hexdigest()
            num_hashes += 1
            if hash in hashed_passwords:
                line = f"{hash_user[hash]}:{word}\n"
                if line not in correct:
                    correct.add(line)
                    with open("cracked2.txt", "a") as f:
                        f.write(line)

def crack3():
    words = [line.strip().lower() for line in open('words.txt')]
    salts = [line.split(":")[1].split("$")[2] for line in open('passwords3.txt')]
    hash_user = {line.split(":")[1].split("$")[3] : line.split(":")[0] for line in open('passwords3.txt')}
    hashed_passwords = set(hash_user.keys())
    correct = set()

    num_hashes = 0

    for word in words:
        for salt in salts:
            hash = sha256((salt + word).encode()).hexdigest()
            num_hashes += 1
            if hash in hashed_passwords:
                line = f"{hash_user[hash]}:{word}\n"
                if line not in correct:
                    correct.add(line)
                    with open("cracked3.txt", "a") as f:
                        f.write(line)

    with open("cracked3.txt", "a") as f:
        f.write(f"\nNumber of hashes computed: {num_hashes}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) <= 1 or sys.argv[1] not in {"1", "2", "3"}:
        print("Please enter a number (1, 2, 3) to run a password-cracking phase.")
    else:
        if sys.argv[1] == "1":
            crack1()
        elif sys.argv[1] == "2":
            crack2()
        elif sys.argv[1] == "3":
            crack3()

