def stop():
    __import__('os').system("netsh wlan stop hostednetwork")