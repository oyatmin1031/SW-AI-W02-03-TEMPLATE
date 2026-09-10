INF = float("inf")


def make_change_greedy(change: int, coins: list[int]) -> tuple[int, dict[int, int]]:
    result: dict[int, int] = {}
    total_coins = 0

    for coin in coins:
        count: int = change // coin
        if count > 0:
            result[coin] = count
            change %= coin
            total_coins += count

    return total_coins, result


def make_change_dp(change, coins) -> tuple[int, dict[int, int]]:
    result: dict = {}

    used_coins: list[int] = [0] * (change + 1)
    changes = [INF] * (change + 1)
    changes[0] = 0

    for i in range(1, change + 1):
        for coin in coins:
            if i >= coin and changes[i - coin] + 1 < changes[i]:
                changes[i] = changes[i - coin] + 1
                used_coins[i] = coin

    current: int = change
    while current != 0:
        result[used_coins[current]] = (
            result[used_coins[current]] + 1 if used_coins[current] in result else 1
        )
        current -= used_coins[current]

    # print(changes)

    return changes[change], result


# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    change1 = 1260
    coins1 = [500, 100, 50, 10]
    total, details = make_change_dp(change1, coins1)

    print("=== 거스름돈 계산 ===")
    print(f"거슬러줄 금액: {change1}원")
    for coin, count in details.items():
        print(f"{coin}원: {count}개")
    print(f"총 {total}개")
    print()

    # 테스트 케이스 2
    change2 = 4570
    coins2 = [500, 100, 50, 10]
    total, details = make_change_dp(change2, coins2)

    print("=== 거스름돈 계산 ===")
    print(f"거슬러줄 금액: {change2}원")
    for coin, count in details.items():
        print(f"{coin}원: {count}개")
    print(f"총 {total}개")
    print()

    # 테스트 케이스 3
    change3 = 1000
    coins3 = [500, 100, 50, 10]
    total, details = make_change_dp(change3, coins3)

    print("=== 거스름돈 계산 ===")
    print(f"거슬러줄 금액: {change3}원")
    for coin, count in details.items():
        print(f"{coin}원: {count}개")
    print(f"총 {total}개")
    print()

    # 테스트 케이스 4
    change4 = 200
    coins4 = [160, 100, 50, 10]
    total, details = make_change_greedy(change4, coins4)

    print("=== 거스름돈 계산 ===")
    print(f"거슬러줄 금액: {change4}원")
    for coin, count in details.items():
        print(f"{coin}원: {count}개")
    print(f"총 {total}개")
    print()

    # 테스트 케이스 5
    change5 = 200
    coins5 = [160, 100, 50, 10]
    total, details = make_change_dp(change5, coins5)

    print("=== 거스름돈 계산 ===")
    print(f"거슬러줄 금액: {change5}원")
    for coin, count in details.items():
        print(f"{coin}원: {count}개")
    print(f"총 {total}개")
    print()
