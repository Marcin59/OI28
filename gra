# Marcin Kapiszewski

def find_way():
    movements = [0] * (n+2)
    for hole in holes:
        if hole[0] == n:
            movements[n] += 1
        else:
            movements[hole[0]] = min(movements[hole[0]]+1, movements[hole[0]+1])
            movements[hole[0]+1] = min(movements[hole[0]+1],  movements[hole[0]])
    return movements

if __name__ == '__main__':

    n, X, z = map(int, input().split())
    holes = []

    for i in range(1, n+1):
        data = map(int, input().split()[1:])
        for distance in data:
            holes.append((i, distance))
    holes.sort(key=lambda k: k[1], reverse=True)

    results = find_way()
    for _ in range(z):
        print(results[int(input())])
