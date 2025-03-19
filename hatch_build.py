from pathlib import Path
import sys
from typing import Any

from hatchling.builders.hooks.plugin.interface import BuildHookInterface  # type: ignore


class BuildFrontend(BuildHookInterface):
    def initialize(self, version: str, build_data: dict[str, Any]) -> None:
        """
        This occurs immediately before each build.

        Any modifications to the build data will be seen by the build target.
        """
        sys.path.append(str(Path(__file__).parent / "src" / "snakemake"))

        from assets import Assets

        # download online assets
        Assets.deploy()
