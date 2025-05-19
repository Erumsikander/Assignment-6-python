    

        # 2   -------- Using cls ----------
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 100
    
    @classmethod
    def show_count(cls):
        print(f"Total Created Objects Here: {cls.count}")

c1 = Counter()
c2 = Counter()
c3 = Counter()
c4 = Counter()
c5 = Counter()
Counter.show_count()