from __future__ import annotations

from typing import TYPE_CHECKING

from discord.ext import commands

from cardstudio.image_gen import apply_patches
from cardstudio.models import CardConfig

if TYPE_CHECKING:
    from ballsdex.core.bot import BallsDexBot


class CardStudio(commands.Cog):
    """Card Studio configuration management."""

    def __init__(self, bot: BallsDexBot):
        self.bot = bot

    async def cog_load(self) -> None:
        """Apply the Card Studio draw_card patch as soon as the cog loads."""
        apply_patches()

    @commands.command(name="reloadcardstudio")
    @commands.is_owner()
    async def reload_cardstudio(self, ctx: commands.Context) -> None:
        """Re-apply the Card Studio draw_card patch with current database config."""
        apply_patches()
        config = await CardConfig.aget_config()
        if config is None:
            await ctx.send(
                "Card Studio has not been configured."
            )
            return

        await ctx.send("Card Studio reloaded.")