# tweet_miner.py
from tweepy import StreamListenerclass Listener(StreamListener):def __init__(self, symbol):
        """
        Initialize twitter listener
        """
        super(Listener,self).__init__()
        self.symbol = symboldef on_error(self,status):
        print(status)
        return True
