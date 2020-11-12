import math

def tour(friends, friend_towns, home_to_town_distances):
    distance = 0
    last_distance = 0
    friend_towns = [[friend,town] for friend,town in friend_towns if friend in friends]
    for iterfriend,itertown in friend_towns:
        if itertown in home_to_town_distances:
            _distance = home_to_town_distances[itertown]
            if distance == 0:
                distance += _distance
                last_distance = _distance
            else:
                distance += math.sqrt(_distance ** 2 - last_distance ** 2)
                last_distance = _distance
    distance += home_to_town_distances[itertown]
    return int(math.floor(distance))
