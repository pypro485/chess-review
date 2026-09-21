BLUNDER = 20
MISTAKE = 10
INACCURACY = 5
EXCELLENT = 2
MISS_TRIGGER = 999
MISS_MIN = 3
def classify(drop, is_best, is_book, is_miss):
    if is_book:
        return "Book"
    if is_best:
        return "Best"
    if drop > BLUNDER:
        return "Blunder"
    if is_miss:
        return "Miss"
    if drop <= EXCELLENT:
        return "Excellent"
    if drop <= INACCURACY:
        return "Good"
    elif drop <= MISTAKE:
        return "Inaccuracy"
    else:
        return "Mistake"