import random

class Quick(object):
    def partition(self, a, ini, fim):
        pivot = a[fim - 1]
        print('pivot: ', pivot)
        start = ini
        for i in range(ini, fim):
            if a[i] <= pivot:
                if a[start] != a[i]:
                    print('troca {0} por {1}'.format(a[start], a[i]))
                a[start], a[i] = a[i], a[start] # swap
                start += 1
        print('array: ', a)
        return start - 1 # removes last increment

    def quickSort(self, a, ini, fim):
        if ini < fim:
            pp = self.partition(a, ini, fim)
            self.quickSort(a, ini, pp)
            self.quickSort(a, pp + 1, fim)
        return a

a = [8, 5, 12, 55, 3, 7, 82, 44, 35, 25, 41, 29, 17]
print(a)
q = Quick()
print(q.quickSort(a, 0, len(a)))
