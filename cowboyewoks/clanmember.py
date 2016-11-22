class ClanMember(object):
	
	def __init__(self, tag, name, expLevel, league, trophies, role, clanRank,
				previousClanRank, donations, donationsReceived):
		"""
		Constructor for clan members
		"""
		self.tag = tag
		self.name = name
		self.expLevel = expLevel
		self.league = league
		self.trophies = trophies
		self.role = role
		self.clanRank = clanRank
		self.previousClanRank = previousClanRank
		self.donations = donations
		self.donationsReceived = donationsReceived