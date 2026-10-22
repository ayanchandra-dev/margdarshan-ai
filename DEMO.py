# demo/search_demo.py
from tinyfish import TinyFish

client = TinyFish()  # reads your TinyFish API key from the environment
result = client.search.query(
    "free skill training batches for school dropouts Delhi",
    location="IN",
    language="en",
)
print(result)
