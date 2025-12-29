import sys

class Node:
    def __init__(self, name, is_dir, parent=None):
        self.name = name
        self.is_dir = is_dir
        self.parent = parent
        self.children = {}

class FileTree:
    def __init__(self):
        self.root = Node("/", True, None)
        self.cwd = self.root
   
    # !!! You can add more functions if needed !!! #
   
    def path_to_nodes(self, path):
        if path.endswith('/') and len(path) > 1:
            path = path[:-1]
        if path == "":

            return None
        path_judge = path.split("/")
        if path_judge[0] == "":
            # print("i am /")
            nodes = [self.root]
            cur_node = self.root
            for node in path_judge:
               

                if node == "":
                # /A/B "/"
                    continue
                elif node == ".":
                #/A/./B
                    continue
                
                elif node == "..":
                    if len(nodes) == 1:
                        nodes = [self.root]
                    else:
                        nodes = nodes[:-1]
                    cur_node = nodes[-1]
                    
                else:
                    if node in cur_node.children:
                        cur_node = cur_node.children[node]
                        nodes.append(cur_node)
                    else:
                        # print(f"{node} {cur_node.children}exception")
                        return None 
            # print([self.root.name])
        elif path_judge[0] == "." :
            # print("i am .")
            nodes = self.trace_parent(self.cwd)
            cur_node = self.cwd
            for node in (path_judge)[1:]:
                

                if  node == ".":
                # ././B "./"
                    continue    
                    
                
                elif node == "..":
            
                    if len(nodes) == 1:
                        nodes = [self.root]
                    else:
                        nodes = nodes[:-1]
                    cur_node = nodes[-1]
                else:
                    if node in cur_node.children:
                        cur_node = cur_node.children[node]
                        nodes.append(cur_node)
                    else:   
                        return None
        elif path_judge[0] == ".." :
            if self.cwd.parent == None:
                nodes = [self.root]
                cur_node = self.root
            # print("hi")
            else:
                nodes = self.trace_parent(self.cwd.parent)
            # print(nodes)
                cur_node = self.cwd.parent
            for node in (path_judge)[1:]:
                
                # print(self.cwd.name if self.cwd else "None")
                if  node == ".":
                # ././B "./"
                    continue    
                    
                
                elif node == "..":
            
                    if len(nodes) == 1:
                        nodes = [self.root]
                    else:
                        nodes = nodes[:-1]
                    cur_node = nodes[-1]
                else:
                    if node in cur_node.children:
                        cur_node = cur_node.children[node]
                        nodes.append(cur_node)
                    else:
                        return None
        else:
            nodes = self.trace_parent(self.cwd)
            cur_node = self.cwd
            for node in path_judge:
                

                if  node == ".":
                # ././B "./"
                    continue    
                    
                
                elif node == "..":
            
                    if len(nodes) == 1:
                        nodes = [self.root]
                    else:
                        nodes = nodes[:-1]
                    cur_node = nodes[-1]
                else:
                    if node in cur_node.children:
                        cur_node = cur_node.children[node]
                        nodes.append(cur_node)
                    else:
                        return None
        return nodes  
          
    def trace_parent(self,cwd_node):
        path_nodes = []
        cur_node = cwd_node
        if cur_node == None:
            return [self.root]
        while cur_node != self.root:
            path_nodes.append(cur_node)
            cur_node = cur_node.parent
        path_nodes.append(self.root)
        return path_nodes[::-1]
    def mkdir(self, path):
        if path.endswith('/') and len(path) > 1:
            path = path[:-1]
        idx = path.rfind('/')
        if idx == -1:
            p_path, name = ".", path
        elif idx == 0:
            p_path, name = "/", path[1:]
        else:
            p_path, name = path[:idx], path[idx+1:]
        nodes = self.path_to_nodes(p_path)
        if nodes:
            parent = nodes[-1]
            if parent.is_dir and name not in parent.children:
                parent.children[name] = Node(name, True, parent)

    def cd(self, path):
        cwd_ori = self.cwd
        while (not self.path_to_nodes(path)):
            if self.cwd == self.root:
                self.cwd = cwd_ori
                break
            self.cwd = self.cwd.parent
        else:
            # print(self.cwd.name)
            nodes = self.path_to_nodes(path)
            # print(nodes[-1].name)
            self.cwd = nodes[-1]

    def ls(self):
        # TODO
        if self.cwd.children.keys():
            print(" ".join(sorted(self.cwd.children.keys())),end = "\n")
        else:
            print("",end = "\n")

    def touch(self, path):
        # TODO
        if path.endswith('/') and len(path) > 1:
            path = path[:-1]
        idx = path.rfind('/')
        if idx == -1:
            p_path, name = ".", path
        elif idx == 0:
            p_path, name = "/", path[1:]
        else:
            p_path, name = path[:idx], path[idx+1:]
        nodes = self.path_to_nodes(p_path)
        if nodes:
            parent = nodes[-1]
            if parent.is_dir and name not in parent.children:
                parent.children[name] = Node(name, False, parent)

    def rm(self, path):
        # TODO
        if path.endswith('/') and len(path) > 1:
            path = path[:-1]
        idx = path.rfind('/')
        if idx == -1:
            p_path, name = ".", path
        elif idx == 0:
            p_path, name = "/", path[1:]
        else:
            p_path, name = path[:idx], path[idx+1:]
        nodes = self.path_to_nodes(p_path)
        if nodes:
            parent = nodes[-1]
            if parent.is_dir and name in parent.children:
                if not parent.children[name].is_dir:
                    del parent.children[name] 

    # Debug functions
    def print_prompt(self):
        nodes = self.path_to_nodes(".")
        path_str = "/" + "/".join([n.name for n in nodes[1:]])
        if path_str.endswith("/") and len(path_str) > 1: path_str = path_str[:-1]
        print(f"{path_str} >", end=" ", flush=True)

    def print_all(self, node=None, prefix=""):
        if node is None: node, prefix = self.root, ""
        current = prefix + ("/" + node.name if node != self.root else "")
        print(current if node.is_dir else f"{current} (file)")
        if node.is_dir:
            for k in sorted(node.children): self.print_all(node.children[k], current)

def main():
    ft = FileTree()
    # !!! Enable debug mode here !!!
    # !!! Remember to disable it when submitting !!!
    DEBUG_MODE = False
    
    while True:
        if DEBUG_MODE: ft.print_prompt()
        try:
            line = sys.stdin.readline()
            if not line:
                if DEBUG_MODE: print()
                break
        except: break

        line = line.strip()
        if not line: continue

        p = line.split()
        cmd, args = p[0], p[1:]

        if   cmd == 'mkdir' and len(args)==1: ft.mkdir(args[0])
        elif cmd == 'cd'    and len(args)==1: ft.cd(args[0])
        elif cmd == 'ls'    and len(args)==0: ft.ls()
        elif cmd == 'touch' and len(args)==1: ft.touch(args[0])
        elif cmd == 'rm'    and len(args)==1: ft.rm(args[0])
        elif cmd == 'print_all':              ft.print_all()

        if DEBUG_MODE and cmd != 'ls':
            print("--- Tree ---"); ft.print_all(); print("------------")

if __name__ == "__main__":
    main()