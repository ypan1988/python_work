def build_profile(first, last, **user_info):
    """Build a directory containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

user_profile = build_profile('yi', 'pan', location='birmingham', field='statistics', programming_language='python')
print(user_profile)
