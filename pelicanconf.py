AUTHOR = "Harshad Sharma"
SITENAME = "Harshad's Blog"
SITEURL = ""
SITELOGO = SITEURL + "/images/profile.png"
FAVICON = SITEURL + "/images/favicon.png"

ARTICLE_URL = "posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html"
PAGE_URL = "pages/{slug}/"
PAGE_SAVE_AS = "pages/{slug}/index.html"

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
    # ("About", "https://harshad.sharma.io/"),
    # ("Software", "https://github.com/hiway/"),
    ("Fediverse", "https://mastodon.sharma.io/@harshad/"),
    ("Atom Feed", "https://blog.harshad.sharma.io/feeds/all.atom.xml"),
)

# Social widget
# SOCIAL = (
#     ("Fediverse", "https://mastodon.sharma.io/@harshad/"),
# )

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
