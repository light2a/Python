def average(numbers) -> float:
    return sum(numbers)/len(numbers)

scores = [8, 6, 9, 7]
print(average(scores))

student = {"name" : "Bình", "scores": [8, 6, 9, 7] }

print(f"{student['name']} có điểm TB là {average(student['scores'])}")

