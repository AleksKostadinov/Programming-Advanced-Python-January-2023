def stock_availability(flavours: list, command: str, *args):
    if command == 'delivery':
       flavours.extend(args)
    if command == 'sell':
        if args:
            for item in args:
                if type(args[0]) == int:
                    sold_items = args[0]
                    flavours = flavours[sold_items:]
                else:
                    while item in flavours:
                        flavours.remove(item)
        else:
            flavours = flavours[1:]
    return flavours


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))