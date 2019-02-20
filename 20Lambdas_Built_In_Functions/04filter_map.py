users =[
    {'username': "samuel", 'tweets': ["I love cake", "i love pie"]},
    {'username': "katie", 'tweets': ["I love cat"]},
    {'username': "jeff", 'tweets': []},
    {'username': "bob123", 'tweets': []},
    {'username': "dogg_luvre", 'tweets': ["Dogs are best"]},
    {'username': "guiter_gal", 'tweets': []}
]
inactive_users = list(filter(lambda user: not user['tweets'], users))
print(inactive_users)

inactive_profile = list(map(lambda u: u['username'],
                        filter(lambda user: not user['tweets'], users)))
print(inactive_users)
print(inactive_profile)

inactive_profile2 = [user['username'] for user in users if not user['tweets']]
print(inactive_profile2)