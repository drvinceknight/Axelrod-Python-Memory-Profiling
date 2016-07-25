import axelrod as axl
from memory_profiler import profile

precision = 5

def read(filename):
    rs = axl.ResultSetFromFile(filename)

def big_read(filename):
    rs = axl.BigResultSet(filename)

fp=open('memory_profiler.log','w+')
@profile(precision=precision, stream=fp)
def main():
    # Hard coding for profiler

    filename = "data/demo_200_100.csv"
    print(filename)
    # Demo strategies
    # Turns: 200
    # Repetitions: 100
    read(filename)
    big_read(filename)

    filename = "data/basic_200_100.csv"
    print(filename)
    # Basic strategies
    # Turns: 200
    # Repetitions: 100
    read(filename)
    big_read(filename)

    filename = "data/full_50_5.csv"
    print(filename)
    # Ordinary strategies
    # Turns: 50
    # Repetitions: 5
    read(filename)
    big_read(filename)

    filename = "data/full_50_10.csv"
    print(filename)
    # Ordinary strategies
    # Turns: 50
    # Repetitions: 10
    read(filename)
    big_read(filename)

    filename = "data/full_50_20.csv"
    print(filename)
    # Ordinary strategies
    # Turns: 50
    # Repetitions: 20
    read(filename)
    big_read(filename)

if __name__ == '__main__':
    main()
