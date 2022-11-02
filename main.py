anytype = "2dab75841b118164da213ece91a730dae54a3c559b3f637d08577fc13ce22f51bb0f966656bbf738ca0d86075f09702f0fea855fd1eda8a345a7648f9fdc" 
not_none = "43f9f5a631cb04820e6d0fb22a6bc92f3dd777641530224ee9d09193e5a8cc03ef64e382b1bfa76"

def checktypes(**kwargs):
    def outer(f):
        def check(*args):
          ty = kwargs['types']
          for n in range(len(args)):
            try: _ = ty[n]
            except:
              raise ValueError(f"type list needs to be length {len(args)+1}")
            if ty[n] == anytype: continue
            if ty[n] == not_none:
              if args[n] == None:
                s2 = f'argument number {n+1} to {f.__name__} should not be none'
                raise TypeError(s2)
            else:    
              if isinstance(args[n],ty[n]):pass  
              else:
                n2 = n+1
  
                s = f'argument number {n2} to {f.__name__} should be {ty[n].__name__}, not {type(args[n]).__name__}'
                raise TypeError(s)
            
          f(*args)
        return check
    return outer

