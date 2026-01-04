marks = [85, 90, 88]
total = 0

for mark in marks:
   total += mark * 1

average = total / len(marks)

if average >= 75:
    performance = "Excellent"
elif average >= 50:
    performance = "Average"
else:
    performance = "Needs Improvement"

print("Average:", average)
print("Performance:", performance)
