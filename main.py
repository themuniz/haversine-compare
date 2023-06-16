import click
from rich import print
from haversine import haversine, Unit

ANSWERS = [
    (48.89561588220521, 2.2677931364957553),
    (54.75167672643377, -3.749124667493804),
    (40.72603857933386, -74.00002993266372),
    (23.18459211047313, 25.099427962111427),
    (45.42950486171175, -75.69900276137741),
    (43.667063369157084, -92.99229089837873),
    (7.965945941184739, 81.00490498188255),
]

Cords = tuple[float, float]


def convert_to_cords(answer: str) -> Cords:
    '''Return cords for lat and long from string representation
    '''
    return (float(answer.split(',')[0]), float(answer.split(',')[1].lstrip()))


@click.command()
@click.option('-q', '--question', 'quest_no', type=int, help='Question number')
@click.option('-a', '--team-a', 'team_a', type=str, help='Team A answer')
@click.option('-b', '--team-b', 'team_b', type=str, help='Team B answer')
def compare_answers(quest_no: int, team_a: str, team_b: str) -> str:
    '''Determines which team's coordinates are closer to an answer's location'''
    a_Cords: Cords = convert_to_cords(team_a)
    b_Cords: Cords = convert_to_cords(team_b)
    a_dist = haversine(ANSWERS[quest_no - 1], a_Cords, unit=Unit.MILES)
    b_dist = haversine(ANSWERS[quest_no - 1], b_Cords, unit=Unit.MILES)
    if b_dist > a_dist:
        print(":bottle_with_popping_cork:",
              "[bold magenta]Team A[/bold magenta] was closer!")
    else:
        print(":call_me_hand_medium_skin_tone:",
              "[bold magenta]Team B[/bold magenta] was closer!")

    print(
        f"\nTeam A's distance: {a_dist} miles\nTeam B's distance: {b_dist} miles"
    )
    exit()


if __name__ == '__main__':
    compare_answers()
