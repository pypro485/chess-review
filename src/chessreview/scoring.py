import math
def win_pct(centipawns):
    return 50 + 50 * (2 / (1 + math.exp(-0.00368208 * centipawns)) - 1)

if __name__ == "__main__":
    print(win_pct(0))
    print(win_pct(300))
    print(win_pct(-300))
    print(win_pct(1000))