def counting_change(amount, coins):
    if amount == 0:
        return 1
    if amount < 0 or not coins:
        return 0
    # 1의 제외하고 현재 동전을 사용하는 경우와 1을 사용하는 경우를 합산
    return counting_change(amount - coins[0], coins) + counting_change(amount, coins[1:])