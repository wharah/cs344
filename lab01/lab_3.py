"""
    This GPS will try to get the person to work on time and with a full stomach,but they don't have food at home
    and their car is out of gas. This shows the different options they could take for getting to work on time but none
    of them will work because the initial conditions aren't sufficient.
"""
from gps import gps

# Formulate the problem states and actions.
problem = {

    'initial': ['no food at home', 'is hungry', 'car out of gas', 'has cash', "time to stop for food"],
    'goal': ['at work on time', 'not hungry'],

    'actions': [
        {
            "action": "eat breakfast",
            "preconds": [
                "has food at home",
                "is hungry"
            ],
            "add": [
                "not hungry"
            ],
            "delete": [
                "is hungry"
            ]
        },
        {
            "action": "take the bus",
            "preconds": [
                "has cash",
                "car out of gas"
            ],
            "add": [
                "no cash",
                "no time to stop for food",
                "at work on time"
            ],
            "delete": [
                "has cash"
            ]
        },
        {
            "action": "drive to work",
            "preconds": [
                "car has gas"
            ],
            "add": [
                "time to stop for food",
                "at work on time",
                "car out of gas"
            ],
            "delete": [
                "car has gas"
            ]
        },
        {
            "action": "stop for food",
            "preconds": [
                "has cash",
                "time to stop for food",
                "is hungry",
                "no food at home"
            ],
            "add": [
                "not hungry",
                "no cash"
            ],
            "delete": [
                "is hungry",
                "has cash"
            ]
        }
    ]
}

if __name__ == '__main__':

    # Use GPS to solve the problem formulated above.
    actionSequence = gps(problem['initial'], problem['goal'], problem['actions'])

    # try to solve problem
    if actionSequence is not None:
        for action in actionSequence:
            print(action)
    else:
        print('plan failure...')
