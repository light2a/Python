def add(a, b):
    return a + b
print(add(2, 3)) 
scores = [7, 8, 5]
scores.append(10)
print(scores)
print(len(scores))
print(scores[0])
print(scores[-1])

for s in scores:
    print(s)

person = {"name": "An", "age": 25}
print(person["name"])
person["age"] = 26
print(person.get("city", "?"))

for key, value in person.items():
    print(key, value)

num = [1, 2, 3, 4, 5, 6]
evens_sq = [x**2 for x in num if x%2 == 0]
people = [{"name": "An", "age": 30}, {"name": "Bình", "age": 25}]
by_age = sorted(people, key = lambda p: p["age"], reverse=True)
print(by_age)
print([p["name"] for p in by_age ])

print(any(n > 5 for n in num))
print(all( n > 3 for n in num))