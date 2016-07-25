import axelrod as axl
import os

turns = 200
repetitions = 100
seed = 0


def run_tournament(filename, players,
                   seed=seed, turns=turns, repetitions=repetitions):
    try:
        os.remove(filename)
    except FileNotFoundError:
        pass
    axl.seed(seed)
    tournament = axl.Tournament(players, turns=turns, repetitions=repetitions)
    tournament.play(processes=0, filename=filename, build_results=False)


if __name__ == '__main__':
    demo_players = [s() for s in axl.demo_strategies]
    basic_players = [s() for s in axl.basic_strategies]
    full_players = [s() for s in axl.ordinary_strategies]
    for filename, players, turns, repetitions in [("demo_200_100.csv", demo_players, 200, 100),
                                                  ("basic_200_100.csv", basic_players, 200, 100),
                                                  ("full_50_5.csv", full_players, 50, 5),
                                                  ("full_50_10.csv", full_players, 50, 10),
                                                  ("full_50_20.csv", full_players, 50, 20)]:
        print(filename, turns, repetitions)
        run_tournament(filename, players, turns=turns, repetitions=repetitions)
