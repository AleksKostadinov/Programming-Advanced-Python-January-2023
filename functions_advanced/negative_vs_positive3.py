numbers_ = [int(x) for x in input().split()]
negative = sum(int(x) for x in numbers_ if x < 0)
positive = sum(int(x) for x in numbers_ if x > 0)

print(negative)
print(positive)

if abs(negative) > positive:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
    