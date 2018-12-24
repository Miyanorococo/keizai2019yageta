from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
from random import randint


doc = """
This is a standard 2-player trust game where the amount sent by player 1 gets
tripled. The trust game was first proposed by
<a href="http://econweb.ucsd.edu/~jandreon/Econ264/papers/Berg%20et%20al%20GEB%201995.pdf" target="_blank">
    Berg, Dickhaut, and McCabe (1995)
</a>.
"""


class Constants(BaseConstants):
    name_in_url = 'round1_2'
    players_per_group = 2
    num_rounds = 1

    instructions_template = 'round1_2/Instructions.html'
    pointsend_template = 'round1_2/PointSend.html'
    pointback_template = 'round1_2/PointBack.html'
    result_template = 'round1_2/PointResult.html'
    wait_template = 'round1_2/PointWait.html'
    select_template = 'round1_2/SelectTemplate.html'

    # Initial amount allocated to each player

    # 初期持ちポイント
    endowment = c(1000)
    # 何倍にして返すか
    multiplier = 3


class Subsession(BaseSubsession):
    def creating_session(self):
        new_structure = [[14, 11], [20, 13], [24, 9], [22, 10], [8, 17], [27, 26], [28, 23], [1, 3], [15, 2], [19, 12], [5, 4], [16, 21], [7, 18], [25, 6]]
        self.set_group_matrix(new_structure)


class Group(BaseGroup):

    # 人か機械の選択 1.人 2.機械
    player_select1 = models.IntegerField(initial=1)
    player_select2 = models.IntegerField(initial=1)

    # プレイヤー１が人に送る
    Sab = models.CurrencyField(
        # initial=0,
        min=0, max=Constants.endowment,
        doc="""Amount sent by P1""",
    )

    # プレイヤー１が機械に送る
    Sam = models.CurrencyField(
        # initial=0,
        min=0, max=Constants.endowment,
        doc="""Amount sent by P1""",
    )

    # プレイヤー２が人に返す
    Rba = models.CurrencyField(
        # initial=0,
        doc="""Amount sent back by P1""",
        min=c(0),
    )

    # プレイヤー２が機械に返す
    Rbm = models.CurrencyField(
        # initial=0,
        doc="""Amount sent back by P1""",
        min=c(0),
    )

    # CPUが送る
    Smb = models.CurrencyField()

    def set_smb(self):
        self.Smb = c(randint(0, Constants.endowment))

    # CPUが送り返す
    def b(self):
        return randint(0, self.Sam * Constants.multiplier)

    Rma = models.CurrencyField()

    # 最終獲得値
    Ga1 = models.CurrencyField()
    Ga2 = models.CurrencyField()
    Ga3 = models.CurrencyField()
    Gb1 = models.CurrencyField()
    Gb2 = models.CurrencyField()
    Gb3 = models.CurrencyField()

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        if self.Sab is None:
            self.Sab = c(0)
        if self.Sam is None:
            self.Sam = c(0)
        if self.Rba is None:
            self.Rba = c(0)
        if self.Rbm is None:
            self.Rbm = c(0)
        self.Rma = c(self.b())
        # Y(a)
        p1.payoff = Constants.endowment - self.Sab + self.Rma * Constants.multiplier
        # X(a)
        p2.payoff = self.Sab * Constants.multiplier - self.Rma
        self.Ga1 = Constants.endowment - self.Sab + self.Rba
        self.Ga2 = Constants.endowment - self.Sam + self.Rma
        self.Ga3 = Constants.endowment - self.Smb + self.Rbm
        self.Gb1 = self.Sab * Constants.multiplier - self.Rba
        self.Gb2 = self.Smb * Constants.multiplier - self.Rbm
        self.Gb3 = self.Sam * Constants.multiplier - self.Rma


class Player(BasePlayer):

    PageSetNum = models.IntegerField(initial=0)
    ResultNum = models.IntegerField(initial=1)

    def page_num(self):
        self.PageSetNum = self.PageSetNum + 1

    def role(self):
        return {1: 'A', 2: 'B'}[self.id_in_group]
