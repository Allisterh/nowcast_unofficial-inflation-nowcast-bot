# Inflation Nowcast Bot
This repo stores data and code for the (unofficial) [Inflation Nowcast Bot](link to acccount later) on Twitter.

## What is this?
This Twitter bot posts the [Federal Reserve Bank of Cleveland's](https://www.clevelandfed.org/) official [CPI inflation nowcast](https://www.clevelandfed.org/indicators-and-data/inflation-nowcasting) for upcoming [CPI releases](https://www.bls.gov/cpi/). For each release, it posts on the last day of the relevant calendar month and then again the night before the official release.

## Why make this?
1. This was something I thought would be useful but did not find in existence.
2. It did not appear the Cleveland Fed had an API and primarily released raw forecasts via its [webpage](https://www.clevelandfed.org/indicators-and-data/inflation-nowcasting).
3. Official Twitter accounts like [@ClevelandFed](https://twitter.com/ClevelandFed) and [@ClevFedResearch](https://twitter.com/ClevFedResearch) did not appear to be sharing nowcasts via Twitter, versus sharing results of the actual releases themselves.
4. As a hedge fund analyst, I noticed how research firms would crop up shortly before CPI releases to tout their inflation prediction models. On top of these models being locked behind paywalls, not all research firms would openly share the historical accuracy of their models. For those that did, the model fits would pale in comparison with the *free* nowcasts from the Cleveland Fed.

# Index:
* **[Preliminary](preliminary):** Outlines background initial steps for the project.
* **[Code](code)**: Stores all the code, from scrapers to containers and more.
