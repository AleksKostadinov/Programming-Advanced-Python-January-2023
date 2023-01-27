numbers_ = [int(x) for x in input().split()]
negative, positive = 0, 0
for num in numbers_:
    if num >= 0:
        positive += num
    else:
        negative += num

print(negative)
print(positive)

if abs(negative) > positive:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")


