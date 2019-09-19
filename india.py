import requests
import json
import readline 
from bs4 import BeautifulSoup

__author__ = "Connor Nelson"
champion_data = {"Jax":{"name":"Jax","id":24,"title":"Grandmaster at Arms","key":"Jax"},"Sona":{"name":"Sona","id":37,"title":"Maven of the Strings","key":"Sona"},"Tristana":{"name":"Tristana","id":18,"title":"the Yordle Gunner","key":"Tristana"},"Varus":{"name":"Varus","id":110,"title":"the Arrow of Retribution","key":"Varus"},"Fiora":{"name":"Fiora","id":114,"title":"the Grand Duelist","key":"Fiora"},"Singed":{"name":"Singed","id":27,"title":"the Mad Chemist","key":"Singed"},"TahmKench":{"name":"Tahm Kench","id":223,"title":"the River King","key":"TahmKench"},"Leblanc":{"name":"LeBlanc","id":7,"title":"the Deceiver","key":"Leblanc"},"Thresh":{"name":"Thresh","id":412,"title":"the Chain Warden","key":"Thresh"},"Karma":{"name":"Karma","id":43,"title":"the Enlightened One","key":"Karma"},"Jhin":{"name":"Jhin","id":202,"title":"the Virtuoso","key":"Jhin"},"Rumble":{"name":"Rumble","id":68,"title":"the Mechanized Menace","key":"Rumble"},"Udyr":{"name":"Udyr","id":77,"title":"the Spirit Walker","key":"Udyr"},"LeeSin":{"name":"Lee Sin","id":64,"title":"the Blind Monk","key":"LeeSin"},"Yorick":{"name":"Yorick","id":83,"title":"Shepherd of Souls","key":"Yorick"},"Kassadin":{"name":"Kassadin","id":38,"title":"the Void Walker","key":"Kassadin"},"Sivir":{"name":"Sivir","id":15,"title":"the Battle Mistress","key":"Sivir"},"MissFortune":{"name":"Miss Fortune","id":21,"title":"the Bounty Hunter","key":"MissFortune"},"Draven":{"name":"Draven","id":119,"title":"the Glorious Executioner","key":"Draven"},"Yasuo":{"name":"Yasuo","id":157,"title":"the Unforgiven","key":"Yasuo"},"Kayle":{"name":"Kayle","id":10,"title":"The Judicator","key":"Kayle"},"Shaco":{"name":"Shaco","id":35,"title":"the Demon Jester","key":"Shaco"},"Renekton":{"name":"Renekton","id":58,"title":"the Butcher of the Sands","key":"Renekton"},"Hecarim":{"name":"Hecarim","id":120,"title":"the Shadow of War","key":"Hecarim"},"Fizz":{"name":"Fizz","id":105,"title":"the Tidal Trickster","key":"Fizz"},"KogMaw":{"name":"Kog'Maw","id":96,"title":"the Mouth of the Abyss","key":"KogMaw"},"Maokai":{"name":"Maokai","id":57,"title":"the Twisted Treant","key":"Maokai"},"Lissandra":{"name":"Lissandra","id":127,"title":"the Ice Witch","key":"Lissandra"},"Jinx":{"name":"Jinx","id":222,"title":"the Loose Cannon","key":"Jinx"},"Urgot":{"name":"Urgot","id":6,"title":"the Headsman's Pride","key":"Urgot"},"Fiddlesticks":{"name":"Fiddlesticks","id":9,"title":"the Harbinger of Doom","key":"Fiddlesticks"},"Galio":{"name":"Galio","id":3,"title":"the Sentinel's Sorrow","key":"Galio"},"Pantheon":{"name":"Pantheon","id":80,"title":"the Artisan of War","key":"Pantheon"},"Talon":{"name":"Talon","id":91,"title":"the Blade's Shadow","key":"Talon"},"Gangplank":{"name":"Gangplank","id":41,"title":"the Saltwater Scourge","key":"Gangplank"},"Ezreal":{"name":"Ezreal","id":81,"title":"the Prodigal Explorer","key":"Ezreal"},"Gnar":{"name":"Gnar","id":150,"title":"the Missing Link","key":"Gnar"},"Teemo":{"name":"Teemo","id":17,"title":"the Swift Scout","key":"Teemo"},"Annie":{"name":"Annie","id":1,"title":"the Dark Child","key":"Annie"},"Mordekaiser":{"name":"Mordekaiser","id":82,"title":"the Iron Revenant","key":"Mordekaiser"},"Azir":{"name":"Azir","id":268,"title":"the Emperor of the Sands","key":"Azir"},"Kennen":{"name":"Kennen","id":85,"title":"the Heart of the Tempest","key":"Kennen"},"Riven":{"name":"Riven","id":92,"title":"the Exile","key":"Riven"},"Chogath":{"name":"Cho'Gath","id":31,"title":"the Terror of the Void","key":"Chogath"},"Aatrox":{"name":"Aatrox","id":266,"title":"the Darkin Blade","key":"Aatrox"},"Poppy":{"name":"Poppy","id":78,"title":"Keeper of the Hammer","key":"Poppy"},"Taliyah":{"name":"Taliyah","id":163,"title":"the Stoneweaver","key":"Taliyah"},"Illaoi":{"name":"Illaoi","id":420,"title":"the Kraken Priestess","key":"Illaoi"},"Heimerdinger":{"name":"Heimerdinger","id":74,"title":"the Revered Inventor","key":"Heimerdinger"},"Alistar":{"name":"Alistar","id":12,"title":"the Minotaur","key":"Alistar"},"XinZhao":{"name":"Xin Zhao","id":5,"title":"the Seneschal of Demacia","key":"XinZhao"},"Lucian":{"name":"Lucian","id":236,"title":"the Purifier","key":"Lucian"},"Volibear":{"name":"Volibear","id":106,"title":"the Thunder's Roar","key":"Volibear"},"Sejuani":{"name":"Sejuani","id":113,"title":"the Winter's Wrath","key":"Sejuani"},"Nidalee":{"name":"Nidalee","id":76,"title":"the Bestial Huntress","key":"Nidalee"},"Garen":{"name":"Garen","id":86,"title":"The Might of Demacia","key":"Garen"},"Leona":{"name":"Leona","id":89,"title":"the Radiant Dawn","key":"Leona"},"Zed":{"name":"Zed","id":238,"title":"the Master of Shadows","key":"Zed"},"Blitzcrank":{"name":"Blitzcrank","id":53,"title":"the Great Steam Golem","key":"Blitzcrank"},"Rammus":{"name":"Rammus","id":33,"title":"the Armordillo","key":"Rammus"},"Velkoz":{"name":"Vel'Koz","id":161,"title":"the Eye of the Void","key":"Velkoz"},"Caitlyn":{"name":"Caitlyn","id":51,"title":"the Sheriff of Piltover","key":"Caitlyn"},"Trundle":{"name":"Trundle","id":48,"title":"the Troll King","key":"Trundle"},"Kindred":{"name":"Kindred","id":203,"title":"The Eternal Hunters","key":"Kindred"},"Quinn":{"name":"Quinn","id":133,"title":"Demacia's Wings","key":"Quinn"},"Ekko":{"name":"Ekko","id":245,"title":"the Boy Who Shattered Time","key":"Ekko"},"Nami":{"name":"Nami","id":267,"title":"the Tidecaller","key":"Nami"},"Swain":{"name":"Swain","id":50,"title":"the Master Tactician","key":"Swain"},"Taric":{"name":"Taric","id":44,"title":"the Shield of Valoran","key":"Taric"},"Syndra":{"name":"Syndra","id":134,"title":"the Dark Sovereign","key":"Syndra"},"Skarner":{"name":"Skarner","id":72,"title":"the Crystal Vanguard","key":"Skarner"},"Braum":{"name":"Braum","id":201,"title":"the Heart of the Freljord","key":"Braum"},"Veigar":{"name":"Veigar","id":45,"title":"the Tiny Master of Evil","key":"Veigar"},"Xerath":{"name":"Xerath","id":101,"title":"the Magus Ascendant","key":"Xerath"},"Corki":{"name":"Corki","id":42,"title":"the Daring Bombardier","key":"Corki"},"Nautilus":{"name":"Nautilus","id":111,"title":"the Titan of the Depths","key":"Nautilus"},"Ahri":{"name":"Ahri","id":103,"title":"the Nine-Tailed Fox","key":"Ahri"},"Jayce":{"name":"Jayce","id":126,"title":"the Defender of Tomorrow","key":"Jayce"},"Darius":{"name":"Darius","id":122,"title":"the Hand of Noxus","key":"Darius"},"Tryndamere":{"name":"Tryndamere","id":23,"title":"the Barbarian King","key":"Tryndamere"},"Janna":{"name":"Janna","id":40,"title":"the Storm's Fury","key":"Janna"},"Elise":{"name":"Elise","id":60,"title":"the Spider Queen","key":"Elise"},"Vayne":{"name":"Vayne","id":67,"title":"the Night Hunter","key":"Vayne"},"Brand":{"name":"Brand","id":63,"title":"the Burning Vengeance","key":"Brand"},"Graves":{"name":"Graves","id":104,"title":"the Outlaw","key":"Graves"},"Soraka":{"name":"Soraka","id":16,"title":"the Starchild","key":"Soraka"},"Karthus":{"name":"Karthus","id":30,"title":"the Deathsinger","key":"Karthus"},"Vladimir":{"name":"Vladimir","id":8,"title":"the Crimson Reaper","key":"Vladimir"},"Zilean":{"name":"Zilean","id":26,"title":"the Chronokeeper","key":"Zilean"},"Katarina":{"name":"Katarina","id":55,"title":"the Sinister Blade","key":"Katarina"},"Shyvana":{"name":"Shyvana","id":102,"title":"the Half-Dragon","key":"Shyvana"},"Warwick":{"name":"Warwick","id":19,"title":"the Uncaged Wrath of Zaun","key":"Warwick"},"Ziggs":{"name":"Ziggs","id":115,"title":"the Hexplosives Expert","key":"Ziggs"},"Kled":{"name":"Kled","id":240,"title":"the Cantankerous Cavalier","key":"Kled"},"Khazix":{"name":"Kha'Zix","id":121,"title":"the Voidreaver","key":"Khazix"},"Olaf":{"name":"Olaf","id":2,"title":"the Berserker","key":"Olaf"},"TwistedFate":{"name":"Twisted Fate","id":4,"title":"the Card Master","key":"TwistedFate"},"Nunu":{"name":"Nunu","id":20,"title":"the Yeti Rider","key":"Nunu"},"Rengar":{"name":"Rengar","id":107,"title":"the Pridestalker","key":"Rengar"},"Bard":{"name":"Bard","id":432,"title":"the Wandering Caretaker","key":"Bard"},"Irelia":{"name":"Irelia","id":39,"title":"the Will of the Blades","key":"Irelia"},"Ivern":{"name":"Ivern","id":427,"title":"the Green Father","key":"Ivern"},"MonkeyKing":{"name":"Wukong","id":62,"title":"the Monkey King","key":"MonkeyKing"},"Ashe":{"name":"Ashe","id":22,"title":"the Frost Archer","key":"Ashe"},"Kalista":{"name":"Kalista","id":429,"title":"the Spear of Vengeance","key":"Kalista"},"Akali":{"name":"Akali","id":84,"title":"the Fist of Shadow","key":"Akali"},"Vi":{"name":"Vi","id":254,"title":"the Piltover Enforcer","key":"Vi"},"Amumu":{"name":"Amumu","id":32,"title":"the Sad Mummy","key":"Amumu"},"Lulu":{"name":"Lulu","id":117,"title":"the Fae Sorceress","key":"Lulu"},"Morgana":{"name":"Morgana","id":25,"title":"Fallen Angel","key":"Morgana"},"Nocturne":{"name":"Nocturne","id":56,"title":"the Eternal Nightmare","key":"Nocturne"},"Diana":{"name":"Diana","id":131,"title":"Scorn of the Moon","key":"Diana"},"AurelionSol":{"name":"Aurelion Sol","id":136,"title":"The Star Forger","key":"AurelionSol"},"Zyra":{"name":"Zyra","id":143,"title":"Rise of the Thorns","key":"Zyra"},"Viktor":{"name":"Viktor","id":112,"title":"the Machine Herald","key":"Viktor"},"Cassiopeia":{"name":"Cassiopeia","id":69,"title":"the Serpent's Embrace","key":"Cassiopeia"},"Nasus":{"name":"Nasus","id":75,"title":"the Curator of the Sands","key":"Nasus"},"Twitch":{"name":"Twitch","id":29,"title":"the Plague Rat","key":"Twitch"},"DrMundo":{"name":"Dr. Mundo","id":36,"title":"the Madman of Zaun","key":"DrMundo"},"Orianna":{"name":"Orianna","id":61,"title":"the Lady of Clockwork","key":"Orianna"},"Evelynn":{"name":"Evelynn","id":28,"title":"the Widowmaker","key":"Evelynn"},"RekSai":{"name":"Rek'Sai","id":421,"title":"the Void Burrower","key":"RekSai"},"Lux":{"name":"Lux","id":99,"title":"the Lady of Luminosity","key":"Lux"},"Sion":{"name":"Sion","id":14,"title":"The Undead Juggernaut","key":"Sion"},"Camille":{"name":"Camille","id":164,"title":"the Steel Shadow","key":"Camille"},"MasterYi":{"name":"Master Yi","id":11,"title":"the Wuju Bladesman","key":"MasterYi"},"Ryze":{"name":"Ryze","id":13,"title":"the Rune Mage","key":"Ryze"},"Malphite":{"name":"Malphite","id":54,"title":"Shard of the Monolith","key":"Malphite"},"Anivia":{"name":"Anivia","id":34,"title":"the Cryophoenix","key":"Anivia"},"Shen":{"name":"Shen","id":98,"title":"the Eye of Twilight","key":"Shen"},"JarvanIV":{"name":"Jarvan IV","id":59,"title":"the Exemplar of Demacia","key":"JarvanIV"},"Malzahar":{"name":"Malzahar","id":90,"title":"the Prophet of the Void","key":"Malzahar"},"Zac":{"name":"Zac","id":154,"title":"the Secret Weapon","key":"Zac"},"Gragas":{"name":"Gragas","id":79,"title":"the Rabble Rouser","key":"Gragas"}}
def get_riot_API_key():
	"""
	This method will eventually be used to get the API key from the riot developers website, but currently im just filling it in manually
	"""
	# loginpage = requests.get("https://auth.riotgames.com/authorize?redirect_uri=https://developer.riotgames.com/oauth2-callback&client_id=riot-developer-portal&response_type=code&scope=openid+email+summoner")
	# bsObj = BeautifulSoup(loginpage.text, "html.parser")
	# print(bsObj)
	key = "RGAPI-e9ae9b9b-be75-4518-9029-0dd8601091f3"
	return key

