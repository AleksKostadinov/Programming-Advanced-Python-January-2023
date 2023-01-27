def negative_positive(numbers_):
    negative, positive = [], []
    for num in numbers_:
        if num >= 0:
            positive.append(num)
        else:
            negative.append(num)
    sum_negative = sum(negative)
    sum_positive = sum(positive)
    print(f'{sum_negative}\n{sum_positive}')

    if abs(sum_negative) > sum_positive:
        print(f"The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


numbers = [int(x) for x in input().split()]

negative_positive(numbers)
