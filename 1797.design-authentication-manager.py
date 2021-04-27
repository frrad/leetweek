class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.tokens = {}

    def generate(self, tokenId: str, currentTime: int) -> None:

        self.tokens[tokenId] = currentTime + self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.tokens:
            return
        if currentTime >= self.tokens[tokenId]:
            return
        self.tokens[tokenId] = currentTime + self.ttl

    def countUnexpiredTokens(self, currentTime: int) -> int:
        return sum([currentTime < self.tokens[id] for id in self.tokens.keys()])


timeToLive = 15
tokenId = "1324"
currentTime = 12
obj = AuthenticationManager(timeToLive)
obj.generate(tokenId, currentTime)
obj.renew(tokenId, currentTime)
param_3 = obj.countUnexpiredTokens(currentTime)
