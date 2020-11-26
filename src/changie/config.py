from enum import Enum
import yaml


class ConfigKey(Enum):
    ChangelogFileName = "changelogFileName"
    ChangelogItemPrefix = "changelogItemPrefix"
    ChangelogItemExtension = "changelogItemExtension"
    ChangelogItemsPath = "changelogItemsPath"


CONFIG_FILE_NAME = ".changierc.yml"  # TODO: .yaml


class Config:
    def load(self):
        config = {
            ConfigKey.ChangelogFileName.value: "CHANGELOG.md",
            ConfigKey.ChangelogItemPrefix.value: "chg",
            ConfigKey.ChangelogItemExtension.value: ".yml",
            ConfigKey.ChangelogItemsPath.value: "chg_items",
        }

        try:
            f = open(CONFIG_FILE_NAME)
            config_from_file = yaml.load(f, Loader=yaml.FullLoader)
            config.update(config_from_file)
        except:  # noqa: E722
            pass

        self._config = config

    def get(self, key: ConfigKey):
        return self._config[key.value]
