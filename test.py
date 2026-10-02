#from tool.tavily_tool import tavily_search

from tool.flight_tool import search_flights

res = search_flights("Plan a 7 days Japan trip from India")
print(res)