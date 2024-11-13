def cleanFromStatus(content:dict, fieldStatus:str, blacklist=[]):
    if content[fieldStatus] == 'no':
        for key in content.keys():
            if key not in blacklist:
                content[key] = None
    return content


def getActualParticipant(content:list):
    actual_participants = []
    for person in content:
        if len(person.strip()) > 0:
            actual_participants.append(person)
    return actual_participants
