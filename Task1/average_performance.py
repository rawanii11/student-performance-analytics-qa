marks = [85, 90, 88]
total = 0

for mark in marks:
    total += mark

average = total / len(marks)

if average >= 80:
    performance = "Excellent"
elif average >= 50:
    performance = "Average"
else:
    performance = "Needs Improvement"

print("Average:", average)
print("Performance:", performance)
