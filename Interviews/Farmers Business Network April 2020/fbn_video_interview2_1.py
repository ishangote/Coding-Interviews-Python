"""
System Design URL Shortner:

https://www.example.com/article/asdasd -> https://bit.ly/abc123

URL Shortener

API:
URLShorten(String url) -> String short_url

Func shorten_url(Sting url) -> loads in map key(short_url) : val(long_url)

			Client
		 API -> URLShorten(long_url)


WebServ	    WebServ	   WebServ

Cache			Cache			Cache

DB			DB			DB

Client:API -> URLShorten(long_url)
WebServ:

Check if long_url exists
Return short_url
Else
Call shorten_url(long_url)
Store output in DB & cache
“””
Long = https://www.example.com/article/asdaje

P1: shorten_url(l1) -> random_generator() -> ”abc123” -> storing if conflict -> call random again
P2: shorten_url(l2) -> random_generator() -> ”abc123”

Func check_url_exists(short_url) -> return True if exists else False
Func shorten_url(long_url)
Pseudo:
Hm = {keys(short 6 digit alphanum): values(None, long_url)}
return hm[]
“””

Func shorten_url(long_url):
https://www.example.com/article/asdajesfhbjrhbfjhebfjhsdbfjahsdbfasd -> https://bit.ly/abc123

6 -> alphanumeric characters 
Abc123 -> 
"""