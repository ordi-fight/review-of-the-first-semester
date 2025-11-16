
class Character:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.buff_func = lambda atk, dfs, hp: (atk, dfs, hp)

    def apply_buffs(self):
        self.attack, self.defense, self.hp = self.buff_func(
            self.attack, self.defense, self.hp
        )

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        self.hp -= max(1, amount - self.defense)

    def attack_target(self, other):
        other.take_damage(self.attack)


def compose_buffs(*funcs):
    def inner(atk, dfs, hp):
        for f in funcs:
            atk, dfs, hp = f(atk, dfs, hp)
        return atk, dfs, hp

    return lambda atk, dfs, hp: inner(atk, dfs, hp)


def buff_factory(cmd, x):
    dx = float(x)
    if cmd == "atk_add":
        return lambda atk, dfs, hp: (atk + dx, dfs, hp)
    elif cmd == "atk_mul":
        return lambda atk, dfs, hp: (atk * dx, dfs, hp)
    elif cmd == "dfs_add":
        return lambda atk, dfs, hp: (atk, dfs + dx, hp)
    elif cmd == "dfs_mul":
        return lambda atk, dfs, hp: (atk, dfs * dx, hp)
    else:
        return lambda atk, dfs, hp: (atk, dfs, hp)   # 防呆
def battle(c1, c2):
    """
    #TODO
    Turn-based battle: c1 attacks first, alternate until one dies.
    returns the winner's name and hp
    
    """
       
       
    while True:
      
      c1.apply_buffs()
      c2.apply_buffs()
      
      c1.attack_target(c2)
      if not c2.is_alive():
        
        return c1.name , c1.hp
      c1.apply_buffs()
      c2.apply_buffs()
      
      c2.attack_target(c1)
      if not c1.is_alive():
        
        return c2.name , c2.hp
        
        
        
if __name__ == "__main__":
  # Input format:
  # name1 hp1 atk1 dfs1
  # name2 hp2 atk2 dfs2
  # n
  # Then n lines:
  # target cmd value
  # (target is either name1 or name2)
  n1, h1, a1, d1 = input().split()
  n2, h2, a2, d2 = input().split()
  c1 = Character(n1, int(h1), int(a1), int(d1))
  c2 = Character(n2, int(h2), int(a2), int(d2))

  n = int(input())
  buffs_c1 = []
  buffs_c2 = []
  for _ in range(n):
      target, cmd, val = input().split()
      buff = buff_factory(cmd, float(val))
      if target == c1.name:
          buffs_c1.append(buff)
      elif target == c2.name:
          buffs_c2.append(buff)

  c1.buff_func = compose_buffs(*buffs_c1)
  c2.buff_func = compose_buffs(*buffs_c2)
  # print(c1.buff_func)
  winner, hp_left = battle(c1, c2)
  print(f"{winner} wins with {hp_left:.1f} HP left.")
