class RandomGenerator(object):
    def __init__(self, seed, randomness):
        self.seed = seed
        self.randomness = randomness
        self.stopped = False
        self.started = True

    def random(self):
        if not self.stopped and self.started:
            randint = None
            import random
            random.seed()
            randompool = range(self.seed * self.randomness)
            randint = random.choice(randompool)
            return randint
        print "Sorry, your generator has been stopped.\nPlease restart it."

    def stop(self):
        self.stopped = True
        self.started = False
        
    def restart(self):
        self.__init__(self.seed, self.randomness)

    def close(self):
        self.__del__()

    def __del__(self):
        pass

gen = RandomGenerator(385, 20)
for i in range(30):
    print gen.random()

gen.__del__()

