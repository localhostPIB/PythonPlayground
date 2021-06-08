import time

import pyotp


class TotP:
    """
    https://pyauth.github.io/pyotp/#time-based-otps
    """
    def test(self):
        totp = pyotp.TOTP('base32secret3232')
        totp.now()
        # OTP verified for current time
        print(totp.verify('492039'))  # => True
        time.sleep(10)
        print(totp.verify('492039'))  # => False


totP = TotP()
totP.test()
