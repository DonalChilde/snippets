import json
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional

# TODO figure out nested function calls, so that i can define
# and_(build_filter_a(),build_filter_b())

"""possible to implement and or not by registering set functions?
"""


@dataclass
class TranslatedArguments:
    args: List[Any] = field(default_factory=list)
    kwargs: Dict[str, Any] = field(default_factory=dict)


@dataclass
class TranslatedKwArgument:
    arg_name: str
    arg_value: Any


@dataclass
class CommandArgument:
    arg_name: str
    arg_value: str


@dataclass
class RegisteredFunctionCommand:
    function_id: str
    args: List[CommandArgument] = field(default_factory=list)
    kwargs: List[CommandArgument] = field(default_factory=list)


@dataclass
class FunctionArgument:
    """Definition of an argument to a function.
    This is a description/definition of a function argument.
    It should have enough infomation to be able to recreate the argument
    from a string, possibly from a json file.
    """

    arg_name: str
    arg_converts_to: str
    format_example: str
    # string_value: str
    type_factory: Optional[Callable] = None
    # default_str_value: str = ""
    required: bool = False
    nullable: bool = False


@dataclass
class RegisteredFunction:
    """A function definition.
    This is a description/definition of a function.
    It should have enough information to be able call the function using
    arguments from a string, possibly stored in a json file.
    It has extra fields used to describe the function.
    """

    name: str
    description: str
    id_key: str
    category: str
    function: Callable
    args: Dict[str, FunctionArgument] = field(default_factory=dict)
    kwargs: Dict[str, FunctionArgument] = field(default_factory=dict)
    # json_signature: str


def validate_command(function: RegisteredFunction, command: RegisteredFunctionCommand):
    """
    guarantee existance of function_id, params,params dict
    if args or kwargs, verify list of {"arg_name": "name", "arg_value": "value"}
    verify that all required arguments are present
    """
    return True


def translate_arguments(
    registered_function: RegisteredFunction, function_command: RegisteredFunctionCommand
) -> TranslatedArguments:

    # pylint: disable=no-member
    # pylint: disable=unsupported-assignment-operation
    translated_args = TranslatedArguments()
    for arg in function_command.args:
        registered_function_argument = registered_function.args[arg.arg_name]
        if registered_function_argument.type_factory:
            translated_args.args.append(
                registered_function_argument.type_factory(arg.arg_value)
            )

            # param_args.append(registered_function_argument.type_factory(arg.arg_value))
        else:
            translated_args.args.append(arg.arg_value)
    for arg in function_command.kwargs:
        registered_function_argument = registered_function.kwargs[arg.arg_name]
        if registered_function_argument.type_factory:
            translated_args.kwargs[
                arg.arg_name
            ] = registered_function_argument.type_factory(arg.arg_value)
        else:
            translated_args.kwargs[arg.arg_name] = arg.arg_value
    return translated_args


class FunctionRegistry:
    """
    The context variable is available to pass common information to functions.
    If the context is None, it will not be passed to the function.
    """

    def __init__(self, context: Dict[Any, Any] = None):
        self.registered_functions: Dict[str, RegisteredFunction] = {}
        self.context = context

    def register_function(self, registered_function: RegisteredFunction):
        """Register a function"""
        self.registered_functions[registered_function.id_key] = registered_function

    def validate_function_sig(self, function_sig):
        """
        guarantee existance of function_id, params,params dict
        if args or kwargs, verify list of {"arg_name": "name", "arg_value": "value"}
        verify that all required arguments are present
        verify function_id in register
        """
        return True

    def perform_function(self, function_command: RegisteredFunctionCommand):
        registered_function: Optional[
            RegisteredFunction
        ] = self.registered_functions.get(function_command.function_id, None)
        if registered_function:
            param_args = []
            param_kwargs = {}
            for arg in function_command.args:
                registered_function_argument = registered_function.args[arg.arg_name]
                if registered_function_argument.type_factory:
                    param_args.append(
                        registered_function_argument.type_factory(arg.arg_value)
                    )
                else:
                    param_args.append(arg.arg_value)
            for arg in function_command.kwargs:
                registered_function_argument = registered_function.kwargs[arg.arg_name]
                if registered_function_argument.type_factory:
                    param_kwargs[
                        arg.arg_name
                    ] = registered_function_argument.type_factory(arg.arg_value)
                else:
                    param_kwargs[arg.arg_name] = arg.arg_value
        if self.context:
            function_result = registered_function.function(
                *param_args, self.context, **param_kwargs
            )
        else:
            function_result = registered_function.function(*param_args, **param_kwargs)
        return function_result

    def perform_function_dict(self, function_dict):
        if not self.validate_function_sig(function_dict):
            raise NotImplementedError(f"invalid function signature {function_dict}")
        registered_function = self.registered_functions[function_dict["function_id"]]

        param_args = []
        param_kwargs = {}
        json_args = function_dict["params"].get("args", [])
        json_kwargs = function_dict["params"].get("kwargs", [])
        for json_arg in json_args:
            registered_function_argument = registered_function.args[
                json_arg["arg_name"]
            ]
            if registered_function_argument.type_factory:
                param_args.append(
                    registered_function_argument.type_factory(json_arg["arg_value"])
                )
            else:
                param_args.append(json_arg["arg_value"])
        for json_arg in json_kwargs:
            registered_function_argument = registered_function.kwargs[
                json_arg["arg_name"]
            ]
            if registered_function_argument.type_factory:

                param_kwargs[
                    json_arg["arg_name"]
                ] = registered_function_argument.type_factory(json_arg["arg_value"])
            else:
                param_kwargs[json_arg["arg_name"]] = json_arg["arg_value"]
        function_result = registered_function.function(*param_args, **param_kwargs)
        return function_result

    def perform_function_json(self, json_string_signature):
        """Call a configured function from a json sig.
        example:
        foo = {
            "function_id": "<id_key of a registered function>",
            "params": {
                "args": [
                    {"arg_name": "name", "arg_value": "value"},
                    {"arg_name": "name", "arg_value": "value"},
                ],
                "kwargs": [
                    {"arg_name": "name", "arg_value": "value"},
                    {"arg_name": "name", "arg_value": "value"},
                ],
            },
        }
        Note, arg_name is used to look up type conversion, if any.
        args may use the same arg name, but kwargs also use
        arg_name as a key, and will overwrite if the same key is used.

        """

        # TODO more error checking, exception raising
        # TODO what about case where param can be NONE?
        # TODO work on signalling logic nullable, missing, default, etc.
        # TODO error capturing for type conversions
        json_signature = json.loads(json_string_signature)
        result = self.perform_function_dict(json_signature)
        return result
