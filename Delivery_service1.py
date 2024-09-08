def min_platforms(robots: list[int], limit: int) -> int:
    """
    Определить минимальное количество транспортных платформ,
    необходимое для перевозки всех роботов.

    Яндекс Контест ID: 117610250	

    """
    robots = sorted(robots)

    platforms = 0  # Количество платформ
    left = 0  # Левая граница текущей платформы
    right = len(robots) - 1  # Правая граница текущей платформы

    while left <= right:
        if left < right and robots[left] + robots[right] <= limit:
            left += 1
        platforms += 1
        right -= 1

    return platforms


if __name__ == '__main__':
    robots = [int(x) for x in input().split()]
    limit = int(input())
    print(min_platforms(robots, limit))
