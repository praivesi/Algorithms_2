def solution(cacheSize, cities):
    answer = 0
    cache = []

    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1

            cache.remove(city)            
            cache.insert(0, city)

        else:
            answer += 5

            if len(cache) == cacheSize:
                cache.pop(-1)
            
            cache.insert(0, city)

    return answer


cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
ans = solution(cacheSize, cities)
print('ans => ' + f'{ans}')