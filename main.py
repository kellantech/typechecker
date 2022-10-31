def checktypes(**kwargs):
    def outer(f):
        def check(*args):
          ty = kwargs['types']
          for n in range(len(args)):
            try: _ = ty[n]
            except:
              raise ValueError(f"type list needs to be length {len(args)+1}")
            if isinstance(args[n],ty[n]):pass    
            else:
              n2 = n+1
              if (n2) == 1:
                suf = 'st'
              elif (n2) == 2: suf = 'nd'
              elif (n2) == 3: suf = 'rd'
              else: suf = 'th'
              s = f'{n2}{suf} argument to {f.__name__} should be {ty[n].__name__}, not {type(args[n]).__name__}'
              raise TypeError(s)
            
          f(*args)
        return check
    return outer
