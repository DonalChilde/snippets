####################################################
#                                                  #
#  src/snippets/parsing/messenger_parse_context.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2022-11-17T14:47:40-07:00            #
# Last Modified: 2022-12-03T23:51:03.920050+00:00  #
# Source: https://github.com/DonalChilde/snippets  #
####################################################
from abc import abstractmethod
from typing import Sequence

from snippets.messages.publisher_consumer import MessageConsumer, MessagePublisherMixin
from snippets.parsing.parse_context import ParseContext


class MessengerParseContext(ParseContext, MessagePublisherMixin):
    def __init__(
        self,
        *,
        source_name: str,
        message_consumers: Sequence[MessageConsumer],
        results_obj=None,
    ) -> None:
        super().__init__(source_name=source_name, results_obj=results_obj)
        self.message_consumers = message_consumers

    @abstractmethod
    def handle_parse_result(self, result) -> str:
        pass
