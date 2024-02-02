import time
import asyncio
import argparse
import traceback

import socketio

# from lib_not_dr.types import Options
from lib_not_dr.loggers import config

from data_struct import SendMessage, ReplyMessage, get_config, BotConfig, BotStatus

_version_ = "0.3.0"

logger = config.get_logger("bot")

BOTCONFIG: BotConfig = get_config()

if __name__ == "__main__":
    # --debug
    # --config=config.toml
    # -n --no-notice
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true")
    parser.add_argument("-n", "--no-notice", action="store_true")
    parser.add_argument("-c", "--config", type=str)
    args = parser.parse_args()
    if args.debug:
        logger.global_level = 0
    if args.config:
        # global BOTCONFIG
        BOTCONFIG: BotConfig = get_config(args.config)
    if args.no_notice:
        BOTCONFIG.notice_start = False