def get_game_list(ID, champion_ID):
	"""
	This method ges the list of games played by a specific account ID by a specific champion(inputted using the champion ID). 
	It returns a list of game ID numbers in backwords order, as in most recently played goes first.
	"""
	list = requests.get("https://na1.api.riotgames.com//lol/match/v3/matchlists/by-account/" + ID + "?champion=" + str(champion_ID) + "&endindex=25&queue=420&api_key=" + get_riot_API_key())
	list_data = json.loads(list.text)
	match_ID_list = []
	for i in list_data["matches"]:
		match_ID_list.append(i["gameId"])
	return(match_ID_list)

def get_champ_ID(name):
	"""
	Takes in the name of a champion as listed in the dictionary containing champion info and turns it into the ID that is required for the API
	"""
	ID = champion_data[name]["id"]
	return ID

def get_account_ID(name):
	"""
	Takes in a profile name and then returns the ID for that summoner name
	"""
	response = requests.get("https://na1.api.riotgames.com/lol//summoner/v3/summoners/by-name/" + name + "?api_key=" + get_riot_API_key())
	response_data = json.loads(response.text)
	print(response.text)
	ID = str(response_data["accountId"])
	return(ID)

def get_result(ID, champion_ID):
	"""
	Returns the result, win or loss, for the individual game specificed by ID and champion ID. 
	"""
	response = requests.get("https://na1.api.riotgames.com//lol/match/v3/matches/" + str(ID) + "?api_key=" + get_riot_API_key())
	game_data = json.loads(response.text)
	for i in game_data["participants"]:
		if (i["championId"] == champion_ID) and i["stats"]["win"] == True:
			return True
	return False

