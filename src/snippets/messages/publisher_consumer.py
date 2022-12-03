####################################################
#                                                  #
#    src/snippets/messages/publisher_consumer.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2022-10-14T04:34:10-07:00            #
# Last Modified: 2022-12-03T23:50:31.883184+00:00  #
# Source: https://github.com/DonalChilde/snippets  #
####################################################
from abc import ABC, abstractmethod
from typing import Dict, Protocol, Sequence

# FIXME use protocol


class MessageConsumer(ABC):
    """
    A consumer of messages.

    Subclass this, and override `consume_messages` to provide custom behavior.
    """

    @abstractmethod
    def consume_message(
        self,
        msg: str,
        *,
        category: str = "",
        level: int | None = None,
        extras: Dict | None = None,
    ):
        """
        Message consumer, usually called from a :class:`MessagePublisherMixin`

        Consumes a message in a particular way, eg. print to stdout

        Args:
            msg: The message to be consumed.
            category: A string used to differentiate messages. Defaults to "".
            level: An optional int used to differentiate messages. Can correspond to
                log levels. Defaults to None.
            extras: A optional Dict which can hold extra information. Defaults to None.

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError("Subclass and override this method.")


class HasMessageConsumersProtocol(Protocol):
    @property
    def message_consumers(self) -> Sequence[MessageConsumer]:
        "Has `self.message_consumers: Sequence[MessageConsumer]`"


class MessagePublisherMixin(HasMessageConsumersProtocol):
    """
    Provides the publish_message method.

    Expects to find `self.message_consumers: Sequence[MessageConsumer]` defined on class.
    """

    def publish_message(
        self,
        msg: str,
        *,
        category: str = "",
        level: int | None = None,
        extras: Dict | None = None,
    ):
        """
        Publish a message to consumers.

        Args:
            msg: The message to be consumed.
            category: A string used to differentiate messages. Defaults to "".
            level: An optional int used to differentiate messages. Can correspond to
                log levels. Defaults to None.
            extras: A optional Dict which can hold extra information. Defaults to None.
        """
        for consumer in self.message_consumers:
            consumer.consume_message(msg, category=category, level=level, extras=extras)


class StdoutConsumer(MessageConsumer):
    """
    Print messages to stdout.
    """

    def consume_message(
        self,
        msg: str,
        *,
        category: str = "",
        level: int | None = None,
        extras: Dict | None = None,
    ):
        print(
            f"Category: {category}\nLevel: {level}\nMessage: {msg}\nExtras: {extras!r}"
        )
