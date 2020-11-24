def fibonachi (n):
    if n==1:
        return 1
    else:
        a=[1, 1]
        _current = 1
        prev = 1
        for i in range(n-2):
            next=_current+prev
            prev=_current
            _current=next
            a.append(_current)
            yield next
        print(*a)
