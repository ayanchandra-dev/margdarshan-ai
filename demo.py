import sys
from tinyfish import TinyFish

client = TinyFish()  # reads TINYFISH_API_KEY from your environment

if len(sys.argv) > 2 and sys.argv[1] == "fetch":
    print(client.fetch.get_contents(urls=[sys.argv[2]]))
else:
    query = " ".join(sys.argv[1:]) or "free skill training batches for school dropouts in Delhi"
    print("Searching:", query)
    print(client.search.query(query, location="IN", language="en"))
