


init -999:
    python:
        import os
        os.environ['SSL_CERT_FILE'] = renpy.config.gamedir + "/python-packages/certifi/cacert.pem"

#⚠: —Pass