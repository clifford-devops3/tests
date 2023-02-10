import json

data = '''{
    "Data": [
        {
            "body": "While the money supply is contracting in both the United States and Europe, China's printer is at full swing.",
            "categories": "ASIA|SPONSORED",
            "downvotes": "0",
            "guid": "https://www.trustnodes.com/?p=51065",
            "id": "9053503",
            "imageurl": "https://images.cryptocompare.com/news/default/trustnodes.png",
            "lang": "EN",
            "published_on": 1675865329,
            "source": "trustnodes",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/trustnodes.png",
                "lang": "EN",
                "name": "TrustNodes"
            },
            "tags": "Asia|Featured|Finance|News",
            "title": "Did China Print Half a Trillion?",
            "upvotes": "0",
            "url": "https://www.trustnodes.com/2023/02/08/did-china-print-half-a-trillion"
        },
        {
            "body": "The post The AI Hype Makes A Bullish Entry Into Crypto! These AI Cryptocurrencies Are Ruling The Market appeared first on Coinpedia Fintech News Since its advent, the crypto market has witnessed multiple ups and downs and attracted investors to jump on this bandwagon. However, the latest trend that has shaken up the crypto space is the integration of artificial intelligence with the crypto market, leaving many investors questioning its future potential and market dominance. As the sideways performance …",
            "categories": "MARKET|BUSINESS|TRADING|ALTCOIN",
            "downvotes": "0",
            "guid": "https://coinpedia.org/?p=181074",
            "id": "9053291",
            "imageurl": "https://images.cryptocompare.com/news/default/coinpedia.png",
            "lang": "EN",
            "published_on": 1675864967,
            "source": "coinpedia",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/coinpedia.png",
                "lang": "EN",
                "name": "coinpedia"
            },
            "tags": "Altcoins|Crypto news|Price Analysis",
            "title": "The AI Hype Makes A Bullish Entry Into Crypto! These AI Cryptocurrencies Are Ruling The Market",
            "upvotes": "0",
            "url": "https://coinpedia.org/altcoin/the-ai-hype-makes-a-bullish-entry-into-crypto-these-ai-cryptocurrencies-are-ruling-the-market/"
        },
        {
            "body": "The central bank of India wants to proceed with CBDC testing in the smoothest way possible, deputy governor Rabi Sankar said.",
            "categories": "FIAT",
            "downvotes": "0",
            "guid": "https://cointelegraph.com/news/india-in-no-hurry-for-cbdc-as-digital-rupee-pilot-onboards-50k-users",
            "id": "9053326",
            "imageurl": "https://resources.cryptocompare.com/news/16/9053326.jpeg",
            "lang": "EN",
            "published_on": 1675864934,
            "source": "cointelegraph",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/cointelegraph.png",
                "lang": "EN",
                "name": "CoinTelegraph"
            },
            "tags": "CBDC|Reserve Bank of India|India|Digital Currency",
            "title": "India in ‘no hurry’ for CBDC as digital rupee pilot onboards 50k users",
            "upvotes": "0",
            "url": "https://cointelegraph.com/news/india-in-no-hurry-for-cbdc-as-digital-rupee-pilot-onboards-50k-users"
        },
        {
            "body": "Voyager Digital has subpoenaed several executives from FTX and Alameda, including Sam Bankman-Fried and Caroline Ellison. The bankrupt crypto lender’s lawyers have requested documents related to communication between FTX and the SEC. Bankrupt crypto lender Voyager Digital has served subpoenas to several FTX executives and its sister firm, Alameda Research. These executives include founder and",
            "categories": "REGULATION",
            "downvotes": "0",
            "guid": "https://ambcrypto.com/?p=289671",
            "id": "9053143",
            "imageurl": "https://images.cryptocompare.com/news/default/ambcrypto.png",
            "lang": "EN",
            "published_on": 1675864849,
            "source": "ambcrypto",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/ambcrypto.png",
                "lang": "EN",
                "name": "AMB Crypto"
            },
            "tags": "News|News 1|Social|Trading View|ftx|FTX collapse|Investo|Sam Bankman Fried|SEC",
            "title": "Voyager Digital subpoenas SBF and others from FTX and Alameda",
            "upvotes": "0",
            "url": "https://ambcrypto.com/voyager-digital-subpoenas-sbf-and-others-from-ftx-and-alameda/"
        },
        {
            "body": "Data science careers tend to have high salaries — often over six figures — as the demand for skilled professionals in this field continues to grow.",
            "categories": "OTHER",
            "downvotes": "0",
            "guid": "https://cointelegraph.com/news/5-high-paying-careers-in-data-science",
            "id": "9053264",
            "imageurl": "https://resources.cryptocompare.com/news/16/9053264.jpeg",
            "lang": "EN",
            "published_on": 1675864800,
            "source": "cointelegraph",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/cointelegraph.png",
                "lang": "EN",
                "name": "CoinTelegraph"
            },
            "tags": "Big Data|Data Science|Machine Learning|Python",
            "title": "5 high-paying careers in data science",
            "upvotes": "0",
            "url": "https://cointelegraph.com/news/5-high-paying-careers-in-data-science"
        },
        {
            "body": "More than 315 million XRP moved over past 24 hours",
            "categories": "XRP",
            "downvotes": "0",
            "guid": "https://u.today/millions-of-xrp-on-move-what-are-whales-up-to",
            "id": "9053140",
            "imageurl": "https://resources.cryptocompare.com/news/64/9053140.jpeg",
            "lang": "EN",
            "published_on": 1675864680,
            "source": "utoday",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/utoday.png",
                "lang": "EN",
                "name": "U.Today"
            },
            "tags": "ripple",
            "title": "Millions of XRP on the Move, What are the Whales Up to",
            "upvotes": "0",
            "url": "https://u.today/millions-of-xrp-on-move-what-are-whales-up-to"
        },
        {
            "body": "Through a signed letter, United State Senators Elizabeth Warren, Edward J Markey, Jeffrey A. Merkley, and Richard J Durbin, among others, requested the US Environmental Protection Agency (EPA) and the Department of Energy (DOE) to disclose the details of energy consumption and the greenhouse gas emission of crypto mining companies. Notably, the letter revealed that The post Crypto Mining Poses Environment Pollution Threat: US Senators appeared first on Coin Edition .",
            "categories": "MINING",
            "downvotes": "0",
            "guid": "https://coinedition.com/?p=248929",
            "id": "9052961",
            "imageurl": "https://resources.cryptocompare.com/news/7/default.png",
            "lang": "EN",
            "published_on": 1675864500,
            "source": "coinquora",
            "source_info": {
                "img": "https://resources.cryptocompare.com/news/7/default.png",
                "lang": "EN",
                "name": "Coin Edition"
            },
            "tags": "News|Mining",
            "title": "Crypto Mining Poses Environment Pollution Threat: US Senators",
            "upvotes": "0",
            "url": "https://coinedition.com/crypto-mining-poses-environment-pollution-threat-us-senators/"
        },
        {
            "body": "The new regulations imposed by Dubai's VARA disallowed the employment of privacy coins, such as XMR and ZEC.",
            "categories": "XMR|ZEC",
            "downvotes": "0",
            "guid": "https://cryptopotato.com/?p=236899",
            "id": "9052822",
            "imageurl": "https://resources.cryptocompare.com/news/27/9052822.jpeg",
            "lang": "EN",
            "published_on": 1675864248,
            "source": "cryptopotato",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/cryptopotato.png",
                "lang": "EN",
                "name": "Crypto Potato"
            },
            "tags": "AA News|Crypto News|XMRBTC|XMRUSD|ZECBTC|ZECUSD|Dubai|Monero|Zcash",
            "title": "Dubai Forbids Operations With Monero, Zcash, and Other Privacy Coins",
            "upvotes": "0",
            "url": "https://cryptopotato.com/dubai-forbids-operations-with-monero-zcash-and-other-privacy-coins/"
        },
        {
            "body": "In a partnership ceremony at the LEAP 2023 conference in Saudi Arabia, the Sandbox entered into an MOU with the government of Saudi Arabia for future metaverse development.",
            "categories": "SAND",
            "downvotes": "0",
            "guid": "https://cointelegraph.com/news/saudi-arabia-partners-with-the-sandbox-for-future-metaverse-plans",
            "id": "9052775",
            "imageurl": "https://resources.cryptocompare.com/news/16/9052775.jpeg",
            "lang": "EN",
            "published_on": 1675864105,
            "source": "cointelegraph",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/cointelegraph.png",
                "lang": "EN",
                "name": "CoinTelegraph"
            },
            "tags": "Web3|Metaverse|Saudi Arabia|Sandbox",
            "title": "Saudi Arabia partners with The Sandbox for future metaverse plans",
            "upvotes": "0",
            "url": "https://cointelegraph.com/news/saudi-arabia-partners-with-the-sandbox-for-future-metaverse-plans"
        },
        {
            "body": "The post MicroStrategy’s Bitcoin Maximalism Wavers, Shift To Ethereum? appeared first on Coinpedia Fintech News One of the leading Bitcoin network supporters Michael Saylor, the executive chairman and a co-founder of MicroStrategy, could be losing steam as a maxi. According to a recently revealed audio clip by altcoin daily, a crypto YouTube channel with over 1.29 million subscribers, Saylor said that he is waiting for the company’s Bitcoin holdings to …",
            "categories": "BTC|ETH|ALTCOIN",
            "downvotes": "0",
            "guid": "https://coinpedia.org/?p=181067",
            "id": "9052654",
            "imageurl": "https://images.cryptocompare.com/news/default/coinpedia.png",
            "lang": "EN",
            "published_on": 1675864091,
            "source": "coinpedia",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/coinpedia.png",
                "lang": "EN",
                "name": "coinpedia"
            },
            "tags": "News|Crypto news",
            "title": "MicroStrategy’s Bitcoin Maximalism Wavers, Shift To Ethereum?",
            "upvotes": "0",
            "url": "https://coinpedia.org/news/microstrategys-bitcoin-maximalism-wavers-shift-to-ethereum/"
        },
        {
            "body": "The post Bitcoin Price Likely to Follow Fetch.ai (FET) Footsteps and Rally to ATH? appeared first on Coinpedia Fintech News The Bitcoin price has been displaying a bullish trend, characterized by higher highs and higher lows, since reaching $24,000 last week. Despite current market indicators suggesting neutrality, potential volatility could drive the price to a new all-time high. The bullish sentiment is on the brink of overtaking the weekly bearish momentum, should the upward trend …",
            "categories": "TRADING|BTC|ALTCOIN|MARKET",
            "downvotes": "0",
            "guid": "https://coinpedia.org/?p=181064",
            "id": "9052229",
            "imageurl": "https://images.cryptocompare.com/news/default/coinpedia.png",
            "lang": "EN",
            "published_on": 1675863421,
            "source": "coinpedia",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/coinpedia.png",
                "lang": "EN",
                "name": "coinpedia"
            },
            "tags": "Altcoins|Price Analysis",
            "title": "Bitcoin Price Likely to Follow Fetch.ai (FET) Footsteps and Rally to ATH?",
            "upvotes": "0",
            "url": "https://coinpedia.org/altcoin/bitcoin-price-likely-to-follow-fetch-ai-fet-footsteps-and-rally-to-ath/"
        },
        {
            "body": "Institutional investors are prioritizing Bitcoin over Ethereum in 2023. The report was published by the digital asset analysis firm Arcane Research. According to the research firm, the open interest of Bitcoin futures climbed 6% in Chicago Mercantile Exchange (CME), while Ethereum’s future has declined by more than 25% in the last month. The data from …",
            "categories": "BTC|ETH|BUSINESS|EXCHANGE|MARKET",
            "downvotes": "0",
            "guid": "https://www.cryptonewsz.com/?p=187178",
            "id": "9052098",
            "imageurl": "https://images.cryptocompare.com/news/default/cryptonewsz.png",
            "lang": "EN",
            "published_on": 1675863136,
            "source": "cryptonewsz",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/cryptonewsz.png",
                "lang": "EN",
                "name": "CryptoNewsZ"
            },
            "tags": "Cryptocurrency|Cryptocurrency News",
            "title": "Institutional Investors prefer Bitcoin over Ethereum now",
            "upvotes": "0",
            "url": "https://www.cryptonewsz.com/institutional-investors-prefer-bitcoin-over-ethereum-now/"
        },
        {
            "body": "The post Top Analyst Issues Warning On FET Price Dramatic Swing appeared first on Coinpedia Fintech News The cryptocurrency, Fetch.ai (FET), has been the center of attention for investors, traders, and market experts following its phenomenal price increase over the last month. With a growth of 262% in the past month and a half, it has become one of the best-performing cryptocurrencies in 2023. However, the current outlook appears bleak. At the …",
            "categories": "TRADING|ALTCOIN|BUSINESS|MARKET",
            "downvotes": "0",
            "guid": "https://coinpedia.org/?p=181042",
            "id": "9052039",
            "imageurl": "https://images.cryptocompare.com/news/default/coinpedia.png",
            "lang": "EN",
            "published_on": 1675863088,
            "source": "coinpedia",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/coinpedia.png",
                "lang": "EN",
                "name": "coinpedia"
            },
            "tags": "Altcoins",
            "title": "Top Analyst Issues Warning On FET Price Dramatic Swing",
            "upvotes": "0",
            "url": "https://coinpedia.org/altcoin/top-analyst-issues-warning-on-fet-price-dramatic-swing/"
        },
        {
            "body": "Today, a layer 1 blockchain Core DAO publicly launched its first-ever Airdrop for its native token CORE. Also, the token",
            "categories": "ICO|BLOCKCHAIN|ETH",
            "downvotes": "0",
            "guid": "https://thenewscrypto.com/?p=66124",
            "id": "9052166",
            "imageurl": "https://images.cryptocompare.com/news/default/thenewscrypto.png",
            "lang": "EN",
            "published_on": 1675863081,
            "source": "thenewscrypto",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/thenewscrypto.png",
                "lang": "EN",
                "name": "The News Crypto"
            },
            "tags": "Altcoin News|Blockchain|CORE|Core DAO|ETHEREUM",
            "title": "Core DAO Launched Its CORE Token",
            "upvotes": "0",
            "url": "https://thenewscrypto.com/core-dao-launched-its-core-token/"
        },
        {
            "body": "The SOPR ratio positioned closer to the market bottom as the TRIX signaled an incoming uptrend. BTC holders adhered to self-custody despite January’s profit-taking offer. Bitcoin [BTC] showed immense prowess after the U.S. Federal Reserve Board raised interest rates by 25 basis points. Initially, the king coin led the crypto market decline, but this only",
            "categories": "BTC|MARKET|FIAT|ICO|TRADING|SPONSORED",
            "downvotes": "0",
            "guid": "https://ambcrypto.com/?p=289520",
            "id": "9052035",
            "imageurl": "https://images.cryptocompare.com/news/default/ambcrypto.png",
            "lang": "EN",
            "published_on": 1675863058,
            "source": "ambcrypto",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/ambcrypto.png",
                "lang": "EN",
                "name": "AMB Crypto"
            },
            "tags": "Bitcoin|BTC Trading View|News|News 1|Social|Trading View|Bitcoin SOPR|Bitcoin-FOMC|BTC bullish|featured",
            "title": "Why Bitcoin [BTC] may climb a new bull ladder despite Fed’s resolve",
            "upvotes": "0",
            "url": "https://ambcrypto.com/why-bitcoin-btc-may-enter-a-new-bull-ladder-despite-feds-resolve/"
        },
        {
            "body": "Ethereum closed in on the $1,700 level on Wednesday, as markets reacted to comments from U.S. Federal Reserve Chair Jerome Powell. Speaking after Tuesday’s session, Powell hinted that the Fed could continue to hike rates, should the data show the need for action. Bitcoin was also boosted by the news, climbing back into the $23,000",
            "categories": "ETH|BTC|MARKET|FIAT|TRADING",
            "downvotes": "0",
            "guid": "https://news.bitcoin.com/?p=572893",
            "id": "9052037",
            "imageurl": "https://resources.cryptocompare.com/news/14/9052037.jpeg",
            "lang": "EN",
            "published_on": 1675863004,
            "source": "bitcoin.com",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/bitcoincom.png",
                "lang": "EN",
                "name": "Bitcoin.com"
            },
            "tags": "Market Updates|Analysis|Bitcoin|BTC|ETH|Ethereum",
            "title": "Bitcoin, Ethereum Technical Analysis: ETH Nears $1,700, Fed Prepared to Maintain Rate Hikes",
            "upvotes": "0",
            "url": "https://news.bitcoin.com/bitcoin-ethereum-technical-analysis-eth-nears-1700-fed-prepared-to-maintain-rate-hikes/"
        },
        {
            "body": "Gala was top gainer in January",
            "categories": "OTHER",
            "downvotes": "0",
            "guid": "https://u.today/gala-gala-worth-millions-of-dollars-shifted-by-bankrupt-crypto-lender-details",
            "id": "9052032",
            "imageurl": "https://resources.cryptocompare.com/news/64/9052032.jpeg",
            "lang": "EN",
            "published_on": 1675863000,
            "source": "utoday",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/utoday.png",
                "lang": "EN",
                "name": "U.Today"
            },
            "tags": "Gala",
            "title": "Gala (GALA) Worth Millions of Dollars Shifted by Bankrupt Crypto Lender: Details",
            "upvotes": "0",
            "url": "https://u.today/gala-gala-worth-millions-of-dollars-shifted-by-bankrupt-crypto-lender-details"
        },
        {
            "body": "Ethereum co-founder and ConsenSys founder Joe Lubin says ETH’s relatively stable value through crypto winter is reason to be bullish about Ethereum’s future.",
            "categories": "ETH|TRADING",
            "downvotes": "0",
            "guid": "https://cointelegraph.com/news/consensys-founder-bullish-on-ethereum-following-crypto-winter-performance",
            "id": "9051971",
            "imageurl": "https://resources.cryptocompare.com/news/16/9051971.jpeg",
            "lang": "EN",
            "published_on": 1675863000,
            "source": "cointelegraph",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/cointelegraph.png",
                "lang": "EN",
                "name": "CoinTelegraph"
            },
            "tags": "Ethereum|co-founder|Joe Lubin|ETH|crypto winter|Merge",
            "title": "ConsenSys founder 'bullish' on Ethereum following crypto winter performance",
            "upvotes": "0",
            "url": "https://cointelegraph.com/news/consensys-founder-bullish-on-ethereum-following-crypto-winter-performance"
        },
        {
            "body": "In one of the most recent achievements of its team, Cardano (ADA) ecosystem developer Input Output has launched a fully … Continued The post Cardano team launches public testnet of Ethereum sidechain appeared first on Finbold .",
            "categories": "ADA|ETH",
            "downvotes": "0",
            "guid": "https://finbold.com/?p=98558",
            "id": "9051847",
            "imageurl": "https://images.cryptocompare.com/news/default/finbold.png",
            "lang": "EN",
            "published_on": 1675862707,
            "source": "finbold",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/finbold.png",
                "lang": "EN",
                "name": "Finbold"
            },
            "tags": "Cryptocurrency news|ADA|Cardano|ETH|Ethereum|sidechain",
            "title": "Cardano team launches public testnet of Ethereum sidechain",
            "upvotes": "0",
            "url": "https://finbold.com/cardano-team-launches-public-testnet-of-ethereum-sidechain/"
        },
        {
            "body": "Crypto analytics platform Santiment tweeted that after a positive crypto price action in the month of January, the market can anticipate a dip in February. The platform added that trader skepticism improves the probability of prices rising further. Moreover, Santiment mentioned that prices usually move in the direction the crowd seems most unlikely. According to The post Market Anticipates Dip In February: Santiment On Trader Skepticism appeared first on Coin Edition .",
            "categories": "MARKET|TRADING",
            "downvotes": "0",
            "guid": "https://coinedition.com/?p=248928",
            "id": "9051784",
            "imageurl": "https://resources.cryptocompare.com/news/7/default.png",
            "lang": "EN",
            "published_on": 1675862686,
            "source": "coinquora",
            "source_info": {
                "img": "https://resources.cryptocompare.com/news/7/default.png",
                "lang": "EN",
                "name": "Coin Edition"
            },
            "tags": "Market News|News|Santiment",
            "title": "Market Anticipates Dip In February: Santiment On Trader Skepticism",
            "upvotes": "0",
            "url": "https://coinedition.com/market-anticipates-dip-in-february-santiment-on-trader-skepticism/"
        },
        {
            "body": "Bank of England has made reference to Ripple in its press release while working on digital pound",
            "categories": "FIAT|XRP",
            "downvotes": "0",
            "guid": "https://u.today/ripple-to-help-bank-of-england-build-cbdc-heres-why-it-may-be-so",
            "id": "9051584",
            "imageurl": "https://resources.cryptocompare.com/news/64/9051584.jpeg",
            "lang": "EN",
            "published_on": 1675862280,
            "source": "utoday",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/utoday.png",
                "lang": "EN",
                "name": "U.Today"
            },
            "tags": "Ripple News|XRP",
            "title": "Ripple to Help Bank of England Build CBDC? Here’s Why It May Be So",
            "upvotes": "0",
            "url": "https://u.today/ripple-to-help-bank-of-england-build-cbdc-heres-why-it-may-be-so"
        },
        {
            "body": "The Securities and Exchange Commission is in charge of regulating the United States’ securities markets. In the context of cryptocurrencies, the SEC has taken a cautious approach to regulation, classifying the majority of cryptocurrencies as securities and subjecting them to federal rules. The U.S. government agency released its yearly assessment goals regarding how it will",
            "categories": "REGULATION|EXCHANGE|MARKET",
            "downvotes": "0",
            "guid": "https://bitcoinist.com/?p=216687",
            "id": "9051533",
            "imageurl": "https://resources.cryptocompare.com/news/13/9051533.jpeg",
            "lang": "EN",
            "published_on": 1675862272,
            "source": "bitcoinist",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/bitcoinist.png",
                "lang": "EN",
                "name": "Bitcoinist"
            },
            "tags": "Crypto News|crypto regulation|digital currency|Gary Gensler|SEC|Securities",
            "title": "SEC To Step Up Probe On Firms And Brokers Pitching Crypto",
            "upvotes": "0",
            "url": "https://bitcoinist.com/sec-probe-on-brokers-pitching-crypto/"
        },
        {
            "body": "The post Coinslotty.com Breaks First Milestone of 2023, Celebrates 100 Partner Deals appeared first on Coinpedia Fintech News Stable Tech N.V., a Curacao-based iGaming operator, is celebrating a significant achievement with its flagship crypto casino. In a press briefing published on Yahoo Finance, the company proudly announced 100 closed affiliate deals. To mark this special milestone, the online casino is expressing its gratitude to its partners by showering them with “golden coins” through …",
            "categories": "SPONSORED|TECHNOLOGY",
            "downvotes": "0",
            "guid": "https://coinpedia.org/?p=181031",
            "id": "9051482",
            "imageurl": "https://images.cryptocompare.com/news/default/coinpedia.png",
            "lang": "EN",
            "published_on": 1675862094,
            "source": "coinpedia",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/coinpedia.png",
                "lang": "EN",
                "name": "coinpedia"
            },
            "tags": "PRESS RELEASE",
            "title": "Coinslotty.com Breaks First Milestone of 2023, Celebrates 100 Partner Deals",
            "upvotes": "0",
            "url": "https://coinpedia.org/press-release/coinslotty-com-breaks-first-milestone-of-2023-celebrates-100-partner-deals/"
        },
        {
            "body": "The post Ethereum on Path to Lead the Way to Valhalla – Says Chris Burniske appeared first on Coinpedia Fintech News The Ethereum (ETH) price has faced difficulty in breaking the stalemate between buyers and sellers, despite experiencing a 30% increase year-to-date. The leading smart contract and decentralized finance ecosystem could surpass its August 2021 peak of approximately $2,000 if buyers gain momentum in the coming weeks. Nevertheless, the ETH bulls face a macro downtrend that …",
            "categories": "ETH|TRADING",
            "downvotes": "0",
            "guid": "https://coinpedia.org/?p=181035",
            "id": "9051197",
            "imageurl": "https://images.cryptocompare.com/news/default/coinpedia.png",
            "lang": "EN",
            "published_on": 1675861843,
            "source": "coinpedia",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/coinpedia.png",
                "lang": "EN",
                "name": "coinpedia"
            },
            "tags": "Ethereum|Crypto news",
            "title": "Ethereum on Path to Lead the Way to Valhalla – Says Chris Burniske",
            "upvotes": "0",
            "url": "https://coinpedia.org/ethereum/ethereum-on-path-to-lead-the-way-to-valhalla-says-chris-burniske/"
        },
        {
            "body": "Bitcoin exposure may be down 77.5%, but Tesla still has the third-largest BTC holdings of a publicly listed company.",
            "categories": "BTC",
            "downvotes": "0",
            "guid": "https://cointelegraph.com/news/happy-bitcoin-anniversary-tesla-elon-musk-firm-still-hodls-9-7k-btc",
            "id": "9051360",
            "imageurl": "https://resources.cryptocompare.com/news/16/9051360.jpeg",
            "lang": "EN",
            "published_on": 1675861830,
            "source": "cointelegraph",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/cointelegraph.png",
                "lang": "EN",
                "name": "CoinTelegraph"
            },
            "tags": "Bitcoin|BTC|Tesla|Elon Musk",
            "title": "Happy Bitcoin anniversary, Tesla — Elon Musk firm still hodls 9.7K BTC",
            "upvotes": "0",
            "url": "https://cointelegraph.com/news/happy-bitcoin-anniversary-tesla-elon-musk-firm-still-hodls-9-7k-btc"
        },
        {
            "body": "The Sandbox (SAND) experienced a surge of 30% following the announcement of a strategic partnership between itself and Saudi Metaverse.",
            "categories": "SAND|TRADING",
            "downvotes": "0",
            "guid": "https://thenewscrypto.com/?p=66121",
            "id": "9052165",
            "imageurl": "https://images.cryptocompare.com/news/default/thenewscrypto.png",
            "lang": "EN",
            "published_on": 1675861775,
            "source": "thenewscrypto",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/thenewscrypto.png",
                "lang": "EN",
                "name": "The News Crypto"
            },
            "tags": "Metaverse|SAND|SandBox",
            "title": "Saudi Metaverse Partnership Pushed Sandbox (Sand) Price by 30%",
            "upvotes": "0",
            "url": "https://thenewscrypto.com/saudi-metaverse-partnership-pushed-sandbox-sand-price-by-30/"
        },
        {
            "body": "Summary: The blockchain-powered sports fan token launched its own layer 1 decentralized network on Tuesday. Chiliz’s L1 chain is compatible with the Ethereum Virtual Machine program, allowing developers to broadcast smart contract codes on Ethereum’s blockchain. The protocol’s token CHZ pumped as high as 20% on the news. Blockchain sports coin Chiliz announced the launch of its brand new layer 1 decentralized chain aimed at driving growth around non-fungible tokens (NFTs) and on-chain gaming tied to reach world sports franchises.",
            "categories": "BLOCKCHAIN|ICO|ETH",
            "downvotes": "0",
            "guid": "https://en.ethereumworldnews.com/?p=580841",
            "id": "9050964",
            "imageurl": "https://images.cryptocompare.com/news/default/ethereumworldnews.png",
            "lang": "EN",
            "published_on": 1675861453,
            "source": "ethereumworldnews",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/ethereumworldnews.png",
                "lang": "EN",
                "name": "Ethereum World News"
            },
            "tags": "Blockchain News|Cryptocurrency|News|NFTs|blockchain|Chiliz|CHZ",
            "title": "Chiliz (CHZ) Debuts EVM-Compatible L1 Blockchain",
            "upvotes": "0",
            "url": "https://en.ethereumworldnews.com/chiliz-chz-debuts-evm-blockchain/"
        },
        {
            "body": "The latest price moves in bitcoin (BTC) and crypto markets in context for Feb. 8 2023. First Mover is CoinDesk’s daily newsletter that contextualizes the latest actions in the crypto markets.",
            "categories": "MARKET|BTC|SAND|TRADING",
            "downvotes": "0",
            "guid": "EU7MKWLUYNBKHLRN33E7USP7DM",
            "id": "9051220",
            "imageurl": "https://resources.cryptocompare.com/news/5/9051220.jpeg",
            "lang": "EN",
            "published_on": 1675861260,
            "source": "coindesk",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/coindesk.png",
                "lang": "EN",
                "name": "CoinDesk"
            },
            "tags": "Markets",
            "title": "First Mover Americas: The Sandbox Is Up on Saudi Arabia Partnership News",
            "upvotes": "0",
            "url": "https://www.coindesk.com/markets/2023/02/08/first-mover-americas-the-sandbox-is-up-on-saudi-arabia-partnership-news/?utm_medium=referral&utm_source=rss&utm_campaign=headlines"
        },
        {
            "body": "Miami-based crypto startup VRRB Labs, which is developing a Layer 1 blockchain network, raised $1.4 million in a pre-seed funding round.",
            "categories": "BLOCKCHAIN|ICO",
            "downvotes": "0",
            "guid": "https://www.theblock.co/post/209609",
            "id": "9051972",
            "imageurl": "https://images.cryptocompare.com/news/default/theblock.png",
            "lang": "EN",
            "published_on": 1675861237,
            "source": "theblock",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/theblock.png",
                "lang": "EN",
                "name": "TheBlock"
            },
            "tags": "Companies|Crypto Ecosystems|Crypto infrastructure|Deals|Layer 1s|Startups|Venture Capital|exclusive|Seed & Pre-Seed",
            "title": "VRRB Labs raises pre-seed round at $20 million valuation as it builds its own Layer 1",
            "upvotes": "0",
            "url": "https://www.theblock.co/post/209609/vrrb-labs-raises-pre-seed-round-at-20-million-valuation-as-it-builds-its-own-layer-1?utm_source=cryptocompare&utm_medium=rss"
        },
        {
            "body": "Data shows the Bitcoin volume dominance of Binance has hit a new all-time high as activity on other exchanges has fallen recently. Binance Accounts For 95% Of Bitcoin Volume Among Bitwise 10 Exchanges According to the latest weekly report from Arcane Research, trading volume excluding Binance has declined 42% during the past week. The “daily",
            "categories": "BTC|EXCHANGE|TRADING",
            "downvotes": "0",
            "guid": "https://bitcoinist.com/?p=216670",
            "id": "9050863",
            "imageurl": "https://resources.cryptocompare.com/news/13/9050863.jpeg",
            "lang": "EN",
            "published_on": 1675861204,
            "source": "bitcoinist",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/bitcoinist.png",
                "lang": "EN",
                "name": "Bitcoinist"
            },
            "tags": "Bitcoin|binance|bitcoin|Bitcoin Binance Volume|Bitcoin trading volume|Bitcoin Volume|btcusd|Crypto exchange Binance",
            "title": "Bitcoin Volume On Exchanges Plunges, Binance’s Dominance Reaches ATH",
            "upvotes": "0",
            "url": "https://bitcoinist.com/bitcoin-volume-exchanges-plunges-binances-ath/"
        },
        {
            "body": "We’re only a few weeks into the new year, but bitcoin is keeping up its good vibes and experiencing further boosts to its price. Bitcoin Is Still Booming Live Bitcoin News has already published a few articles detailing the jumps of the world’s number one digital currency by market cap since the beginning of January. ... The post Bitcoin Experiences Another Surge, Now at $21K appeared first on Live Bitcoin News .",
            "categories": "BTC|MARKET|TRADING",
            "downvotes": "0",
            "guid": "https://www.livebitcoinnews.com/?p=76551",
            "id": "9050747",
            "imageurl": "https://images.cryptocompare.com/news/default/livebitcoinnews.png",
            "lang": "EN",
            "published_on": 1675861200,
            "source": "livebitcoinnews",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/livebitcoinnews.png",
                "lang": "EN",
                "name": "Live Bitcoin News"
            },
            "tags": "Bitcoin News|News|bitcoin|bitcoin price|James Butterfill",
            "title": "Bitcoin Experiences Another Surge, Now at $21K",
            "upvotes": "0",
            "url": "https://www.livebitcoinnews.com/bitcoin-experiences-another-surge-now-at-21k/"
        },
        {
            "body": "While the current environment for Bitcoin miners may be challenging, there are emerging opportunities for investment.",
            "categories": "BTC|BUSINESS",
            "downvotes": "0",
            "guid": "https://bitcoinmagazine.com/business/bitcoin-miners-uncertain-in-2023",
            "id": "9050781",
            "imageurl": "https://images.cryptocompare.com/news/default/bitcoinmagazine.png",
            "lang": "EN",
            "published_on": 1675861200,
            "source": "bitcoinmagazine",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/bitcoinmagazine.png",
                "lang": "EN",
                "name": "Bitcoin Magazine"
            },
            "tags": "Hash Price|Business|Bitcoin mining|hash rate|Opinion",
            "title": "Bitcoin Miners Chart An Uncertain Path In 2023, But Opportunity Calls",
            "upvotes": "0",
            "url": "https://bitcoinmagazine.com/business/bitcoin-miners-uncertain-in-2023"
        },
        {
            "body": "The new crypto classification effort aims to help investors and regulators spot potential crypto failures like those seen in 2022.",
            "categories": "BUSINESS",
            "downvotes": "0",
            "guid": "https://cointelegraph.com/news/coingecko-and-21shares-propose-global-crypto-classification-standard",
            "id": "9050928",
            "imageurl": "https://resources.cryptocompare.com/news/16/9050928.jpeg",
            "lang": "EN",
            "published_on": 1675861200,
            "source": "cointelegraph",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/cointelegraph.png",
                "lang": "EN",
                "name": "CoinTelegraph"
            },
            "tags": "Cryptocurrencies|CoinGecko|Research|Education",
            "title": "CoinGecko and 21Shares propose global crypto classification standard",
            "upvotes": "0",
            "url": "https://cointelegraph.com/news/coingecko-and-21shares-propose-global-crypto-classification-standard"
        },
        {
            "body": "Sometimes we are so engrossed in internecine warfare among the chains and tokens that we fail to realize the regular folks who have no idea what we are talking about.",
            "categories": "ICO",
            "downvotes": "0",
            "guid": "https://cointelegraph.com/innovation-circle/the-war-among-blockchains-should-stop-to-speed-up-adoption",
            "id": "9051171",
            "imageurl": "https://resources.cryptocompare.com/news/16/9051171.jpeg",
            "lang": "EN",
            "published_on": 1675861200,
            "source": "cointelegraph",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/cointelegraph.png",
                "lang": "EN",
                "name": "CoinTelegraph"
            },
            "tags": "",
            "title": "The war among blockchains should stop to speed up adoption",
            "upvotes": "0",
            "url": "https://cointelegraph.com/innovation-circle/the-war-among-blockchains-should-stop-to-speed-up-adoption"
        },
        {
            "body": "Lawyers have challenged a potentially consequential move from the U.S. Securities and Exchange Commission (SEC) to build a list of crypto tokens it considers unregistered securities.",
            "categories": "ICO|REGULATION|EXCHANGE",
            "downvotes": "0",
            "guid": "WTTLCGGZVNHM3D7C7KPBZ5V3MI",
            "id": "9051218",
            "imageurl": "https://resources.cryptocompare.com/news/5/9051218.jpeg",
            "lang": "EN",
            "published_on": 1675861200,
            "source": "coindesk",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/coindesk.png",
                "lang": "EN",
                "name": "CoinDesk"
            },
            "tags": "Policy",
            "title": "Will the SEC Convince a Court It’s Right To Label These Tokens As Securities?",
            "upvotes": "0",
            "url": "https://www.coindesk.com/policy/2023/02/08/will-the-sec-convince-a-court-its-right-to-label-these-tokens-as-securities/?utm_medium=referral&utm_source=rss&utm_campaign=headlines"
        },
        {
            "body": "Cryptocurrency is an incredibly broad and diverse field, with a huge array of wholly different assets, making the industry an intimidating one to enter.",
            "categories": "BUSINESS",
            "downvotes": "0",
            "guid": "S2JQV6K3OFD65AKW7VUGQ4VPVA",
            "id": "9051219",
            "imageurl": "https://resources.cryptocompare.com/news/5/9051219.jpeg",
            "lang": "EN",
            "published_on": 1675861200,
            "source": "coindesk",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/coindesk.png",
                "lang": "EN",
                "name": "CoinDesk"
            },
            "tags": "Business",
            "title": "Crypto Classification Seeks to Make Industry More Welcoming to TradFi Participants",
            "upvotes": "0",
            "url": "https://www.coindesk.com/business/2023/02/08/crypto-classification-seeks-to-make-industry-more-welcoming-to-tradfi-participants/?utm_medium=referral&utm_source=rss&utm_campaign=headlines"
        },
        {
            "body": "Prominent cryptocurrency influencer and entrepreneur believes in NFT technology",
            "categories": "TECHNOLOGY",
            "downvotes": "0",
            "guid": "https://u.today/arthur-hayes-becomes-biggest-holder-of-this-asset",
            "id": "9050625",
            "imageurl": "https://resources.cryptocompare.com/news/64/9050625.jpeg",
            "lang": "EN",
            "published_on": 1675860900,
            "source": "utoday",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/utoday.png",
                "lang": "EN",
                "name": "U.Today"
            },
            "tags": "LooksRare",
            "title": "Arthur Hayes Become Biggets Holder of This Asset",
            "upvotes": "0",
            "url": "https://u.today/arthur-hayes-becomes-biggest-holder-of-this-asset"
        },
        {
            "body": "United Kingdom intends to launch a central bank digital currency (CBDC) as they issued a consultation paper outlining the proposed",
            "categories": "FIAT",
            "downvotes": "0",
            "guid": "https://thenewscrypto.com/?p=66115",
            "id": "9052164",
            "imageurl": "https://images.cryptocompare.com/news/default/thenewscrypto.png",
            "lang": "EN",
            "published_on": 1675860768,
            "source": "thenewscrypto",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/thenewscrypto.png",
                "lang": "EN",
                "name": "The News Crypto"
            },
            "tags": "Bitcoin News",
            "title": "Bank of England Launches Digital Pound CBDC Project with Limitation",
            "upvotes": "0",
            "url": "https://thenewscrypto.com/bank-of-england-launches-digital-pound-cbdc-project-with-limitation/"
        },
        {
            "body": "The cryptocurrency market has experienced a massive influx of capital in 2023, helping the sector take initial steps towards exiting … Continued The post $300 billion inflows global crypto market in 2023; Is the rally sustainable? appeared first on Finbold .",
            "categories": "MARKET|BTC|TRADING",
            "downvotes": "0",
            "guid": "https://finbold.com/?p=98549",
            "id": "9050501",
            "imageurl": "https://images.cryptocompare.com/news/default/finbold.png",
            "lang": "EN",
            "published_on": 1675860723,
            "source": "finbold",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/finbold.png",
                "lang": "EN",
                "name": "Finbold"
            },
            "tags": "Cryptocurrency news|Bitcoin|BTC|cryptocurrency",
            "title": "$300 billion inflows global crypto market in 2023; Is the rally sustainable?",
            "upvotes": "0",
            "url": "https://finbold.com/300-billion-inflows-global-crypto-market-in-2023-is-the-rally-sustainable/"
        },
        {
            "body": "Chris Blec, a popular crypto influencer who describes himself as a fierce advocate for immutable decentralized technology, has alleged that the decentralized finance (DeFi) industry is colluding to hide a key vulnerability associated with Chainlink. According to Blec, the developers, decentralized autonomous organizations (DAO) and venture capitalists, and others in the DeFi space are colluding, The post Crypto Influencer Claims Chainlink’s Multisig May Destroy DeFi appeared first on Coin Edition .",
            "categories": "LINK|TECHNOLOGY",
            "downvotes": "0",
            "guid": "https://coinedition.com/?p=248898",
            "id": "9050439",
            "imageurl": "https://resources.cryptocompare.com/news/7/default.png",
            "lang": "EN",
            "published_on": 1675860600,
            "source": "coinquora",
            "source_info": {
                "img": "https://resources.cryptocompare.com/news/7/default.png",
                "lang": "EN",
                "name": "Coin Edition"
            },
            "tags": "News|Chainlink (LINK)|DeFi News",
            "title": "Crypto Influencer Claims Chainlink’s Multisig May Destroy DeFi",
            "upvotes": "0",
            "url": "https://coinedition.com/crypto-influencer-claims-chainlinks-multisig-may-destroy-defi/"
        },
        {
            "body": "The infamous Terra founder has been in hot water for nearly a year, but the cat and mouse game continues. Continue reading Fugitive Founder Do Kwon Followed by South Korean Sleuths to Serbia at DailyCoin.",
            "categories": "ALTCOIN|LUNC",
            "downvotes": "0",
            "guid": "https://dailycoin.com/?p=90069",
            "id": "9052618",
            "imageurl": "https://images.cryptocompare.com/news/default/dailycoin.png",
            "lang": "EN",
            "published_on": 1675860341,
            "source": "dailycoin",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/dailycoin.png",
                "lang": "EN",
                "name": "Daily Coin"
            },
            "tags": "Altcoins|Hacks and Scams|zz_index|zz_popular|zz_top|ZZZ Editors' Picks|ZZZ Native|Do Kwon|Terra (LUNA)|Terra (UST)|Terra Luna Classic (LUNC)",
            "title": "Fugitive Founder Do Kwon Followed by South Korean Sleuths to Serbia",
            "upvotes": "0",
            "url": "https://dailycoin.com/chase-terra-luna-founder-do-kwon-in-serbia/"
        },
        {
            "body": "The post Ethereum Price Analysis: ETH Price Secretly Rising to These Levels in February 2023 appeared first on Coinpedia Fintech News Ethereum’s price has been trading flat for the past few days. The price is not offering any clue like Bitcoin depending on which the further price action could have determined. However, judging from the market sentiment, it can be assumed that the current trade setup for the ETH price is bullish and may head beyond …",
            "categories": "TRADING|ETH|MARKET|BTC|ICO",
            "downvotes": "0",
            "guid": "https://coinpedia.org/?p=181026",
            "id": "9050220",
            "imageurl": "https://images.cryptocompare.com/news/default/coinpedia.png",
            "lang": "EN",
            "published_on": 1675860331,
            "source": "coinpedia",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/coinpedia.png",
                "lang": "EN",
                "name": "coinpedia"
            },
            "tags": "Price Analysis|Ethereum",
            "title": "Ethereum Price Analysis: ETH Price Secretly Rising to These Levels in February 2023",
            "upvotes": "0",
            "url": "https://coinpedia.org/price-analysis/ethereum-price-analysis-eth-price-secretly-rising-to-these-levels-in-february-2023/"
        },
        {
            "body": "A Dogecoin (DOGE) wallet is suddenly re-awakening after more than nine years of hibernation to realize a massive increase in the value of its holdings. According to data from crypto whale tracker Whale Alert, the dormant address, which was holding 2,043,137 DOGE, unloaded the tokens over the weekend to pocket exponential gains. The holder accumulated The post Dogecoin (DOGE) Wallet Abruptly Comes to Life After Nine Years of Hibernation appeared first on The Daily Hodl .",
            "categories": "DOGE|ALTCOIN|ICO|TRADING",
            "downvotes": "0",
            "guid": "https://dailyhodl.com/?p=234602",
            "id": "9050193",
            "imageurl": "https://images.cryptocompare.com/news/default/dailyhodl.png",
            "lang": "EN",
            "published_on": 1675860329,
            "source": "dailyhodl",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/dailyhodl.png",
                "lang": "EN",
                "name": "The Daily Hodl"
            },
            "tags": "Altcoins|Trading|Blockchair|Crypto|crypto wallet|doge|dogecoin|IntoTheBlock|Libdogecoin|News",
            "title": "Dogecoin (DOGE) Wallet Abruptly Comes to Life After Nine Years of Hibernation",
            "upvotes": "0",
            "url": "https://dailyhodl.com/2023/02/08/dogecoin-doge-wallet-abruptly-comes-to-life-after-nine-years-of-hibernation/"
        },
        {
            "body": "Contributors at Lido have come up with Lido V2, a step to further decentralize Ethereum. Lido V2 is being termed the biggest upgrade to date and an important step in the direction of decentralization. Lido V2 centers around Staking Routers and Withdrawals as the two major upgrades. Staking Router is a new modular architecture that …",
            "categories": "BLOCKCHAIN|ETH",
            "downvotes": "0",
            "guid": "https://www.cryptonewsz.com/?p=187172",
            "id": "9050241",
            "imageurl": "https://images.cryptocompare.com/news/default/cryptonewsz.png",
            "lang": "EN",
            "published_on": 1675860324,
            "source": "cryptonewsz",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/cryptonewsz.png",
                "lang": "EN",
                "name": "CryptoNewsZ"
            },
            "tags": "Blockchain|Blockchain News",
            "title": "Lido presents its largest upgrade – Lido V2",
            "upvotes": "0",
            "url": "https://www.cryptonewsz.com/lido-presents-its-largest-upgrade-lido-v2/"
        },
        {
            "body": "The Sandbox token surged following its deal with Saudi Arabia.",
            "categories": "SAND|ICO|MARKET",
            "downvotes": "0",
            "guid": "https://www.theblock.co/post/209630",
            "id": "9049828",
            "imageurl": "https://images.cryptocompare.com/news/default/theblock.png",
            "lang": "EN",
            "published_on": 1675859828,
            "source": "theblock",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/theblock.png",
                "lang": "EN",
                "name": "TheBlock"
            },
            "tags": "Art & Collectibles|Crypto Ecosystems|Equities|Macro|Markets|Metaverse|Metaverse & NFT|Organizations|People|Token Projects|Web3|breaking|The Sandbox",
            "title": "SAND token jumps over 20% following metaverse discussions with Saudi Arabia",
            "upvotes": "0",
            "url": "https://www.theblock.co/post/209630/sand-token-jumps-over-20-following-metaverse-discussions-with-saudi-arabia?utm_source=cryptocompare&utm_medium=rss"
        },
        {
            "body": "The post Bankruptcy Proceedings Come At A High Cost For FTX, Law Firm To Earn Millions appeared first on Coinpedia Fintech News The FTX bankruptcy case has proved to be a lucrative opportunity for Sullivan & Cromwell, a well-known law firm, as it is expected to earn millions in fees for handling the fallen crypto empire’s finances. According to a recent court filing, Sullivan & Cromwell has already billed them $7.5 million for just 19 days of …",
            "categories": "REGULATION",
            "downvotes": "0",
            "guid": "https://coinpedia.org/?p=181023",
            "id": "9049704",
            "imageurl": "https://images.cryptocompare.com/news/default/coinpedia.png",
            "lang": "EN",
            "published_on": 1675859602,
            "source": "coinpedia",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/coinpedia.png",
                "lang": "EN",
                "name": "coinpedia"
            },
            "tags": "News|Crypto news",
            "title": "Bankruptcy Proceedings Come At A High Cost For FTX, Law Firm To Earn Millions",
            "upvotes": "0",
            "url": "https://coinpedia.org/news/bankruptcy-proceedings-come-at-a-high-cost-for-ftx-law-firm-to-earn-millions/"
        },
        {
            "body": "Shibarium to be utilized by freelance marketplace to offer crypto payment solutions",
            "categories": "OTHER",
            "downvotes": "0",
            "guid": "https://u.today/shibarium-to-power-payments-on-crypto-freelance-marketplace-details",
            "id": "9049702",
            "imageurl": "https://resources.cryptocompare.com/news/64/9049702.jpeg",
            "lang": "EN",
            "published_on": 1675859520,
            "source": "utoday",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/utoday.png",
                "lang": "EN",
                "name": "U.Today"
            },
            "tags": "Shibarium",
            "title": "Shibarium To Power Payments on Crypto Freelance Marketplace: Details",
            "upvotes": "0",
            "url": "https://u.today/shibarium-to-power-payments-on-crypto-freelance-marketplace-details"
        },
        {
            "body": "The report reveals that the node hosting service’s cumulative voting power never reached chain-breaking levels, as detractors previously claimed. Node hosting provider Allnodes has released a transparency report detailing its voting power statistics for Tendermint blockchains to respond further to concerns about its operations, particularly regarding the Terra Classic chain. Allnodes shared the report in The post Allnodes Releases Transparency Report to Further Address Terra Classic Concerns first appeared on The Crypto Basic .",
            "categories": "LUNC|MARKET",
            "downvotes": "0",
            "guid": "https://thecryptobasic.com/?p=41487",
            "id": "9049660",
            "imageurl": "https://images.cryptocompare.com/news/default/thecryptobasic.png",
            "lang": "EN",
            "published_on": 1675859492,
            "source": "thecryptobasic",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/thecryptobasic.png",
                "lang": "EN",
                "name": "The Crypto Basic"
            },
            "tags": "Crypto News|Market|Allnodes|Altcoin News|LUNC|Terra Classic|Terra Luna Classic",
            "title": "Allnodes Releases Transparency Report to Further Address Terra Classic Concerns",
            "upvotes": "0",
            "url": "https://thecryptobasic.com/2023/02/08/allnodes-releases-transparency-report-to-further-address-terra-classic-concerns/?utm_source=rss&#038;utm_medium=rss&#038;utm_campaign=allnodes-releases-transparency-report-to-further-address-terra-classic-concerns"
        },
        {
            "body": "Two South Korean officials traveled to Serbia to track down Do Kwon. The Terraform Labs founder was last reported in Serbia after fleeing Singapore following Terra’s collapse. Two officials from South Korea reportedly traveled to Serbia last week to track down Do Kwon, the man behind Terraform Labs and LUNA. Kwon has been on the",
            "categories": "ASIA|LUNA",
            "downvotes": "0",
            "guid": "https://ambcrypto.com/?p=289611",
            "id": "9049579",
            "imageurl": "https://images.cryptocompare.com/news/default/ambcrypto.png",
            "lang": "EN",
            "published_on": 1675859456,
            "source": "ambcrypto",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/ambcrypto.png",
                "lang": "EN",
                "name": "AMB Crypto"
            },
            "tags": "News|News 1|Social|Trading View|Do Kwon|Investo|South Korea|Terraform Labs",
            "title": "South Korean officials reportedly travel to Balkan nation to find Do Kwon",
            "upvotes": "0",
            "url": "https://ambcrypto.com/south-korean-officials-reportedly-travel-to-balkan-nation-to-find-do-kwon/"
        },
        {
            "body": "A16z didn’t quash a proposal to launch Uniswap onto Binance’s BNB Chain, but that doesn’t mean it couldn’t have.",
            "categories": "UNI|EXCHANGE|TECHNOLOGY",
            "downvotes": "0",
            "guid": "EOQ3O7OG2VHTLOV7AI4UMLV5PA",
            "id": "9049923",
            "imageurl": "https://resources.cryptocompare.com/news/5/9049923.jpeg",
            "lang": "EN",
            "published_on": 1675859400,
            "source": "coindesk",
            "source_info": {
                "img": "https://images.cryptocompare.com/news/default/coindesk.png",
                "lang": "EN",
                "name": "CoinDesk"
            },
            "tags": "Tech",
            "title": "Contentious Uniswap Vote Highlights the Opaqueness of Decentralized Governance",
            "upvotes": "0",
            "url": "https://www.coindesk.com/tech/2023/02/08/contentious-uniswap-vote-highlights-the-opaqueness-of-decentralized-governance/?utm_medium=referral&utm_source=rss&utm_campaign=headlines"
        }
    ],
    "HasWarning": false,
    "Message": "News list successfully returned",
    "Promoted": [],
    "RateLimit": {},
    "Type": 100
}'''

data = json.loads(data)
