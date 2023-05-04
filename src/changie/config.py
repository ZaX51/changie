from enum import Enum
from os.path import isfile
import yaml


class ConfigKey(Enum):
    ChangelogFileName = "changelogFileName"
    ChangeFilePrefix = "changeFilePrefix"
    ChangeFileExtension = "changeFileExtension"
    ChangeFilesPath = "changeFilesPath"


CONFIG_FILE_NAME = ".changierc.yml"  # TODO: .yaml


class Config:
    def load(self, config_path: str = None):
        config = {
            ConfigKey.ChangelogFileName.value: "CHANGELOG.md",
            ConfigKey.ChangeFilePrefix.value: "chg",
            ConfigKey.ChangeFileExtension.value: ".yml",
            ConfigKey.ChangeFilesPath.value: "chg_items",
        }

        path = config_path or CONFIG_FILE_NAME

        if isfile(path):
            f = open(path)
            config_from_file = yaml.load(f, Loader=yaml.FullLoader)
            config.update(config_from_file)

        self._config = config

    def get(self, key: ConfigKey):
        return self._config[key.value]
