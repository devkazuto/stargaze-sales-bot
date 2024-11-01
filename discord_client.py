import discord
from discord import SyncWebhook
from datetime import datetime, timezone
from constants import DISCORD_EMBED_COLOR, STARGAZE_ICON_URL, STARGAZE_NFT_URL, COLLECTION_ADDRESS, DISCORD_WEBHOOK

def shorten_address(address):
    if not address:  # Handles None or empty string
        return "-"
    return f"{address[:6]}...{address[-3:]}"

async def create_discord_embed(activity: dict):
    token = activity.get('token', {})
    name = token.get('name')
    rarity = token.get('rarityOrder')
    traits = token.get('traits', {})
    price_micro = int(activity.get('price', 0))
    price = price_micro * 1e-6
    buyerAddr = activity.get('buyerAddr')
    token_id = token.get('tokenId')
    thumbnail = token.get('media', {}).get('visualAssets', {}).get('md', {}).get('url')
    currency = 'STARS'
    nft_url = await get_token_url(COLLECTION_ADDRESS, token_id)
    STARGAZE_ACCOUNT_URL = "https://www.stargaze.zone/p/"  # adjust this to your actual base URL
    shortened_addr = shorten_address(buyerAddr)
    buyer_link = f"[{shortened_addr}]({STARGAZE_ACCOUNT_URL}{buyerAddr}/tokens)"

    description = ""
    # Add rarity if it exists
    if rarity:
        description += f"**Rarity:** `{str(rarity)}`\n"
    # Format price with thousand separator
    formatted_value = "{:,}".format(int(price))
    description += f"**Price:** `{formatted_value} {currency}`\n"
    # Add buyer
    description += f"**Buyer:** {buyer_link}"

    embed = discord.Embed(title=name,
                          description=description,
                          url=nft_url,
                          color=DISCORD_EMBED_COLOR)

    embed.set_author(name="Sold on Stargaze", icon_url=STARGAZE_ICON_URL)

    # if rarity:
    #     embed.add_field(name="Rarity", value="```" + str(rarity) + "```", inline=False)
    # formatted_value = "{:,}".format(int(price))
    # embed.add_field(name="Price", value="```" + formatted_value + " " + currency + "```", inline=False)
    # embed.add_field(name="Buyer", value=buyer_link, inline=False)
    

    # Handle optional attributes data
    # text = ""
    # sorted_attributes = sorted(traits, key=lambda x: x["name"])
    # for attribute in sorted_attributes:
    #     if 'name' in attribute and 'value' in attribute:
    #         text = text + f"**⦁ {attribute['name']}:** {attribute['value']}\n"
    # if len(text) > 0:
    #     embed.add_field(name="Traits", value=text, inline=False)

    embed.set_image(url=thumbnail)
    activity_date = activity.get('date')
    if activity_date:
        activity_timestamp = datetime.strptime(activity_date, '%Y-%m-%dT%H:%M:%S.%fZ')
        activity_timestamp = activity_timestamp.replace(tzinfo=timezone.utc)
        embed.timestamp = activity_timestamp
    embed.set_footer(text="@Steamland",
                     icon_url="https://pbs.twimg.com/profile_images/1690381994356768768/oLGVaGnb_400x400.jpg")
    return embed


async def get_token_url(collection_address: str, token_id: str):
    nft_url = STARGAZE_NFT_URL.replace('{collection_address}', collection_address)
    nft_url = nft_url.replace('{token_id}', token_id)
    return nft_url


class DiscordClient:

    def __init__(self):
        self.webhook = SyncWebhook.from_url(DISCORD_WEBHOOK)

    async def send_message(self, embed):
        self.webhook.send(embed=embed)
