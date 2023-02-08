def stock_availability(items, *args):
    list_of_flavours = [] + items

    if args[0] == 'delivery':
        list_of_flavours += args[1:]
    if args[0] == 'sell':
        if not args[1:]:
            del list_of_flavours[0]
        elif str(args[1]).isdigit():
            del list_of_flavours[:args[1]]
        elif args[1:]:
            for item in args[1:]:
                while item in list_of_flavours:
                    list_of_flavours.remove(item)
    return list_of_flavours


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
