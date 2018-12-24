from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time

class First(Page):
    # timeout_seconds = 60
    pass

class appearin(Page):
    # timeout_seconds = 60
    pass

class Select1(Page):
    form_model = 'group'
    form_fields = ['player_select1']

    def is_displayed(self):
        return self.player.id_in_group == 1


class Select2(Page):
    form_model = 'group'
    form_fields = ['player_select2']

    def is_displayed(self):
        return self.player.id_in_group == 2


class Introduction(Page):
    # timeout_seconds = 60
    pass


class PlayerSelectWait(WaitPage):
    title_text = "ペアが選択中です"
    body_text = "ペアがの選択を待っています"

    def is_displayed(self):
        return self.player.id_in_group == 1


class SendMachine(Page):
    # timeout_seconds = 60
    """This page is only for P1
    P1 sends amount (all, some, or none) to P2
    This amount is tripled by experimenter,
    i.e if sent amount by P1 is 5, amount received by P2 is 15"""

    form_model = 'group'
    form_fields = ['Sam']

    def is_displayed(self):
        return self.player.id_in_group == 1 and self.group.player_select1 == 2


class Send(Page):
    # timeout_seconds = 60
    """This page is only for P1
    P1 sends amount (all, some, or none) to P2
    This amount is tripled by experimenter,
    i.e if sent amount by P1 is 5, amount received by P2 is 15"""

    form_model = 'group'
    form_fields = ['Sab']

    def is_displayed(self):
        return self.player.id_in_group == 1 and (self.group.player_select1 != 2 or self.group.player_select2 != 2)

    def vars_for_template(self):
        self.player.page_num()


class MyWaitPage(WaitPage):
    template_name = 'round1/MyWaitPage.html'
    title_text = "ペアが選択中です"
    body_text = "ペアの選択を待っています"

    def after_all_players_arrive(self):
        self.group.set_smb()


class SendBackMachine(Page):
    # timeout_seconds = 60
    """This page is only for P2
    P2 sends back some amount (of the tripled amount received) to P1"""

    form_model = 'group'
    form_fields = ['Rbm']

    def is_displayed(self):
        return self.player.id_in_group == 2 and self.group.player_select2 == 2

    def vars_for_template(self):
        tripled_amount = self.group.Smb * Constants.multiplier
        cpu_count = Constants.endowment - self.group.Smb

        return {
                'tripled_amount': tripled_amount,
                'cpu_count': cpu_count,
                'prompt': '0ポイントから{}の間でペアに渡すポイントを打ち込んでください'.format(tripled_amount)}

    def Rbm_max(self):
        return self.group.Smb * Constants.multiplier


class SendBack(Page):
    # timeout_seconds = 60
    """This page is only for P2
    P2 sends back some amount (of the tripled amount received) to P1"""

    form_model = 'group'
    form_fields = ['Rba']

    def is_displayed(self):
        return self.player.id_in_group == 2 and (self.group.player_select1 != 2 or self.group.player_select2 != 2)

    def vars_for_template(self):
        tripled_amount = self.group.Sab * Constants.multiplier
        cpu_count = Constants.endowment - self.group.Sab
        self.player.page_num()

        return {
                'tripled_amount': tripled_amount,
                'cpu_count': cpu_count,
                'prompt': '0ポイントから{}の間でペアに渡すポイントを打ち込んでください'.format(tripled_amount)}

    def Rba_max(self):
        return self.group.Sab * Constants.multiplier


class ResultsWaitPage(WaitPage):
    template_name = 'round1/MyWaitPage.html'
    title_text = "ペアのターンです"
    body_text = "ペアの選択を待っています"

    def vars_for_template(self):
        if self.group.Sab is None:
            self.group.Sab = c(0)
        if self.group.Sam is None:
            self.group.Sam = c(0)
        my_point_machine = Constants.endowment - self.group.Sam
        your_point_machine = self.group.Sam * Constants.multiplier
        my_point_human = Constants.endowment - self.group.Sab
        your_point_human = self.group.Sab * Constants.multiplier

        return {
                'my_point_machine': my_point_machine,
                'your_point_machine': your_point_machine,
                'my_point_human': my_point_human,
                'your_point_human': your_point_human
        }

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results1(Page):
    # timeout_seconds = 60
    """This page displays the earnings of each player"""

    def vars_for_template(self):
        self.player.ResultNum = 1 and (self.group.player_select1 == 1 or self.group.player_select2 == 1)
        return {
            'tripled_amount': self.group.Sab * Constants.multiplier
        }
        self.player.ResultNum = 1 and (self.group.player_select1 == 2 and self.group.player_select2 == 2)
        return {
            'tripled_amount': self.group.Smb * Constants.multiplier
        }

class Results2(Page):

    def vars_for_template(self):
        self.player.ResultNum = 2
        return {
            'tripled_amount': self.group.Smb * Constants.multiplier
        }

    def is_displayed(self):
        return self.group.player_select1 == 2 or self.group.player_select2 == 2


class NextWait(Page):
    pass


page_sequence = [
    First,
    appearin,
    Introduction,
    PlayerSelectWait,
    SendMachine,
    Send,
    MyWaitPage,
    SendBackMachine,
    SendBack,
    ResultsWaitPage,
    Results1,
    Results2,
    NextWait,
]
