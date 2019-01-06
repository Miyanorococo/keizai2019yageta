from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
from random import randint
from numpy.random import *


doc = """
This is a standard 2-player trust game where the amount sent by player 1 gets
tripled. The trust game was first proposed by
<a href="http://econweb.ucsd.edu/~jandreon/Econ264/papers/Berg%20et%20al%20GEB%201995.pdf" target="_blank">
    Berg, Dickhaut, and McCabe (1995)
</a>.
"""


class Constants(BaseConstants):
    name_in_url = 'Round21'
    players_per_group = 2
    num_rounds = 1

    instructions_template = 'Round21/Instructions.html'
    pointsend_template = 'Round21/PointSend.html'
    pointback_template = 'Round21/PointBack.html'
    result_template = 'Round21/PointResult.html'
    wait_template = 'Round21/PointWait.html'
    select_template = 'Round21/SelectTemplate.html'

    # Initial amount allocated to each player

    # 初期持ちポイント
    endowment = c(1000)
    # 何倍にして返すか
    multiplier = 3


class Subsession(BaseSubsession):
    def creating_session(self):
        new_structure = [[11, 20], [13, 14], [17, 24], [26, 22], [9, 8], [10, 27], [23, 1], [3, 28], [12, 15], [2, 19], [4, 16], [21, 5], [6, 7], [18, 25]]
        self.set_group_matrix(new_structure)


class Group(BaseGroup):

    # 人か機械の選択 1.人 2.機械
    player_select1 = models.IntegerField(initial=2)
    player_select2 = models.IntegerField(initial=2)

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
        self.Smb = c(Constants.endowment * normal(0.502, 0.124))
        if self.Smb > 1000:
            self.Smb = c(1000)
        if self.Smb < 0:
            self.Smb = c(0)

    # CPUが送り返す
    rrand = models.CurrencyField()

    def b(self):
        self.rrand = normal(0.372, 0.114)
        if self.rrand > 1:
            self.rrand = 1
        if self.rrand < 0:
            self.rrand = 0
        return self.rrand

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
        self.Rma = self.b() * self.Sam
        # Y(a)
        p1.payoff = Constants.endowment - self.Sab + self.Rma
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
