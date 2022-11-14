def solution(price, money, count):
    price_sum = 0
    cur_price = price
    for _ in range(count):
        price_sum += cur_price
        cur_price += price

    return 0 if price_sum < money else price_sum - money

ans = solution(3, 20, 4)
print(ans)