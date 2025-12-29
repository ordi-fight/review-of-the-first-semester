
def double_gen(val_list):
    """Yield each number doubled."""
    # TODO
    # nums is a list
    for i in val_list:
      yield 2*i
    

def square_gen(val_list):
    """Yield each number squared."""
    # TODO
    for i in val_list:
      yield i*i
      
def odd_gen(val_list):
    """Yield only odd numbers."""
    # TODO
    for i in val_list: 
      if (i % 2) == 1:
        yield i

def even_gen(val_list):
    """Yield only even numbers."""
    # TODO
    for i in val_list:
      if (i % 2) == 0:
        yield i

def compose_generators(gens, nums):
    """Chain all generators together in order."""
    # TODO: apply each generator in sequence to the stream
    # gens is a list and start_stream is a nums
    stream = [i for i in range(1,nums+1)]
    
    for gen in gens :
      
      stream = [i for i in gen(stream)]
      
    return stream
      
    
    

def main():
    m = int(input())
    ops = []
    # Mapping operation names to their generator functions
    gen_map = {
        "double": double_gen,
        "square": square_gen,
        "odd": odd_gen,
        "even": even_gen,
    }
    for _ in range(m):
        line = input().split()
        cmd = line[0]
        if cmd == "add":
            # TODO: add the generator function to ops
            ops.append(gen_map[line[1]])
            
        elif cmd == "remove":
            # TODO: remove the first matching generator from ops
            ops.remove(gen_map[line[1]])
            
        elif cmd == "process":
            # TODO: apply all generators to numbers from 1 to n
            # and print results one per line
            
          if  compose_generators(ops,int(line[1])):
            print("\n".join(map(str,compose_generators(ops,int(line[1])))))

if __name__ == "__main__":
    main()