def get_win_rate(summoner_name, champion):
	"""
	Utilizes the above methods to get the win rate for a champion name and summoner name
	"""
	ID = get_account_ID(summoner_name)
	champ_ID = get_champ_ID(champion)
	match_list = get_game_list(ID, champ_ID)
	wins = 0.0
	for i in match_list:
		if get_result(i, champ_ID) == True:
			wins = wins + 1
	return wins/len(match_list)

def riot_API():
	"""
	Uses the win rate and combines it with the user input and output
	THIS METHOD CURRENTLY DOES NOT WORK DUE TO THE FACT MY API KEY GOT BANNED FOR TOO MANY REQUESTS
	"""
	print("League of Legends(Riot) API")
	# profile_name = input("Profile Name: ")
	# champion = input("Champion: ")
	profile_name = "An Extra Second"
	champion = "Ekko"
	print("Profile:", profile_name)
	print("Champion:", champion)
	print("Win Rate in Last 25 Games:", str(100 * get_win_rate(profile_name, champion))[:5])
	# get_game_list(get_account_ID("An Extra Second"), get_champ_ID("Ekko"))
	# print(str(get_win_rate("An Extra Second", "Ekko"))[:5])
	# print(get_result("2896390097", 245))
def top_clash_royal_clans():
	"""
	Simply uses the clash royal API in order to print out the top 10 clans
	"""
	print("Loading Clash Royal API Usage")
	header = {'auth': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTk0NSwiaWRlbiI6IjE2ODU0Mzg0ODMwNDIxNDAxNiIsIm1kIjp7fSwidHMiOjE1NDExNzU4ODYwODV9.JOv_1ygXEBMNNON78IzVTJoIVSZrBMawFUrrd_uOn84",}
	clans = requests.get("https://api.royaleapi.com/top/clans/", headers=header)
	clans_data = json.loads(clans.text)
	# print(clans_data)
	print("Top Clash Royal Clans:")
	for i in range(10):
		print("Rank: " + str(clans_data[i]["rank"]) + "     Name: " + clans_data[i]["name"])

def translate_to_minion():
	"""
	Uses a translate API to take user input and translate it to minion 
	"""
	to_be_translated = input("Text to Be Translated: ")
	# to_be_translated = "Hi my name is connor"
	parameters = {"text": to_be_translated}
	response = requests.get("https://api.funtranslations.com/translate/minion.json", params = parameters)
	translate_data = json.loads(response.text)
	translated_text = translate_data["contents"]["translated"]
	print("Translation:", translated_text)
if __name__ == '__main__':
	# riot_API()
	# THIS METHOD DOESNT WORK DUE TO THE FACT MY API KEY GOT BANNED - you checked me off in class
	translate_to_minion()
	top_clash_royal_clans()





