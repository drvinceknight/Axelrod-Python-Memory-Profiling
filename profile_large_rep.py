import axelrod as axl
from memory_profiler import profile

precision = 5

fp=open('memory_profiler_large_rep.log','w+')
@profile(precision=precision, stream=fp)
def main():
    players = [s() for s in axl.basic_strategies]
    tournament = axl.Tournament(players, turns=100, repetitions=100000)
    tournament.play(filename="test.out", build_results=False, processes=0)
    results = axl.ResultSetFromFile("test.out")

if __name__ == '__main__':
    main()
