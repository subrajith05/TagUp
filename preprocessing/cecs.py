CASUAL_MAP = {
    "lol":   "laughing",      "lmao":  "laughing",    "lmfao": "laughing",
    "rofl":  "laughing",      "haha":  "laughing",    "hehe":  "laughing",
    "omg":   "oh my god",     "omfg":  "oh my god",
    "wtf":   "what the",      "wth":   "what the",
    "smh":   "disappointing", "fml":   "frustrated",  "ftw":   "winning",
    "tbh":   "honestly",      "ngl":   "honestly",
    "imo":   "i think",       "imho":  "i think",
    "ikr":   "i agree",       "idk":   "i do not know",
    "fyi":   "note",          "btw":   "by the way",  "nvm":   "never mind",
    "brb":   "back soon",     "afk":   "away",
    "atm":   "currently",     "rn":    "right now",   "asap":  "immediately",
    "bc":    "because",       "cuz":   "because",     "coz":   "because",
    "tho":   "though",        "thru":  "through",
    "ur":    "your",          "u":     "you",         "r":     "are",
    "gr8":   "great",         "b4":    "before",      "l8r":   "later",
    "2day":  "today",         "2nite": "tonight",     "4ever": "forever",
    "nite":  "night",         "luv":   "love",
    "rly":   "really",        "srsly": "seriously",
    "sry":   "sorry",         "srry":  "sorry",
    "thx":   "thanks",        "thnx":  "thanks",      "pls":   "please",
    "plz":   "please",
    "fave":  "favourite",     "fav":   "favourite",
    "prob":  "probably",      "probs": "probably",
    "obv":   "obviously",     "def":   "definitely",  "defo":  "definitely",
    "diff":  "different",     "convo": "conversation","peeps": "people",
    "bf":    "boyfriend",     "gf":    "girlfriend",  "bff":   "best friend",
    "rt":    "retweet",       "dm":    "message",     "tbt":   "throwback",
    "noob":  "beginner",      "newb":  "beginner",    "goat":  "greatest",
    "gg":    "good game",     "wp":    "well played",
    "epic fail": "complete failure", "u": "you",
    "ur": "your",
    "r": "are",
    "gr8": "great",
    "btw": "by the way",
    "idk": "i do not know",
    "lol": "laugh out loud",
    "omg": "oh my god",
    "tdy": "today",
    "tmrw": "tomorrow",
    "pls": "please",
    "plz": "please",
}

def convert_casual(text):
    words = text.lower().split()

    converted = [
        CASUAL_MAP.get(w, w)
        for w in words
    ]

    return " ".join(converted)