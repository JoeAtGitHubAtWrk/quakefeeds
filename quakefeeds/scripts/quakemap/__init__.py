def main():
    import sys
    from quakefeeds import QuakeFeed

    try:
        level = sys.argv[1]
        period = sys.argv[2]
        filename = sys.argv[3]
    except:
        sys.exit("Usage: python quakemap.py <level> <period> <filename>")

    feed = QuakeFeed(level, period)
    feed.create_google_map(filename, style="titled")