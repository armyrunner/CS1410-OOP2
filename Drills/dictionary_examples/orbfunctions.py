def create_orb(emotion,location,data):

    emlst = {}
    emlst["emotion"]= emotion
    emlst["location"] = location
    emlst["data"] = data

    return emlst

def orb_get_emotion(orb):
    return orb["emotion"]

def change_orb_emotion(orb,new_emotion):
    orb["emotion"] = new_emotion
    return orb

def orb_get_location(orb):
    return orb["location"]

def move_orb(orb,new_location):
    orb["location"] = new_location
    return orb

def orb_get_data(orb):
    return orb["data"]
