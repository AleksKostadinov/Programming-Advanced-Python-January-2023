number_of_guests = int(input())
codes = set()
for code in range(number_of_guests):
    codes.add(input())
while True:
    code = input()
    if code == "END":
        break
    codes.remove(code)
print(len(codes))
print("\n".join(sorted(codes)))
