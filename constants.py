import os

# Required parameters
# COLLECTION_ADDRESS = os.getenv('COLLECTION_ADDRESS')
COLLECTION_ADDRESS = "stars1j9rk6fte8j2qlwx6qewxh6ezu83r0a290j4wemn0h0hjw37fn3wqvzan3s"
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1021711117346689075/YO1ILHT1KxDKQF1LOYZ2_rFufFkNK2Kngscvq54likgFR5mPw-iXayJMawecFLq84_Fh";

# Optional parameters
STARGAZE_API_HOST = os.getenv('STARGAZE_API_HOST', 'https://graphql.mainnet.stargaze-apis.com/graphql')
STARGAZE_ICON_URL = os.getenv('STARGAZE_ICON_URL',
                              'https://pbs.twimg.com/profile_images/1507391623914737669/U3fR7nxh_400x400.jpg')
STARGAZE_NFT_URL = os.getenv('STARGAZE_NFT_URL', 'https://www.stargaze.zone/m/{collection_address}/{token_id}')
PAGINATION_LIMIT = int(os.getenv('PAGINATION_LIMIT', 25))
DISCORD_EMBED_COLOR = int(os.getenv('DISCORD_EMBED_COLOR', 0xe170a4))
CHECK_FREQUENCY_SECONDS = int(os.getenv('CHECK_FREQUENCY', 60))

# Application constants
TIMESTAMP_FILE = 'timestamp.txt'