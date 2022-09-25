import json
from datetime import timedelta

from utilities.function_register import (
    CommandArgument,
    FunctionArgument,
    FunctionRegistry,
    RegisteredFunction,
    RegisteredFunctionCommand,
)


def registered_timedelta_1():
    days = FunctionArgument(
        arg_name="days",
        arg_converts_to="int",
        format_example="'5'",
        type_factory=int,
        required=False,
        nullable=False,
    )
    hours = FunctionArgument(
        arg_name="hours",
        arg_converts_to="int",
        format_example="'5'",
        type_factory=int,
        required=False,
        nullable=False,
    )
    seconds = FunctionArgument(
        arg_name="seconds",
        arg_converts_to="int",
        format_example="'5'",
        type_factory=int,
        required=False,
        nullable=False,
    )
    registered_timedelta = RegisteredFunction(
        name="registered_timedelta",
        description="foo bar stuuffff",
        id_key="registered_timedelta",
        category="foo",
        function=timedelta,
        kwargs={days.arg_name: days, hours.arg_name: hours, seconds.arg_name: seconds},
    )
    return registered_timedelta


def registered_print():
    print_item = FunctionArgument(
        arg_name="print_item",
        arg_converts_to="string",
        format_example="",
        type_factory=str,
        required=True,
        nullable=False,
    )
    separator = FunctionArgument(
        arg_name="sep",
        arg_converts_to="string",
        format_example="",
        type_factory=str,
        required=False,
        nullable=False,
    )
    registered_print = RegisteredFunction(
        name="registered_print",
        description="foo bar stuuffff",
        id_key="registered_print",
        category="foo",
        function=print,
        args={print_item.arg_name: print_item},
        kwargs={separator.arg_name: separator},
    )
    return registered_print


def test_registered_print():
    registry = FunctionRegistry()
    registry.register_function(registered_print())
    # json_string_sig = {
    #     "function_id": "registered_print",
    #     "params": {
    #         "args": [
    #             {"arg_name": "print_item", "arg_value": "This prints first"},
    #             {"arg_name": "print_item", "arg_value": "This prints second"},
    #         ]
    #     },
    # }
    # registry.perform_function(json.dumps(json_string_sig))
    print_test1 = RegisteredFunctionCommand(function_id="registered_print")
    print_test1.args.append(
        CommandArgument(arg_name="print_item", arg_value="This prints first")
    )
    print_test1.args.append(
        CommandArgument(arg_name="print_item", arg_value="This prints second")
    )
    registry.perform_function(print_test1)
    # json_string_sig2 = {
    #     "function_id": "registered_print",
    #     "params": {
    #         "args": [
    #             {"arg_name": "print_item", "arg_value": "This prints first"},
    #             {"arg_name": "print_item", "arg_value": "This prints second"},
    #         ],
    #         "kwargs": [{"arg_name": "sep", "arg_value": "::::"}],
    #     },
    # }
    # registry.perform_function(json.dumps(json_string_sig2))
    print_test2 = RegisteredFunctionCommand(function_id="registered_print")
    print_test2.args.append(
        CommandArgument(arg_name="print_item", arg_value="This prints first")
    )
    print_test2.args.append(
        CommandArgument(arg_name="print_item", arg_value="This prints second")
    )
    print_test2.kwargs.append(CommandArgument(arg_name="sep", arg_value="::::"))
    registry.perform_function(print_test2)
