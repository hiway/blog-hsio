AUTHOR = "Harshad Sharma"
SITENAME = "Harshad's Blog"
SITEURL = ""
SITELOGO = SITEURL + "/images/profile.png"
FAVICON = SITEURL + "/images/favicon.png"

PATH = "content"
STATIC_PATHS = ["images"]
THEME = "themes/Flex"
PLUGINS = [
    "minchin.pelican.plugins.cname",
    "minchin.pelican.plugins.nojekyll",
]

TIMEZONE = "Asia/Kolkata"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("About", "https://harshad.sharma.io/"),
    ("Fediverse", "https://mastodon.sharma.io/@harshad/"),
    ("Software", "https://github.com/hiway/"),
)

# Social widget
# SOCIAL = (
#     ("You can add links in your config file", "#"),
#     ("Another social link", "#"),
# )

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
