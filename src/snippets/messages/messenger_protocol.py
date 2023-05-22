####################################################
#                                                  #
#   src/snippets/messages/messenger_protocol.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2023-04-26T11:15:08-07:00            #
# Last Modified: 2023-05-22T12:50:58.354458+00:00  #
# Source: https://github.com/DonalChilde/snippets  #
####################################################
from typing import Protocol


class MessageProtocol(Protocol):
    def produce_message(self) -> str:
        ...


class MessengeListenerProtocol(Protocol):
    def receive_message(self, msg: MessageProtocol):
        ...


class MessagePublisherProtocol(Protocol):
    consumers: list[MessengeListenerProtocol]

    def publish_message(self, msg: MessageProtocol):
        ...
