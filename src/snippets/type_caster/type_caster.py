# FIXME no longer current refactored into other. keep until tests are done for new code.


# from typing import Any, Callable, Collection, Dict, List, Type, TypeVar
# from copy import deepcopy


# T = TypeVar("T", bound=Collection[Any])


# class TypeCaster:
#     def __init__(self, copy: Callable[[T], T] | None = deepcopy) -> None:
#         self.copy = copy
#         self.is_tuple: bool = False
#         self.is_named_tuple: bool = False

#     def _copy(self, data: T) -> T:
#         if self.copy is None:
#             return data
#         return self.copy(data)

#     def _ensure_mutable(self, data: T) -> List | Dict:
#         # Make sure collection is mutable, chane tuples to list and namedtuples to dict
#         if isinstance(data, tuple):
#             if hasattr(data, "_asdict"):
#                 copied_data = data._asdict()
#                 self.is_named_tuple = True
#                 return copied_data
#             copied_data = list(data)
#             self.is_tuple = True
#             return copied_data
#         if isinstance(data, list) or isinstance(data, dict):
#             return data
#         raise ValueError(
#             f"Collection type was {type(data)}, expected List, Dict, Tuple, or NamedTuple."
#         )

#     def __call__(self, data: T) -> List | Dict:
#         copied_data = self._copy(data=data)
#         mutable_data = self._ensure_mutable(copied_data)
#         mutable_data = self._iter_values(mutable_data)
#         return mutable_data

#     def _iter_values(self, data: List | Dict):
#         if isinstance(data, list):
#             for index, value in enumerate(data):
#                 data[index] = self._transform_type(value, index=index)
#             return data
#         if isinstance(data, dict):
#             for key, value in data.items():
#                 data[key] = self._transform_type(value, key=key)
#             return data
#         raise ValueError(f"Collection type was {type(data)}, expected List or Dict.")

#     def _transform_type(self, value: Any, *args, **kwargs) -> Any:
#         raise NotImplementedError


# class TypeMapTypeCaster(TypeCaster):
#     def __init__(
#         self,
#         type_map: Dict[Type[Any], Callable[[Any], Any]],
#         copy: Callable[[T], T] | None = deepcopy,
#     ) -> None:
#         self.type_map = type_map
#         super().__init__(copy)

#     def _transform_type(self, value: Any, *args, **kwargs) -> Any:
#         value_type = type(value)
#         if value_type in self.type_map:
#             trans_func = self.type_map[value_type]
#             return trans_func(value)
#         return value
