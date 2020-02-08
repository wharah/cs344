"""
    This module implements the simple blocks world using PAIP GPS.
"""
from gps import gps

# Formulate the problem states and actions.
problem = {

    'initial': ['c on a', 'space on b', 'space on c', 'b on table2', 'space on table1', 'a on table3'],
    'goal': ['b on table1', 'a on table2', 'c on table3', 'space on c', 'space on b', 'space on a'],

    'actions': [
        # {
        #     'action': 'move a from b to c',
        #     'preconds': [
        #         'space on a',
        #         'space on c',
        #         'a on b'
        #     ],
        #     'add': [
        #         'a on c',
        #         'space on b'
        #     ],
        #     'delete': [
        #         'a on b',
        #         'space on c'
        #     ]
        # },
        {
            'action': 'move c from a to table1',
            'preconds': [
                'c on a',
                'space on table1',
                'space on c'
            ],
            'add': [
                'c on table1',
                'space on a'
            ],
            'delete': [
                'c on a',
                'space on table1'
            ]
        },
        {
            'action': 'move b from table2 to c',
            'preconds': [
                'b on table2',
                'space on c',
                'space on b'
            ],
            'add': [
                'space on table2',
                'b on c'
            ],
            'delete': [
                'b on table2',
                'space on c'
            ]
        },
        {
            'action': 'move a from table3 to table2',
            'preconds': [
                'a on table3',
                'space on table2',
                'space on a'
            ],
            'add': [
                'a on table2',
                'space on table3'
            ],
            'delete': [
                'a on table3',
                'space on table2'
            ]
        },
        {
            'action': 'move b from c to a',
            'preconds': [
                'b on c',
                'space on a',
                'space on b'
            ],
            'add': [
                'b on a',
                'space on c'
            ],
            'delete': [
                'space on a',
                'b on c'
            ]
        },
        {
            'action': 'move c from table1 to table3',
            'preconds': [
                'c on table1',
                'space on c'
                'space on table3'
            ],
            'add': [
                'space on table1',
                'c on table3'
            ],
            'delete': [
                'c on table1',
                'space on table3'
            ]
        },
        {
            'action': 'move b from a to table1',
            'preconds': [
                'b on a',
                'space on table1'
                'space on b'
            ],
            'add': [
                'space on a',
                'b on table1'
            ],
            'delete': [
                'space on table1',
                'b on a'
            ]
        },
        {
            'action': 'move c from table3 to b',
            'preconds': [
                'c on table3',
                'space on b'
                'space on c'
            ],
            'add': [
                'space on table3',
                'c on b'
            ],
            'delete': [
                'c on table3',
                'space on b'
            ]
        },
        {
            'action': 'move a from table1 to table3',
            'preconds': [
                'a on table1',
                'space on table3'
                'space on a'
            ],
            'add': [
                'space on table1',
                'a on table3'
            ],
            'delete': [
                'a on table1',
                'space on table3'
            ]
        },
        {
            'action': 'move c from b to table1',
            'preconds': [
                'c on b',
                'space on table1'
                'space on c'
            ],
            'add': [
                'space on b',
                'c on table1'
            ],
            'delete': [
                'space on table1',
                'c on b'
            ]
        },
        {
            'action': 'move a from table3 to b',
            'preconds': [
                'space on b',
                'space on a'
                'a on table3'
            ],
            'add': [
                'space on table3',
                'a on b'
            ],
            'delete': [
                'a on table3',
                'space on b'
            ]
        },
        # {
        #     'action': 'move a from table to b',
        #     'preconds': [
        #         'space on a',
        #         'space on b',
        #         'a on table'
        #     ],
        #     'add': [
        #         'a on b'
        #     ],
        #     'delete': [
        #         'a on table',
        #         'space on b'
        #     ]
        # },
        # {
        #     'action': 'move a from b to table',
        #     'preconds': [
        #         'space on a',
        #         'space on table',
        #         'a on b'
        #     ],
        #     'add': [
        #         'a on table',
        #         'space on b'
        #     ],
        #     'delete': [
        #         'a on b'
        #     ]
        # },
        # {
        #     'action': 'move a from c to b',
        #     'preconds': [
        #         'space on a',
        #         'space on b',
        #         'a on c'
        #     ],
        #     'add': [
        #         'a on b',
        #         'space on c'
        #     ],
        #     'delete': [
        #         'a on c',
        #         'space on b'
        #     ]
        # },
        # {
        #     'action': 'move a from table to c',
        #     'preconds': [
        #         'space on a',
        #         'space on c',
        #         'a on table'
        #     ],
        #     'add': [
        #         'a on c'
        #     ],
        #     'delete': [
        #         'a on table',
        #         'space on c'
        #     ]
        # },
        # {
        #     'action': 'move a from c to table',
        #     'preconds': [
        #         'space on a',
        #         'space on table',
        #         'a on c'
        #     ],
        #     'add': [
        #         'a on table',
        #         'space on c'
        #     ],
        #     'delete': [
        #         'a on c'
        #     ]
        # },
        # {
        #     'action': 'move b from a to c',
        #     'preconds': [
        #         'space on b',
        #         'space on c',
        #         'b on a'
        #     ],
        #     'add': [
        #         'b on c',
        #         'space on a'
        #     ],
        #     'delete': [
        #         'b on a',
        #         'space on c'
        #     ]
        # },
        # {
        #     'action': 'move b from table to a',
        #     'preconds': [
        #         'space on b',
        #         'space on a',
        #         'b on table'
        #     ],
        #     'add': [
        #         'b on a'
        #     ],
        #     'delete': [
        #         'b on table',
        #         'space on a'
        #     ]
        # },
        # {
        #     'action': 'move b from a to table',
        #     'preconds': [
        #         'space on b',
        #         'space on table',
        #         'b on a'
        #     ],
        #     'add': [
        #         'b on table',
        #         'space on a'
        #     ],
        #     'delete': [
        #         'b on a'
        #     ]
        # },
        # {
        #     'action': 'move b from c to a',
        #     'preconds': [
        #         'space on b',
        #         'space on a',
        #         'b on c'
        #     ],
        #     'add': [
        #         'b on a',
        #         'space on c'
        #     ],
        #     'delete': [
        #         'b on c',
        #         'space on a'
        #     ]
        # },
        # {
        #     'action': 'move b from table to c',
        #     'preconds': [
        #         'space on b',
        #         'space on c',
        #         'b on table'
        #     ],
        #     'add': [
        #         'b on c'
        #     ],
        #     'delete': [
        #         'b on table',
        #         'space on c'
        #     ]
        # },
        # {
        #     'action': 'move b from c to table',
        #     'preconds': [
        #         'space on b',
        #         'space on table',
        #         'b on c'
        #     ],
        #     'add': [
        #         'b on table',
        #         'space on c'
        #     ],
        #     'delete': [
        #         'b on c'
        #     ]
        # },
        # {
        #     'action': 'move c from a to b',
        #     'preconds': [
        #         'space on c',
        #         'space on b',
        #         'c on a'
        #     ],
        #     'add': [
        #         'c on b',
        #         'space on a'
        #     ],
        #     'delete': [
        #         'c on a',
        #         'space on b'
        #     ]
        # },
        # {
        #     'action': 'move c from table to a',
        #     'preconds': [
        #         'space on c',
        #         'space on a',
        #         'c on table'
        #     ],
        #     'add': [
        #         'c on a'
        #     ],
        #     'delete': [
        #         'c on table',
        #         'space on a'
        #     ]
        # },
        # {
        #     'action': 'move c from a to table',
        #     'preconds': [
        #         'space on c',
        #         'space on table',
        #         'c on a'
        #     ],
        #     'add': [
        #         'c on table',
        #         'space on a'
        #     ],
        #     'delete': [
        #         'c on a'
        #     ]
        # },
        # {
        #     'action': 'move c from b to a',
        #     'preconds': [
        #         'space on c',
        #         'space on a',
        #         'c on b'
        #     ],
        #     'add': [
        #         'c on a',
        #         'space on b'
        #     ],
        #     'delete': [
        #         'c on b',
        #         'space on a'
        #     ]
        # },
        # {
        #     'action': 'move c from table to b',
        #     'preconds': [
        #         'space on c',
        #         'space on b',
        #         'c on table'
        #     ],
        #     'add': [
        #         'c on b'
        #     ],
        #     'delete': [
        #         'c on table',
        #         'space on b'
        #     ]
        # },
        # {
        #     'action': 'move c from b to table',
        #     'preconds': [
        #         'space on c',
        #         'space on table',
        #         'c on b'
        #     ],
        #     'add': [
        #         'c on table',
        #         'space on b'
        #     ],
        #     'delete': [
        #         'c on b'
        #     ]
        # }
    ]
}


if __name__ == '__main__':

    # Use GPS to solve the problem formulated above.
    actionSequence = gps(
        problem['initial'],
        problem['goal'],
        problem['actions']
    )

    # Print the solution, if there is one.
    if actionSequence is not None:
        for action in actionSequence:
            print(action)
    else:
        print('plan failure...')