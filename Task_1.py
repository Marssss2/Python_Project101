is_logged_in = True
is_guest = False
is_banned = True

print((is_logged_in or is_guest) and not is_banned) # it will return true because is_logged_in is true, not is_guest is true, and not is_banned is true.
   