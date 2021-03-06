from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [
    {
     'name': 'round1',
     'display_name': "round1",
     'num_demo_participants': 2,
     'app_sequence': ['round1'],
    },
    {
     'name': 'round1_2',
     'display_name': "round1_2",
     'num_demo_participants': 2,
     'app_sequence': ['round1_2'],
    },
    {
     'name': 'round2',
     'display_name': "round2",
     'num_demo_participants': 2,
     'app_sequence': ['round2'],
    },
    {
     'name': 'round2_2',
     'display_name': "round2_2",
     'num_demo_participants': 2,
     'app_sequence': ['round2_2',],
    },
    {
     'name': 'round3',
     'display_name': "round3",
     'num_demo_participants': 2,
     'app_sequence': ['round3'],
    },
    {
     'name': 'round3_2',
     'display_name': "round3_2",
     'num_demo_participants': 2,
     'app_sequence': ['round3_2'],
    },
    {
     'name': 'sequence1',
     'display_name': "sequence1",
     'num_demo_participants': 2,
     'app_sequence': ['round1','round1_2','round2','round2_2','round3','round3_2'],
    },
    {
        'name': 'Round21',
        'display_name': "Round21",
        'num_demo_participants': 2,
        'app_sequence': ['Round21'],
    },
    {
        'name': 'Round21_2',
        'display_name': "Round21_2",
        'num_demo_participants': 2,
        'app_sequence': ['Round21_2'],
    },
    {
        'name': 'Round12',
        'display_name': "Round12",
        'num_demo_participants': 2,
        'app_sequence': ['Round12'],
    },
    {
        'name': 'Round12_2',
        'display_name': "Round12_2",
        'num_demo_participants': 2,
        'app_sequence': ['Round12_2', ],
    },
    {
        'name': 'sequence2',
        'display_name': "sequence2",
        'num_demo_participants': 2,
        'app_sequence': ['Round21', 'Round21_2', 'Round12', 'Round12_2', 'round3', 'round3_2'],
    },
]
# see the end of this file for the inactive session configs


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'ja'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'JPY'
USE_POINTS = True

ROOMS = [
    {
        'name': 'ForMyExperimet',
        'display_name': 'ForMyExperiment',
        'participant_label_file': '_rooms/test.txt',
    },
]


# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')


# Consider '', None, and '0' to be empty/false
DEBUG = (environ.get('OTREE_PRODUCTION') in {None, '', '0'})

DEMO_PAGE_INTRO_HTML = """
Here are various games implemented with 
oTree. These games are open
source, and you can modify them as you wish.
"""

# don't share this with anybody.
SECRET_KEY = 'fd^l+hs*9w*3utklz)m!)p6*w!ip7r6f0kr5ufdpfd)+12tq*h'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

# inactive session configs

### {
###     'name': 'prisoner',
###     'display_name': "Prisoner's Dilemma",
###     'num_demo_participants': 2,
###     'app_sequence': ['prisoner', 'payment_info'],
### },
### {
###     'name': 'ultimatum',
###     'display_name': "Ultimatum (randomized: strategy vs. direct response)",
###     'num_demo_participants': 2,
###     'app_sequence': ['ultimatum', 'payment_info'],
### },
### {
###     'name': 'ultimatum_strategy',
###     'display_name': "Ultimatum (strategy method treatment)",
###     'num_demo_participants': 2,
###     'app_sequence': ['ultimatum', 'payment_info'],
###     'use_strategy_method': True,
### },
### {
###     'name': 'ultimatum_non_strategy',
###     'display_name': "Ultimatum (direct response treatment)",
###     'num_demo_participants': 2,
###     'app_sequence': ['ultimatum', 'payment_info'],
###     'use_strategy_method': False,
### },
### {
###     'name': 'vickrey_auction',
###     'display_name': "Vickrey Auction",
###     'num_demo_participants': 3,
###     'app_sequence': ['vickrey_auction', 'payment_info'],
### },
### {
###     'name': 'volunteer_dilemma',
###     'display_name': "Volunteer's Dilemma",
###     'num_demo_participants': 3,
###     'app_sequence': ['volunteer_dilemma', 'payment_info'],
### },
### {
###     'name': 'cournot',
###     'display_name': "Cournot Competition",
###     'num_demo_participants': 2,
###     'app_sequence': [
###         'cournot', 'payment_info'
###     ],
### },
### {
###     'name': 'principal_agent',
###     'display_name': "Principal Agent",
###     'num_demo_participants': 2,
###     'app_sequence': ['principal_agent', 'payment_info'],
### },
### {
###     'name': 'dictator',
###     'display_name': "Dictator Game",
###     'num_demo_participants': 2,
###     'app_sequence': ['dictator', 'payment_info'],
### },
### {
###     'name': 'matching_pennies',
###     'display_name': "Matching Pennies",
###     'num_demo_participants': 2,
###     'app_sequence': [
###         'matching_pennies',
###     ],
### },
### {
###     'name': 'traveler_dilemma',
###     'display_name': "Traveler's Dilemma",
###     'num_demo_participants': 2,
###     'app_sequence': ['traveler_dilemma', 'payment_info'],
### },
### {
###     'name': 'bargaining',
###     'display_name': "Bargaining Game",
###     'num_demo_participants': 2,
###     'app_sequence': ['bargaining', 'payment_info'],
### },
### {
###     'name': 'common_value_auction',
###     'display_name': "Common Value Auction",
###     'num_demo_participants': 3,
###     'app_sequence': ['common_value_auction', 'payment_info'],
### },
### {
###     'name': 'bertrand',
###     'display_name': "Bertrand Competition",
###     'num_demo_participants': 2,
###     'app_sequence': [
###         'bertrand', 'payment_info'
###     ],
### },
### {
###     'name': 'real_effort',
###     'display_name': "Real-effort transcription task",
###     'num_demo_participants': 1,
###     'app_sequence': [
###         'real_effort',
###     ],
### },
### {
###     'name': 'lemon_market',
###     'display_name': "Lemon Market Game",
###     'num_demo_participants': 3,
###     'app_sequence': [
###         'lemon_market', 'payment_info'
###     ],
### },
### {
###     'name': 'public_goods_simple',
###     'display_name': "Public Goods (simple version from tutorial)",
###     'num_demo_participants': 3,
###     'app_sequence': ['public_goods_simple', 'payment_info'],
### },
### {
###     'name': 'trust_simple',
###     'display_name': "Trust Game (simple version from tutorial)",
###     'num_demo_participants': 2,
###     'app_sequence': ['trust_simple'],
### },
