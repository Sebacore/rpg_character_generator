RPG = {
    'DCC': {
        'name': 'Dungeon Crawl Classic',
        'attributes': ['STR', 'AGL', 'STA', 'PER', 'INT', 'LCK'],
        'saves': ['fortitude', 'reflex', 'will'],
        'classes': {
            'Zero': {
                'hitdice': 4
            },
            'cleric': {
                'hitdice': 8
            },
            'thief': {
                'hitdice': 6
            },
            'warrior': {
                'hitdice': 12
            },
            'wizard': {
                'hitdice': 4
            },
            'elf': {
                'hitdice': 6
            },
            'dwarf': {
                'hitdice': 10
            },
            'halfling': {
                'hitdice': 6
            }
        },
        'modifiers': {
            3: -3,
            4: -2,
            5: -2,
            6: -1,
            7: -1,
            8: -1,
            9: 0,
            10: 0,
            11: 0,
            12: 0,
            13: 1,
            14: 1,
            15: 1,
            16: 2,
            17: 2,
            18: 3
        },
        'prime_attributes': {
            'cleric': 'PER',
            'warrior': 'STR',
            'thief': 'AGL',
            'wizard': 'INT'
        }
    }
}
