import json
from pathlib import Path
from typing import Dict

import yaml


class SerializeMixin:
    """Provides serialization and deserialization functions for pydantic models."""

    def serialize_json(self, exclude_defaults=True, indent=2, **kwargs):
        serialized_json = self.json(
            exclude_defaults=exclude_defaults, indent=indent, **kwargs
        )
        return serialized_json

    def serialize_yaml(self, sort_keys=False, **kwargs):
        json_string = self.serialize_json()
        json_rep = json.loads(json_string)
        serialized_yaml = yaml.dump(json_rep, sort_keys=sort_keys, **kwargs)
        return serialized_yaml

    @classmethod
    def deserialize_obj(cls, obj: Dict):
        return cls(**obj)  # type: ignore

    @classmethod
    def deserialize_yaml(cls, yaml_string: str):
        obj = yaml.safe_load(yaml_string)
        instance = cls.deserialize_obj(obj)
        return instance

    @classmethod
    def deserialize_json(cls, json_string):
        obj = json.loads(json_string)
        instance = cls.deserialize_obj(obj)
        return instance

    @classmethod
    def deserialize_file(cls, file_path: Path):
        valid_suffixes = [".json", ".yaml"]
        if not file_path.is_file():
            raise ValueError(f"{file_path} is not a file.")
        if file_path.suffix.lower() not in valid_suffixes:
            raise ValueError(f"Invalid file suffix, must be one of {valid_suffixes}")
        string_data = file_path.read_text()
        if file_path.suffix.lower() == ".json":
            return cls.deserialize_json(string_data)
        return cls.deserialize_yaml(string_data)

    def serialize_file(self, file_path: Path, file_format: str, **kwargs) -> Path:
        valid_formats = ["json", "yaml"]
        if file_format.lower() not in valid_formats:
            raise ValueError(f"Invalid file suffix, must be one of {valid_formats}")
        file_ending = "." + file_format
        if file_path.suffix.lower() != file_ending:
            file_path = file_path.with_suffix(file_ending)
        if file_format == "json":
            string_data = self.serialize_json(**kwargs)
        else:
            string_data = self.serialize_yaml(**kwargs)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(string_data)
        return file_path
