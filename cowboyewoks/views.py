import urllib.request
import json

from cowboyewoks import claninfo, clanmember
from django.views import generic

class IndexView(generic.ListView):
	template_name = 'index.html'
	context_object_name = 'claninfo'
	
	def getClanMembers(self):
		"""
		Gets the clan member information
		"""
		req = urllib.request.Request('https://api.clashofclans.com/v1/clans/%23LGCUP8L0/members')
		req.add_header('Accept', 'application/json')
		req.add_header('authorization', 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjY1N2ZjZmY2LWFhYWItNGE2MC05MzFlLWJjOGVhMzRmNWI3NCIsImlhdCI6MTQ3ODU1OTg3Mywic3ViIjoiZGV2ZWxvcGVyLzI5NDc2YzQyLWJkNTAtMmEzMy01OTQ4LTU5MWIwN2RiNzI2YyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjY0LjIyOC4xOTYuMTAiXSwidHlwZSI6ImNsaWVudCJ9XX0.iaBfy3Re0LR-YSngvy9jfjf2LYCUePr6Ye5_t2l5VVDBEIebbap8aqYj5UNTgqQH7B9hN_nn1lm1_0Mr7auRDA')
		r = urllib.request.urlopen(req)
		data = json.loads(r.read().decode('utf-8'))
		clanMembers = list()
		
		for member in data["items"]:
			clanMember = clanmember.ClanMember(member["tag"], member["name"], member["expLevel"], 
							member["league"], member["trophies"], member["role"], member["clanRank"],
							member["previousClanRank"], member["donations"], member["donationsReceived"])
			clanMembers.append(clanMember)
		return clanMembers
	
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
	
	def get_context_data(self, *args, **kwargs):
		context = super(IndexView, self).get_context_data(*args, **kwargs)
		context['clanmembers'] = self.getClanMembers()
		return context

class ClanMembersView(generic.ListView):
	template_name = 'clan_members.html'
	context_object_name = 'clanmembers'
	
	def get_queryset(self):
		"""
		Gets the clan member information
		"""
		req = urllib.request.Request('https://api.clashofclans.com/v1/clans/%23LGCUP8L0/members')
		req.add_header('Accept', 'application/json')
		req.add_header('authorization', 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjY1N2ZjZmY2LWFhYWItNGE2MC05MzFlLWJjOGVhMzRmNWI3NCIsImlhdCI6MTQ3ODU1OTg3Mywic3ViIjoiZGV2ZWxvcGVyLzI5NDc2YzQyLWJkNTAtMmEzMy01OTQ4LTU5MWIwN2RiNzI2YyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjY0LjIyOC4xOTYuMTAiXSwidHlwZSI6ImNsaWVudCJ9XX0.iaBfy3Re0LR-YSngvy9jfjf2LYCUePr6Ye5_t2l5VVDBEIebbap8aqYj5UNTgqQH7B9hN_nn1lm1_0Mr7auRDA')
		r = urllib.request.urlopen(req)
		data = json.loads(r.read().decode('utf-8'))
		clanMembers = data["items"]
		
		"""for member in data["items"]:
			clanMember = clanmember.ClanMember(member["tag"], member["name"], member["expLevel"], 
							member["league"], member["trophies"], member["role"], member["clanRank"],
							member["previousClanRank"], member["donations"], member["donationsReceived"])
			clanMembers.append(clanMember)"""
		return clanMembers