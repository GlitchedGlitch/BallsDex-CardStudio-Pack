import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ballsdex.core.bot import BallsDexBot

log = logging.getLogger("ballsdex.packages.cardstudio")


async def setup(bot: BallsDexBot):
    log.info("Loading CardStudio package...")
    from .cog import CardStudio
    await bot.add_cog(CardStudio(bot))
    log.info("CardStudio package loaded successfully!")