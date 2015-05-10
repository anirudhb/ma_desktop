# library
def echo(str):
    import sys
    sys.stdout.write(str)

class Game:
        def __init__(self, players, name):
                self.players = []
                for player in players:
                        self.players.append(player)
                self.name = name
                self.session = None
                self.session_working = False

        def attack(self, enemy, player):
                if enemy or player not in self.players:
                        print 'You have not joined the game or you are kicked out'
                        return
                if player.defending:
                        print 'This player has lost his defence, but not a life'
                        player.defending = False
                        return
                enemy.ammo -= 1
                player.life -= 1
                print 'Player attacked and lost a life'
                enemy.gold += player.power * 10
                print 'You got', player.power * 10, 'gold!'

        def defend(self, player):
                player.defending = True

        def kill(self, enemy, player):
                if player or enemy not in self.players:
                        print 'You are not in the game'
                        return
                if player.power > enemy.power:
                        print 'The player is more powerful than you'
                        return
                enemy.ammo -= player.life
                if enemy.ammo <= 0:
                        print 'The enemy has no ammo'
                player.life = 0
                print 'Player died'
                player.alive = False

        def get_ammo(self, player, ammo):
                if player.gold < ammo:
                        print 'You don\'t have enough gold'
                        return
                player.gold -= ammo
                player.ammo += ammo
                print 'Nice doing money with you!'

        def cast_gems(self, player, gems=1):
                if player.gold != gems * 10:
                        print 'You do not have enough gold to cast your gems'
                        return
                player.gold -= gems * 10
                player.gems += gems
                print 'Thanks for casting gems!'

        def upgrade_power_level(self, player, power):
                if player.gems != power * 100:
                        print 'You need more gems'
                        return
                player.gems -= power * 100
                player.power += power
                print 'You are now stronger!'

        def revive(self, player):
                if player.gems < 1:
                        print 'You cannot revive'
                        return
                if player not in self.players:
                        print 'You are kicked out'
                        return
                player.gems -= 1
                player.alive = True
                print 'You are revived!'

        def add_player(self, player):
                self.players.append(player)

        def update(self):
                for player in self.players:
                        if not player.alive:
                                self.players.remove(player)


class Player:
        def __init__(self, name):
                self.life = 10
                self.power = 0
                self.gold = 0
                self.gems = 0
                self.alive = True
                self.ammo = 5
                self.level = 1
                self.name = name

        def level(self):
                self.level = self.power // 10
                print self.level

        def join(self, game):
                game.add_player(self)
                self.game = game

        def cheat(self, password, power, ammo, gold, gems, life, enemy):
                if password == 'cheat engine':
                        self.alive = True
                        del enemy
                        self.gold = gold
                        self.gems = gems
                        self.power = power
                        self.ammo = ammo
                        self.life = life
                        return
                print 'Wrong cheating password!'

        def work(self, gold):
                import time
                time.sleep(gold * 10)
                self.gold += gold

        def quit_game(self):
                self.game.players.remove(self)


                        
                
class Launcher:
    def __init__(self):
        self.log = ""
        self.session = None
        self.player = None
    
    def print_log(self):
        print self.log
    
    def launch_session(self):
        self.session = Game([], "<default>")
        self.log += "[*] Launched new session!\n"
    
    def add_player(self, player):
        self.session.add_player(player)
        self.log += "[+] New player added!\n"
    
    def quit(self):
        for player in self.session.players:
            self.session.remove_player(player)
        self.log += "[X] Exit launcher\n"
        while 1:
            raise SystemExit()

    def start_game(self):
        self.log += "[+] Game started!\n"
        while True:
            self.choose_player()
            self.show_menu()
        self.log += "[-] Game ended\n"
    
    def copy(self):
        c = Launcher()
        c.session = self.session
        c.session.players = self.session.players
        c.player = self.player
        c.log = self.log
        return c
    
    def choose_player(self):
        print ' '.join([p.name for p in self.session.players])
        player = raw_input("Player name: ")
        for p in self.session.players:
            if p.name == player:
                self.player = p
                self.log += "[*] New player chosen: %s\n" % p.name
    
    def show_menu(self):
        if self.player is None:
            self.log += "[-] No player to work with\n"
            print "No player selected"
            return
        print "1) Work"
        print "2) Check Level"
        print "3) Upgrade power level"
        choice = int(raw_input())

l = Launcher()
l.launch_session()
p1 = Player("P1")
p2 = Player("P2")
p3 = Player("P3")
p1.join(l)
p2.join(l)
p3.join(l)
