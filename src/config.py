import tomllib
from dataclasses import dataclass


@dataclass
class Config():
    websites: list(str)

    def from_toml(source: str):
        parsed = tomllib.loads(source)
        root: dict = parsed["config"]
        websites: list = root["websites"]
        Config(websites=websites)
