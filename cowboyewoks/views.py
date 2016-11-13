import urllib.request
import json

from cowboyewoks import claninfo
from django.views import generic

class IndexView(generic.ListView):
	template_name = 'index.html'
	context_object_name = 'claninfo'
	model = claninfo
	
	def get_queryset(self):
		"""
		Required for the class
		json.dumps(data, indent=2) - full JSON object
		"""
		req = urllib.request.Request('https://api.clashofclans.com/v1/clans/%23LGCUP8L0')
		req.add_header('Accept', 'application/json')
		req.add_header('authorization', 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjY1N2ZjZmY2LWFhYWItNGE2MC05MzFlLWJjOGVhMzRmNWI3NCIsImlhdCI6MTQ3ODU1OTg3Mywic3ViIjoiZGV2ZWxvcGVyLzI5NDc2YzQyLWJkNTAtMmEzMy01OTQ4LTU5MWIwN2RiNzI2YyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjY0LjIyOC4xOTYuMTAiXSwidHlwZSI6ImNsaWVudCJ9XX0.iaBfy3Re0LR-YSngvy9jfjf2LYCUePr6Ye5_t2l5VVDBEIebbap8aqYj5UNTgqQH7B9hN_nn1lm1_0Mr7auRDA')
		r = urllib.request.urlopen(req)
		data = json.loads(r.read().decode('utf-8'))
		clanInfo = claninfo.ClanInfo(data["tag"], data["name"], data["location"], data["badgeUrls"],
							data["clanLevel"], data["clanPoints"], data["members"], data["type"],
							data["requiredTrophies"], data["warFrequency"], data["warWinStreak"],
							data["warWins"], data["warTies"], data["warLosses"], data["isWarLogPublic"],
							data["description"])
		return clanInfo
		