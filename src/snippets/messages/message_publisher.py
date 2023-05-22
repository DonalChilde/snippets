####################################################
#                                                  #
#       src/snippets/messages/publisher.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2023-04-26T11:15:44-07:00            #
# Last Modified: 2023-05-22T17:37:55.447971+00:00  #
# Source: https://github.com/DonalChilde/snippets  #
####################################################
from typing import Sequence

from .messenger_protocol import (
    MessageProtocol,
    MessagePublisherProtocol,
    MessengeListenerProtocol,
)


class MessagePublisher(MessagePublisherProtocol):
    def __init__(self, listeners: Sequence[MessengeListenerProtocol]) -> None:
        self.listeners = list(listeners)

    def publish_message(self, msg: MessageProtocol):
        for listener in self.listeners:
            listener.receive_message(msg=msg)
