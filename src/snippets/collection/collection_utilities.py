# def index_list_of_dicts(
#     data: Sequence[Dict[str, Any]], key_field: str
# ) -> Dict[str, Dict[str, Any]]:
#     result = {}
#     for item in data:
#         key_field_value = item[key_field]  # will error if field not found
#         result[str(key_field_value)] = item
#     return result


# def index_list_of_objects(
#     data: Iterable[Union[Sequence, Any]],
#     key_field,
#     use_get_item: bool,
#     cast_index: Callable = None,
# ):
#     """
#     Will index a list of objects based on key_field.

#     Returns a dict with key based on key_field of object

#     Parameters
#     ----------
#     data : Iterable[Union[Sequence, Any]]
#         [description]
#     key : [type]
#         [description]
#     use_get_item : bool
#         [description]
#     cast_index : Callable, optional
#         [description], by default None

#     Returns
#     -------
#     [type]
#         [description]
#     """
#     if use_get_item:
#         indexer: itemgetter | attrgetter = itemgetter(key_field)
#     else:
#         indexer = attrgetter(key_field)
#     result = {}
#     for item in data:
#         key_field_value = indexer(item)
#         if cast_index is not None:
#             key_field_value = cast_index(key_field_value)
#         result[key_field_value] = item
#     return result


# def index_list_of_objects_multiple(
#     data: Iterable[Union[Sequence, Any]],
#     key_field,
#     use_get_item: bool,
#     cast_index: Callable = None,
# ) -> Dict[Any, List[Any]]:
#     if use_get_item:
#         indexer: itemgetter | attrgetter = itemgetter(key_field)
#     else:
#         indexer = attrgetter(key_field)
#     result: Dict[Any, List[Any]] = {}
#     for item in data:
#         key_field_value = indexer(item)
#         if cast_index is not None:
#             key_field_value = cast_index(key_field_value)
#         indexed_field = result.get(key_field_value, [])
#         indexed_field.append(item)
#         result[key_field_value] = indexed_field
#     return result
