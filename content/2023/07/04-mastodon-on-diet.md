Title: Putting your Mastodon on a diet
Date: 2023-07-04
Category: Mastodon

I have been preparing to move my Mastodon instance from self-hosted in the cloud to shelf-hosted at home.
Since November 2022, I have accumulated 80+ GB of media and a 1.2GB database - 
this is while having `Media cache retention period` under 
Settings > Administration > Server Settings > Content retention set at `7 days`.

After backing up the database and media, I looked up ways to reduce the amount of data 
I need to download over my 4G connection during the server move and [found a blog post
that solved my query](https://ricard.dev/improving-mastodons-disk-usage/).

While running each command seperately, I noticed 1 million+ statuses,
some 300,000+ photos and 80,000+ header images getting purged.
That's a lot of storage and liability!

After the purge, I now have a ~700MB database and ~26 GB in media.

If I have not interacted with a post in a day, I'm likely not going to.
Hence, setting up the cron script to regularly purge posts and media after 1 day.

Here's my crontab entry:

```crontab
0 */3 * * * /bin/bash /home/mastodon/purge.sh
```

And here's `purge.sh`

```sh
#!/bin/bash

# Prune remote accounts that never interacted with a local user
RAILS_ENV=production /home/mastodon/live/bin/tootctl accounts prune;

# Remove remote statuses that local users never interacted with older than 1 days
RAILS_ENV=production /home/mastodon/live/bin/tootctl statuses remove --days 1;

# Remove media attachments older than 4 days
RAILS_ENV=production /home/mastodon/live/bin/tootctl media remove --days 1;

# Remove all headers (including people I follow)
RAILS_ENV=production /home/mastodon/live/bin/tootctl media remove --remove-headers --include-follows --days 0;

# Remove link previews older than 16 days 
# Not 1 day as they aren't fetched for ~14 days since posted-at date
RAILS_ENV=production /home/mastodon/live/bin/tootctl preview_cards remove --days 16;

# Remove files not linked to any post
RAILS_ENV=production /home/mastodon/live/bin/tootctl media remove-orphans;
```
