import redis

r_server = redis.Redis("localhost")


with open("mobythes.aur") as f:
    for line in f:
        results = line.split(",")
        word = results[0]
        synonyms = results[1:]
        synonyms[-1] = synonyms[-1].strip()
        r_server.set(word, synonyms)

