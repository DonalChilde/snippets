####################################################
#                                                  #
#       src/snippets/messages/messenger.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2023-04-26T11:15:26-07:00            #
# Last Modified: 2023-05-22T14:38:53.210034+00:00  #
# Source: https://github.com/DonalChilde/snippets  #
####################################################
from io import TextIOWrapper

from .messenger_protocol import MessageProtocol, MessengeListenerProtocol


class MessengeListener(MessengeListenerProtocol):
    def receive_message(self, msg: MessageProtocol):
        raise NotImplementedError

    def format_message(self, msg: MessageProtocol) -> str:
        return msg.produce_message()

    def filter_message(self, msg: MessageProtocol) -> bool:
        _ = msg
        return True


class PrintMessengeListener(MessengeListener):
    def __init__(
        self, end: str = "\n", file: TextIOWrapper | None = None, flush: bool = False
    ) -> None:
        super().__init__()
        self.end = end
        self.file = file
        self.flush = flush

    def receive_message(self, msg: MessageProtocol):
        if self.filter_message(msg=msg):
            msg_txt = self.format_message(msg)
            print(
                msg_txt,
                end=self.end,
                file=self.file,
                flush=self.flush,
            )
