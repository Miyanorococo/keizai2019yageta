from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time


class Introduction(Page):
    # timeout_seconds = 60
    pass


class Send(Page):
    # timeout_seconds = 60
    """This page is only for P1
    P1 sends amount (all, some, or none) to P2
    This amount is tripled by experimenter,
    i.e if sent amount by P1 is 5, amount received by P2 is 15"""

    form_model = 'group'
    form_fields = ['sent_amount']

    def is_displayed(self):
        return self.player.id_in_group == 1


class SendBackWaitPage(WaitPage):
    pass


class MyWaitPage(WaitPage):
    title_text = "Custom title text"
    body_text = "ss"


class SendBack(Page):
    # timeout_seconds = 60
    """This page is only for P2
    P2 sends back some amount (of the tripled amount received) to P1"""

    form_model = 'group'
    form_fields = ['sent_back_amount']

    def is_displayed(self):
        return self.player.id_in_group == 2

    def vars_for_template(self):
        tripled_amount = self.group.sent_cpu * Constants.multiplier
        cpu_count = Constants.endowment - self.group.sent_cpu

        return {
                'tripled_amount': tripled_amount,
                'cpu_count': cpu_count,
                'prompt': 'Please an amount from 0 to {}'.format(tripled_amount)}

    def sent_back_amount_max(self):
        return self.group.sent_cpu * Constants.multiplier


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    # timeout_seconds = 60
    """This page displays the earnings of each player"""

    def vars_for_template(self):
        return {
            'tripled_amount': self.group.sent_amount * Constants.multiplier
        }


page_sequence = [
    Introduction,
    Send,
    MyWaitPage,
    SendBack,
    ResultsWaitPage,
    Results,
]
