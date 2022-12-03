####################################################
#                                                  #
#  src/snippets/click/click_message_consumer.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2022-11-27T06:42:11-07:00            #
# Last Modified: 2022-12-03T23:45:37.159391+00:00  #
# Source: https://github.com/DonalChilde/snippets  #
####################################################

from typing import Dict

import click

from snippets.messages.publisher_consumer import MessageConsumer


class ClickMessageConsumer(MessageConsumer):
    def consume_message(
        self,
        msg: str,
        *,
        category: str = "",
        level: int | None = None,
        extras: Dict | None = None,
    ):
        click.echo(msg)
