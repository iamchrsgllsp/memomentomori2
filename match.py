import json


def matcher(userid):
  with open('users.json') as f:
    data = json.load(f)['users']
    for u in data:
      if u['id'] == userid:
        uRID = u['rest']
        pRID = u['partnerid']
        got = restmatch(uRID, pRID)
        re = findrest(got)
        return re

def gmatcher(userid):
  with open('users.json') as f:
    data = json.load(f)['users']
    for u in data:
      if u['id'] == userid:
        uRID = u['rest']
        pRID = u['partnerid']
        got = restmatch(uRID, pRID)
        re = findrest(got)
        return re

def restmatch(uRID, pRID):
  matched = []
  with open('users.json') as f:
    data = json.load(f)['users']
    for u in data:
      if u['id'] == pRID:
        print(uRID)
        print(pRID)
        print(u['rest'])
        for r in uRID:
          for p in u['rest']:
            if r == p:
              matched.append(p)
              break
  return matched


def findrest(ID):
  found = []
  with open('restaurants.json') as restaurant:
    data = json.load(restaurant)['restaurant']
    for r in data:
      for i in ID:
        if i == r['id']:
          found.append({
              "name": r['name'],
              "image": r['image'],
              "link": r['href']
          })
          break
  return found
