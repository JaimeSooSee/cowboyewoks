class ClanInfo(object):
	
	def __init__(self, tag, name, location, badgeUrls, clanLevel, clanPoints,
				members, type, requiredTrophies, warFrequency, warWinStreak,
				warWins, warTies, warLosses, isWarLogPublic, description):
		"""Constructor for Clan Info"""
		self.tag = tag
		self.name = name
		self.location = location
		self.badgeUrls = badgeUrls
		self.clanLevel = clanLevel
		self.clanPoints = clanPoints
		self.members = members
		self.type = type
		self.requiredTrophies = requiredTrophies
		self.warFrequency = warFrequency
		self.warWinStreak = warWinStreak
		self.warWins = warWins
		self.warTies = warTies
		self.warLosses = warLosses
		self.isWarLogPublic = isWarLogPublic
		self.description = description